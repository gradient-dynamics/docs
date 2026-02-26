# AI Assistant

The Gradient Dynamics AI Assistant is an intelligent co-pilot built into Studio that helps you configure meshes, set up simulations, and troubleshoot issues using natural language conversation.

## What the Assistant Can Do

### Geometry Analysis
- Check if your geometry is ready for meshing
- Identify and fix watertightness, manifold, and topology issues
- Detect special features like wheels, rotating parts, and surface faces
- Recommend repair strategies for problematic geometry

### Mesh Configuration
- Suggest domain type and sizing based on your application
- Recommend mesh parameters (cell size, boundary layers, refinement)
- Configure refinement zones for key flow features
- Set up multi-region domains for CHT and rotating machinery

### Simulation Setup
- Select appropriate turbulence models for your application
- Configure boundary conditions from surface names
- Set solver parameters and convergence criteria
- Launch simulations with your confirmation

### Results Interpretation
- Calculate force and moment coefficients
- Explain flow features visible in the results
- Suggest post-processing views for your application
- Provide context on whether results look reasonable

## How to Use the Assistant

### Opening the Panel

The AI Assistant appears as a panel on the right side of the workspace. Click the **Assistant** button in the toolbar to toggle it open or closed.

### Asking Questions

Type your question or instruction in natural language at the bottom of the panel. Examples:

```
"Is my geometry ready for meshing?"
```

```
"Set up an external aerodynamics mesh for a car at 120 km/h"
```

```
"What turbulence model should I use for pipe flow?"
```

```
"Run a simulation with k-omega SST at 30 m/s"
```

### Confirming Actions

When the assistant wants to make changes to your project (e.g., creating a domain box, setting boundary conditions, launching a simulation), it presents the action for your approval:

> **Assistant:** I'd like to create an external flow domain with the following dimensions:
> - Upstream: 6.75 m
> - Downstream: 13.5 m
> - Sides: 2.7 m each
> - Top: 3.6 m
>
> **[Confirm]** **[Cancel]**

Click **Confirm** to apply the action, or **Cancel** to reject it and provide different instructions.

### Reasoning Display

The assistant shows a collapsible **"See reasoning"** section that reveals its thought process. This helps you understand:
- Why it chose specific parameters
- What trade-offs it considered
- What assumptions it made about your application

## Tips for Effective Use

### Be Specific About Your Application

Instead of:
> "Mesh this geometry"

Say:
> "Create an external aerodynamics mesh for a sedan at highway speed with boundary layers"

The more context you provide, the better the recommendations.

### Start with Analysis

Before configuring, ask the assistant to analyze your geometry:

> "Analyze my geometry and tell me if it's ready for meshing"

This catches problems early and informs the meshing strategy.

### Use It Iteratively

The assistant works best as an interactive partner:

1. Start with a question: *"What domain type should I use?"*
2. Refine based on the response: *"Use external flow with a ground plane"*
3. Request specific actions: *"Set boundary layers to 10 layers with y+ = 30"*
4. Confirm each step before moving to the next

### Ask for Explanations

If you're unsure about a parameter or recommendation:

> "Why did you choose 10 boundary layers instead of 5?"

> "What does the skewness metric mean and is mine acceptable?"

The assistant will explain the reasoning and help you make informed decisions.

## Limitations

- The assistant operates within the context of your **current project** — it doesn't have access to other projects
- It requires your **explicit confirmation** before making changes
- For very complex multi-physics setups, manual configuration may be needed alongside assistant guidance
- The assistant's suggestions are recommendations — always apply your engineering judgment
