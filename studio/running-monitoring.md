# Running and monitoring

Submitting a simulation creates a managed job associated with the active
project, mesh and simulation configuration.

## Job stages

A run typically moves through validation, queueing, mesh preparation,
accelerator start-up, solution, result finalisation and completion. Studio
shows the current stage and retains logs if you leave the page.

## What to monitor

- **Residuals** indicate how the discrete equations are contracting.
- **Forces and moments** show whether aerodynamic loads have stabilised.
- **Mass flow or pressure loss** shows whether an internal-flow operating point
  is stable.
- **Temperature and heat rate** show whether a thermal system has reached a
  meaningful state.
- **Runtime progress** distinguishes an active solve from queueing, data
  preparation or result export.

## Stop, retry or revise

Stop a run when the configuration is known to be wrong or the solution is
moving toward a non-physical state. Retry infrastructure interruptions without
changing the case. Revise the project configuration when geometry, mesh,
physics or numerical evidence is the cause.

Do not hide a poor setup by only increasing the iteration budget. Fix missing
boundaries, incorrect units, insufficient domain clearance, mesh defects or
unresolved physics first.
