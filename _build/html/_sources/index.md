# Introduction

Gradient Dynamics builds simulation technology for engineering teams that need fast, practical CFD and multiphysics workflows without managing local solver and meshing infrastructure. Our platform combines meshing, solver setup, cloud execution, monitoring, and post-processing in a single browser-based environment.

Studio is the main GUI interface to this technology. It lets you move from geometry to mesh, simulation, and results review in one workspace, while still exposing the engineering controls needed for production work.

```{admonition} Beta
:class: warning
Gradient Dynamics Studio is currently in beta. Features and capabilities are actively being expanded.
```

## What We Support

Gradient Dynamics supports a broad set of simulation and meshing workflows:

| Area | Highlights |
|------|------------|
| **Mesh support** | Structured and unstructured mesh workflows, with unstructured meshing recommended as the starting point for most production CFD cases. |
| **Solver support** | Solver workflows for structured and unstructured meshes, including pressure-based low-speed CFD, explicit compressible flow, steady simulation, and transient simulation. |
| **Flow physics** | External aerodynamics, internal flows, rotating machinery, thermal analysis, and conjugate heat transfer. |
| **Turbulence modelling** | RANS, URANS, LES, and hybrid RANS-LES workflows for different accuracy and cost targets. |
| **Geometry handling** | CAD and surface geometry import, geometry checks, named surfaces, region setup, and repair-oriented workflows. |
| **Mesh quality** | Quality review, local refinement, near-wall controls, multi-region interfaces, and export workflows. |
| **Results** | Browser-based post-processing for fields, slices, streamlines, probes, forces, moments, heat-transfer metrics, and convergence history. |

## What is Gradient Dynamics Studio?

Studio is designed for engineering teams that need a guided workflow from model preparation through post-processing without managing local installations.

The typical workflow is:

1. **Upload** CAD or surface geometry.
2. **Prepare** the simulation domain and boundary surfaces.
3. **Mesh** using unstructured or structured meshing.
4. **Simulate** fluid, thermal, rotating machinery, or coupled multiphysics cases.
5. **Review** convergence, fields, forces, heat transfer, and derived quantities in the browser.

## Key Capabilities

### [Studio](studio/overview.md)
The main browser workspace for projects, geometry review, meshing, simulation setup, run monitoring, and post-processing.

### [Meshing](meshing/index.md)
Two meshing routes are available: **unstructured** meshes for the recommended production CFD starting point and **structured** meshes for automated, repeatable workflows where that approach fits the case.

### [Simulation](simulation/index.md)
Multiphysics solver workflows for external aerodynamics, internal flows, thermal analysis, rotating machinery, conjugate heat transfer, explicit compressible flow, and pressure-based low-speed CFD.

### [Post-Processing](simulation/post-processing.md)
Interactive visualization with surface coloring, slice planes, streamlines, isosurfaces, force and moment calculations, heat-transfer metrics, and probe tools.

## Quick Links

- [Quick Start](getting-started/quick-start.md) — Run your first simulation in minutes
- [Studio Examples](examples/index.md) — Step-by-step walkthroughs for common applications
- [Best Practices](knowledge-base/best-practices.md) — Tips for getting accurate results
- [FAQ](knowledge-base/faq.md) — Answers to common questions
