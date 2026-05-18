# Overview

Gradient Dynamics Studio provides a complete browser workflow for engineering simulation: geometry preparation, meshing, solver setup, execution, and post-processing. This page introduces the core concepts you will use across the documentation.

## Platform Concepts

### Projects

Everything in Studio is organized into projects.

| Project Type | Use For |
|--------------|---------|
| **Meshing** | Preparing, generating, inspecting, and exporting meshes. |
| **Simulation** | Running end-to-end workflows from geometry or mesh through results. |

### Workspace

Each project opens into a workspace with:

- **3D Viewer** - Inspect geometry, domains, surfaces, meshes, and results.
- **Setup Panel** - Configure workflow-specific settings.
- **Feature Tree** - Navigate geometry, regions, zones, surfaces, simulations, and results.
- **Assistant** - Ask for guided setup, troubleshooting, and workflow recommendations.
- **Logs and Monitors** - Track meshing and simulation progress.

### Cloud Execution

Meshing and simulation runs execute in the cloud. You only need a modern browser to configure, submit, monitor, and review work.

### Credits

Compute usage is measured in credits. Studio shows an estimate before you submit mesh generation or simulation runs. See [Subscription Tiers](/reference/subscription-tiers.md) for plan details.

## Meshing Options

Studio supports two meshing types:

| Mesh Type | Best For |
|-----------|----------|
| **Unstructured** | Production CFD, complex topology, boundary-layer workflows, imported mesh workflows, interoperability, and cases needing flexible element layouts. |
| **Structured** | Automated, repeatable workflows, geometry screening, parametric studies, and cases where a structured approach fits the solver and validation target. |

Start with the unstructured workflow unless your geometry, downstream workflow, or validation requirement specifically calls for a structured mesh.

## Simulation Capabilities

Gradient Dynamics supports solver workflows for:

- External aerodynamics
- Internal flows
- Thermal analysis
- Conjugate heat transfer
- Rotating machinery
- Coupled multiphysics cases
- Steady and transient studies
- Laminar and turbulent flow modelling

Studio exposes these capabilities through project-level choices, boundary conditions, materials, solver settings, run controls, and post-processing tools.

## Workflow Overview

### Meshing Workflow

```text
Upload geometry -> Check geometry -> Configure domain -> Select mesh type -> Set resolution -> Generate mesh -> Review quality
```

### Simulation Workflow

```text
Prepare mesh -> Assign physics -> Set boundary conditions -> Configure run controls -> Run simulation -> Post-process results
```

## Supported Applications

| Application | Typical Use |
|------------|-------------|
| Vehicle aerodynamics | Drag, lift, flow visualization, underbody flow, cooling flow. |
| Aerospace | Wings, ducts, nacelles, bodies, and control surfaces. |
| Wind engineering | Building loads, pedestrian comfort, external flow studies. |
| Pipe and duct flows | Pressure drop, flow distribution, HVAC design. |
| Thermal management | Fan flow, heat sinks, cold plates, and thermal performance. |
| Rotating machinery | Fans, pumps, compressors, turbines, propellers. |
| Heat exchangers | Fluid-solid heat transfer and thermal performance. |

## Next Steps

- [Quick Start](quick-start.md) - Create your first project.
- [Projects](projects.md) - Learn how work is organized.
- [Studio](../studio/overview.md) - Understand the main GUI workspace.
