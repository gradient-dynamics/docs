# Boundary Layers

Boundary layers are thin layers of prismatic cells grown from wall surfaces. They are **essential** for accurately capturing the velocity gradient near walls in CFD simulations, which directly affects drag, heat transfer, and separation predictions.

## Why Boundary Layers Matter

In real fluid flow, velocity changes rapidly from zero at a solid wall (no-slip condition) to the freestream value over a thin region called the boundary layer. To resolve this gradient accurately, the mesh needs:

- Very thin cells at the wall
- Gradually expanding cells moving away from the wall
- Alignment of cell faces parallel to the wall surface

Without boundary layers, the solver must interpolate across large cells near walls, leading to inaccurate wall shear stress and heat transfer predictions.

## Configuration Parameters

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| **Number of layers** | Total prism layers grown from the wall | 5 – 15 |
| **First layer height** | Thickness of the cell immediately adjacent to the wall | 0.00001 – 0.001 m |
| **Growth rate** | Ratio of each layer's thickness to the previous one | 1.15 – 1.2 |

### First Layer Height and y+

The **first layer height** determines the y+ value at the wall, which must match your turbulence model's requirements:

| Turbulence Model | Target y+ | Description |
|-----------------|-----------|-------------|
| k-ω SST | ~1 (resolved) or ~30 (wall function) | y+ ≈ 30 is the practical default |
| k-ε | 30 – 300 | Wall function approach |
| Spalart-Allmaras | ~1 or ~30 | Flexible, works with both |

```{admonition} y+ Rule of Thumb
:class: tip

For a target y+ of 30 (standard RANS):
- **Highway vehicle (30 m/s):** First layer height ≈ 0.001 m
- **Race car (80 m/s):** First layer height ≈ 0.0003 m
- **Aircraft cruise (250 m/s):** First layer height ≈ 0.00005 m

These are approximate — use the y+ calculator in the Mesh Settings tab for precise values based on your flow conditions.
```

### Number of Layers

More layers provide a smoother transition from the wall to the volume mesh:

- **5 layers** — Minimum for wall-function RANS (y+ ≈ 30)
- **10 layers** — Good balance for most RANS simulations
- **15+ layers** — Recommended for wall-resolved simulations (y+ ≈ 1)

### Growth Rate

Controls how quickly layers expand away from the wall:

- **1.15** — Conservative growth, more layers needed but smoother transition
- **1.2** — Standard for most applications
- **1.3+** — Aggressive growth, may cause quality issues at the transition to volume cells

```{admonition} Quality Consideration
:class: warning
If the growth rate is too high, the last boundary layer cell may be much larger than the adjacent volume cell, causing a poor quality transition. Keep growth rate below 1.25 for best results.
```

## Where Boundary Layers Are Applied

Boundary layers are grown from **wall-type** surfaces:

- Geometry surfaces (car body, wing surface, pipe wall)
- Ground plane (if enabled)

They are **not** grown from:

- Inlet and outlet boundaries
- Symmetry planes
- Far-field boundaries

## Enabling Boundary Layers

1. Navigate to the **Mesh Settings** tab
2. Toggle **Boundary Layers** to **Enabled**
3. Set the number of layers, first layer height, and growth rate
4. Optionally use the y+ calculator to determine the correct first layer height

```{note}
Boundary layers require a Starter tier or higher subscription.
```

## Troubleshooting

### Layers colliding with nearby surfaces
If two wall surfaces are very close together, boundary layers from each side can collide. The mesher automatically detects this and reduces layers in tight gaps.

### Poor quality at layer termination
Where boundary layers end (e.g., at the trailing edge of a wing), there can be quality issues. Adding a refinement zone in these areas helps smooth the transition.

### High aspect ratio warnings
Boundary layer cells are intentionally thin (high aspect ratio). This is expected and desirable — the warning can be disregarded for BL cells specifically. Aspect ratios of 100+ are normal for boundary layer prisms.
