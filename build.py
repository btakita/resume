#!/usr/bin/env python3
"""Build a tailored resume PDF from data.toml + TOML profile via agent-resume."""

import subprocess
import sys
import tempfile
from pathlib import Path


def build_markdown(resume_dir: Path, profile: str) -> str:
    """Generate tailored markdown via agent-resume CLI."""
    data_path = resume_dir / "data.toml"
    profile_path = resume_dir / "profiles" / f"{profile}.toml"

    if not data_path.exists():
        print(f"Error: data.toml not found: {data_path}", file=sys.stderr)
        sys.exit(1)
    if not profile_path.exists():
        print(f"Error: profile not found: {profile_path}", file=sys.stderr)
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


def build_pdf_playwright(html_path: Path, pdf_path: Path, css_path: Path):
    """Convert HTML to PDF via Playwright (fallback when WeasyPrint unavailable)."""
    html_content = html_path.read_text()
    css_url = css_path.resolve().as_uri()
    styled = html_content.replace(
        "</head>", f'<link rel="stylesheet" href="{css_url}"></head>'
    )
    html_path.write_text(styled)
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

    # Content assembly via agent-resume
    tailored = build_markdown(resume_dir, args.profile)

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
