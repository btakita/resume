# Resume — Brian Takita

[**Download PDF**](https://btakita.github.io/resume/BrianTakita.pdf) | [View Markdown](BrianTakita.md)

## How It Works

The resume is authored in Markdown (`BrianTakita.md`) and converted to PDF using [pandoc](https://pandoc.org/) + [weasyprint](https://weasyprint.org/) with a custom stylesheet (`resume.css`).

A GitHub Action automatically rebuilds the PDF and deploys it to GitHub Pages whenever the source files change.

## Local Build

```sh
# Prerequisites
# pandoc: https://pandoc.org/installing.html
# weasyprint: pip install weasyprint

make pdf        # Build BrianTakita.pdf
make clean      # Remove generated PDF
```

## GitHub Action

The workflow (`.github/workflows/build-pdf.yml`) triggers on pushes to:
- `BrianTakita.md` — resume content
- `resume.css` — print stylesheet
- `Makefile` — build configuration

It can also be triggered manually via `workflow_dispatch`.

**What it does:**
1. Installs pandoc + weasyprint
2. Runs `make pdf` to generate the PDF
3. Commits and pushes the updated PDF
4. Deploys to GitHub Pages at [btakita.github.io/resume](https://btakita.github.io/resume/)

## GitHub Pages

The resume is hosted at **https://btakita.github.io/resume/** with:
- Direct PDF download link
- Markdown source view
