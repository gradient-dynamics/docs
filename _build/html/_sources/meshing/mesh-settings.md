# Mesh Settings

Mesh settings control the type, resolution, quality targets, and expected cost of a generated mesh. Configure them in the **Mesh Settings** tab after the geometry and domain are defined.

## Mesh Type

Studio supports two mesh types.

| Mesh Type | When to Use |
|-----------|-------------|
| **Unstructured** | Recommended for most Studio workflows. Use it for production CFD, boundary-layer workflows, complex topology, imported meshes, and interoperability with external tools. |
| **Structured** | Use it for automated repeatable workflows, geometry screening, parametric studies, and cases where a structured approach fits the solver and validation target. |

Changing mesh type can change which settings are shown. Start with the unstructured option for standard CFD workflows, then switch to structured when the case requirements call for it.

## Core Resolution Controls

### Base Cell Size

The base cell size sets the coarse resolution of the mesh. Smaller values increase detail and cell count.

| Application | Typical Starting Point |
|------------|------------------------|
| Coarse preview | Large enough to generate quickly and validate setup. |
| Vehicle aerodynamics | Fine enough to resolve the body, wake, ground gap, and major features. |
| Detailed component analysis | Fine enough to resolve small gaps, fillets, and local gradients. |
| Thermal management | Fine enough to resolve heat sinks, cold plates, vents, and flow passages. |

```{tip}
Start coarse, verify the setup, then refine. A quick preview mesh often catches geometry, domain, and boundary-condition issues before you spend credits on a final mesh.
```

### Surface Resolution

Surface resolution controls how much detail is retained near geometry. Increase it when:

- Important features are under-resolved.
- Curved surfaces look faceted in the mesh view.
- Small gaps or passages affect the result.
- Forces, pressure drop, or heat-transfer quantities are sensitive to local geometry.

### Local Refinement

Use refinement zones to add resolution only where it is needed, such as wakes, jets, separation regions, rotating zones, constrictions, or thermal plumes. Local refinement helps control cell count while preserving accuracy in regions of interest.

### Near-Wall Resolution

Near-wall settings control the first cells adjacent to walls and are important for drag, pressure drop, separation, and heat transfer. Use the y+ calculator to choose settings that match your turbulence model and application.

See [Near-Wall Resolution](boundary-layers.md) for practical guidance.

## Cell Count Estimation

The final cell count depends on:

- Domain size
- Base cell size
- Surface resolution
- Local refinement zones
- Boundary-layer or near-wall settings
- Geometry complexity
- Mesh type

Studio estimates cell count before generation. Treat the estimate as a planning tool, then review the generated mesh quality report before running a simulation.

```{admonition} Cell Count Limits by Tier
:class: note

| Tier | Max Cells |
|------|-----------|
| Starter | 50 million |
| Pro | 100 million |
| Team | 500 million |
| Enterprise | Unlimited |
```

## Quality Targets

Mesh quality metrics indicate whether a mesh is suitable for simulation.

| Metric | What to Check |
|--------|---------------|
| **Skewness** | Lower values are better; review any highlighted regions before running. |
| **Non-orthogonality** | High values can reduce solver stability and accuracy. |
| **Aspect ratio** | High values can be acceptable near walls but should be intentional. |
| **Minimum volume** | Very small or invalid cells must be addressed before simulation. |
| **Connectivity** | Regions and interfaces should be connected as intended. |

See [Mesh Quality](mesh-quality.md) for details on interpreting reports.

## Recommended Workflow

1. Generate a coarse mesh to validate setup.
2. Review named surfaces, regions, and quality metrics.
3. Add local refinement where physics or geometry require it.
4. Check near-wall resolution for turbulence and heat-transfer cases.
5. Run a mesh sensitivity study for final engineering results.

## Meshing Time

Typical generation time depends on mesh type, cell count, geometry complexity, and current cloud resources.

| Mesh Size | Typical Time |
|-----------|-------------|
| < 5 million cells | 1 - 3 minutes |
| 5 - 20 million cells | 3 - 8 minutes |
| 20 - 100 million cells | 8 - 30 minutes |
| > 100 million cells | 30 minutes - 1 hour |

Monitor progress in the **Logs** panel and review the final quality report before launching a simulation.
