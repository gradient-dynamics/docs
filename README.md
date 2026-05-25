---
orphan: true
---

# Gradient Dynamics Documentation

The official documentation for [Gradient Dynamics](https://gradientdynamics.com) — public facing documentation for engineers.

> **Note:** This documentation is currently in active development alongside the product. Some sections may be incomplete or subject to change.

## What is Gradient Dynamics?

Gradient Dynamics Studio is a browser-based platform for computational fluid dynamics (CFD) and multiphysics simulation. Upload geometry, generate unstructured or structured meshes, run simulations, and visualize results from a single interface. No software installation or license management required.

## Documentation Contents

| Section | Description |
|---------|-------------|
| [Getting Started](getting-started/overview.md) | Platform overview, quick start guide, and project types |
| [Studio](studio/overview.md) | GUI workspace for setup, meshing, simulation, monitoring, and post-processing |
| [Meshing](meshing/index.md) | Geometry preparation, structured and unstructured meshing, quality review, and export |
| [Simulation](simulation/index.md) | Turbulence models, boundary conditions, solver settings, running simulations, and post-processing |
| [Examples](examples/index.md) | Studio walkthroughs for vehicle aerodynamics, aircraft wings, pipe flow, and rotating machinery |
| [Knowledge Base](knowledge-base/best-practices.md) | Best practices, troubleshooting, validation studies, FAQ, and glossary |
| [Reference](reference/supported-formats.md) | Supported file formats, subscription tiers, and keyboard shortcuts |

## Building the Docs Locally

### Prerequisites

Python 3.8+ and pip.

```bash
pip install "jupyter-book<2"
```

### Build

```bash
git clone https://github.com/gradient-dynamics/docs.git
cd docs
jupyter-book build .
```

Open the output in your browser:

```bash
open _build/html/index.html
```


### Writing Guidelines

- **User-facing** — Focus on how to use the product, not internal engineering notes
- **Action-oriented** — Use clear, imperative language ("Click Upload", "Select External Flow")
- **Concrete** — Include parameter tables, typical values, and worked examples
- **Callouts** — Use `{tip}`, `{warning}`, and `{note}` admonitions for important information

### Adding a Page

1. Create a `.md` file in the appropriate section directory
2. Add the file path to `_toc.yml`
3. Rebuild and verify with `jupyter-book build .`

### Adding an Example

Examples follow a consistent structure: **Objective → Step-by-step setup → Results analysis**. Add new `.md` files to `examples/`, register them in `_toc.yml`, and link them from `examples/index.md`.

## Feedback

Found an error or missing information? [Open an issue](https://github.com/gradient-dynamics/docs/issues) or reach out at [support@gradientdynamics.com](mailto:support@gradientdynamics.com).
