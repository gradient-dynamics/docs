# Glossary

Key terms and concepts used throughout the Gradient Dynamics documentation.

## A

**Adaptive Mesh**
: A mesh that varies cell size across the domain, using smaller cells where detail is needed and larger cells elsewhere.

**AMG (Algebraic Multigrid)**
: A preconditioner that solves linear systems efficiently by using a hierarchy of coarser approximations. Default in Gradient Dynamics.

**Angle of Attack (AoA)**
: The angle between the freestream velocity direction and the reference line of a body (e.g., a wing chord). Measured in degrees.

**Artificial Compressibility Method (ACM)**
: A technique for solving incompressible flows using a compressible-like formulation by adding a pseudo-compressibility term to the continuity equation, enabling explicit time marching on GPU hardware.

**Aspect Ratio**
: The ratio of a cell's longest dimension to its shortest. Boundary layer cells have intentionally high aspect ratios; volume cells should have low aspect ratios.

**AUSM+ (Advection Upstream Splitting Method)**
: A low-dissipation flux scheme that splits the inviscid flux into convective and pressure parts. Particularly accurate for low-Mach number flows.

## B

**Block (AMR)**
: A fixed-size array of Cartesian cells (typically 8×8×8) that forms the fundamental unit of the block-AMR mesh hierarchy. Blocks are refined by splitting into child blocks.

**Boundary Condition**
: A mathematical specification of what happens at the edge of the computational domain (inlet velocity, outlet pressure, wall no-slip, etc.).

**Boundary Layer**
: The thin region near a solid surface where the fluid velocity changes from zero (at the wall) to the freestream value. Also refers to the mesh layers (prisms) grown on walls to resolve this region.

**Bluff Body**
: A non-streamlined body that creates significant flow separation and a large wake. Examples: trucks, buildings, flat plates.

## C

**CAD (Computer-Aided Design)**
: Software and file formats for creating 3D geometry. STEP and IGES are common CAD exchange formats.

**Cd (Drag Coefficient)**
: A dimensionless number representing aerodynamic drag force, normalized by dynamic pressure and reference area: Cd = Fd / (0.5 × ρ × V² × A).

**Cell**
: The fundamental volume element of a computational mesh. The flow equations are solved for each cell.

**Coupled Solver**
: A solver that solves the momentum and pressure equations simultaneously as a single block system, rather than sequentially. More robust for strongly coupled flows.

**Cut Cell**
: A Cartesian hexahedral cell that has been clipped by a geometry surface to form a polyhedral cell conforming to the boundary. Cut cells carry volume fraction, shifted centroid, and aperture metadata.

**CFD (Computational Fluid Dynamics)**
: The use of numerical methods to solve fluid flow equations on a computer.

**CHT (Conjugate Heat Transfer)**
: A simulation type that couples fluid flow (convection) with solid heat conduction, sharing temperature and heat flux at their interface.

**Cl (Lift Coefficient)**
: A dimensionless number representing aerodynamic lift force, normalized by dynamic pressure and reference area.

**Convergence**
: The process by which iterative solver residuals decrease to acceptable levels, indicating the solution has stabilized.

**CGNS (CFD General Notation System)**
: A standard file format for storing CFD data, supported by many commercial and open-source solvers.

## D

**DES (Detached Eddy Simulation)**
: A hybrid RANS-LES approach that uses RANS near walls and LES in the bulk flow. Good for massively separated flows.

**Divergence**
: When a simulation fails to converge — residuals increase without bound. Usually indicates a numerical or setup problem.

**Domain**
: The region of space being simulated. For external flow, this is a wind-tunnel-like box around the geometry.

## F

**FSAC (Fractional Step Artificial Compressibility)**
: A hybrid explicit-implicit solver method that combines fractional step time advancement with an artificial compressibility formulation for pressure, bridging the gap between fully explicit and fully implicit approaches.

**Face**
: A polygon shared between two mesh cells (internal face) or between a cell and the domain boundary (boundary face).

**Far-field**
: The outer boundaries of the domain that are far from the geometry of interest.

**FVM (Finite Volume Method)**
: A numerical technique that discretizes the governing equations over control volumes (cells). The standard method in CFD.

## G

**Gauge Pressure**
: Pressure relative to a reference value (usually atmospheric). In incompressible CFD, only pressure differences matter, so outlet is typically set to 0 Pa gauge.

**Ground Effect**
: The aerodynamic influence of the ground on a nearby body (e.g., a car). Requires a moving ground boundary condition for accurate simulation.

## H

**Hexahedron (Hex)**
: A six-faced volume cell. Hexahedral meshes generally provide better numerical accuracy and convergence than tetrahedral meshes.

**HLLC (Harten-Lax-van Leer-Contact)**
: A Riemann solver that captures contact discontinuities in addition to shocks. A robust general-purpose flux scheme for compressible flow.

## I

**Isosurface**
: A 3D surface connecting all points where a field has the same value (e.g., a surface of constant pressure).

## K

**k (Turbulent Kinetic Energy)**
: The kinetic energy contained in turbulent fluctuations. Half the sum of the velocity variance in all three directions. Units: m²/s².

## L

**LES (Large Eddy Simulation)**
: A turbulence modeling approach that resolves large-scale eddies directly and models only the smallest scales. More accurate but much more expensive than RANS.

**Linelet**
: A wall treatment technique that embeds a one-dimensional sub-grid within each near-wall cell, solving the boundary layer profile locally. Provides wall-resolved accuracy on coarser meshes.

## M

**MUSCL (Monotone Upstream-centered Scheme for Conservation Laws)**
: A higher-order spatial reconstruction method that interpolates cell-centered values to face centers for improved accuracy. Default reconstruction scheme in the density-based solver.

**Manifold**
: A surface where every edge is shared by exactly two faces. Non-manifold surfaces have topology errors.

**MRF (Multiple Reference Frame)**
: A steady-state method for simulating rotating machinery. The flow equations in the rotating zone include Coriolis and centrifugal source terms.

## N

**No-Slip**
: The wall boundary condition where fluid velocity equals zero at the surface. This is the physical reality for viscous flows.

**Non-Orthogonality**
: The angle between a face normal vector and the vector connecting adjacent cell centers. High values indicate poor mesh quality.

## O

**Octree**
: A hierarchical spatial decomposition where each cube is recursively divided into 8 sub-cubes. Used for adaptive mesh generation.

## P

**Patch**
: A named group of boundary faces. Used to apply boundary conditions (e.g., "inlet" patch, "car_body" patch).

**PIMPLE**
: A hybrid pressure-velocity coupling algorithm combining SIMPLE outer iterations with PISO inner corrections. The most stable option for transient flows with large time steps.

**PISO (Pressure-Implicit with Splitting of Operators)**
: A pressure-velocity coupling algorithm used primarily for transient simulations with small time steps.

**Prism**
: A wedge-shaped cell typically used in boundary layers, with triangular faces on the wall and outer surfaces.

## R

**RANS (Reynolds-Averaged Navier-Stokes)**
: A CFD approach that solves time-averaged flow equations with turbulence models. The industry standard for engineering CFD.

**Relaxation Factor**
: A number between 0 and 1 that controls how much the solution is updated each iteration. Lower values are more stable; higher values converge faster.

**Residual**
: A measure of how well the discretized equations are satisfied at the current iteration. Lower is better.

**Reynolds Number (Re)**
: A dimensionless number representing the ratio of inertial to viscous forces: Re = ρVL/μ. Determines whether flow is laminar or turbulent.

## S

**Segregated Solver**
: A solver strategy that solves each governing equation (momentum, pressure, turbulence) sequentially and iterates to convergence. SIMPLE, PISO, and PIMPLE are segregated algorithms.

**Signed Distance Field (SDF)**
: A scalar field where each point stores the signed distance to the nearest geometry surface — negative inside solids, positive in fluid. Used for cell classification and cut-cell generation.

**SIMPLE (Semi-Implicit Method for Pressure-Linked Equations)**
: The standard pressure-velocity coupling algorithm for steady-state CFD.

**SIMPLEC (SIMPLE-Consistent)**
: An improved variant of SIMPLE that requires less under-relaxation and can converge faster for some problems.

**Skewness**
: A mesh quality metric measuring how much a cell deviates from its ideal shape (0 = perfect, 1 = degenerate).

**Slip Wall**
: A boundary condition with zero shear stress — the fluid slides freely along the surface.

**Streamline**
: A curve that is everywhere tangent to the velocity field. Shows the path a fluid particle would follow.

## T

**Turbulence Intensity (TI)**
: The ratio of velocity fluctuations to the mean velocity, expressed as a percentage. Defines the level of incoming turbulence.

## V

**Volume Fraction**
: For cut cells, the ratio of the fluid portion of the cell to the full Cartesian cell volume. A volume fraction of 1.0 means the cell is entirely fluid; values near 0 indicate a thin sliver that is typically merged with a neighbor.

**VTU (VTK Unstructured)**
: A file format for unstructured meshes and field data, used by ParaView and other visualization tools.

## W

**WENO (Weighted Essentially Non-Oscillatory)**
: A high-order spatial reconstruction scheme that maintains accuracy near discontinuities without introducing spurious oscillations. Available in 3rd and 5th order variants.

**Watertight**
: A surface mesh that is completely closed with no gaps or holes. Required for volume mesh generation.

## Y

**y+**
: A dimensionless wall distance: y+ = (u_τ × y) / ν. Determines the first cell height needed for proper turbulence model behavior.

**ω (Specific Dissipation Rate)**
: The rate of dissipation per unit turbulent kinetic energy. Used in k-ω turbulence models. Units: 1/s.

**ε (Dissipation Rate)**
: The rate at which turbulent kinetic energy is dissipated into heat. Used in k-ε turbulence models. Units: m²/s³.
