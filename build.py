#!/usr/bin/env python3
"""Build a tailored resume PDF from markdown template + TOML profile."""

import re
import subprocess
import sys
import tomllib
from pathlib import Path


def load_profile(profile_path: Path) -> dict:
    with open(profile_path, "rb") as f:
        return tomllib.load(f)


def read_template(md_path: Path) -> str:
    return md_path.read_text()


def split_sections(md: str) -> list[tuple[str, str]]:
    """Split markdown into (heading, content) pairs.
    Returns list of (section_name, full_text_including_heading).
    The first entry has section_name="" for content before any h2.
    """
    sections = []
    current_name = ""
    current_lines = []

    for line in md.split("\n"):
        if line.startswith("## "):
            if current_lines:
                sections.append((current_name, "\n".join(current_lines)))
            current_name = line[3:].strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        sections.append((current_name, "\n".join(current_lines)))

    return sections


def split_experience_entries(content: str) -> list[tuple[str, str]]:
    """Split Experience section content into (company_prefix, entry_text) pairs."""
    entries = []
    current_prefix = ""
    current_lines = []

    for line in content.split("\n"):
        if line.startswith("### "):
            if current_lines:
                entries.append((current_prefix, "\n".join(current_lines)))
            # Extract company name (before the em dash)
            title = line[4:].strip()
            current_prefix = title.split("—")[0].split("–")[0].strip().rstrip(" *")
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        entries.append((current_prefix, "\n".join(current_lines)))

    return entries


def filter_experience(section_content: str, allowed: list[str] | None) -> str:
    """Filter/reorder experience entries. If allowed is None/empty, include all."""
    entries = split_experience_entries(section_content)

    # First entry is the h2 heading + any preamble before first h3
    preamble = ""
    h3_entries = {}  # preserves insertion order (Python 3.7+)
    for prefix, text in entries:
        if not prefix:
            preamble = text
        else:
            h3_entries[prefix] = text

    # If no filter specified, include all entries in original order
    if not allowed:
        ordered = [preamble] if preamble else []
        ordered.extend(h3_entries.values())
        return "\n\n".join(ordered)

    # Reorder according to allowed list
    ordered = [preamble] if preamble else []
    matched_names = set()
    for name in allowed:
        for prefix, text in h3_entries.items():
            if prefix.startswith(name) or name in prefix:
                ordered.append(text)
                matched_names.add(name)
                break
        else:
            print(
                f"Warning: experience filter '{name}' did not match any heading",
                file=sys.stderr,
            )

    return "\n\n".join(ordered)


def bold_phrases(text: str, phrases: list[str]) -> str:
    """Bold specified phrases in text, avoiding already-bolded or linked text."""
    for phrase in phrases:
        # Skip if phrase is empty
        if not phrase:
            continue
        # Match phrase only when not already inside **...** or [...] or <...>
        # Simple approach: replace only in plain text contexts
        pattern = re.compile(
            r"(?<!\*\*)(?<!\[)(?<!<)" + re.escape(phrase) + r"(?!\*\*)(?!\])(?!>)",
            re.IGNORECASE,
        )
        # Use original case from the text for the replacement
        def replace_preserving_case(m):
            return f"**{m.group(0)}**"

        text = pattern.sub(replace_preserving_case, text)

    return text


def bold_skills(text: str, skills: list[str]) -> str:
    """Bold specified skills in a comma-separated skills line."""
    for skill in skills:
        # Match whole skill (bounded by comma, start, or end)
        pattern = re.compile(
            r"(?<=^|(?<=, ))" + re.escape(skill) + r"(?=,|$)",
            re.MULTILINE,
        )
        text = text.replace(skill, f"**{skill}**")

    return text


def apply_profile(md: str, profile: dict) -> str:
    """Apply TOML profile transformations to markdown."""
    sections = split_sections(md)
    highlight = profile.get("highlight", {})
    sections_config = profile.get("sections", {})

    include = sections_config.get("include")
    experience_filter = sections_config.get("experience")

    result_parts = []

    for name, content in sections:
        # Filter sections if include list is specified
        if include and name and name not in include:
            continue

        # Filter experience entries
        if name == "Experience" and experience_filter:
            content = filter_experience(content, experience_filter)

        # Bold skills in Skills section
        if name == "Skills" and highlight.get("skills"):
            content = bold_skills(content, highlight["skills"])

        # Bold phrases in all content
        if highlight.get("phrases"):
            content = bold_phrases(content, highlight["phrases"])

        result_parts.append(content)

    return "\n\n".join(result_parts)


def build_html(md_content: str, html_path: Path):
    """Convert markdown to HTML via pandoc (fragment mode)."""
    body = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html"],
        input=md_content,
        capture_output=True,
        text=True,
        check=True,
    ).stdout

    html = (
        '<!DOCTYPE html>\n<html>\n<head><meta charset="utf-8"></head>\n<body>\n'
        + body
        + "</body>\n</html>\n"
    )
    html_path.write_text(html)


def build_pdf(html_path: Path, pdf_path: Path, css_path: Path):
    """Convert HTML to PDF via weasyprint."""
    subprocess.run(
        ["weasyprint", str(html_path), str(pdf_path), "--stylesheet", str(css_path)],
        check=True,
    )


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Build tailored resume PDF")
    parser.add_argument(
        "--profile",
        "-p",
        default="default",
        help="Profile name (looks for profiles/<name>.toml)",
    )
    parser.add_argument(
        "--md",
        default="BrianTakita.md",
        help="Source markdown file",
    )
    parser.add_argument(
        "--css",
        default="resume.css",
        help="CSS stylesheet",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output PDF path (default: <name>.pdf or BrianTakita-<profile>.pdf)",
    )
    args = parser.parse_args()

    resume_dir = Path(__file__).parent
    profile_path = resume_dir / "profiles" / f"{args.profile}.toml"
    md_path = resume_dir / args.md
    css_path = resume_dir / args.css

    if not profile_path.exists():
        print(f"Error: profile not found: {profile_path}", file=sys.stderr)
        sys.exit(1)

    profile = load_profile(profile_path)
    md = read_template(md_path)
    tailored = apply_profile(md, profile)

    if args.output:
        pdf_path = Path(args.output)
    elif args.profile == "default":
        pdf_path = resume_dir / "BrianTakita.pdf"
    else:
        pdf_path = resume_dir / f"BrianTakita-{args.profile}.pdf"

    html_path = Path("/tmp/resume.html")
    build_html(tailored, html_path)
    build_pdf(html_path, pdf_path, css_path)

    print(f"Built: {pdf_path}")


if __name__ == "__main__":
    main()
