# Preprocessing

Preprocessing turns imported geometry into a simulation-ready model with
explicit domains, regions and boundary names.

## Import and inspect

Upload a supported CAD, surface or mesh file. Confirm the model scale before
doing anything else. Use the 3D viewer to check orientation, extents, missing
parts and unexpectedly small features.

Studio can analyse surface geometry for open edges, disconnected components,
degenerate elements and other conditions that can prevent robust volume
meshing. Repair or simplify only after deciding which features affect the
engineering quantity.

## Prepare geometry

- Remove duplicate or irrelevant parts.
- Preserve gaps, passages, leading edges and thermal contact areas that control
  the physics.
- Define an external farfield or identify the internal fluid volume.
- Split solids by material for conjugate heat transfer.
- Create named surfaces for every boundary condition and requested component
  output.

## Named surfaces

Stable names are part of the simulation contract. Prefer names such as
`inlet_main`, `outlet`, `vehicle_body`, `ground`, `heat_sink` and
`symmetry` over names inherited from a CAD export. A named surface can be used
by meshing controls, boundary conditions, rotating-wall definitions and force
or heat-transfer outputs.

## Multi-region models

For conjugate heat transfer, use a multi-solid STEP assembly with distinct,
named solids. Studio prepares shared interfaces and retains material regions in
the mesh. Review the region list and expected contacts before launching the
mesh job; missing or unintended contact changes the thermal problem.

```{tip}
Keep an untouched geometry revision in the project. Create a prepared revision
for defeaturing and naming so downstream changes remain auditable.
```
