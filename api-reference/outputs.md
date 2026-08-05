# Solutions and outputs

```{py:module} gradientdynamics.outputs
:no-index:
```

A completed {py:class}`gradientdynamics.Solution` contains summary metadata,
convergence histories, requested engineering quantities and downloadable field
assets.

## Asset

````{py:class} Asset

Downloadable result asset.

```{py:attribute} name
:type: str
```

```{py:attribute} format
:type: str

Examples include `cgns`, `vtu`, `vtp`, `pvd`, `json` and `csv`.
```

```{py:attribute} size_bytes
:type: int | None
```

```{py:method} download(path: str | Path, *, overwrite: bool = False) -> Path

Download the asset and return the local path.
```
````

## Field collection

````{py:class} FieldCollection

Field and surface assets attached to a solution.

```{py:method} list(*, format: str | None = None) -> tuple[Asset, ...]

List available field assets, optionally filtered by format.
```

```{py:method} download(path: str | Path, *, format: str = "cgns", overwrite: bool = False) -> Path

Download the preferred volume-field asset.
```
````

## History

````{py:class} History

Named residual or engineering-monitor series.

```{py:attribute} name
:type: str
```

```{py:attribute} x
:type: Sequence[float]

Iteration, physical time or sample coordinate.
```

```{py:attribute} values
:type: Sequence[float]
```

```{py:method} to_dataframe() -> pandas.DataFrame

Convert the series to a two-column data frame.
```
````

## Force result

````{py:class} ForceResult

Integrated force and moment result produced by a named
{py:class}`gradientdynamics.fluxcore.ForceOutput`.

```{py:attribute} force
:type: tuple[float, float, float]
```

```{py:attribute} moment
:type: tuple[float, float, float] | None
```

```{py:attribute} coefficient
:type: float | None

Primary requested coefficient, such as drag coefficient.
```

```{py:attribute} pressure_contribution
:type: tuple[float, float, float] | None
```

```{py:attribute} viscous_contribution
:type: tuple[float, float, float] | None
```
````

## Reading a solution

```python
solution = simulation.run().wait().result()

drag = solution.outputs["vehicle_loads"]
print(f"CD = {drag.coefficient:.4f}")

residuals = solution.histories["continuity"].to_dataframe()
solution.fields.download("solution.cgns")
```

Field availability depends on simulation type and requested output definition:

- **CGNS** preserves interoperable mesh and solution data.
- **VTU** provides unstructured volume fields for VTK-compatible tools.
- **VTP** provides selected boundary surfaces and fields.
- **PVD and snapshots** describe optional time-resolved series.

Time-series manifests preserve snapshot order, physical time, shared topology
and available fields. Copy required assets into governed organisational storage
before a preview retention period expires, and preserve the solution summary
and manifest so units, revisions and reference values remain interpretable.
