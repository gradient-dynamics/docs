# Output and monitoring controls

```{py:currentmodule} gradientdynamics.fluxcore
```

Output scheduling is explicit about its clock. Histories, forces, fields and
checkpoints can be emitted by pseudo-step, physical step, simulated time or at
completion without confusing inner convergence work with physical evolution.

## Output schedule

````{py:class} OutputSchedule(*, history_every_pseudo_steps: int | None = 10, forces_every_pseudo_steps: int | None = 10, fields_every_pseudo_steps: int | None = None, checkpoint_every_pseudo_steps: int | None = 250, history_every_physical_steps: int | None = 1, forces_every_physical_steps: int | None = 1, fields_every_physical_steps: int | None = 1, surfaces_every_physical_steps: int | None = 1, checkpoint_every_physical_steps: int | None = 100, every_simulated_time: float | None = None, write_initial: bool = False, write_final: bool = True)

Cadences for scalar histories, forces, fields, surfaces and restart state.

```{py:attribute} history_every_pseudo_steps
:type: int | None

Residual and scalar-monitor cadence during pseudo-time advancement.
```

```{py:attribute} forces_every_pseudo_steps
:type: int | None

Integrated force and moment cadence during pseudo-time advancement.
```

```{py:attribute} fields_every_pseudo_steps
:type: int | None

Volume-field cadence in pseudo-steps. Usually disabled because full fields are
substantially larger than histories.
```

```{py:attribute} history_every_physical_steps
:type: int | None

History cadence on accepted physical steps.
```

```{py:attribute} fields_every_physical_steps
:type: int | None

Volume-field cadence on accepted physical steps.
```

```{py:attribute} every_simulated_time
:type: float | None

Optional output cadence in simulated seconds, independent of step count.
```
````

## Field selection

````{py:class} FieldOutput(*, fields: Sequence[str] = ("velocity", "pressure"), derived_fields: Sequence[str] = (), surfaces: Sequence[str] = (), volume_format: str = "cgns", surface_format: str = "vtk", precision: str = "single", compression: str = "balanced", include_cell_ids: bool = False)

Volume and surface field selection.

```{py:attribute} fields
:type: Sequence[str]

Primary solution fields to export. Available fields depend on enabled physics.
```

```{py:attribute} derived_fields
:type: Sequence[str]

Requested derived quantities such as vorticity, wall shear, heat flux,
temperature gradient, turbulent viscosity or Q-criterion.
```

```{py:attribute} surfaces
:type: Sequence[str]

Named patches included in surface results. Empty selects all solution patches.
```

```{py:attribute} precision
:type: Literal["single", "double"]
```

```{py:attribute} compression
:type: Literal["none", "fast", "balanced", "maximum"]
```
````

## Statistical sampling

````{py:class} StatisticsOutput(*, start_after_physical_steps: int = 0, sample_for_physical_steps: int | None = None, sample_every_physical_steps: int = 1, mean_fields: Sequence[str] = ("velocity", "pressure"), rms_fields: Sequence[str] = (), covariance_fields: Sequence[tuple[str, str]] = (), reset_on_restart: bool = False)

Online time statistics for URANS, DES and DDES workflows.

```{py:attribute} start_after_physical_steps
:type: int

Washout period excluded from statistics.
```

```{py:attribute} sample_for_physical_steps
:type: int | None

Sampling-window length. `None` samples until the run completes.
```

```{py:attribute} sample_every_physical_steps
:type: int

Accepted physical-step cadence for accumulator updates.
```

```{py:attribute} rms_fields
:type: Sequence[str]

Fields for which root-mean-square fluctuation statistics are accumulated.
```
````

## Force and moment monitoring

````{py:class} ForceMonitor(*, name: str, surfaces: Sequence[str], direction: tuple[float, float, float] | None = None, moment_center: tuple[float, float, float] | None = None, reference_frame: str = "global", reference_values: ReferenceValues | None = None, per_surface: bool = False, pressure: bool = True, viscous: bool = True, rolling_average: int | None = None, convergence_window: int | None = None, convergence_delta: float | None = None)

Integrated loads, coefficients and optional convergence monitoring.

```{py:attribute} per_surface
:type: bool

Report each surface separately in addition to the aggregate load.
```

```{py:attribute} pressure
:type: bool

Include pressure loads.
```

```{py:attribute} viscous
:type: bool

Include viscous loads.
```

```{py:attribute} rolling_average
:type: int | None

Number of accepted samples in the trailing reported average.
```

```{py:attribute} convergence_delta
:type: float | None

Maximum coefficient range across {py:attr}`convergence_window` required for a
force-based convergence signal.
```
````

## Aggregate output controls

````{py:class} OutputControls(*, schedule: OutputSchedule = OutputSchedule(), fields: FieldOutput | None = None, statistics: StatisticsOutput | None = None, forces: Sequence[ForceMonitor] = (), live_history_interval: float = 2.0, stream_linear_history: bool = False, callback_url: str | None = None, callback_headers: Mapping[str, str] | None = None, validation_metadata: Mapping[str, Any] | None = None)

Output, live monitoring and provenance policy.

```{py:attribute} live_history_interval
:type: float

Minimum wall-clock seconds between Studio live-history updates.
```

```{py:attribute} stream_linear_history
:type: bool

Include GPU-native linear convergence traces in live monitoring.
```

```{py:attribute} validation_metadata
:type: Mapping[str, Any] | None

Case, reference, revision and experiment metadata stored with the solution.
```
````

## Output example

```python
from gradientdynamics.fluxcore import (
    FieldOutput,
    ForceMonitor,
    OutputControls,
    OutputSchedule,
    StatisticsOutput,
)

output_controls = OutputControls(
    schedule=OutputSchedule(
        history_every_pseudo_steps=5,
        forces_every_pseudo_steps=10,
        fields_every_pseudo_steps=None,
        fields_every_physical_steps=20,
        checkpoint_every_physical_steps=100,
    ),
    fields=FieldOutput(
        fields=("velocity", "pressure", "temperature"),
        derived_fields=("wall_shear", "heat_flux", "q_criterion"),
        surfaces=("vehicle", "wheels"),
    ),
    statistics=StatisticsOutput(
        start_after_physical_steps=2_000,
        sample_for_physical_steps=10_000,
        mean_fields=("velocity", "pressure"),
        rms_fields=("velocity", "pressure"),
    ),
    forces=(
        ForceMonitor(
            name="vehicle_drag",
            surfaces=("vehicle", "wheels"),
            direction=(1.0, 0.0, 0.0),
            per_surface=True,
            rolling_average=200,
        ),
    ),
    stream_linear_history=True,
    validation_metadata={"case": "DrivAer baseline", "revision": 4},
)
```
