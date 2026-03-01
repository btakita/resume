# Resume Build System — Specification

## Overview

A TOML-driven resume build system that generates tailored PDFs from a single markdown template. Each job application can have its own profile that controls emphasis, section ordering, and content filtering.

## Architecture

```
BrianTakita.md          Master template — all content, no bolding
profiles/<name>.toml    Job-specific configuration
build.py                Applies profile → tailored markdown → HTML → PDF
resume.css              Print stylesheet (fonts, layout, colors)
Makefile                Build orchestration
```

## Files

| File | Purpose |
|------|---------|
| `BrianTakita.md` | Master resume content. Plain markdown — no bold emphasis (applied dynamically by profiles). |
| `resume.css` | Weasyprint stylesheet. Controls page layout, fonts, heading styles, bullet formatting. |
| `build.py` | Python build script. Reads template + profile, applies transformations, shells out to pandoc and weasyprint. |
| `Makefile` | Build entry point. `make` builds default, `make PROFILE=X` builds tailored variant. |
| `profiles/default.toml` | Default profile — general full-stack + AI emphasis. |

## Profile Schema

```toml
[highlight]
# Phrases to auto-bold in Experience and Summary sections.
# Case-insensitive matching. Skips already-bolded or linked text.
phrases = ["real-time video pipeline", "NVIDIA H100 GPUs"]

# Skills to bold in the Skills comma list.
skills = ["Rust", "Python", "TypeScript"]

[sections]
# Experience entries to include, by company name prefix.
# Order here controls order in output.
# Omit an entry to exclude it from the PDF.
experience = [
  "Presence AI",
  "Open Source",
  "Brian Takita",
  "Censible",
]

# Top-level sections (h2) to include.
# Omit a section to exclude it entirely.
include = [
  "Summary",
  "Skills",
  "Experience",
  "Education",
  "Certifications",
  "Languages",
]
```

## Build Process

1. **Load profile** — Read `profiles/<name>.toml`
2. **Read template** — Read `BrianTakita.md`
3. **Apply transformations:**
   - Filter top-level sections per `sections.include`
   - Filter and reorder experience entries per `sections.experience`
   - Bold skills in Skills section per `highlight.skills`
   - Bold phrases in Experience/Summary per `highlight.phrases`
4. **Generate HTML** — Pandoc fragment mode (no injected CSS)
5. **Generate PDF** — Weasyprint with `resume.css`

## Phrase Highlighting Rules

- Matching is case-insensitive
- Preserves original case in output
- Skips text already inside `**...**`, `[...]`, or `<...>`
- Applied only to Experience and Summary sections (not headings or contact info)
- Longer phrases should be listed before shorter ones if they overlap

## Section Filtering

- `sections.include` controls which h2 sections appear
- `sections.experience` controls which h3 entries within Experience appear
- Both preserve the order specified in the TOML array
- Content before the first h2 (name, tagline, contact) is always included

## CLI Usage

```bash
# Via Makefile (preferred)
make                          # Default profile → BrianTakita.pdf
make PROFILE=backend-ai       # Named profile → BrianTakita-backend-ai.pdf

# Via build.py directly
python3 build.py                              # Default profile
python3 build.py -p backend-ai                # Named profile
python3 build.py -p backend-ai -o custom.pdf  # Custom output path
```

## Dependencies

- Python 3.11+ (`tomllib` in stdlib)
- pandoc (markdown → HTML)
- weasyprint (HTML → PDF)
