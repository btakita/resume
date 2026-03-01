# Resume Build System

TOML-driven resume generator. Single markdown template + per-job profiles → tailored PDFs.

## Architecture

```
BrianTakita.md          Master template — all content, no bold emphasis
profiles/<name>.toml    Job-specific configuration (phrase bolding, section filtering)
build.py                Applies profile → tailored markdown → HTML → PDF
resume.css              Print stylesheet (weasyprint, @page layout)
Makefile                Build entry point
```

## Design Principles

- **Markdown is the source of truth.** Profiles only *add* emphasis and *optionally* filter — they never silently drop content.
- **Safe by default.** Unset `sections.experience` or `sections.include` = include ALL. Only set when actively filtering for a specific job.
- **No injected CSS.** Pandoc runs in fragment mode (no `--standalone`). All styling is in `resume.css`.

## Build

```bash
make                          # Default profile → BrianTakita.pdf
make PROFILE=backend-ai       # Named profile → BrianTakita-backend-ai.pdf
```

Dependencies: Python 3.11+ (tomllib), pandoc, weasyprint.

## Profile Schema

```toml
[highlight]
phrases = ["real-time video pipeline", "NVIDIA H100 GPUs"]  # Auto-bold in Experience/Summary
skills = ["Rust", "Python"]                                   # Bold in Skills section

[sections]
# Both optional — unset = include all
# experience = ["Presence AI", "Open Source"]   # Filter/reorder by h3 prefix
# include = ["Summary", "Skills", "Experience"] # Filter top-level h2 sections
```

## Conventions

- Master template (`BrianTakita.md`) has no bold emphasis — bolding is applied dynamically by profiles.
- Contact info uses `<div class="contact-line">` with inline `text-align:center`.
- Experience entries use `### Company — *Job Title*` pattern with `<small>` date ranges.
- CSS uses `list-style-position: inside` for flush-left bullets.
- Mismatched filter names print warnings to stderr.

## Files

| File | Purpose |
|------|---------|
| `BrianTakita.md` | Master resume content (plain markdown) |
| `resume.css` | Weasyprint stylesheet (page layout, fonts, colors) |
| `build.py` | Python build script (profile → markdown → HTML → PDF) |
| `Makefile` | Build orchestration (`make`, `make PROFILE=X`) |
| `profiles/default.toml` | Default profile (general full-stack + AI emphasis) |
| `SPEC.md` | Full specification |
| `README.md` | User-facing documentation |
