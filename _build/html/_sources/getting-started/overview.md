# Overview

Gradient Dynamics Studio provides a complete CFD workflow in the browser, from CAD import through meshing, simulation, and post-processing. This page introduces the core concepts and platform architecture.

## Platform Concepts

### Projects

Everything in Studio is organized into **projects**. There are two project types:

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

## Technology

### Structured Cartesian Cut-Cell Meshing

Gradient Dynamics uses a **structured Cartesian cut-cell** mesher with **block-based Adaptive Mesh Refinement (AMR)**. The domain is divided into a sparse hierarchy of regular Cartesian blocks, with blocks near geometry surfaces refined to capture geometric detail through cut-cell representation. Cut cells are formed by clipping Cartesian hexahedral cells against the exact geometry surface, producing polyhedral boundary cells that conform precisely to the shape — no surface approximation or manual mesh topology decisions required.

This architecture is purpose-built for GPU simulation: the structured, regular memory layout of Cartesian block meshes enables coalesced GPU memory access and fully parallel cell updates — delivering mesh generation and simulation performance that is not possible with unstructured mesh topologies. See [Mesh Settings](/meshing/mesh-settings.md) for a detailed explanation of how block AMR and cut-cell generation work.

### GPU-Native Solver Suite

Gradient Dynamics provides a comprehensive suite of CFD solvers, all designed for GPU-native execution:

- **Density-based solver** (recommended) — Solves the compressible Navier-Stokes equations using explicit time marching (SSP-RK3). All solution variables update simultaneously in a single parallel sweep. Low-Mach preconditioning ensures accuracy for subsonic flows. Supports both compressible and incompressible flow regimes
- **Pressure-based solver** — Segregated incompressible formulation with SIMPLE, SIMPLEC, PISO, and PIMPLE coupling algorithms
- **Coupled solver** — Block-coupled implicit incompressible formulation that solves momentum and pressure simultaneously
- **FSAC solver** — Hybrid explicit/implicit approach using fractional step artificial compressibility
- **ACM solver** — Artificial Compressibility Method for explicit time marching of incompressible flows

The density-based solver is recommended for optimal GPU performance across the widest range of applications. See [Solver Settings](/simulation/solver-settings.md) for a detailed comparison of all solver types.

## Workflow Overview

### Meshing Workflow

```
Upload CAD → Analyze Geometry → Configure Domain → Set Mesh Parameters → Generate Mesh → Export
```

1. **Upload** a CAD file (STEP, IGES) or surface mesh (STL, OBJ)
2. **Analyze** geometry for watertightness, manifold issues, and repair if needed
3. **Configure** the domain type (external, internal, rotating, etc.) and domain bounds
4. **Set** mesh parameters — base cell size, AMR refinement levels, refinement zones
5. **Generate** the mesh on cloud GPUs
6. **Proceed** directly to simulation, or inspect the mesh quality first

### CFD Workflow

```
Upload CAD → Mesh → Configure Simulation → Run → Post-Process
```

1. **Upload** geometry and generate a mesh (or use a mesh from a Meshing project)
2. **Configure** the simulation — solver type, turbulence model, boundary conditions
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
