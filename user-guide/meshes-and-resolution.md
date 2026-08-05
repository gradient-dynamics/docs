# Meshes and resolution

The mesh determines where the simulation can represent gradients. Put
resolution where it can change the engineering answer.

## Prism–octree meshes

Gradient Dynamics' current production meshing route combines an adaptive
octree volume mesh with near-wall prism layers. The octree efficiently places
hexahedral resolution across large domains and refinement zones. Prism columns
resolve the thin, anisotropic gradients next to walls. Transition cells join
the two regions while preserving a usable volume mesh for FluxCore.

This route is suited to external aerodynamics, internal flow, rotating zones
and multi-region thermal models. Clean STL and surface archives are accepted
for external workflows; multi-solid STEP assemblies support conformal
multi-region meshing.

## Resolution controls

- **Minimum spacing** controls the finest permitted octree scale.
- **Maximum spacing** controls the coarsest volume scale.
- **Target cell count** provides a planning target for the total mesh budget.
- **Refinement boxes** preserve resolution in wakes, passages, jets, thermal
  plumes and other regions of interest.
- **Prism layers, first-layer height and growth rate** control near-wall
  resolution.
- **Named surfaces and regions** carry engineering intent into boundary
  conditions, outputs and result review.

## A practical sensitivity study

1. Build a baseline mesh that resolves the known flow mechanisms.
2. Refine the wall, wake, gap or thermal region expected to control the output.
3. Re-run with otherwise identical physics and output definitions.
4. Compare the engineering quantity and the local fields that explain it.
5. Stop when the change is smaller than the tolerance required for the
   decision—not merely when the images look similar.

See [Meshing in Studio](../studio/meshing.md) for the product workflow.
