# Choosing physics and fidelity

Choose the simplest model that captures the mechanisms controlling your
engineering quantity. Extra complexity is useful only when it changes the
answer in a justified way.

## Flow regime

| Question | Typical choice |
|---|---|
| Is the flow expected to settle to a stable operating point? | Start with a steady RANS study. |
| Do wakes, loads or thermal response vary materially with time? | Use a time-resolved workflow after obtaining a stable initial solution. |
| Are density, pressure and temperature changes important? | Enable a compressible thermodynamic treatment. |
| Are rotating components important to the mean flow? | Define a rotating region and the associated walls and frame of reference. |
| Does heat move through both fluids and solids? | Use conjugate heat transfer with explicit material regions and interfaces. |

## Turbulence

RANS is the normal starting point for production engineering. It provides a
time-averaged representation of turbulent transport at a practical cost.
Time-resolved and scale-resolving approaches demand greater spatial and
temporal resolution and should be used with a clear validation plan.

Wall treatment and mesh resolution must be selected together. A turbulence
model cannot compensate for missing boundary-layer resolution, poor surface
coverage or an incorrect first-cell height.

## Steady and transient studies

A steady study seeks a stable mean solution. A transient study resolves a
physical time history. For transient work, choose the time step from the
smallest relevant motion or flow time scale, collect enough washout time to
remove start-up effects, and sample for long enough to compute meaningful
statistics.

## Thermal and conjugate heat transfer

Conjugate heat transfer solves the interaction between fluid convection and
solid conduction. Define material conductivity, heat capacity, density, heat
sources, contact assumptions and thermal boundary conditions deliberately.
Monitor both temperature and heat balance across the coupled system.
