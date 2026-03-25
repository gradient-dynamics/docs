# Turbulence Models

Gradient Dynamics groups turbulence modelling into four simulation types: **RANS**, **LES**, **DES**, and **URANS**. Select the simulation type first, then choose the specific model within it.

## RANS

Reynolds-Averaged Navier-Stokes (RANS) models solve for a time-averaged flow field. All turbulent fluctuations are modelled rather than resolved, making RANS the fastest and most practical approach for the majority of engineering CFD.

**When to use:** Steady-state external aerodynamics, internal flows, rotating machinery, heat transfer — any application where time-averaged quantities (drag, lift, pressure drop, temperature) are the primary output.

**Tier:** Starter and above

---

### k-ω SST

The **Shear Stress Transport** model combines k-ω near walls with k-ε in the freestream via a blending function. The most versatile RANS model and the recommended starting point for most applications.

**Strengths:**
- Accurate prediction of flow separation under adverse pressure gradients
- Robust wall treatment — works with both y+ ≈ 1 and y+ ≈ 30
- Good all-around performance for external and internal flows
- Multiple variants available for specific applications

**Limitations:**
- Can overpredict turbulence in regions of strong streamline curvature

**Variants:** The standard SST-2003 formulation is the default. A vorticity-based production variant and rotation correction variant are available for flows with strong swirl or curved streamlines — these can be selected through the AI Assistant for advanced use cases.

**Best for:** Vehicle aerodynamics, wing analysis, duct flows, general-purpose CFD

**Near-wall AMR:** Medium (y+ ≈ 30) or Fine (y+ ≈ 1)

---

### k-ε

A two-equation model solving for turbulent kinetic energy (k) and dissipation rate (ε). The most numerically stable RANS model.

**Strengths:**
- Very robust and stable convergence
- Good for fully turbulent flows away from walls
- Well-validated for pipe flows and free shear layers

**Limitations:**
- Overpredicts turbulence in stagnation regions
- Requires wall functions (y+ ≈ 30–300)
- Less accurate for separated flows

**Best for:** Internal pipe flows, industrial duct systems, fully turbulent flows

**Near-wall AMR:** Medium (y+ ≈ 30–300)

---

### Spalart-Allmaras

A one-equation model solving a single transport equation for turbulent viscosity. The lightest RANS model computationally. Several variants are available to handle specific flow conditions.

**Strengths:**
- Lowest computational cost of all RANS models
- Good for attached boundary layers
- Stable and fast-converging
- Well-suited for compressible flows (integrated with the density-based solver)

**Limitations:**
- Less accurate for separated flows
- Overpredicts turbulence in free shear layers
- Not well-suited for complex 3D flow patterns

**Variants:**

| Variant | Description |
|---------|-------------|
| **Standard** | Classic SA formulation — recommended starting point |
| **SA-neg** | Handles negative turbulence variable values gracefully — more robust for difficult initializations |
| **SA-noft2** | Removes the ft2 laminar suppression term — simpler and often equivalent for fully turbulent flows |
| **Compressibility correction** | Accounts for compressibility effects on turbulence at high Mach numbers |
| **Rotation correction** | Improved accuracy in rotating or strongly curved flows |

The default is the **standard** variant. Studio selects the appropriate variant automatically based on your solver and flow configuration, or you can select one explicitly through the AI Assistant.

**Best for:** Streamlined bodies, aerospace applications, compressible flows, preliminary analysis

**Near-wall AMR:** Medium (y+ ≈ 30) or Fine (y+ ≈ 1)

---

### Reynolds Stress Model (RSM)

A second-order closure solving transport equations for all six Reynolds stress components plus a dissipation equation. The most physically complete RANS model available.

**Strengths:**
- Captures anisotropic turbulence effects that eddy-viscosity models cannot
- Accurate for swirling flows, strong streamline curvature, and 3D separation
- Best RANS accuracy for complex flows with turbulence anisotropy

**Limitations:**
- Computationally expensive — 7 additional transport equations
- Can be less stable; typically initialized from a converged k-ω SST solution
- Requires more conservative relaxation/CFL tuning

**Pressure-strain correlation models:**

| Model | Description |
|-------|-------------|
| **LRR-IP** | Launder-Reece-Rodi with isotropization of production — robust general-purpose default |
| **SSG** | Speziale-Sarkar-Gatski — quadratic pressure-strain; better for complex 3D flows |

The default is **LRR-IP**. Studio applies conservative relaxation factors automatically for RSM to ensure stable convergence.

**Best for:** Swirling flows, cyclones, rotating machinery, complex 3D separation, turbomachinery

**Near-wall AMR:** Medium (y+ ≈ 30) or Fine (y+ ≈ 1)

---

## LES

Large Eddy Simulation directly resolves large-scale turbulent structures and only models the smallest (sub-grid) scales using a Sub-Grid Scale (SGS) model. It provides time-accurate, physically rich results but at significantly higher cost than RANS.

**When to use:** Aeroacoustics, vortex shedding, wake dynamics, bluff body flows, or any case where the time-resolved turbulence structure matters — not just the mean flow.

**Requirements:** Very fine mesh (Fine or Very Fine near-wall AMR), transient simulation with small time steps.

**Tier:** Pro and above

---

### Smagorinsky

The classical SGS model. Applies a constant eddy-viscosity based on the local strain rate and a mixing-length coefficient (Smagorinsky constant Cs).

**Strengths:**
- Simple, robust, and computationally cheap
- Well-understood behaviour

**Limitations:**
- Overly dissipative in transitional or near-wall regions
- Cs must be tuned for different flow types

**Best for:** High-Reynolds fully turbulent flows, channel flows, jets

---

### Dynamic Smagorinsky

Extends the Smagorinsky model by computing the Cs coefficient dynamically from the resolved flow field using Germano's identity — no manual constant tuning required.

**Strengths:**
- Automatically adapts to local flow conditions
- More accurate in transitional and near-wall regions
- Better performance for complex geometries

**Limitations:**
- Slightly higher cost than static Smagorinsky
- Can occasionally produce negative eddy viscosity (clipped automatically)

**Best for:** General-purpose LES, complex geometries, transitional flows

---

### WALE

The **Wall-Adapting Local Eddy-viscosity** model uses a formulation based on the velocity gradient tensor that naturally goes to zero at solid walls — no damping function needed.

**Strengths:**
- Correct near-wall scaling without explicit damping
- Well-suited for wall-bounded flows
- Good performance on coarser near-wall meshes than Dynamic Smagorinsky

**Limitations:**
- Slightly more expensive than static Smagorinsky

**Best for:** Wall-bounded LES, turbulent channel flows, complex internal geometries

---

### Vreman

An algebraic SGS model with similar near-wall behaviour to WALE but at lower computational cost.

**Strengths:**
- Zero SGS viscosity in laminar and transitional regions (no manual switching)
- Lower cost than WALE and Dynamic Smagorinsky
- Robust on moderately coarse LES meshes

**Best for:** Transitional flows, cost-sensitive LES, engineering LES on moderate meshes

---

## DES

Detached Eddy Simulation is a hybrid approach: RANS is used in attached boundary layers (where it is efficient and accurate), and LES is used in detached separated regions (where it is needed). This combines the wall-efficiency of RANS with the accuracy of LES in wakes and separated zones.

**When to use:** Flows with large separated regions where RANS is inaccurate but full LES is unaffordable — ground vehicle wakes, bluff bodies, buffet, stall.

**Requirements:** Fine near-wall AMR for the RANS region; the LES region is handled automatically by the DES switching function.

**Tier:** Pro and above

---

### SA-DES

The original DES formulation, using **Spalart-Allmaras** as the RANS backbone. The DES limiter switches the model from RANS to LES mode based on the ratio of wall distance to local grid spacing.

**Best for:** External aerodynamics with significant separation, ground vehicles, bluff bodies

---

### SST-DES

DES formulation using **k-ω SST** as the RANS backbone. Offers the same RANS-to-LES switching but with SST's superior wall-bounded flow prediction in the RANS region.

**Best for:** Cases where SST is preferred for the near-wall RANS treatment — vehicle aerodynamics, wing flows with trailing-edge separation

---

### DDES

**Delayed DES** adds a shielding function to prevent the LES mode from activating prematurely inside attached boundary layers (a known issue with the original DES). Available with both SA and SST backbones. Recommended over standard DES for most applications.

**Best for:** All cases where DES would be used — DDES is the safer default

---

### IDDES

**Improved Delayed DES** extends DDES with wall-modelled LES capability. When the mesh is fine enough near walls, IDDES can operate as a wall-modelled LES in the inner layer, providing higher accuracy than standard DDES in the near-wall region.

**Best for:** High-fidelity analysis of massively separated flows where near-wall LES accuracy is needed

---

## URANS

Unsteady RANS solves the RANS equations as a time-accurate transient simulation. The same turbulence models as steady RANS are used, but the flow is allowed to evolve in time. This captures large-scale periodic unsteadiness without the cost of LES.

**When to use:** Periodic vortex shedding, pulsating flows, rotating machinery with transient effects, any flow where large-scale unsteadiness exists but full LES resolution is not required.

**Note:** URANS does not resolve turbulent fluctuations — it only captures deterministic, large-scale unsteadiness. Use LES or DES when turbulence structure itself matters.

**Tier:** Pro and above

---

### URANS k-ω SST

Time-accurate integration of the k-ω SST equations. The most common URANS setup and the recommended starting point.

**Best for:** Vortex shedding behind bluff bodies, oscillating airfoil flows, transient wake interactions

---

### URANS k-ε

Time-accurate k-ε for flows where the high stability of k-ε is beneficial in a transient context.

**Best for:** Transient internal flows, pulsating pipe flows, HVAC transients

---

### URANS RSM

Time-accurate Reynolds Stress Model for transient flows with strong anisotropy or swirl.

**Best for:** Transient swirling flows, transient rotating machinery, precessing vortex cores

---

## Comparison Table

| Model | Type | Equations | Relative Cost | Separation Accuracy | Steady/Transient | Tier |
|-------|------|-----------|---------------|--------------------|--------------------|------|
| k-ω SST | RANS | 2 | Low | Good | Steady | Starter+ |
| k-ε | RANS | 2 | Low | Fair | Steady | Starter+ |
| Spalart-Allmaras | RANS | 1 | Very Low | Fair | Steady | Starter+ |
| RSM (LRR-IP / SSG) | RANS | 7 | High | Very Good | Steady | Starter+ |
| Smagorinsky | LES | SGS | Very High | Excellent | Transient | Pro+ |
| Dynamic Smagorinsky | LES | SGS | Very High | Excellent | Transient | Pro+ |
| WALE | LES | SGS | Very High | Excellent | Transient | Pro+ |
| Vreman | LES | SGS | High | Excellent | Transient | Pro+ |
| SA-DES | DES | Hybrid | High | Very Good | Transient | Pro+ |
| SST-DES | DES | Hybrid | High | Very Good | Transient | Pro+ |
| DDES | DES | Hybrid | High | Very Good | Transient | Pro+ |
| IDDES | DES | Hybrid | Very High | Excellent | Transient | Pro+ |
| URANS k-ω SST | URANS | 2 | Medium | Good | Transient | Pro+ |
| URANS k-ε | URANS | 2 | Medium | Fair | Transient | Pro+ |
| URANS RSM | URANS | 7 | Very High | Very Good | Transient | Pro+ |

## Choosing a Simulation Type

```{mermaid}
flowchart TD
    A[Start] --> B{Need time-accurate results?}
    B -->|No| C[RANS]
    B -->|Yes| D{Is turbulence structure important?}
    D -->|No| E[URANS]
    D -->|Yes| F{Can you afford full LES cost?}
    F -->|Yes| G[LES]
    F -->|No| H[DES / DDES]
    C --> I{Strong swirl or rotation?}
    I -->|Yes| J[RSM]
    I -->|No| K{Quick estimate?}
    K -->|Yes| L[Spalart-Allmaras]
    K -->|No| M[k-ω SST]
```

When in doubt, **start with RANS k-ω SST**. It covers the widest range of applications at the lowest cost and provides a good initial field for switching to higher-fidelity methods if needed.
