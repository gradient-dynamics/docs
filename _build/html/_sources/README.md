# Gradient Dynamics Documentation

The official documentation for [Gradient Dynamics](https://gradientdynamics.com) — production multiphysics simulation in the browser.

> **Note:** This documentation is currently in active development alongside the product. Some sections may be incomplete or subject to change.

## What is Gradient Dynamics?

Gradient Dynamics Studio is a browser-based platform for computational fluid dynamics (CFD) and multiphysics simulation. Upload geometry, generate meshes, run simulations, and visualize results — all from a single interface with GPU-native cloud compute. No software installation or license management required.

## Documentation Contents

| Section | Description |
|---------|-------------|
| [Getting Started](getting-started/overview.md) | Platform overview, quick start guide, and project types |
| [Meshing](meshing/geometry.md) | Geometry preparation, domain setup, mesh settings, boundary layers, refinement zones, multi-region meshing, and export |
| [Simulation](simulation/setup.md) | Turbulence models, boundary conditions, solver settings, running simulations, and post-processing |
| [AI Assistant](agent/overview.md) | Using the built-in AI assistant for mesh and simulation setup |
| [Examples](examples/index.md) | Step-by-step walkthroughs for vehicle aerodynamics, aircraft wings, pipe flow, electronics cooling, and rotating machinery |
| [Knowledge Base](knowledge-base/best-practices.md) | Best practices, troubleshooting guide, FAQ, and glossary |
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

## Contributing

We welcome corrections, improvements, and new examples. Please open an issue or pull request.

### Writing Guidelines

- **User-facing** — Focus on how to use the product, not internal implementation details
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
