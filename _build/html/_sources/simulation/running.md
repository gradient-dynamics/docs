# Running Simulations

Once your simulation is configured, this page covers how to launch, monitor, and manage simulation runs.

## Launching a Simulation

1. Review your configuration in the **Simulation** tab:
   - Solver family selected
   - Turbulence model selected
   - Boundary conditions assigned to all surfaces
   - Solver settings configured
2. Click **Run Simulation**
3. A confirmation dialog shows:
   - Estimated credit cost
   - Mesh cell count
   - Selected turbulence model
4. Click **Confirm** to submit the job

The simulation is queued and dispatched for cloud execution.

## Job Status

Your simulation progresses through these stages:

| Status | Description |
|--------|-------------|
| **Pending** | Job submitted, waiting for resources |
| **Queued** | Resources allocated, initializing |
| **Running** | Solver actively iterating |
| **Completed** | Converged or reached max iterations |
| **Failed** | Error occurred — check logs |

The current status is displayed in the workspace header with color coding.

## Monitoring Convergence

### Residual Plot

While the simulation runs, the **convergence plot** updates in real time. The residuals shown depend on the selected physics and solver family. Common residuals include mass, momentum, energy, and turbulence quantities.

All residuals are plotted on a **logarithmic scale** vs. iteration number.

**What to look for:**
- Residuals should **decrease monotonically** (trending downward)
- A converged solution shows residuals reaching a **plateau** at a low level
- Oscillating residuals indicate the solution is struggling. Consider using more conservative solver settings or reviewing mesh quality and boundary conditions.

### Convergence Indicators

| Residual Level | Meaning |
|---------------|---------|
| > 1e-2 | Not converged — solution is changing significantly |
| 1e-2 to 1e-4 | Partially converged — trends are established |
| < 1e-5 | Well converged for many engineering workflows |
| < 1e-4 | Often acceptable when monitor quantities are stable |
| < 1e-6 | Tightly converged — research-grade accuracy |

```{tip}
For engineering applications, residual targets should be checked alongside monitor quantities. Force, moment, pressure-drop, and heat-transfer values should plateau before you treat the run as final.
```

## Logs

The **Logs** panel shows real-time solver output:

- Iteration count and residual values
- Solver diagnostics and stability indicators
- Error messages if something goes wrong
- Execution timing

Use the filter and search functions to find specific information in the log.

## Simulation Completion

When the simulation completes (converged or max iterations reached), you'll see:

- **Final residual values** — How far the solution converged
- **Total iterations** — How many iterations were run
- **Runtime** — Total wall-clock time
- **Credits used** — Actual credit consumption

The results are automatically saved and available in the **Results** tab.

## Failed Simulations

If a simulation fails, check:

1. **Logs** — Error messages indicate the cause
2. **Mesh quality** — Poor mesh quality is the most common cause of failure
3. **Boundary conditions** — Inconsistent or missing BCs cause solver errors
4. **Solver settings** — Overly aggressive relaxation can cause divergence

### Common Failure Causes

| Error | Cause | Fix |
|-------|-------|-----|
| Floating point exception | Solution diverged | Use more conservative settings and review mesh quality |
| Negative cell volume | Mesh error | Regenerate mesh, check geometry |
| Matrix singularity | Isolated cells or patches | Check mesh connectivity |
| Credit limit reached | Insufficient credits | Upgrade tier or wait for monthly reset |

## Re-Running

You can re-run a simulation with modified settings:

1. Adjust parameters in the Simulation tab
2. Click **Run Simulation** again
3. Previous results remain accessible for comparison
