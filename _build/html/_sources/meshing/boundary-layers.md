# Near-Wall Resolution

Accurate prediction of wall-bounded flows — drag, heat transfer, separation — depends on resolving the thin region of rapidly-changing velocity near solid surfaces. In Gradient Dynamics, near-wall resolution is achieved through **AMR block refinement** near geometry surfaces, without the need for traditional prismatic boundary layer extrusion.

## How It Works

The structured Cartesian cut-cell approach resolves near-wall flow by **recursively refining blocks** in the AMR hierarchy near geometry surfaces. The cut-cells at the geometry boundary form the wall-adjacent layer, and the resolution of those cells is set by the AMR level applied near the surface.

This is different from traditional unstructured meshing approaches, which grow prismatic "prism layers" from wall surfaces. With block AMR:

- Near-wall resolution is controlled by the **surface refinement level** setting
- The wall-adjacent cell size is `base_cell_size / 2^(AMR_levels_near_wall)`
- Resolution increases geometrically approaching the surface — similar in effect to growth-rate prism layers, but achieved through the block hierarchy
- No separate configuration of layer count, first-layer height, or growth rate is needed

## Wall Cell Size and y+

The y+ value of the first wall cell determines which wall treatment your turbulence model uses. You control y+ through the **near-wall AMR level** setting (in the Mesh Settings tab → Surface Refinement → Near-Wall Levels).

### Estimating Wall Cell Size

For a given near-wall AMR level `n` and base cell size `h`:

```
wall_cell_size ≈ h / 2^n
```

Use the **y+ calculator** in the Mesh Settings tab to compute the expected y+ for your flow speed and geometry scale.

### y+ Guidelines by Turbulence Model

| Turbulence Model | Target y+ | Near-Wall AMR | Wall Treatment |
|-----------------|-----------|---------------|----------------|
| k-ω SST | ~30 (wall function) | Medium (default) | Spalding or Reichardt |
| k-ω SST | ~1 (resolved) | Fine or Very Fine | None (resolved) |
| k-ε | 30 – 300 | Medium | Spalding or Reichardt |
| Spalart-Allmaras | ~1 or ~30 | Medium to Fine | Spalding or Linelets |
| RSM | ~30 or ~1 | Medium to Fine | Spalding or Reichardt |
| LES (any SGS model) | ~1 | Very Fine | None (resolved) |
| DES / DDES | ~1 – 30 | Fine | Spalding (RANS region) |

```{tip}
For most RANS simulations, the default **Medium** surface refinement with y+ ≈ 30 and **Spalding wall function** gives good results. Use **Fine** or **Very Fine** only when wall-resolved treatment is needed (LES, detailed heat transfer, or sensitive separation prediction). The **linelet** wall treatment offers a middle ground — wall-resolved accuracy at wall-function mesh resolution — and is particularly effective on Cartesian cut-cell meshes. See [Solver Settings](/simulation/solver-settings.md) for details on wall treatment options.
```

## Configuring Near-Wall Resolution

1. Navigate to the **Mesh Settings** tab
2. Under **Surface Refinement**, set the **Near-Wall Levels** slider
3. Use the **y+ Calculator** to verify the resulting wall cell size for your flow speed
4. Generate the mesh and check the reported y+ distribution in the **Mesh Quality** panel

## Anisotropic Near-Wall Refinement

For high-Reynolds-number flows where extreme wall resolution would be costly in all directions, enable **anisotropic near-wall refinement**. Instead of splitting blocks into 8 equal children (2×2×2), anisotropic refinement can split in selected directions only — for example, 2×1×1 in the wall-normal direction. This produces cells that are fine in the wall-normal direction but coarser in the wall-parallel directions, dramatically reducing cell count while maintaining the y+ target at the wall.

**How it works:**
- Blocks adjacent to geometry surfaces are tagged for directional refinement based on the local wall-normal direction
- The refinement direction is determined automatically from the geometry surface orientation
- 2:1 balance is still enforced between neighboring blocks to ensure smooth transitions
- The solver handles the resulting anisotropic cells natively — no special treatment required

**When to use anisotropic refinement:**
- High-Reynolds-number external aerodynamics where y+ ≈ 1 would otherwise produce excessive cell counts
- Cases where near-wall resolution is critical but far-field cell count must be controlled
- LES or DES simulations where wall-parallel resolution requirements are less stringent than wall-normal

```{note}
Anisotropic near-wall refinement is available on Pro tier and above.
```

## Mesh Quality Near Walls

The wall-adjacent cut-cells are the only cells that deviate from perfect Cartesian quality. The mesher automatically:

- Merges very small cut-cell slivers (volume fraction < 0.1) with neighboring cells
- Reports the minimum cut-cell volume fraction in the quality report
- Flags problematic cut-cells for inspection in the 3D viewer

High aspect-ratio cells in the near-wall region are expected and desirable — these are flagged informatively, not as errors.
