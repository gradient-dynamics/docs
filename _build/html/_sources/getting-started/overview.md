# Overview

Gradient Dynamics Studio provides a complete CFD workflow in the browser, from CAD import through meshing, simulation, and post-processing. This page introduces the core concepts and platform architecture.

## Platform Concepts

### Projects

Everything in Gradient Dynamics is organized into **projects**. There are two project types:

- **Meshing Projects** — Generate high-quality meshes for use in external solvers or within the platform
- **CFD Projects** — Complete end-to-end workflow: geometry → mesh → simulation → results

### The Workspace

Each project opens into a **workspace** with:

- **3D Viewer** — Interactive visualization of your geometry, mesh, and results
- **Tab Panel** — Context-aware settings for each workflow stage (Setup, Geometry, Mesh, Simulation, Results)
- **AI Assistant** — A conversational panel to help configure and troubleshoot
- **Feature Tree** — Hierarchical view of all project elements (geometry, regions, surfaces, zones)
- **Logs** — Real-time job execution status and output

### Cloud Compute

All mesh generation and simulation runs execute on **cloud GPUs**. This means:

- No local hardware requirements beyond a modern web browser
- Consistent, fast compute regardless of your machine
- Automatic scaling for large meshes and simulations

### Credits

Compute usage is measured in **credits**:

| Operation | Credit Rate |
|-----------|-------------|
| Mesh generation | 0.2 credits/GPU-min |
| CFD simulation | 1.0 credits/GPU-min |

Your remaining credit balance is shown in the dashboard. See [Subscription Tiers](/reference/subscription-tiers.md) for details on plans and credit allocations.

## Workflow Overview

### Meshing Workflow

```
Upload CAD → Analyze Geometry → Configure Domain → Set Mesh Parameters → Generate Mesh → Export
```

1. **Upload** a CAD file (STEP, IGES) or surface mesh (STL, OBJ)
2. **Analyze** geometry for watertightness, manifold issues, and repair if needed
3. **Configure** the domain type (external, internal, rotating, etc.) and domain box
4. **Set** mesh parameters — cell size, boundary layers, refinement zones
5. **Generate** the mesh on cloud GPUs
6. **Export** to your solver format of choice (OpenFOAM, Fluent, CGNS, etc.)

### CFD Workflow

```
Upload CAD → Mesh → Configure Simulation → Run → Post-Process
```

1. **Upload** geometry and generate a mesh (or use a mesh from a Meshing project)
2. **Configure** the simulation — turbulence model, boundary conditions, solver settings
3. **Run** the simulation on cloud GPUs with live monitoring
4. **Post-process** — visualize fields, extract forces, generate slice planes and streamlines

## Supported Applications

Gradient Dynamics is designed for a wide range of CFD applications:

| Application | Domain Type | Typical Use |
|------------|-------------|-------------|
| Vehicle aerodynamics | External | Drag, lift, flow visualization around cars, trucks, motorcycles |
| Aerospace | External | Wing analysis, fuselage flows, rotorcraft |
| Wind engineering | External | Building loads, pedestrian comfort, wind farm layout |
| Pipe and duct flows | Internal | Pressure drop, flow distribution, HVAC design |
| Electronics cooling | Internal / CHT | Thermal management, heat sink optimization |
| Turbomachinery | Rotating | Fans, pumps, turbines, compressors |
| Heat exchangers | Conjugate | Fluid-solid thermal coupling |

## Next Steps

- [Quick Start](quick-start.md) — Get hands-on with your first project
- [Projects](projects.md) — Learn about project types and management
