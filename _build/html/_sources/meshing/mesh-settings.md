# Mesh Settings

Mesh settings control the resolution, quality, and structure of the generated mesh. These parameters are configured in the **Mesh Settings** tab.

## How the Mesher Works

Gradient Dynamics uses a **structured Cartesian cut-cell** mesher with **block-based Adaptive Mesh Refinement (AMR)**. This approach is purpose-built for GPU-native simulation.

### Cartesian Block AMR

The domain is divided into a regular grid of **blocks**, each containing a fixed array of Cartesian (hexahedral) cells. Where higher resolution is needed — near surfaces, in wakes, or in user-defined zones — blocks are recursively refined by splitting each block into eight sub-blocks at double the resolution. This produces a fully structured, hierarchical mesh.

```{admonition} Why Cartesian Block AMR?
:class: note

Structured Cartesian meshes are the optimal topology for GPU-accelerated simulation. Their regular, predictable memory layout enables fully coalesced memory access patterns, branch-free compute kernels, and maximum utilization of GPU L1/L2 cache — resulting in significantly faster solves compared to unstructured mesh topologies.
```

### Cut-Cell Geometry Representation

Where Cartesian blocks intersect a solid geometry surface, the cells are **cut** by the geometry boundary to form partial cells that conform to the surface. This means:

- No geometry approximation — surfaces are represented exactly at the finest AMR level
- No prismatic boundary layer extrusion required
- Near-wall resolution is achieved by AMR block refinement near surfaces (see [Near-Wall Resolution](boundary-layers.md))

The result is a mesh that is structurally regular everywhere except at geometry boundaries, where cut-cells provide an accurate surface representation.

## Core Parameters

### Base Cell Size

The **base cell size** sets the resolution of the coarsest level of the block grid. All refinement levels subdivide from this baseline.

| Application | Typical Base Cell Size |
|------------|------------------------|
| Coarse preview | 0.5 – 1.0 m |
| Vehicle aerodynamics (medium) | 0.05 – 0.2 m |
| Detailed component analysis | 0.01 – 0.05 m |
| Small-scale electronics | 0.001 – 0.01 m |

```{tip}
Start with a coarser base cell size to verify your setup, then refine. A coarse mesh generates in seconds and lets you catch configuration errors early.
```

### AMR Refinement Levels

Controls the maximum depth of block refinement. Each level doubles the resolution (halves the cell size) in all three dimensions.

| Max AMR Level | Finest Cell Size (relative to base) | Use Case |
|---------------|--------------------------------------|----------|
| 3 | 1/8 base | Quick preview, large domains |
| 4 | 1/16 base | General-purpose CFD |
| 5 | 1/32 base | Detailed analysis |
| 6 | 1/64 base | High-fidelity near-wall resolution, LES |

The mesher applies refinement automatically based on proximity to surfaces and user-defined refinement zones. You set the maximum number of levels; the mesher decides where to apply them.

### Surface Refinement

Controls the number of AMR levels applied in blocks that intersect or are adjacent to geometry surfaces. Higher values produce finer cut-cells at the geometry boundary.

| Setting | Description |
|---------|-------------|
| **Coarse** | 2 levels near surfaces |
| **Medium** | 3–4 levels near surfaces (default) |
| **Fine** | 5 levels near surfaces |
| **Very Fine** | 6 levels — use for LES or high-detail geometry |

### Curvature-Based Refinement

When enabled, the mesher automatically increases refinement levels in blocks adjacent to regions of high surface curvature (tight fillets, leading edges, rounded geometry). This captures curved features accurately without manual zone configuration.

## Cell Count Estimation

The number of cells in your mesh depends on:

- **Domain volume** — Larger domains require more coarse-level blocks
- **Base cell size** — Smaller base size = more blocks (cubic relationship)
- **Max AMR levels** — Each additional level can multiply local cell count by up to 8×
- **Geometry complexity** — More surface area and curvature drives more surface refinement blocks

```{admonition} Cell Count Limits by Tier
:class: note

| Tier | Max Cells |
|------|-----------|
| Starter | 50 million |
| Pro | 100 million |
| Team | 500 million |
| Enterprise | Unlimited |
```

## Mesh Quality

Cartesian cut-cell block AMR meshes have inherently excellent quality in the bulk of the domain — all Cartesian cells have zero skewness and perfect orthogonality by construction. Quality metrics are only relevant at the cut-cell layer adjacent to geometry surfaces.

| Metric | Target | Description |
|--------|--------|-------------|
| **Cut-cell volume fraction** | > 0.1 | Minimum ratio of cut-cell volume to full-cell volume — very small slivers are merged |
| **Non-orthogonality** | < 70° | Relevant only at cut-cell faces |
| **Aspect ratio** | < 100 | Near-wall AMR blocks can be refined anisotropically if needed |

The mesher automatically merges or adjusts very small cut-cell slivers to maintain solver stability.

See [Mesh Quality](mesh-quality.md) for details on interpreting quality metrics after mesh generation.

## Meshing Time

After clicking **Generate Mesh**, the job runs on cloud GPUs. Typical generation times:

| Mesh Size | Typical Time |
|-----------|-------------|
| < 5 million cells | 1 – 3 minutes |
| 5 – 20 million cells | 3 – 8 minutes |
| 20 – 100 million cells | 8 – 30 minutes |
| > 100 million cells | 30 minutes – 1 hour |

As a rough guide, expect **1–10 million cells per minute** — simpler geometries and lower AMR levels are at the faster end; complex surfaces with many AMR levels are at the slower end. Monitor progress in the **Logs** panel.
