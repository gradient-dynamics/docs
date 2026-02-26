# Gradient Dynamics Studio

**Production CFD in the browser.** Upload geometry, generate meshes, run simulations, and visualize results — all from a single web-based platform with GPU-accelerated cloud compute.

```{admonition} Beta
:class: warning
Gradient Dynamics Studio is currently in beta. Features and capabilities are actively being expanded.
```

## What is Gradient Dynamics?

Gradient Dynamics Studio is a browser-based computational fluid dynamics (CFD) platform that streamlines the entire simulation workflow:

1. **Upload** your CAD geometry (STEP, IGES, STL, OBJ)
2. **Mesh** with GPU-accelerated adaptive meshing and automatic boundary layer generation
3. **Simulate** using industry-standard RANS turbulence models on cloud GPUs
4. **Visualize** results with interactive 3D post-processing — slices, streamlines, force calculations, and more

No software installation. No license management. Just open your browser and start simulating.

## Key Capabilities

### [Meshing](meshing/geometry.md)
GPU-accelerated hex-dominant adaptive meshing with boundary layers, refinement zones, and multi-region support. Export to OpenFOAM, ANSYS Fluent, CGNS, and more.

### [Simulation](simulation/setup.md)
Steady-state RANS CFD with k-ω SST, k-ε, Spalart-Allmaras, and more. Cloud GPU execution with live residual monitoring and convergence tracking.

### [AI Assistant](agent/overview.md)
An intelligent assistant that analyzes your geometry, suggests mesh configurations, sets up boundary conditions, and guides you through the entire workflow using natural language.

### [Post-Processing](simulation/post-processing.md)
Interactive 3D visualization with surface coloring, slice planes, streamlines, isosurfaces, force/moment calculations, and probe tools — all in the browser.

## Quick Links

- [Quick Start](getting-started/quick-start.md) — Run your first simulation in minutes
- [Examples](examples/index.md) — Step-by-step walkthroughs for common applications
- [Best Practices](knowledge-base/best-practices.md) — Tips for getting accurate results
- [FAQ](knowledge-base/faq.md) — Answers to common questions
