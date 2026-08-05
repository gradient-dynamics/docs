# Exceptions and limits

```{py:module} gradientdynamics.exceptions
:no-index:
```

All SDK exceptions derive from {py:class}`GradientDynamicsError`.

```{py:exception} GradientDynamicsError

Base exception raised by the `gradientdynamics` package.
```

```{py:exception} AuthenticationError

Credentials are missing, expired or not permitted to access the resource.
```

````{py:exception} ValidationError

Configuration validation failed before compute allocation.

```{py:attribute} errors
:type: Sequence[FieldError]

Structured field paths, messages and rejected values.
```
````

```{py:exception} NotFoundError

The requested resource or completed asset does not exist in the authenticated
organisation.
```

```{py:exception} ResourceNotReadyError

A result was requested before its job completed.
```

````{py:exception} CapacityError

Current meshing or GPU capacity is full.

```{py:attribute} retry_after
:type: float | None

Suggested delay in seconds before another request.
```
````

````{py:exception} JobFailedError

Remote execution reached a terminal failure.

```{py:attribute} stage
:type: str | None
```

```{py:attribute} job_id
:type: str
```
````

```{py:exception} ServiceUnavailableError

The service cannot safely execute the operation at present.
```

## Handling temporary failures

```python
import time

from gradientdynamics.exceptions import CapacityError

try:
    job = simulation.run(idempotency_key="road-car-baseline-v1")
except CapacityError as exc:
    time.sleep(exc.retry_after or 30.0)
    job = simulation.run(idempotency_key="road-car-baseline-v1")
```

Retry temporary network, capacity and availability failures with bounded
backoff. Do not automatically retry schema, topology or boundary-name errors.
Read the original job before retrying after a lost response, and reuse the same
idempotency key only for the same intended operation.

## Organisation limits

Meshing concurrency, CPU memory, GPU capacity, project quotas, storage and
retention are organisation- and environment-specific. The client exposes
enabled capabilities and quota summaries through
{py:attr}`gradientdynamics.Client.organisation`; scripts should handle queueing
without creating duplicate work.
