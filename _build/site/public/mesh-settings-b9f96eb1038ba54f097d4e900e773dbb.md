# Mesh Settings

Mesh settings control the resolution, quality, and structure of the generated mesh. These parameters are configured in the **Mesh Settings** tab.

## Core Parameters

### Target Cell Size

The **base cell size** sets the overall resolution of the mesh in the bulk of the domain. Smaller values produce finer meshes with more cells.

| Application | Typical Cell Size |
|------------|-------------------|
| Coarse preview | 0.5 – 1.0 m |
| Vehicle aerodynamics (medium) | 0.05 – 0.2 m |
| Detailed component analysis | 0.01 – 0.05 m |
| Small-scale electronics | 0.001 – 0.01 m |

```{tip}
Start with a coarser mesh to verify your setup, then refine. A coarse mesh runs in seconds and lets you catch configuration errors early.
```

### Minimum Cell Size

The smallest cell the mesher will create. This prevents excessive refinement in tight geometric features that could produce millions of unnecessary cells.

Set this to roughly **1/10th to 1/100th** of your target cell size, depending on the geometric detail you need to resolve.

### Refinement Levels

Controls the **octree depth** — how many times the mesh can subdivide to capture geometric features. Higher values allow finer resolution near surfaces.

| Level | Relative Size | Use Case |
|-------|--------------|----------|
| 6 | Coarse | Quick preview, large domains |
| 8 | Medium | General-purpose CFD |
| 10 | Fine | Detailed analysis |
| 12 | Very fine | Boundary layer resolution, LES |

## Mesh Generation

### How It Works

Gradient Dynamics uses an **adaptive octree** meshing approach:

1. The domain is divided into a regular grid of hexahedral cells
2. Cells near the geometry surface are recursively refined (subdivided into 8 smaller cells)
3. **Transition layers** of pyramids smooth the size changes between refinement levels
4. **Boundary layer prisms** are grown from wall surfaces (if enabled)
5. The result is a hex-dominant mesh with pyramidal transitions and prismatic boundary layers

This approach produces meshes with:
- Excellent quality metrics (low skewness, good orthogonality)
- Efficient cell counts (fine only where needed)
- Good solver convergence properties

### Curvature-Based Refinement

When enabled, the mesher automatically refines cells in areas of high surface curvature. This captures curved features (fillets, leading edges, rounded bodies) without requiring manual refinement zones.

## Cell Count Estimation

The number of cells in your mesh depends on:

- **Domain volume** — Larger domains = more cells
- **Target cell size** — Smaller cells = more cells (cubic relationship)
- **Refinement levels** — Higher refinement = more cells near surfaces
- **Boundary layers** — Add significant cell count near walls

```{admonition} Cell Count Limits by Tier
:class: note

| Tier | Max Cells |
|------|-----------|
| Free | 2 million |
| Starter | 50 million |
| Pro | 100 million |
| Team | 500 million |
| Enterprise | Unlimited |
```

## Mesh Quality Targets

The mesher automatically optimizes for quality during generation. Key quality targets:

| Metric | Target | Description |
|--------|--------|-------------|
| **Skewness** | < 0.85 | Measures cell shape distortion |
| **Non-orthogonality** | < 70° | Angle between face normal and cell-to-cell vector |
| **Aspect ratio** | < 100 | Ratio of longest to shortest cell dimension |

See [Mesh Quality](mesh-quality.md) for details on interpreting quality metrics after mesh generation.
