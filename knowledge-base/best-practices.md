# Best Practices

Guidelines for getting accurate, reliable results from Gradient Dynamics Studio.

## Geometry Preparation

### Start with a Clean Geometry

- **Always run geometry analysis** before meshing — catch problems early
- **Use STEP format** for CAD files — it preserves topology that helps meshing and surface identification
- **Simplify complex assemblies** — remove small features (screws, bolts, labels) that don't affect flow
- **Close gaps and holes** — the geometry must be watertight for volume meshing
- **Remove internal surfaces** — overlapping or duplicate faces cause cut-cell meshing errors

### Geometry Scale

- Verify your geometry is in the correct units (meters)
- A car should be ~4.5 m long, not 4500 (millimeters) or 0.0045 (micrometers)
- Incorrect scale leads to wrong mesh sizes, Reynolds numbers, and results

## Meshing

### Start Coarse, Then Refine

1. **Coarse mesh first** — Run a quick mesh (lower AMR levels) to verify the setup
2. **Check quality** — Review cut-cell volume fractions and any flagged problem cells
3. **Refine** — Increase AMR levels and regenerate
4. **Compare** — Check that key quantities (Cd, pressure drop) change by < 5% between meshes

This "mesh independence study" ensures your results are not artifacts of the mesh resolution.

### Near-Wall Resolution

- **Use the y+ calculator** to determine the appropriate near-wall AMR level for your flow speed and turbulence model
- **y+ ≈ 30** (wall-function RANS, medium surface refinement) works well for most external aerodynamics
- **y+ ≈ 1** (wall-resolved, fine or very fine surface refinement) is needed for LES, detailed heat transfer, or sensitive separation
- Do not over-refine walls unnecessarily — each additional near-wall AMR level multiplies local cell count significantly

### Refinement Zones

- **Focus refinement where it matters** — wakes, separation zones, stagnation regions
- **Don't over-refine far-field regions** — cells far from the geometry contribute little to accuracy
- **Avoid extreme level jumps** — 2–3 AMR level difference between adjacent regions is the practical limit
- **Cover the full wake** — for bluff bodies, the wake zone should extend at least 3× body length downstream

### Domain Sizing

- **Too small** is worse than too large — boundary effects contaminate the solution
- **External flow:** Minimum 1.5× upstream, 3× downstream, 1.5× sides
- **Internal flow:** Ensure adequate inlet development length (10× hydraulic diameter)
- **When in doubt, go larger** — the extra cells are cheap compared to a wrong solution

## Simulation

### Solver Type

Use the **density-based solver** (the default) for all standard CFD applications. It runs significantly faster on GPU hardware than the pressure-based solver and produces equivalent accuracy for incompressible flows via low-Mach preconditioning. Reserve the pressure-based solver only for cases that specifically require an incompressible formulation.

### Turbulence Model Selection

| Situation | Recommended Model |
|-----------|------------------|
| First analysis / general purpose | k-ω SST |
| Industrial pipe/duct flow | k-ε |
| Quick preliminary study | Spalart-Allmaras |
| Strong swirl or rotation | RSM |
| Unsteady/acoustic analysis | LES |

### Convergence

- **Monitor residuals** — density residual should decrease monotonically to at least 1e-5
- **Check integrated quantities** — Cd, Cl, pressure drop should plateau before you declare convergence
- **Residuals alone are not sufficient** — a simulation can have low residuals but wrong results if the setup is incorrect
- **Run enough iterations** — 500 minimum for RANS, 1000+ for complex geometries
- **Use CFL ramping** for difficult starting conditions — let the solver build up gradually

### Common Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|-----------|
| Forgetting moving ground for vehicle aero | Unrealistic ground boundary layer | Set ground as moving wall at freestream speed |
| Wrong turbulence intensity at inlet | Incorrect turbulence levels in domain | Use 1% for external, 5% for internal |
| CFL too high at startup | Immediate divergence | Enable CFL ramping; start at CFL 0.5 |
| Coarse mesh near features of interest | Inaccurate local flow | Add refinement zones at correct AMR level |
| Ignoring mesh quality warnings | Poor convergence or wrong results | Inspect flagged cut-cells before simulating |
| Using pressure-based solver for large meshes | Slow GPU performance | Switch to density-based solver |

## Post-Processing

### Validate Your Results

- **Compare with known data** — use published Cd values, analytical solutions, or experimental data where available
- **Check mass conservation** — inlet and outlet mass flow rates should match within 0.1%
- **Look for non-physical artifacts** — negative pressures in unexpected places, symmetric flow that should be asymmetric, etc.
- **Verify force coefficients** — are they in the expected range for your geometry type?

### Effective Visualization

- **Start with surface coloring** — pressure on the body shows the overall flow structure
- **Use slice planes** — mid-span/centerline cuts reveal internal flow patterns
- **Add streamlines sparingly** — too many streamlines create visual clutter
- **Set color ranges manually** — auto-scaling can hide important features

## Workflow Efficiency

### Use the AI Assistant

The AI Assistant saves time by:
- Automating geometry analysis and repair recommendations
- Suggesting appropriate mesh settings and AMR levels for your application
- Auto-detecting boundary conditions from surface names
- Interpreting quality reports and results

### Save Time with Symmetry

If your geometry and flow are symmetric:
- Use a **symmetry plane** to mesh only half the domain
- This halves cell count and compute cost
- Results are mirrored automatically in visualization

### Iterate Systematically

For design optimization:
1. Establish a baseline configuration
2. Change one parameter at a time
3. Use the same mesh settings for fair comparison
4. Record all results in a structured format
