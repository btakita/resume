# Resume — Brian Takita

[**Download PDF**](https://btakita.github.io/resume/BrianTakita.pdf) | [View Markdown](BrianTakita.md)

## Quick Start

```bash
make                          # Build default PDF
make PROFILE=backend-ai       # Build with a specific profile
```

## How It Works

The resume is authored in Markdown (`BrianTakita.md`) and converted to PDF via [pandoc](https://pandoc.org/) + [weasyprint](https://weasyprint.org/) with a custom stylesheet (`resume.css`).

**TOML profiles** (`profiles/<name>.toml`) control job-specific tailoring — phrase highlighting, skill emphasis, and section filtering. See [SPEC.md](SPEC.md) for the full specification.

### Pipeline

```
BrianTakita.md + profiles/X.toml
        ↓ build.py
   tailored markdown
        ↓ pandoc (fragment mode)
      HTML body
        ↓ weasyprint + resume.css
       PDF
```

## Creating a New Profile

```bash
cp profiles/default.toml profiles/backend-ai.toml
# Edit profiles/backend-ai.toml
make PROFILE=backend-ai
```

### Profile Options

| Key | Effect |
|-----|--------|
| `highlight.phrases` | Auto-bolds matching text in Experience and Summary |
| `highlight.skills` | Bolds matching skills in the Skills section |
| `sections.experience` | Filters and orders Experience entries by company name |
| `sections.include` | Controls which top-level sections appear |

## Local Build

```sh
# Prerequisites
# pandoc: https://pandoc.org/installing.html
# weasyprint: pip install weasyprint
# Python 3.11+ (for tomllib)

make              # Build BrianTakita.pdf (default profile)
make clean        # Remove generated PDFs
```

## GitHub Action

The workflow (`.github/workflows/build-pdf.yml`) triggers on pushes to `.md`, `.css`, `Makefile`, or profile changes. It can also be triggered manually via `workflow_dispatch`.

1. Installs pandoc + weasyprint
2. Runs `make` to generate the PDF
3. Commits and pushes the updated PDF
4. Deploys to GitHub Pages at [btakita.github.io/resume](https://btakita.github.io/resume/)
