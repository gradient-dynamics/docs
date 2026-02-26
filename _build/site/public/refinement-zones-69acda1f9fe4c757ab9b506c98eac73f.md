# Refinement Zones

Refinement zones allow you to increase mesh resolution in specific regions of the domain without refining the entire mesh. This is essential for capturing flow features like wakes, separation zones, and shear layers.

## Why Use Refinement Zones?

The base mesh resolution is set by the target cell size, which applies uniformly across the domain. But many flow features are localized:

- **Wake behind a vehicle** — Needs finer cells to resolve turbulent structures
- **Separation region** around a wing — Needs resolution to capture recirculation
- **Gap between components** — Needs fine cells to resolve flow through narrow passages
- **Jet or exhaust plume** — Needs fine cells along the jet path

Refinement zones let you concentrate cells where they matter most, keeping the total cell count manageable.

## Zone Shapes

### Box

A rectangular region defined by center position and dimensions (length × width × height).

**Best for:**
- Vehicle wakes (elongated box behind the car)
- Ground effect regions (flat box under the vehicle)
- Rectangular flow passages

### Cylinder

A cylindrical region defined by center, axis direction, radius, and length.

**Best for:**
- Rotating zones (fans, wheels, propellers)
- Jet flows and exhaust plumes
- Pipe sections requiring higher resolution

### Sphere

A spherical region defined by center and radius.

**Best for:**
- Point sources or sinks
- Localized regions of interest
- Probe locations where you want high resolution

## Adding Refinement Zones

1. In the **Setup** tab, click **Add Refinement Zone**
2. Select the zone shape (Box, Cylinder, or Sphere)
3. Position and size the zone using either:
   - **3D viewer** — Drag the zone handles to position and resize
   - **Numerical input** — Enter exact coordinates and dimensions in the panel
4. Set the **refinement cell size** — this overrides the base cell size within the zone

## Refinement Cell Size

Each zone has its own target cell size that applies within its volume. The cell size should be:

- **Smaller** than the base mesh cell size (otherwise the zone has no effect)
- **Proportional** to the feature you want to capture
- **Not too small** relative to the base mesh — very large jumps in cell size cause poor quality transitions

```{admonition} Sizing Guideline
:class: tip
A good rule of thumb: the refinement zone cell size should be no more than **4× smaller** than the surrounding cells per refinement level. The octree mesher handles transitions automatically, but extreme jumps require more transition cells.
```

## Common Refinement Strategies

### Vehicle Aerodynamics

| Zone | Shape | Position | Purpose |
|------|-------|----------|---------|
| **Wake zone** | Box | Behind vehicle, 2–3× car length | Capture wake structure |
| **Underbody zone** | Box | Under vehicle, ground to floor | Resolve ground effect |
| **Wheel zones** | Cylinder | Around each wheel | Capture wheel rotation effects |
| **Front zone** | Box | Ahead of vehicle, 0.5× length | Resolve stagnation region |

### Airfoil / Wing

| Zone | Shape | Position | Purpose |
|------|-------|----------|---------|
| **Leading edge** | Box | Extends upstream of LE | Capture stagnation |
| **Trailing edge** | Box | Behind TE, 1–2× chord | Resolve wake and mixing |
| **Suction side** | Box | Above airfoil | Capture separation bubble |

### Internal Flow

| Zone | Shape | Position | Purpose |
|------|-------|----------|---------|
| **Bend region** | Box/Cylinder | Around pipe bends | Capture separation in turns |
| **Constriction** | Cylinder | At flow restrictions | Resolve acceleration |
| **Mixing zone** | Box | Downstream of junctions | Capture flow mixing |

## Managing Zones

- **Edit** — Click a zone in the feature tree or 3D viewer to modify its properties
- **Delete** — Remove zones you no longer need
- **Toggle visibility** — Show/hide zones in the 3D viewer for clarity

Multiple refinement zones can overlap. Where zones overlap, the **finest** (smallest cell size) takes precedence.
