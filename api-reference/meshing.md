# Meshing objects

```{py:module} gradientdynamics.meshing
:no-index:
```

Meshing objects describe intent and validation constraints. Submitting a
configuration through {py:meth}`gradientdynamics.Geometry.mesh` returns a
typed asynchronous {py:class}`gradientdynamics.jobs.Job` whose result is a
{py:class}`gradientdynamics.Mesh`.

## Prism layers

````{py:class} PrismLayers(*, count: int, first_height: float, growth_rate: float = 1.2)

Near-wall prism-layer definition. Lengths use the geometry coordinate system.

```{py:attribute} count
:type: int

Number of prism layers. Must be non-negative.
```

```{py:attribute} first_height
:type: float

Height of the wall-adjacent layer.
```

```{py:attribute} growth_rate
:type: float

Ratio between successive layer heights.
```
````

## Local refinement

````{py:class} RefinementBox(*, minimum: tuple[float, float, float], maximum: tuple[float, float, float], spacing: float, name: str | None = None)

Axis-aligned volume refinement.

```{py:attribute} minimum
:type: tuple[float, float, float]
```

```{py:attribute} maximum
:type: tuple[float, float, float]
```

```{py:attribute} spacing
:type: float

Target Cartesian spacing inside the box.
```
````

## External-flow configuration

````{py:class} PrismOctreeConfig(*, domain_min: tuple[float, float, float], domain_max: tuple[float, float, float], target_cell_count: int, minimum_spacing: float, maximum_spacing: float, prism_layers: PrismLayers | None = None, refinement_boxes: Sequence[RefinementBox] = (), surface_preparation: str = "auto", output_format: str = "cgns")

Configuration for an external-flow prism–octree mesh.

```{py:attribute} domain_min
:type: tuple[float, float, float]

Minimum corner of the fluid domain.
```

```{py:attribute} domain_max
:type: tuple[float, float, float]

Maximum corner of the fluid domain.
```

```{py:attribute} target_cell_count
:type: int

Requested global cell-count target. The realised count is reported by the
completed mesh manifest.
```

```{py:attribute} minimum_spacing
:type: float

Smallest permitted octree spacing.
```

```{py:attribute} maximum_spacing
:type: float

Coarsest permitted octree spacing.
```

```{py:attribute} prism_layers
:type: PrismLayers | None

Optional wall-layer definition.
```

```{py:attribute} refinement_boxes
:type: Sequence[RefinementBox]

Local volume-refinement requests, applied in sequence.
```

```{py:method} model_dump() -> dict[str, Any]

Return a JSON-compatible representation for audit or persistence.
```
````

```python
from gradientdynamics.meshing import (
    PrismLayers,
    PrismOctreeConfig,
    RefinementBox,
)

config = PrismOctreeConfig(
    domain_min=(-5.0, -2.0, -1.0),
    domain_max=(12.0, 2.0, 4.0),
    minimum_spacing=0.01,
    maximum_spacing=0.50,
    target_cell_count=5_000_000,
    surface_preparation="auto",
    prism_layers=PrismLayers(
        count=14,
        first_height=0.00025,
        growth_rate=1.2,
    ),
    refinement_boxes=[
        RefinementBox(
            name="wake",
            minimum=(-1.0, -1.0, -0.2),
            maximum=(8.0, 1.0, 2.0),
            spacing=0.04,
        )
    ],
)

mesh = geometry.mesh(config).wait().result()
print(mesh.cell_count)
print(mesh.manifest.quality)
```

The values are illustrative. Determine domain size, first-layer height and
refinement from the case physics and validation target.

## Multi-region CHT configuration

````{py:class} CHTMeshConfig(*, target_cell_count: int, material_regions: Mapping[str, str], interfaces: Sequence[tuple[str, str]], minimum_spacing: float | None = None, maximum_spacing: float | None = None, output_format: str = "cgns")

Configuration for a named multi-solid STEP assembly.

```{py:attribute} material_regions
:type: Mapping[str, str]

Mapping from STEP body names to material-region labels.
```

```{py:attribute} interfaces
:type: Sequence[tuple[str, str]]

Expected touching-region pairs. Missing or unexpected topology is rejected
rather than silently changing the region model.
```
````

```python
from gradientdynamics.meshing import CHTMeshConfig

assembly = project.geometry.upload("cold-plate.step")

mesh = assembly.mesh(
    CHTMeshConfig(
        target_cell_count=8_000_000,
        material_regions={
            "fluid_volume": "coolant",
            "cold_plate": "aluminium",
            "heater": "copper",
        },
        interfaces=[
            ("coolant", "aluminium"),
            ("aluminium", "copper"),
        ],
    )
).wait().result()
```

## Mesh manifest

````{py:class} MeshManifest

Realised mesh counts, quality metrics, timings and provenance.

```{py:attribute} cell_count
:type: int
```

```{py:attribute} boundary_count
:type: int
```

```{py:attribute} region_counts
:type: Mapping[str, int]
```

```{py:attribute} quality
:type: Mapping[str, float]
```

```{py:attribute} elapsed_seconds
:type: float
```
````
