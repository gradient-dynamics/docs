# Mesh Configuration with the Assistant

The AI Assistant can guide you through the entire meshing workflow, from geometry analysis to mesh generation. This page shows common conversation patterns for mesh setup.

## Geometry Analysis

### Basic Readiness Check

> **You:** "Is my geometry ready for meshing?"
>
> **Assistant:** *Runs geometry analysis and reports:*
> - Watertight: Yes/No
> - Manifold: Yes/No
> - Number of bodies detected
> - Bounding dimensions
> - Recommended repairs (if any)

### Detailed Analysis

> **You:** "Run a detailed geometry analysis"
>
> **Assistant:** *Performs enhanced analysis comparing raw vs. welded mesh, identifies specific problem areas, and provides repair recommendations with severity ratings.*

### Repair Geometry

> **You:** "Fix the geometry issues"
>
> **Assistant:** *Applies recommended repairs (welding, hole filling, non-manifold fixing) and reports the results. For CAD files, offers B-Rep healing.*

## Domain Setup

### Automatic Configuration

> **You:** "Set up an external aero mesh for a car"
>
> **Assistant:** *Analyzes geometry dimensions and creates an external flow domain with:*
> - Appropriately sized wind tunnel box
> - Ground plane enabled
> - Default padding ratios based on car dimensions
> - Presents configuration for confirmation

### Specific Requirements

> **You:** "Set up an internal flow domain for a pipe system"
>
> **Assistant:** *Switches to internal flow domain type, identifies inlet/outlet faces, and configures the mesh to fill the internal volume.*

### Rotating Machinery

> **You:** "This is a centrifugal pump impeller rotating at 3000 RPM"
>
> **Assistant:** *Sets up rotating machinery domain type, creates MRF zone with correct axis and speed, identifies rotating and stationary regions.*

## Mesh Parameters

### Guided Recommendations

> **You:** "What mesh settings should I use?"
>
> **Assistant:** *Based on the geometry dimensions and domain type, recommends:*
> - Target cell size
> - Boundary layer settings with y+ targeting
> - Refinement levels
> - Estimated cell count

### Boundary Layer Setup

> **You:** "Set up boundary layers for highway speed (120 km/h)"
>
> **Assistant:** *Calculates:*
> - Reynolds number based on geometry length
> - Appropriate first layer height for target y+
> - Number of layers and growth rate
> - Presents configuration for confirmation

### Refinement Zones

> **You:** "Add refinement zones for the wake and underbody"
>
> **Assistant:** *Creates:*
> - A box refinement zone behind the geometry for the wake
> - A flat box refinement zone under the geometry
> - Sizes and positions based on geometry dimensions
> - Presents each zone for confirmation

## Surface Naming

### Auto-Detection

> **You:** "Detect and name the surfaces"
>
> **Assistant:** *Analyzes the geometry and mesh boundary, identifies:*
> - Inlet/outlet faces by position
> - Wall surfaces by orientation
> - Domain boundaries by location
> - Suggests names for each

### Specific Naming

> **You:** "Name the front face as inlet and the back face as outlet"
>
> **Assistant:** *Identifies the specified faces and assigns the names.*

## Mesh Generation

### Generate with Current Settings

> **You:** "Generate the mesh"
>
> **Assistant:** *Summarizes the current configuration, shows estimated cell count and credit cost, and submits the mesh generation job with your confirmation.*

### Quality Review

> **You:** "How is the mesh quality?"
>
> **Assistant:** *Reviews the mesh quality report and explains:*
> - Overall quality rating
> - Any areas of concern (high skewness cells, etc.)
> - Whether the mesh is suitable for your intended simulation
> - Suggestions for improvement if needed

## Example: Complete Workflow

Here's a full conversation for setting up a vehicle aerodynamics mesh:

> **You:** "I uploaded a car model. Help me set up a mesh for aerodynamic analysis."
>
> **Assistant:** "Let me analyze your geometry first."
> *Runs analysis...*
> "Your geometry looks good — it's watertight and manifold. The car is 4.5 m long, 1.8 m wide, and 1.4 m high. I'll set up an external aerodynamics mesh. I recommend:
>
> - External flow domain with ground plane
> - Domain: 6.75 m upstream, 13.5 m downstream, 2.7 m sides, 2.8 m top
> - Base cell size: 0.1 m
> - 10 boundary layers, first height 0.001 m (y+ ≈ 30 at 120 km/h)
> - Wake refinement zone: 9 m × 2.7 m × 2.1 m behind the car at 0.05 m cell size
>
> **[Confirm]** **[Cancel]**"
>
> **You:** "Confirm. Also add underbody refinement."
>
> **Assistant:** "Domain created. I'll add an underbody refinement zone:
> - Box: 5.4 m × 2.2 m × 0.3 m under the car
> - Cell size: 0.04 m
>
> **[Confirm]**"
>
> **You:** "Confirm. Generate the mesh."
>
> **Assistant:** "Estimated mesh: ~8 million cells, ~0.5 credits. Submitting mesh generation now.
>
> **[Confirm]**"
