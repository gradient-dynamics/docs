# Solver settings

FluxCore settings balance accuracy, robustness and runtime without exposing
implementation-specific solver architecture. Begin with validated defaults and
change a setting only when the physics or a sensitivity study justifies it.

## Simulation mode

| Mode | Use for |
|---|---|
| **Steady** | Design points where a stable mean flow or thermal state is the main result. |
| **Time resolved** | Varying loads, wakes, rotating motion, start-up or thermal transients. |
| **Conjugate heat transfer** | Coupled fluid convection and solid conduction across multiple regions. |

## Accuracy profile

| Profile | Use for |
|---|---|
| **Robust** | Initial checks, difficult geometry or a new operating point. |
| **Standard** | Most production engineering runs. |
| **High accuracy** | Final studies on a suitable mesh with a validation target. |

Higher accuracy cannot recover geometry or gradients that the mesh does not
resolve. Review mesh quality and sensitivity before escalating numerical
settings.

## Run controls

| Control | Purpose |
|---|---|
| **Maximum iterations** | Limits solver work for a steady run. |
| **Residual target** | Defines the requested equation-convergence threshold. |
| **Physical steps** | Sets the length of a time-resolved study. |
| **Time step** | Resolves the physical time scale of interest. |
| **Inner work budget** | Controls the convergence effort within each physical step. |
| **Output cadence** | Selects how often accepted states are written for time history. |
| **Early stopping** | Ends a run after residual and engineering-monitor criteria are met. |

## Engineering monitors

Select at least one quantity tied directly to the design decision: force,
moment, pressure loss, mass flow, temperature, heat rate or another component
output. Judge convergence from residuals and engineering monitors together.

## Reference values

Force and moment coefficients require explicit reference area, velocity,
density, directions, moment centre and reference lengths. Reuse the same
definitions across variants. An automatic projected area is useful for
exploration but is not a universal reporting standard.

## When to revise a setting

Revise settings when residuals and physical monitors disagree, the case is
genuinely unsteady, a mesh or time-step study shows sensitivity, or a benchmark
requires a defined accuracy level. Do not use a larger run budget to conceal
incorrect geometry, units, materials or boundary conditions.
