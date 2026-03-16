# Subscription Tiers

Gradient Dynamics Studio offers tiered subscriptions to match different usage levels, from individual engineers to enterprise deployment.

## Tier Comparison

| Feature | Starter | Pro | Team | Enterprise |
|---------|---------|-----|------|-----------|
| **Monthly credits** | 100 | 2,000 | 5,000 | Unlimited |
| **Projects** | Unlimited | Unlimited | Unlimited | Unlimited |
| **Max mesh cells** | 50M | 100M | 500M | Unlimited |
| **Storage** | 50 GB | 200 GB | 500 GB | Custom |
| **Near-wall AMR** | Yes | Yes | Yes | Yes |
| **CHT support** | No | Yes | Yes | Yes |
| **MRF (rotating)** | No | Yes | Yes | Yes |
| **CFD simulation** | Yes | Yes | Yes | Yes |

## Turbulence Models by Tier

| Model | Starter | Pro | Team | Enterprise |
|-------|---------|-----|------|-----------|
| k-ω SST | Yes | Yes | Yes | Yes |
| k-ε | Yes | Yes | Yes | Yes |
| Spalart-Allmaras | Yes | Yes | Yes | Yes |
| RSM | Yes | Yes | Yes | Yes |
| LES | — | Yes | Yes | Yes |
| DES / DDES | — | Yes | Yes | Yes |
| URANS | — | Yes | Yes | Yes |

## Credit Rates

| Operation | Credits per GPU-minute |
|-----------|----------------------|
| Mesh generation | 0.2 |
| CFD simulation | 1.0 |

### Estimating Credit Usage

**Mesh generation** typically takes 1–10 GPU-minutes depending on cell count:
- 2M cells: ~2 min → 0.4 credits
- 10M cells: ~5 min → 1.0 credits
- 50M cells: ~15 min → 3.0 credits

**CFD simulation** runtime depends on mesh size and convergence:
- 2M cells, 500 iterations: ~5 min → 5 credits
- 10M cells, 1000 iterations: ~20 min → 20 credits
- 50M cells, 1000 iterations: ~60 min → 60 credits

*These are rough estimates — actual usage varies by geometry complexity and solver behavior.*

## Starter Tier

For individual engineers and small projects:

- 100 monthly credits
- Unlimited projects
- 50M cell limit
- RANS simulation with all standard models
- Near-wall AMR support

## Pro Tier

For professional users and advanced analysis:

- 2,000 monthly credits
- 100M cell limit
- LES, DES, and URANS transient capabilities
- Conjugate heat transfer (CHT)
- Rotating machinery (MRF)

## Team Tier

For engineering teams:

- 5,000 monthly credits
- 500M cell limit
- All Pro features
- Team management and shared projects

## Enterprise Tier

For large organizations:

- Unlimited credits and cells
- Custom storage
- Dedicated support
- Custom integrations
- SLA guarantees

Contact sales for Enterprise pricing and custom configurations.
