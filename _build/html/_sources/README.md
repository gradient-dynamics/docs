# Gradient Dynamics Documentation

This directory contains the source for the Gradient Dynamics Studio documentation, built with [Jupyter Book](https://jupyterbook.org/).

## Structure

```
docs/
├── _config.yml                 # Jupyter Book config
├── _toc.yml                    # Table of contents
├── _static/                    # Static assets (CSS, images, logo)
├── index.md                    # Landing page
├── getting-started/            # Overview, quick start, projects
├── meshing/                    # Geometry, domain, mesh settings, BL, refinement, export
├── simulation/                 # Setup, turbulence models, BCs, solver, running, post-processing
├── agent/                      # AI assistant usage guides
├── examples/                   # Step-by-step walkthroughs (vehicle, wing, pipe, cooling, rotating)
├── knowledge-base/             # Best practices, troubleshooting, FAQ, glossary
└── reference/                  # Supported formats, subscription tiers, shortcuts
```

## Prerequisites

```bash
pip install "jupyter-book<2"
```

## Building

Build the HTML documentation:

```bash
cd docs
jupyter-book build .
```

Then open the output in your browser:

```bash
open _build/html/index.html
```

Or paste this into your browser bar:

```
file:///Users/jamiesadler/Documents/gradient-dynamics/docs/_build/html/index.html
```

## Content Guidelines

- **User-facing only** — Document how to use the product, not internal implementation details
- **No framework names** — Don't reference internal libraries, APIs, or tech stack
- **Action-oriented** — Use clear, imperative instructions ("Click Upload", "Select External Flow")
- **Tables for parameters** — Use tables for configuration options with descriptions and typical values
- **Tips and warnings** — Use MyST admonitions (`{tip}`, `{warning}`, `{note}`) for callouts
- **Cross-links** — Use standard markdown links with `.md` extensions

## Adding a New Page

1. Create a `.md` file in the appropriate directory
2. Add the file to `_toc.yml`
3. Rebuild with `jupyter-book build .`

## Adding an Example

1. Create a new `.md` file in `examples/`
2. Follow the structure of existing examples (Objective → Steps → Results Analysis)
3. Add the file to the Examples section in `_toc.yml`
4. Add a link in `examples/index.md`
