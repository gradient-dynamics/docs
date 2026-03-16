# Turbulence Models

Gradient Dynamics supports a range of turbulence models for different flow regimes and accuracy requirements. This page helps you choose the right model for your application.

## Available Models

### k-ω SST (Recommended Default)

The **Shear Stress Transport** model combines the best properties of k-ω (near walls) and k-ε (in the freestream). It is the most versatile RANS model and the recommended starting point for most applications.

**Strengths:**
- Accurate prediction of flow separation under adverse pressure gradients
- Robust wall treatment (works with both y+ ≈ 1 and y+ ≈ 30)
- Good all-around performance for external and internal flows

**Best for:** Vehicle aerodynamics, wing analysis, duct flows, general-purpose CFD

**Wall treatment:** Supports both y+ ≈ 30 (wall function, medium near-wall AMR) and y+ ≈ 1 (wall-resolved, fine near-wall AMR)

**Tier:** Starter and above

---

### k-ε (k-Epsilon)

A well-established two-equation model that solves for turbulent kinetic energy (k) and dissipation rate (ε).

**Strengths:**
- Very robust and stable convergence
- Good for fully turbulent flows away from walls
- Well-validated for pipe flows and free shear layers

**Limitations:**
- Overpredicts turbulence in stagnation regions
- Requires wall functions (y+ ≈ 30–300)
- Less accurate for separated flows

**Best for:** Internal pipe flows, industrial duct systems, fully turbulent flows

**Tier:** Starter and above

---

### Spalart-Allmaras

A one-equation model that solves a single transport equation for turbulent viscosity. Computationally the lightest RANS model.

**Strengths:**
- Low computational cost (one equation vs. two)
- Good for attached boundary layers
- Stable and fast-converging
- Flexible y+ requirements

**Limitations:**
- Less accurate for separated flows
- Not ideal for complex 3D flow patterns
- Overpredicts turbulence in free shear layers

**Best for:** Streamlined bodies, aerospace applications with attached flow, preliminary analysis

**Tier:** Starter and above

---

### Reynolds Stress Model (RSM)

A second-order closure that solves transport equations for all six Reynolds stress components. The most physically complete RANS model.

**Strengths:**
- Captures anisotropic turbulence effects
- Better for swirling flows, strong streamline curvature
- Most accurate RANS model for complex 3D flows

**Limitations:**
- Computationally expensive (7 extra equations)
- Can be less stable — needs careful relaxation
- Requires a good initial field (often started from k-ω SST)

**Best for:** Swirling flows, cyclones, rotating machinery, complex 3D separation

**Tier:** Starter and above

---

### LES (Large Eddy Simulation)

Resolves large-scale turbulent structures directly, modeling only the smallest scales. Provides time-accurate, transient results.

**Strengths:**
- Captures unsteady flow features (vortex shedding, wake dynamics)
- More accurate than RANS for massively separated flows
- Provides detailed turbulence statistics

**Limitations:**
- Requires very fine meshes (especially near walls)
- Transient — much longer simulation times
- Results need time-averaging for engineering quantities

**Best for:** Aeroacoustics, vortex dynamics, bluff body flows, academic research

**Tier:** Pro and above

---

### DES (Detached Eddy Simulation)

A hybrid approach: RANS near walls and LES in the bulk flow. Combines the efficiency of RANS in boundary layers with the accuracy of LES in separated regions.

**Best for:** Massive separation, buffet analysis, ground vehicle wakes

**Tier:** Pro and above

## Model Comparison

| Model | Equations | Cost | Separation Accuracy | Stability | Target y+ | Near-Wall AMR |
|-------|-----------|------|-------------------|-----------|-----------|---------------|
| **k-ω SST** | 2 | Low | Good | High | 1 or 30 | Medium (30) / Fine (1) |
| **k-ε** | 2 | Low | Fair | Very High | 30–300 | Medium |
| **Spalart-Allmaras** | 1 | Very Low | Fair | High | 1 or 30 | Medium (30) / Fine (1) |
| **RSM** | 7 | High | Very Good | Medium | 1 or 30 | Medium (30) / Fine (1) |
| **LES** | 0 (resolved) | Very High | Excellent | Medium | ~1 | Fine / Very Fine |
| **DES** | 2 (hybrid) | High | Very Good | Medium | ~1 | Fine |

The **Near-Wall AMR** column indicates the surface refinement setting to use in Mesh Settings to achieve the target y+. See [Near-Wall Resolution](../meshing/boundary-layers.md) for how to configure this.

## Choosing a Model

```{mermaid}
flowchart TD
    A[Start] --> B{Is the flow mostly attached?}
    B -->|Yes| C{Need quick results?}
    B -->|No| D{Is separation predictable?}
    C -->|Yes| E[Spalart-Allmaras]
    C -->|No| F[k-ω SST]
    D -->|Yes| F
    D -->|No| G{Need time-accurate results?}
    G -->|Yes| H[LES or DES]
    G -->|No| I{Strong swirl or rotation?}
    I -->|Yes| J[RSM]
    I -->|No| F
```

When in doubt, **start with k-ω SST**. It provides the best balance of accuracy, robustness, and computational cost for the widest range of applications.
