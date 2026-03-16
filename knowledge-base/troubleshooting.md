# Troubleshooting

Common issues and their solutions when working with Gradient Dynamics Studio.

## Geometry Issues

### "Geometry is not watertight"

**Cause:** Gaps between faces in the surface mesh.

**Solutions:**
1. For STL/OBJ files: Run **vertex welding** in the Geometry tab. This merges nearby vertices that should be connected.
2. For STEP/IGES files: Run **CAD healing** to sew adjacent faces.
3. If welding doesn't fix it: The geometry has genuine holes. Run **hole filling** to patch them.
4. If issues persist: Return to your CAD software and fix the model.

### "Non-manifold edges detected"

**Cause:** An edge is shared by more than two faces (T-junction topology) or faces overlap.

**Solutions:**
1. Run **non-manifold edge repair** — Studio will remove duplicate faces near problem edges.
2. In severe cases, simplify the geometry in your CAD tool to eliminate the topology issue.

### "Geometry is very large/small"

**Cause:** Incorrect units — the geometry was exported in millimeters, inches, or another unit instead of meters.

**Solutions:**
1. Re-export the geometry in meters from your CAD software
2. Scale the geometry in your CAD tool before upload

## Meshing Issues

### Mesh generation fails

**Possible causes and solutions:**

| Cause | Solution |
|-------|----------|
| Non-watertight geometry | Fix geometry first (see above) |
| Cell size too small for geometry | Increase minimum cell size |
| Too many refinement levels | Reduce to 8–10 levels |
| Complex geometry features | Simplify small features in CAD |

### Very high cell count

**Cause:** Cell size is too small relative to the domain, or excessive refinement.

**Solutions:**
1. Increase the target cell size
2. Reduce refinement levels
3. Use refinement zones instead of global refinement
4. Enable symmetry to halve the domain

### Poor mesh quality (high skewness)

**Cause:** Complex geometry features or extreme size transitions.

**Solutions:**
1. Increase refinement levels (smoother transitions)
2. Add refinement zones near problem areas
3. Reduce boundary layer growth rate
4. Simplify geometry features near the problem area

### Boundary layers fail to generate

**Cause:** Insufficient space between surfaces, or geometry issues preventing layer growth.

**Solutions:**
1. Check for narrow gaps between surfaces — layers from opposite walls can collide
2. Reduce the number of layers or first layer height
3. Ensure the geometry is clean near wall surfaces

## Simulation Issues

### Simulation diverges immediately

**Cause:** Usually aggressive relaxation or very poor mesh quality.

**Solutions:**
1. Reduce relaxation factors by 30% (velocity: 0.5→0.3, pressure: 0.2→0.15)
2. Enable turbulence ramping (delay turbulence activation by 50 iterations)
3. Check mesh quality — fix any cells with skewness > 0.95
4. Verify boundary conditions are physically consistent

### Residuals oscillate but don't decrease

**Cause:** The solver is struggling with the numerics or the flow is inherently unsteady.

**Solutions:**
1. Reduce relaxation factors
2. Enable non-orthogonal correctors if mesh quality is moderate
3. For inherently unsteady flows (e.g., bluff body vortex shedding), the flow may not have a steady-state solution — consider transient simulation
4. Check that boundary conditions don't conflict

### Residuals plateau at a high level (e.g., 1e-2)

**Cause:** The mesh may be too coarse, boundary conditions may be inconsistent, or the solver is hitting stability limits.

**Solutions:**
1. Refine the mesh in areas of high gradients
2. Check boundary conditions for consistency (e.g., mass flow in = mass flow out)
3. Review the logs for limiter warnings — extensive velocity clamping suggests the mesh needs refinement
4. Try a more robust turbulence model (k-ω SST if not already using it)

### Unrealistic pressure or velocity values

**Cause:** Poor boundary conditions, mesh errors, or insufficient convergence.

**Solutions:**
1. Check inlet velocity and outlet pressure values
2. Verify the geometry scale (wrong scale = wrong Reynolds number)
3. Ensure the simulation has converged (check residual plot)
4. Check for negative cell volumes in the mesh quality report

### Simulation takes too long

**Cause:** Very large mesh, slow convergence, or excessively tight criteria.

**Solutions:**
1. Reduce mesh size (start coarser)
2. Increase relaxation factors slightly (if convergence is stable)
3. Relax convergence criteria (1e-4 is adequate for most engineering applications)
4. Reduce max iterations and check if results are already stable

## Post-Processing Issues

### Results look wrong or asymmetric

**Possible causes:**
1. **Insufficient convergence** — Run more iterations
2. **Asymmetric mesh** — Check that the mesh is symmetric for a symmetric problem
3. **Wrong boundary conditions** — Verify all surfaces have correct conditions
4. **Physical asymmetry** — Some flows are genuinely asymmetric (vortex shedding, flow bifurcation)

### Force coefficients seem too high or too low

**Check:**
1. **Reference area** — Is it correct? Drag uses frontal area; lift uses planform area.
2. **Reference velocity** — Must match the inlet freestream velocity
3. **Surface selection** — Are you measuring forces on the correct surfaces?
4. **Convergence** — Forces may not have converged even if residuals look okay. Run more iterations.

## Account and Platform Issues

### "Credit limit reached"

Your credit balance has been exhausted.

**Solutions:**
1. Wait for monthly credit reset
2. Upgrade to a higher tier for more credits
3. Optimize your workflow — use coarser meshes for initial setup, fine meshes only for final analysis

### Mesh generation or simulation stuck in "Pending"

**Cause:** Cloud compute resources are being allocated.

**Solutions:**
1. Wait a few minutes — resource allocation may take time during peak usage
2. Check the status periodically
3. Contact support if the job is stuck for more than 15 minutes

## Getting Help

If these troubleshooting steps don't resolve your issue:

1. **Ask the AI Assistant** — Describe the problem in natural language
2. **Check the logs** — Detailed error messages are in the Logs panel
3. **Contact support** — Include your project ID and a description of the issue
