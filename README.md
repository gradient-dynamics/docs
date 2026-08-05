# Gradient Dynamics documentation

The public Gradient Dynamics documentation is a Sphinx site using the Furo
theme and MyST Markdown.

## Local build

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make html
```

Open `_build/html/index.html` in a browser. For an auto-reloading authoring
server, install `sphinx-autobuild` and run:

```bash
sphinx-autobuild . _build/html
```

## Information architecture

The root navigation is intentionally limited to six product-oriented areas:

1. Getting Started
2. User Guide
3. Studio
4. API Reference
5. Release Notes
6. Knowledge Base

Add a page to the nearest section index using a MyST `toctree`. Keep solver
implementation details private; public numerical content should explain
capabilities, inputs, outputs, validation and engineering use.
