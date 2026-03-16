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

| Turbulence Model | Target y+ | Near-Wall AMR |
|-----------------|-----------|---------------|
| k-ω SST | ~30 (wall function) | Medium (default) |
| k-ω SST | ~1 (resolved) | Fine or Very Fine |
| k-ε | 30 – 300 | Medium |
| Spalart-Allmaras | ~1 or ~30 | Medium to Fine |

```{tip}
For most RANS simulations, the default **Medium** surface refinement with y+ ≈ 30 (wall function) gives good results. Use **Fine** or **Very Fine** only when wall-resolved treatment is needed (LES, detailed heat transfer, or sensitive separation prediction).
```

## Configuring Near-Wall Resolution

1. Navigate to the **Mesh Settings** tab
2. Under **Surface Refinement**, set the **Near-Wall Levels** slider
3. Use the **y+ Calculator** to verify the resulting wall cell size for your flow speed
4. Generate the mesh and check the reported y+ distribution in the **Mesh Quality** panel

## Anisotropic Near-Wall Refinement

For high-Reynolds-number flows where extreme wall resolution would be costly in all directions, enable **anisotropic near-wall refinement**. This refines blocks in the wall-normal direction more aggressively than in the wall-parallel directions, reducing cell count while maintaining y+ targets.

```{note}
Anisotropic near-wall refinement is available on Pro tier and above.
```

## Mesh Quality Near Walls

The wall-adjacent cut-cells are the only cells that deviate from perfect Cartesian quality. The mesher automatically:

- Merges very small cut-cell slivers (volume fraction < 0.1) with neighboring cells
- Reports the minimum cut-cell volume fraction in the quality report
- Flags problematic cut-cells for inspection in the 3D viewer

High aspect-ratio cells in the near-wall region are expected and desirable — these are flagged informatively, not as errors.
