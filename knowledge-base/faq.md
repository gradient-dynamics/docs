# Frequently Asked Questions

## General

### What is Gradient Dynamics Studio?

Gradient Dynamics Studio is a browser-based CFD (Computational Fluid Dynamics) platform. It allows you to upload CAD geometry, generate meshes, run flow simulations, and visualize results — all from your web browser with no software installation required.

### Do I need to install anything?

No. Gradient Dynamics runs entirely in the browser. All mesh generation and simulation runs execute on cloud GPUs. You just need a modern web browser (Chrome, Firefox, Edge, or Safari).

### What types of simulations can I run?

Gradient Dynamics supports a comprehensive range of simulation types:

- **Steady-state RANS** — The most common type of industrial CFD simulation (k-ω SST, k-ε, Spalart-Allmaras, RSM)
- **URANS** — Time-accurate unsteady RANS for periodic or transient flows
- **LES** — Large Eddy Simulation for high-fidelity turbulence resolution (Pro tier and above)
- **DES / DDES / IDDES** — Hybrid RANS-LES methods for massively separated flows (Pro tier and above)

The platform handles both **compressible** and **incompressible** flows using multiple solver formulations: density-based (explicit, recommended), pressure-based (implicit, segregated), coupled (implicit), FSAC (hybrid), and ACM (explicit incompressible). Applications include external aerodynamics, internal flows, thermal analysis, rotating machinery, and compressible high-Mach flows.

### Is my data secure?

Your geometry files, meshes, and simulation results are stored securely in the cloud. Each user's data is isolated and accessible only through your authenticated account.

## Geometry

### What file formats can I upload?

- **STEP** (.step, .stp) — Recommended
- **IGES** (.iges, .igs)
- **STL** (.stl)
- **OBJ** (.obj)

### Why is STEP recommended over STL?

STEP files preserve the CAD topology — face boundaries, edges, and multi-body structure. This enables:
- Per-surface mesh controls
- Automatic face detection and naming
- Better geometry repair options
- Multi-body assembly handling

STL files only contain triangle soup — no face structure, edges, or topology.

### My geometry has issues. What should I do?

Run the geometry analysis in the Geometry tab. The most common fixes:
1. **Vertex welding** — For STL/OBJ with small gaps between triangles
2. **Hole filling** — For surfaces with missing patches
3. **CAD healing** — For STEP/IGES with tolerance issues

The AI Assistant can also diagnose and recommend repairs.

### How large can my geometry file be?

File upload limits depend on your subscription tier. For very large assemblies, consider simplifying the geometry by removing small features that don't significantly affect the flow.

## Meshing

### How do I choose the right cell size?

Start with the geometry's characteristic length divided by 50–100. For example:
- 4.5 m car → Start with 0.05–0.1 m cell size
- 50 mm pipe → Start with 0.5–1.0 mm cell size

Then refine until your results don't change significantly between meshes (mesh independence).

### What is y+ and why does it matter?

y+ is a dimensionless distance that describes the first cell height relative to the boundary layer thickness. It must match your turbulence model's requirements:
- **y+ ≈ 30:** Standard for wall-function RANS (k-ω SST, k-ε)
- **y+ ≈ 1:** Required for wall-resolved simulations

The mesh settings tab includes a y+ calculator to help determine the correct first layer height.

### Do I need boundary layers?

**Yes**, for almost all CFD simulations. Boundary layers resolve the velocity gradient at walls, which directly affects:
- Drag prediction
- Heat transfer rates
- Separation behavior
- Wall shear stress

Without boundary layers, results near walls will be inaccurate.

### What geometry formats can I upload?

STEP (.step, .stp), IGES (.iges, .igs), STL, and OBJ. STEP is recommended as it preserves face topology and named faces, enabling automatic surface detection and per-face mesh controls.

## Simulation

### Which turbulence model should I use?

**k-ω SST** is the best default for most applications. Use k-ε for simple pipe flows, Spalart-Allmaras for quick estimates, and RSM for strongly swirling flows. See [Turbulence Models](/simulation/turbulence-models.md) for a detailed comparison.

### How do I know if my simulation has converged?

1. All residuals should be decreasing and reach at least 1e-4
2. Integrated quantities (drag, lift, pressure drop) should be stable
3. The residual plot should show a clear downward trend, not oscillations

### Which solver should I choose?

For most applications, use the **density-based solver** — it is the fastest on GPU hardware and handles both compressible and low-speed flows through low-Mach preconditioning. Use the **pressure-based solver** (SIMPLE, PISO, PIMPLE) for strictly incompressible workflows, the **coupled solver** for strongly coupled physics, or **FSAC/ACM** for GPU-efficient incompressible explicit solvers. When in doubt, start with density-based.

### My simulation diverged. What went wrong?

The most common causes:
1. Poor mesh quality (check skewness and non-orthogonality)
2. Too aggressive CFL or relaxation factors (reduce CFL or relaxation by 30%)
3. Incorrect boundary conditions (check all surfaces)
4. Wrong geometry scale (verify dimensions are in meters)

See [Troubleshooting](troubleshooting.md) for detailed guidance.

### How many iterations do I need?

Typical ranges:
- Simple geometries: 300–500 iterations
- Moderate complexity: 500–1000 iterations
- Complex geometries: 1000–2000 iterations

Start with 500–1000 and extend if residuals haven't converged.

## Credits and Billing

### How are credits consumed?

| Operation | Rate |
|-----------|------|
| Mesh generation | 0.2 credits per GPU-minute |
| CFD simulation | 1.0 credits per GPU-minute |

Credit cost depends on mesh size and simulation duration.

### Can I estimate the cost before running?

Yes. When you click **Run Simulation** or **Generate Mesh**, a cost estimate is shown before you confirm.

### What happens if I run out of credits?

Jobs will not be submitted until credits are available. Credits reset monthly and overage billing options are available on higher tiers.

## AI Assistant

### What can the AI Assistant do?

The assistant can analyze geometry, recommend mesh settings, configure simulations, set boundary conditions, and interpret results. It works through natural language conversation.

### Does the assistant automatically change my settings?

No. The assistant always asks for your **explicit confirmation** before making any changes to your project. You can review every action before it's applied.

### Can the assistant access my other projects?

No. The assistant only has context about the current project you're working in.
