# Resume — Brian Takita

[**Download PDF**](https://btakita.github.io/resume/BrianTakita.pdf) | [View Markdown](BrianTakita.md) | [Search Experience](https://btakita.github.io/resume/search.html)

## Quick Start

```bash
make                          # Build default PDF
make PROFILE=apex-cvs         # Build with a specific profile
```

## Prerequisites

- **agent-resume** — Rust CLI for content assembly ([btakita/agent-resume](https://github.com/btakita/agent-resume))
- **pandoc** — Markdown to HTML ([pandoc.org](https://pandoc.org/installing.html))
- **weasyprint** — HTML to PDF (`pip install weasyprint`)
- **Python 3.11+** (for build.py)

### Installing agent-resume

```bash
cargo install agent-resume
```

Or build from source:

```bash
git clone https://github.com/btakita/agent-resume.git
cd agent-resume
cargo install --path .
```

## How It Works

Resume data lives in `data.toml` (experiences, skills, accomplishments) and is assembled into markdown by [agent-resume](https://github.com/btakita/agent-resume), then converted to PDF via pandoc + weasyprint.

**TOML profiles** (`profiles/<name>.toml`) control job-specific tailoring — phrase highlighting, skill emphasis, and experience filtering. See [SPEC.md](SPEC.md) for the full specification.

### Pipeline

```
data.toml + profiles/X.toml
        ↓ agent-resume build (Rust: content assembly, phrase bolding)
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

## Search

An interactive experience search is available at [btakita.github.io/resume/search.html](https://btakita.github.io/resume/search.html).

To regenerate the search index:
```bash
agent-resume search-index -d data.toml > search-index.json
```

## Local Build

```sh
make              # Build BrianTakita.pdf (default profile)
make clean        # Remove generated PDFs
```

## Testing

```bash
make test         # 12 tests (search index validation + LightPanda DOM tests)
```

## GitHub Action

The workflow (`.github/workflows/build-pdf.yml`) triggers on pushes to `.md`, `.css`, `Makefile`, or profile changes. It can also be triggered manually via `workflow_dispatch`.

1. Installs pandoc + weasyprint + agent-resume
2. Runs `make` to generate the PDF
3. Commits and pushes the updated PDF
4. Deploys to GitHub Pages at [btakita.github.io/resume](https://btakita.github.io/resume/)
