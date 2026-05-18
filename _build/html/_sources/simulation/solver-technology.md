# Solver Technology

Gradient Dynamics solvers are built around conservative CFD and multiphysics methods that work with both structured and unstructured meshes. This page explains the public numerical ideas behind the available solver families, what they mean in practice, and when they matter for engineering work.

Implementation-specific tuning, internal coefficients, and infrastructure details are intentionally omitted. The descriptions below use standard CFD terminology and public academic references.

## Solver Families

Studio groups solver choices by the physics you are trying to capture.

| Solver family | What it is for | What it means in practice |
|---------------|----------------|---------------------------|
| **Pressure-based low-speed flow** | Incompressible and low-Mach CFD where density changes are not central. | Efficient for cars, ducts, pumps, HVAC, liquid flow, and many rotating-machinery studies. |
| **Explicit compressible flow** | Density changes, pressure waves, high-speed flow, nozzles, shocks, and transonic or supersonic applications. | Advances mass, momentum, and energy in conservative form using flux reconstruction and numerical fluxes at cell faces. |
| **Transient flow** | Time-varying wakes, startup, rotating machinery, and unsteady thermal response. | Resolves how the solution evolves over time instead of only targeting a steady mean state. |
| **Coupled multiphysics** | Interacting regions or physics fields, such as fluid-solid heat transfer. | Couples field information across regions so temperature, heat flux, flow, and material response are consistent. |

Most low-speed industrial CFD starts with the pressure-based route. Use the explicit compressible route when compressibility is part of the physics, not just because a case is difficult.

## Conservation Form

Many CFD solvers are based on conservation laws. For a flow problem, that means the update accounts for what enters and leaves each cell through its faces:

- mass conservation tracks density or volume flux,
- momentum conservation tracks forces and momentum transport,
- energy conservation tracks pressure work, heat transfer, and thermal effects where applicable.

This is why mesh quality matters. Every face contributes to the flux balance of neighboring cells. Poor skewness, high non-orthogonality, unresolved wall layers, or abrupt size jumps can make that balance harder to compute accurately.

## Explicit Compressible Path

The explicit compressible path uses a flux-reconstruction approach. In practical terms, each update follows this pattern:

1. Reconstruct the solution near each face from neighboring cell values.
2. Build left and right face states for density, velocity, pressure, and energy.
3. Evaluate a conservative numerical flux through the face.
4. Accumulate those face fluxes back into each cell.
5. Advance the conservative variables through explicit time stepping.

The value of flux reconstruction is that it combines conservation with higher spatial accuracy. Smooth flow regions can use sharper reconstructed states, while limiters or non-oscillatory reconstruction keep shocks, contact surfaces, and steep gradients from producing spurious oscillations.

For users, this means the compressible path is most useful for:

- transonic and supersonic external aerodynamics,
- nozzles, diffusers, vents, and high-pressure gas systems,
- pressure-wave and acoustic propagation studies,
- flows where density, pressure, and temperature are strongly coupled,
- mixed-speed applications where high-speed regions are part of the engineering question.

Flux reconstruction is a broad high-order CFD family. The original formulation by Huynh introduced a way to recover several high-order schemes, including discontinuous Galerkin-like methods, within a unified reconstruction framework. Later energy-stable families, including the Vincent-Castonguay-Jameson-Huynh schemes, developed the stability theory further. Studio documentation uses these public references to explain the method class, not to expose internal implementation details.

## Numerical Fluxes

Numerical fluxes decide how information crosses a cell face. For compressible flow, they are often based on approximate Riemann solvers or pressure-velocity splitting methods.

| Flux family | What it is useful for |
|-------------|-----------------------|
| **Rusanov / local Lax-Friedrichs** | Robust startup, difficult shocks, and conservative fallback behaviour. |
| **HLLC** | Compressible production cases where shocks and contact surfaces matter. |
| **Roe-type fluxes** | Sharp wave resolution on clean high-speed cases. |
| **AUSM-family fluxes** | All-speed and mixed-Mach applications where pressure and velocity splitting helps reduce excess low-Mach dissipation. |

You usually do not need to choose these directly in Studio. The important engineering point is that flux choice controls the tradeoff between robustness, sharpness, and numerical dissipation.

## Gradient Schemes

Gradient schemes estimate how a field changes inside and around each cell. Gradients are used for:

- second-order face reconstruction,
- pressure and velocity correction,
- turbulence production terms,
- wall shear and heat-transfer estimates,
- non-orthogonal mesh corrections,
- smoothness and limiter calculations.

On structured meshes, gradients can use regular stencil relationships. On unstructured meshes, the solver must infer the local slope from arbitrary neighbor layouts, so face-based Green-Gauss and least-squares-style reconstructions are common public methods.

| Gradient approach | Typical strength | Watch point |
|-------------------|------------------|-------------|
| **Green-Gauss** | Uses face values and face geometry directly. | Can be sensitive to poor face interpolation on distorted cells. |
| **Weighted least squares** | Handles irregular unstructured neighborhoods well. | Needs a well-conditioned local stencil, especially near thin or highly stretched cells. |
| **Limited gradients** | Reduces overshoots near discontinuities or steep gradients. | Adds numerical diffusion when the limiter activates. |

For users, gradient schemes explain why mesh quality and local refinement matter. A high-order solver cannot recover missing geometric resolution. If the boundary layer, wake, thermal plume, shock, or pressure-gradient region is under-resolved, the reconstructed gradients will also be under-resolved.

## Pressure-Based Flow

For low-speed flows, pressure-based solvers are usually more efficient because they avoid marching acoustic waves that are not part of the engineering question. These methods solve velocity and pressure in a coupled or segregated loop so that the final velocity field satisfies mass conservation.

Common public algorithms in this family include:

- **SIMPLE** for steady pressure-velocity coupling,
- **SIMPLEC** for a more consistent steady pressure correction,
- **PISO** for transient pressure correction,
- **PIMPLE** for transient cases that need outer correction loops.

For users, the pressure-based route is the right starting point for most low-speed external aerodynamics, internal flow, pump, HVAC, and liquid-flow studies. It is also a good match for many heat-transfer cases where density change is not the dominant physics.

## Implicit Linear Solvers

Implicit pressure-based and coupled workflows repeatedly solve large sparse linear systems. These systems come from discretized momentum, pressure, turbulence, heat-transfer, or coupled-field equations. In abstract form they look like:

```text
A x = b
```

where `A` represents the discretized equation, `x` is the unknown field correction, and `b` is the current residual or source term.

The solver does not usually invert `A` directly. Instead, iterative methods improve an approximate solution until the remaining error is small enough for the CFD iteration. This is why linear-solver settings affect robustness and runtime, especially for large meshes, stretched boundary layers, non-orthogonal cells, and tightly coupled physics.

| Method | What it does | Typical role |
|--------|--------------|--------------|
| **PCG** | Uses conjugate search directions to solve symmetric positive-definite systems efficiently. | Pressure Poisson equations, diffusion-like systems, and other well-conditioned symmetric solves. |
| **BiCGStab-type methods** | Handles nonsymmetric systems that arise from convection, coupling, and linearized transport. | Momentum, turbulence, and coupled transport equations where the matrix is not symmetric. |
| **GAMG / AMG** | Builds a hierarchy of coarser algebraic systems so long-wavelength error can be removed cheaply. | Pressure solves and elliptic operators where single-level iterations converge too slowly. |
| **Chebyshev smoothing** | Applies a polynomial smoother that damps targeted error modes without requiring a full Krylov solve. | Multigrid smoothing, preconditioning, and parallel-friendly damping of high-frequency error. |

The practical distinction is that Krylov methods such as PCG are good at building an improved correction from recent residual history, while multigrid methods are good at removing errors across multiple length scales. Many production CFD solvers combine both ideas.

## Preconditioners

A preconditioner changes the linear system into an easier equivalent problem. Instead of solving:

```text
A x = b
```

the solver approximately solves:

```text
M^-1 A x = M^-1 b
```

where `M` is chosen to be much cheaper to apply than `A^-1`, but close enough to reduce the number of iterations. A good preconditioner clusters the difficult error modes, improves the effective conditioning of the problem, and reduces how many linear-solver iterations are needed.

| Preconditioner or smoother | How it helps | Engineering meaning |
|----------------------------|--------------|---------------------|
| **Jacobi / diagonal scaling** | Scales each equation by its diagonal strength. | Cheap and robust, but may need many iterations on difficult pressure systems. |
| **Chebyshev** | Uses a polynomial filter over an estimated eigenvalue range. | Good at damping selected error frequencies and useful inside multigrid cycles. |
| **GAMG / AMG preconditioning** | Moves residuals to coarser algebraic levels, solves cheaper coarse corrections, then interpolates them back. | Reduces slow pressure convergence caused by large domains, fine meshes, and long-range pressure coupling. |
| **Block or field-aware preconditioning** | Treats related unknowns together instead of as isolated scalar entries. | Useful for coupled physics where fields influence one another strongly. |

Preconditioners do not change the physical model. They change how efficiently the numerical correction is found. A poor preconditioner can make a stable setup look slow or fragile; a good one can turn the same discretized equations into a practical production run.

### How Multigrid Works

Multigrid methods are based on a simple observation: local smoothers remove short-wavelength error quickly, but long-wavelength error can remain for many iterations. On a coarser level, that same long-wavelength error becomes easier to see and cheaper to correct.

A typical multigrid cycle:

1. Smooth the fine-level error.
2. Restrict the residual to a coarser level.
3. Solve or smooth the coarse correction.
4. Prolong the correction back to the fine level.
5. Smooth again on the fine level.

Geometric multigrid uses a known grid hierarchy. Algebraic multigrid builds the hierarchy from the matrix relationships, which makes it useful for unstructured meshes and complex connectivity.

### What Users Should Watch

For most Studio workflows, Automatic settings should choose suitable linear solvers and preconditioners. Tune them when:

- pressure residuals stall while other fields improve,
- continuity converges slowly on a large or highly stretched mesh,
- a thermal or coupled solve is dominated by diffusion-like behaviour,
- mesh non-orthogonality or boundary-layer aspect ratio makes the pressure correction difficult,
- the run spends most of its time in linear solves rather than field updates.

Changing solver or preconditioner settings is a numerical-performance choice. It should be paired with mesh-quality review, residual history, and engineering monitors rather than treated as a substitute for fixing poor geometry, boundary conditions, or under-resolution.

## Turbulence and Wall Treatment

Turbulence models estimate the effect of unresolved turbulent motion. Studio supports workflows across common engineering levels:

- **RANS** for steady or statistically averaged engineering studies,
- **URANS** for large-scale unsteadiness while retaining RANS closure,
- **LES** for resolving larger turbulent structures at higher cost,
- **hybrid RANS-LES** approaches for separated flows where pure RANS can be too restrictive.

Near-wall treatment must match the mesh. Wall functions are efficient for industrial-scale meshes, while low-y-plus approaches need fine near-wall spacing. For drag, pressure drop, separation, and heat-transfer studies, the first-cell height, layer growth, and surface coverage are often as important as the solver selection.

## Structured and Unstructured Capability

Gradient Dynamics supports solver workflows on both structured and unstructured meshes.

| Mesh route | Solver relevance |
|------------|------------------|
| **Unstructured** | Recommended starting point for most production CFD, complex topology, boundary layers, imported meshes, and interoperability. |
| **Structured** | Useful for repeatable automated workflows, controlled studies, and cases where a structured layout fits the geometry and validation objective. |

The same engineering checks apply to both: preserve the geometry that matters, resolve the gradients you care about, check quality metrics before running, and compare final quantities against a mesh-sensitivity or validation target when accuracy matters.

## How to Use This

Use the solver technology as decision support:

1. Start with the physics: low-speed, high-speed, transient, thermal, rotating, or coupled.
2. Choose the mesh route that best represents the geometry and gradients.
3. Use Automatic settings for the first run unless you have a validation requirement.
4. Review residuals and engineering monitors together.
5. Increase accuracy only after the mesh, boundary conditions, and monitors look physically consistent.

For final studies, do not rely on solver order alone. Run mesh sensitivity, compare monitor quantities, inspect wall resolution, and use validation data where available.

## Selected Literature

These references are useful starting points for the public methods discussed above:

- H. T. Huynh, "A Flux Reconstruction Approach to High-Order Schemes Including Discontinuous Galerkin Methods," AIAA Paper 2007-4079, 2007. [doi:10.2514/6.2007-4079](https://doi.org/10.2514/6.2007-4079)
- P. E. Vincent, P. Castonguay, and A. Jameson, "A New Class of High-Order Energy Stable Flux Reconstruction Schemes," Journal of Scientific Computing, 47, 50-72, 2011. [doi:10.1007/s10915-010-9420-z](https://doi.org/10.1007/s10915-010-9420-z)
- B. van Leer, "Towards the Ultimate Conservative Difference Scheme. V. A Second-Order Sequel to Godunov's Method," Journal of Computational Physics, 32, 101-136, 1979.
- G.-S. Jiang and C.-W. Shu, "Efficient Implementation of Weighted ENO Schemes," Journal of Computational Physics, 126, 202-228, 1996. [doi:10.1006/jcph.1996.0130](https://doi.org/10.1006/jcph.1996.0130)
- P. L. Roe, "Approximate Riemann Solvers, Parameter Vectors, and Difference Schemes," Journal of Computational Physics, 43, 357-372, 1981. [doi:10.1016/0021-9991(81)90128-5](https://doi.org/10.1016/0021-9991(81)90128-5)
- E. F. Toro, M. Spruce, and W. Speares, "Restoration of the Contact Surface in the HLL-Riemann Solver," Shock Waves, 4, 25-34, 1994. [doi:10.1007/BF01414629](https://doi.org/10.1007/BF01414629)
- M.-S. Liou, "A Sequel to AUSM, Part II: AUSM+-up for All Speeds," Journal of Computational Physics, 214, 137-170, 2006. [doi:10.1016/j.jcp.2005.09.020](https://doi.org/10.1016/j.jcp.2005.09.020)
- V. Venkatakrishnan, "Convergence to Steady State Solutions of the Euler Equations on Unstructured Grids with Limiters," Journal of Computational Physics, 118, 120-130, 1995. [doi:10.1006/jcph.1995.1084](https://doi.org/10.1006/jcph.1995.1084)
- F. R. Menter, "Two-Equation Eddy-Viscosity Turbulence Models for Engineering Applications," AIAA Journal, 32, 1598-1605, 1994. [doi:10.2514/3.12149](https://doi.org/10.2514/3.12149)
- M. R. Hestenes and E. Stiefel, "Methods of Conjugate Gradients for Solving Linear Systems," Journal of Research of the National Bureau of Standards, 49, 409-436, 1952. [doi:10.6028/jres.049.044](https://doi.org/10.6028/jres.049.044)
- A. Brandt, "Multi-Level Adaptive Solutions to Boundary-Value Problems," Mathematics of Computation, 31, 333-390, 1977. [doi:10.1090/S0025-5718-1977-0431719-X](https://doi.org/10.1090/S0025-5718-1977-0431719-X)
- J. W. Ruge and K. Stuben, "Algebraic Multigrid," in Multigrid Methods, SIAM, 1987. [doi:10.1137/1.9781611971057.ch4](https://doi.org/10.1137/1.9781611971057.ch4)
- G. H. Golub and R. S. Varga, "Chebyshev Semi-Iterative Methods, Successive Over-Relaxation Iterative Methods, and Second Order Richardson Iterative Methods," Numerische Mathematik, 3, 147-168, 1961. [doi:10.1007/BF01386013](https://doi.org/10.1007/BF01386013), [doi:10.1007/BF01386014](https://doi.org/10.1007/BF01386014)
- Y. Saad, Iterative Methods for Sparse Linear Systems, 2nd ed., SIAM, 2003. [doi:10.1137/1.9780898718003](https://doi.org/10.1137/1.9780898718003)
