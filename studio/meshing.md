# Meshing

Studio's current production meshing engine builds prism–octree meshes for
external, internal and multi-region workflows.

## How the mesh is organised

An adaptive octree forms the volume core and distributes resolution across the
domain. Complete prism columns grow from resolved wall surfaces to capture
near-wall gradients. Transition cells connect the prism front to the octree
core. The resulting mesh carries named boundary patches, cell zones and quality
metadata into FluxCore.

This structure gives you fine wall-normal control without paying for the same
resolution everywhere in the domain.

## Main controls

| Control | Engineering effect |
|---|---|
| **Domain bounds** | Defines the computational extent and clearance around the model. |
| **Minimum spacing** | Limits the smallest octree cells in refined regions. |
| **Maximum spacing** | Limits the coarsest cells away from important geometry. |
| **Target cell count** | Sets the planning target used to calibrate global spacing. |
| **Refinement zones** | Preserve resolution in wakes, gaps, jets, rotating regions or thermal plumes. |
| **Prism-layer count** | Sets the number of near-wall layers. |
| **First-layer height** | Controls the wall-normal resolution at the surface. |
| **Growth rate** | Controls how rapidly prism thickness increases away from the wall. |

## External-flow workflow

Upload STL or a prepared surface archive, define the outer domain, select
surface preparation, choose a cell budget and configure prism layers. Studio
can preserve a clean surface or create a robust meshing surface when the input
is unsuitable. Always compare the prepared surface against the original
geometry in critical areas.

## Conjugate heat-transfer workflow

Upload a named multi-solid STEP assembly. The CHT route builds a shared,
conformal multi-region mesh with material cell zones and paired interfaces.
Specify the expected region names and contacts so topology mistakes fail early
instead of creating a plausible-looking but incorrect thermal model.

## Rotating regions

Define cylindrical rotating zones with a centre, axis, width, height and
rotational speed. Verify that the selected region contains the intended cells
and that rotating and non-rotating walls are named consistently.

## Quality and completion

The completed job includes the CGNS mesh and a manifest containing count,
quality and timing information. Review the realised cell count, prism coverage,
cell-quality limits, patch names, material zones and interfaces before creating
a simulation.

See the detailed [meshing guide](../meshing/index.md) for individual controls.
