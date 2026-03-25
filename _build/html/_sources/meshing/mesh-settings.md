# Mesh Settings

Mesh settings control the resolution, quality, and structure of the generated mesh. These parameters are configured in the **Mesh Settings** tab.

## How the Mesher Works

Gradient Dynamics uses a **structured Cartesian cut-cell** mesher with **block-based Adaptive Mesh Refinement (AMR)**. This approach is purpose-built for GPU-native simulation and represents a fundamentally different paradigm from traditional unstructured mesh generation.

### Cartesian Block AMR

The domain is divided into a regular grid of **blocks**, each containing a fixed-size array of Cartesian (hexahedral) cells (typically 8×8×8 cells per block). Where higher resolution is needed — near surfaces, in wakes, or in user-defined zones — blocks are recursively refined by splitting each block into sub-blocks at double the resolution. This produces a fully structured, hierarchical mesh that can be stored and accessed sparsely — only blocks that contain fluid are allocated.

**How block refinement works:**

1. **Initial grid** — The domain is covered by a coarse uniform grid of blocks
2. **Refinement criteria** — Blocks are tagged for refinement based on geometry proximity, user-defined zones, curvature, or solution gradients
3. **Block splitting** — Tagged blocks are split into child blocks. For **isotropic refinement**, each block splits into 8 children (2×2×2), doubling resolution in all three directions. For **anisotropic refinement**, blocks can be split in selected directions only (e.g., 2×1×1 for wall-normal refinement), producing 2 or 4 children
4. **2:1 balancing** — The mesh enforces a maximum 2:1 refinement ratio between neighboring blocks, ensuring smooth transitions and numerical stability
5. **Sparse storage** — Only blocks classified as containing fluid or cut cells are retained; solid-interior blocks are discarded, keeping memory usage efficient

```{admonition} Why Cartesian Block AMR?
:class: note

Structured Cartesian meshes are the optimal topology for GPU-accelerated simulation. Every cell within a block has the same size and shape, enabling:

- **Coalesced memory access** — GPU threads access adjacent memory locations, maximizing bandwidth
- **Branch-free compute kernels** — No cell-type branching within blocks; all cells follow the same computation path
- **Cache efficiency** — Fixed block sizes fit naturally into GPU L1/L2 cache
- **Predictable parallelism** — Each block is an independent unit of work, enabling straightforward GPU workload distribution

The result is significantly faster solves compared to unstructured mesh topologies, with near-linear scaling across GPU cores.
```

### Cut-Cell Geometry Representation

Where Cartesian blocks intersect a solid geometry surface, the cells are **cut** by the geometry boundary to form partial cells that conform exactly to the surface shape. This is the key innovation that allows a structured Cartesian mesh to represent arbitrarily complex geometries.

**How cut-cell generation works:**

1. **Signed Distance Field (SDF)** — A distance field is computed from the geometry surface. Each point in space has a signed distance: negative inside the solid, positive in the fluid, zero on the surface
2. **Cell classification** — Every cell in geometry-adjacent blocks is classified as **fluid** (entirely outside the solid), **solid** (entirely inside), or **cut** (intersected by the surface)
3. **Hex clipping** — Cut cells are clipped against the SDF isosurface using geometric intersection algorithms, producing polyhedral cells that conform exactly to the geometry boundary
4. **Metric computation** — For each cut cell, the solver needs the **volume fraction** (ratio of fluid volume to full-cell volume), the **shifted centroid** (center of the fluid portion), and **face apertures** (the open area of each face)
5. **Small-cell treatment** — Very small cut cells (volume fraction below a threshold) are automatically merged with neighboring cells to prevent numerical instability. This is handled transparently by the mesher

**Key properties of cut-cell meshes:**

- **Exact geometry representation** — The surface is captured at the resolution of the finest AMR level with no facet approximation
- **No prismatic boundary layer extrusion** — Near-wall resolution is achieved through AMR block refinement near surfaces (see [Near-Wall Resolution](boundary-layers.md))
- **Automatic and robust** — No manual surface meshing, layer insertion, or mesh topology decisions required; the mesher handles all geometry-mesh intersection automatically
- **Solver-aware stabilization** — The solver applies specific treatments to cut cells (flux redistribution, cell merging) to maintain stability and accuracy at the geometry boundary

The result is a mesh that is structurally regular everywhere except at geometry boundaries, where cut cells provide an accurate, automatically generated surface representation.

```{admonition} Cut-Cell Quality
:class: tip
Because cut cells are the only non-Cartesian cells in the entire mesh, the vast majority of cells have perfect orthogonality, zero skewness, and uniform aspect ratio by construction. Mesh quality issues are confined to a thin layer of cut cells at the geometry surface, and the mesher handles these automatically through merging and metric correction.
```

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
