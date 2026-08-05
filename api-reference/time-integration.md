# Time integration

```{py:currentmodule} gradientdynamics.fluxcore
```

FluxCore distinguishes physical time from pseudo-time. Physical time advances
the simulated system. Pseudo-time is the nonlinear work used to converge a
steady state or the implicit equations inside one physical step.

## Pseudo-time step methods

````{py:class} FixedPseudoTimeStep(*, value: float)

Use a fixed pseudo-time increment in seconds.

```{py:attribute} value
:type: float
```
````

````{py:class} CflPseudoTimeStep(*, cfl: float = 50.0, local: bool = True)

Choose pseudo-time increments from a requested Courant number.

```{py:attribute} cfl
:type: float

Requested pseudo-time Courant number.
```

```{py:attribute} local
:type: bool

Permit cell-local pseudo-time scales for steady convergence.
```
````

````{py:class} AdaptiveCfl(*, initial: float = 1.0, target: float = 100.0, ramp_steps: int = 500, growth_factor: float = 1.25, retreat_factor: float = 0.5, minimum: float = 0.1, maximum: float | None = None, recovery_window: int = 8)

Residual-aware pseudo-time CFL progression.

```{py:attribute} initial
:type: float

CFL used at the beginning of the solve or after a restart that lacks history.
```

```{py:attribute} target
:type: float

Production CFL earned after stable nonlinear progress.
```

```{py:attribute} growth_factor
:type: float

Largest allowed CFL increase over one successful control window.
```

```{py:attribute} retreat_factor
:type: float

CFL reduction applied when progress or stability checks fail.
```
````

## Steady time controls

````{py:class} SteadyTimeControls(*, max_pseudo_steps: int = 2000, minimum_pseudo_steps: int = 100, pseudo_time_step: FixedPseudoTimeStep | CflPseudoTimeStep | AdaptiveCfl = AdaptiveCfl(), convergence: ConvergenceCriteria | None = None, output_schedule: OutputSchedule | None = None)

Pseudo-time advancement to a steady converged solution.

```{py:attribute} max_pseudo_steps
:type: int

Maximum nonlinear pseudo-iterations.
```

```{py:attribute} minimum_pseudo_steps
:type: int

Minimum iterations completed before convergence can terminate the run.
```

```{py:attribute} pseudo_time_step
:type: FixedPseudoTimeStep | CflPseudoTimeStep | AdaptiveCfl

Pseudo-time step selection and progression method.
```
````

## Inner pseudo-time controls

````{py:class} PseudoTimeControls(*, maximum_steps: int = 100, minimum_steps: int = 3, residual_drop: float = 2.0, absolute_residual: float | None = None, step_method: FixedPseudoTimeStep | CflPseudoTimeStep | AdaptiveCfl = CflPseudoTimeStep(), chunk_size: int = 25, early_stop: bool = True, output_every: int | None = None)

Nonlinear convergence policy inside each physical-time step.

```{py:attribute} maximum_steps
:type: int

Maximum pseudo-iterations permitted for one physical step.
```

```{py:attribute} minimum_steps
:type: int

Minimum pseudo-iterations before early stopping is evaluated.
```

```{py:attribute} residual_drop
:type: float

Required orders of residual reduction within the physical step.
```

```{py:attribute} absolute_residual
:type: float | None

Optional absolute inner-convergence threshold.
```

```{py:attribute} chunk_size
:type: int

Number of pseudo-iterations executed between convergence, cancellation and
live-output checks.
```

```{py:attribute} output_every
:type: int | None

Optional inner-history cadence in pseudo-iterations. Field and checkpoint
cadences are configured with {py:class}`OutputSchedule`.
```
````

## Physical time controls

````{py:class} PhysicalTimeControls(*, time_step: float, steps: int | None = None, end_time: float | None = None, order: int = 2, startup_steps: int = 1, predictor: str = "extrapolate", inner: PseudoTimeControls = PseudoTimeControls(), statistics: StatisticsOutput | None = None, output_schedule: OutputSchedule | None = None)

Implicit physical-time advancement for URANS, DES and DDES simulations.

```{py:attribute} time_step
:type: float

Physical time increment in seconds.
```

```{py:attribute} steps
:type: int | None

Number of physical steps. Supply this or {py:attr}`end_time`.
```

```{py:attribute} end_time
:type: float | None

Final simulated time in seconds. Supply this or {py:attr}`steps`.
```

```{py:attribute} order
:type: Literal[1, 2]

Requested physical-time accuracy order.
```

```{py:attribute} startup_steps
:type: int

Initial steps advanced with the startup time discretisation before the
requested higher-order history is available.
```

```{py:attribute} predictor
:type: Literal["previous", "extrapolate"]

Initial field prediction for each new physical step.
```

```{py:attribute} inner
:type: PseudoTimeControls

Pseudo-time convergence policy applied inside every physical step.
```
````

## Physical and pseudo-time example

```python
from gradientdynamics.fluxcore import (
    AdaptiveCfl,
    OutputSchedule,
    PhysicalTimeControls,
    PseudoTimeControls,
)

time_controls = PhysicalTimeControls(
    time_step=2.5e-5,
    steps=12_000,
    order=2,
    startup_steps=1,
    predictor="extrapolate",
    inner=PseudoTimeControls(
        maximum_steps=80,
        minimum_steps=4,
        residual_drop=2.5,
        step_method=AdaptiveCfl(
            initial=1.0,
            target=75.0,
            ramp_steps=40,
        ),
        chunk_size=10,
        early_stop=True,
        output_every=5,
    ),
    output_schedule=OutputSchedule(
        history_every_pseudo_steps=5,
        fields_every_physical_steps=20,
        checkpoint_every_physical_steps=100,
    ),
)
```
