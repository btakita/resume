#!/usr/bin/env python3
"""Build a tailored resume PDF from data.toml + TOML profile via agent-resume.

Falls back to reading BrianTakita.md directly when agent-resume is not installed.
"""

import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path


def load_profile(profile_path: Path) -> dict:
    with open(profile_path, "rb") as f:
        return tomllib.load(f)


def build_markdown_agent_resume(resume_dir: Path, profile: str) -> str:
    """Generate tailored markdown via agent-resume CLI."""
    data_path = resume_dir / "data.toml"
    profile_path = resume_dir / "profiles" / f"{profile}.toml"

    if not data_path.exists():
        print(f"Error: data.toml not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    result = subprocess.run(
        ["agent-resume", "build", "-d", str(data_path), "-p", str(profile_path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"agent-resume failed: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    return result.stdout


# ── Fallback: apply profile transforms directly to BrianTakita.md ──


def split_sections(md: str) -> list[tuple[str, str]]:
    """Split markdown into (heading, content) pairs."""
    sections = []
    current_name = ""
    current_lines: list[str] = []

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
    """Split Experience section into (company_prefix, entry_text) pairs."""
    entries = []
    current_prefix = ""
    current_lines: list[str] = []

    for line in content.split("\n"):
        if line.startswith("### "):
            if current_lines:
                entries.append((current_prefix, "\n".join(current_lines)))
            title_text = re.sub(r"<[^>]+>", "", line[4:].strip())
            current_prefix = title_text.strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        entries.append((current_prefix, "\n".join(current_lines)))
    return entries


def filter_experience(section_content: str, allowed: list[str] | None) -> str:
    entries = split_experience_entries(section_content)

    preamble = ""
    h3_entries: dict[str, str] = {}
    for prefix, text in entries:
        if not prefix:
            preamble = text
        else:
            h3_entries[prefix] = text

    if not allowed:
        ordered = [preamble] if preamble else []
        ordered.extend(h3_entries.values())
        return "\n\n".join(ordered)

    ordered = [preamble] if preamble else []
    for name in allowed:
        for prefix, text in h3_entries.items():
            if prefix.startswith(name) or name in prefix:
                ordered.append(text)
                break
    return "\n\n".join(ordered)


def bold_phrases(text: str, phrases: list[str]) -> str:
    for phrase in phrases:
        if not phrase:
            continue
        pattern = re.compile(
            r"(?<!\*\*)(?<!\[)(?<!<)" + re.escape(phrase) + r"(?!\*\*)(?!\])(?!>)",
            re.IGNORECASE,
        )
        text = pattern.sub(lambda m: f"**{m.group(0)}**", text)
    return text


def bold_skills(text: str, skills: list[str]) -> str:
    for skill in skills:
        text = text.replace(skill, f"**{skill}**")
    return text


def build_markdown_fallback(resume_dir: Path, profile: dict) -> str:
    """Read BrianTakita.md and apply profile transforms directly."""
    md_path = resume_dir / "BrianTakita.md"
    if not md_path.exists():
        print(f"Error: {md_path} not found", file=sys.stderr)
        sys.exit(1)

    md = md_path.read_text(encoding="utf-8")
    sections = split_sections(md)
    highlight = profile.get("highlight", {})
    sections_config = profile.get("sections", {})
    include = sections_config.get("include")
    experience_filter = sections_config.get("experience")

    result_parts = []
    for name, content in sections:
        if include and name and name not in include:
            continue
        if name == "Experience" and experience_filter:
            content = filter_experience(content, experience_filter)
        if name == "Skills" and highlight.get("skills"):
            content = bold_skills(content, highlight["skills"])
        if highlight.get("phrases"):
            content = bold_phrases(content, highlight["phrases"])
        result_parts.append(content)

    return "\n\n".join(result_parts)


def build_markdown(resume_dir: Path, profile_name: str, profile: dict) -> str:
    """Try agent-resume CLI first, fall back to direct markdown processing."""
    if shutil.which("agent-resume"):
        return build_markdown_agent_resume(resume_dir, profile_name)

    print("agent-resume not found, using BrianTakita.md fallback...", file=sys.stderr)
    return build_markdown_fallback(resume_dir, profile)


def apply_replacements(md: str, profile: dict) -> str:
    """Apply per-profile [[replace]] text substitutions.

    Each entry has 'find' (unique substring identifying a line) and 'text'
    (full replacement line). Matches the first line containing 'find'.
    """
    for entry in profile.get("replace", []):
        find = entry.get("find", "")
        text = entry.get("text", "")
        if not find or not text:
            continue
        lines = md.split("\n")
        for i, line in enumerate(lines):
            if find in line:
                lines[i] = text
                break
        md = "\n".join(lines)
    return md


def build_html(md_content: str, html_path: Path):
    """Convert markdown to HTML via pandoc (fragment mode)."""
    body = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html"],
        input=md_content,
        capture_output=True,
        text=True,
        check=True,
        encoding="utf-8",
    ).stdout

    html = (
        '<!DOCTYPE html>\n<html>\n<head><meta charset="utf-8"></head>\n<body>\n'
        + body
        + "</body>\n</html>\n"
    )
    html_path.write_text(html, encoding="utf-8")


def build_pdf_playwright(html_path: Path, pdf_path: Path, css_path: Path):
    """Convert HTML to PDF via Playwright (fallback when WeasyPrint unavailable)."""
    html_content = html_path.read_text(encoding="utf-8")
    css_url = css_path.resolve().as_uri()
    styled = html_content.replace(
        "</head>", f'<link rel="stylesheet" href="{css_url}"></head>'
    )
    html_path.write_text(styled, encoding="utf-8")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri())
        page.pdf(path=str(pdf_path), format="Letter", margin={"top": "0.5in", "right": "0.6in", "bottom": "0.5in", "left": "0.6in"})
        browser.close()


def build_pdf(html_path: Path, pdf_path: Path, css_path: Path):
    """Convert HTML to PDF via weasyprint, fallback to Playwright on failure."""
    try:
        subprocess.run(
            ["weasyprint", str(html_path), str(pdf_path), "--stylesheet", str(css_path)],
            check=True,
        )
    except subprocess.CalledProcessError:
        print("WeasyPrint failed, using Playwright fallback...", file=sys.stderr)
        build_pdf_playwright(html_path, pdf_path, css_path)


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
        "--css",
        default="resume.css",
        help="CSS stylesheet",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output PDF path (default: BrianTakita.pdf or BrianTakita-<profile>.pdf)",
    )
    args = parser.parse_args()

    resume_dir = Path(__file__).parent
    css_path = resume_dir / args.css

    profile_path = resume_dir / "profiles" / f"{args.profile}.toml"
    if not profile_path.exists():
        print(f"Error: profile not found: {profile_path}", file=sys.stderr)
        sys.exit(1)
    profile = load_profile(profile_path)

    tailored = build_markdown(resume_dir, args.profile, profile)
    tailored = apply_replacements(tailored, profile)

    if args.output:
        pdf_path = Path(args.output)
    elif args.profile == "default":
        pdf_path = resume_dir / "BrianTakita.pdf"
    else:
        pdf_path = resume_dir / f"BrianTakita-{args.profile}.pdf"

    html_path = Path(tempfile.gettempdir()) / "resume.html"
    build_html(tailored, html_path)
    build_pdf(html_path, pdf_path, css_path)

    print(f"Built: {pdf_path}")


if __name__ == "__main__":
    main()
