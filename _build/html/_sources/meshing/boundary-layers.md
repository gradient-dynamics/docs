# Near-Wall Resolution

Accurate wall-bounded simulations depend on resolving the region close to solid surfaces. Near-wall resolution affects drag, pressure drop, separation, heat transfer, and wall shear.

## Why It Matters

Wall-bounded flows contain steep velocity and temperature gradients near surfaces. If the mesh is too coarse near walls, results can show incorrect forces, pressure losses, heat-transfer rates, or separation behaviour.

## y+ Guidance

The y+ value describes how fine the wall-adjacent mesh is relative to the local flow. Studio includes a y+ calculator to help choose near-wall settings from flow speed, length scale, fluid properties, and turbulence model.

| Target | Typical Use |
|--------|-------------|
| **y+ around 1** | Wall-resolved studies, detailed heat transfer, LES-like workflows, sensitive separation prediction. |
| **y+ around 30** | General RANS engineering workflows with wall functions. |
| **y+ 30-300** | Some high-Reynolds-number wall-function workflows where global trends are more important than local wall detail. |

```{tip}
For most first-pass RANS simulations, start with the default near-wall settings and use the y+ calculator before committing to a final mesh.
```

## Configuring Near-Wall Resolution

1. Open the **Mesh Settings** tab.
2. Select the mesh type and base resolution.
3. Set the near-wall or boundary-layer controls.
4. Use the **y+ Calculator** for the expected operating condition.
5. Generate the mesh and review y+ and quality metrics in the **Mesh Quality** panel.

## Structured and Unstructured Meshes

Both structured and unstructured meshing workflows include near-wall controls. The exact controls differ by mesh type, but the engineering goal is the same: place enough resolution near walls for the selected turbulence model and quantity of interest.

## Practical Checks

- Review wall-adjacent quality warnings before running.
- Check y+ distribution, not only the average value.
- Refine locally near leading edges, separation points, heat sources, and narrow gaps.
- Keep final settings consistent across comparative design studies.
- Perform a mesh sensitivity check for final reported results.
