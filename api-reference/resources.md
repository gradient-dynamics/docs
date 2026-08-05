# Core objects

```{py:currentmodule} gradientdynamics
```

The object model preserves the ownership and provenance relationships used in
Studio. Identifiers are stable, opaque strings; revisions are immutable once
used by a completed downstream resource.

## Project collections

````{py:class} ProjectCollection

Organisation-scoped access to engineering projects.

```{py:method} create(*, name: str, description: str | None = None) -> Project

Create a project and return its initial revision.
```

```{py:method} get(project_id: str) -> Project

Retrieve one project by opaque identifier.
```

```{py:method} list(*, limit: int = 50, cursor: str | None = None) -> Page[Project]

Return a cursor-paginated project page.
```
````

## Project

````{py:class} Project

Ownership and traceability boundary for one engineering study.

```{py:attribute} id
:type: str

Opaque project identifier.
```

```{py:attribute} name
:type: str

Human-readable project name.
```

```{py:attribute} geometry
:type: GeometryCollection

Versioned CAD and surface assets owned by this project.
```

```{py:attribute} meshes
:type: MeshCollection

Generated and imported meshes owned by this project.
```

```{py:attribute} simulations
:type: SimulationCollection

Simulation definitions and their revision history.
```

```{py:attribute} solutions
:type: SolutionCollection

Accepted results produced inside this project.
```
````

## Geometry

````{py:class} Geometry

A versioned CAD or surface asset prepared for meshing.

```{py:attribute} id
:type: str
```

```{py:attribute} filename
:type: str
```

```{py:attribute} revision
:type: int
```

```{py:attribute} named_surfaces
:type: tuple[str, ...]

Boundary names discovered or assigned during preparation.
```

```{py:method} mesh(config: meshing.PrismOctreeConfig | meshing.CHTMeshConfig, *, idempotency_key: str | None = None) -> jobs.Job[Mesh]

Validate the geometry and submit an asynchronous mesh operation.
```
````

Upload through the parent project:

```python
geometry = project.geometry.upload(
    "vehicle.stl",
    named_surfaces="vehicle-surfaces.zip",
)
```

## Mesh

````{py:class} Mesh

A completed volume mesh with boundary patches, cell zones, quality metrics and
provenance.

```{py:attribute} id
:type: str
```

```{py:attribute} cell_count
:type: int
```

```{py:attribute} boundaries
:type: tuple[str, ...]
```

```{py:attribute} regions
:type: tuple[str, ...]
```

```{py:attribute} manifest
:type: meshing.MeshManifest
```

```{py:attribute} simulations
:type: SimulationCollection

Factory for simulations tied to this exact mesh revision.
```

```{py:method} download(path: str | Path, *, format: str = "cgns") -> Path

Download the interoperable mesh asset.
```
````

## Simulation

````{py:class} Simulation

A validated FluxCore physics, run-control and output definition associated with
one immutable mesh revision.

```{py:attribute} id
:type: str
```

```{py:attribute} mesh
:type: Mesh
```

```{py:attribute} config
:type: fluxcore.SimulationConfig
```

```{py:method} run(*, idempotency_key: str | None = None) -> jobs.Job[Solution]

Allocate managed FluxCore capacity and start the simulation.
```
````

## Solution

````{py:class} Solution

Accepted result of one simulation revision. A solution keeps its exact mesh,
configuration, deployment version, histories and field assets together.

```{py:attribute} id
:type: str
```

```{py:attribute} simulation
:type: Simulation
```

```{py:attribute} outputs
:type: outputs.OutputCollection
```

```{py:attribute} histories
:type: outputs.HistoryCollection
```

```{py:attribute} fields
:type: outputs.FieldCollection
```
````
