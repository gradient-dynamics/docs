# Jobs and status

```{py:module} gradientdynamics.jobs
:no-index:
```

Meshing and simulation methods return typed jobs because both operations can
queue and allocate managed compute.

## Job status

````{py:class} JobStatus

Lifecycle state of an asynchronous operation.

```{py:attribute} QUEUED
:value: "queued"

Accepted and waiting for capacity.
```

```{py:attribute} RUNNING
:value: "running"

Active preparation, meshing, solution or export work.
```

```{py:attribute} COMPLETED
:value: "completed"

Result and manifest committed successfully.
```

```{py:attribute} FAILED
:value: "failed"

Terminal execution failure. Inspect {py:attr}`Job.error`.
```

```{py:attribute} CANCELLED
:value: "cancelled"

Stopped before completion by the client or platform.
```
````

## Generic job

````{py:class} Job[T]

Handle to one asynchronous operation whose successful result is type `T`.

```{py:attribute} id
:type: str

Opaque job identifier.
```

```{py:attribute} status
:type: JobStatus
```

```{py:attribute} progress
:type: float | None

Best available completion estimate from 0.0 to 1.0.
```

```{py:attribute} stage
:type: str | None

Diagnostic stage label. Treat {py:attr}`status` as the lifecycle contract.
```

```{py:attribute} error
:type: JobError | None

Structured terminal error, available when status is `FAILED`.
```

```{py:method} refresh() -> Job[T]

Read current state from the service and return the updated job.
```

```{py:method} wait(*, timeout: float | None = None, poll_interval: float = 5.0) -> Job[T]

Poll until the job reaches a terminal state. Raises `TimeoutError` if the local
timeout expires without cancelling remote work.
```

```{py:method} cancel() -> Job[T]

Request cancellation and return the refreshed job state.
```

```{py:method} result() -> T

Return the completed typed result. Raises
{py:class}`gradientdynamics.exceptions.ResourceNotReadyError` before completion
or {py:class}`gradientdynamics.exceptions.JobFailedError` after failure.
```
````

## Waiting and monitoring

```python
from gradientdynamics.jobs import JobStatus

job = geometry.mesh(mesh_config, idempotency_key="baseline-mesh-v1")

while job.refresh().status not in {
    JobStatus.COMPLETED,
    JobStatus.FAILED,
    JobStatus.CANCELLED,
}:
    print(job.stage, job.progress)

mesh = job.result()
```

For most scripts, the compact form is sufficient:

```python
mesh = geometry.mesh(mesh_config).wait(timeout=3600).result()
```

## Idempotency and retries

Supply a stable idempotency key when a lost network response could otherwise
create duplicate work. A network interruption does not imply job failure;
retrieve or refresh the original job before submitting a replacement.

Clients should respect server-provided retry delays, use bounded backoff and
avoid concurrent poll loops for the same job. Approved integrations can also
receive authenticated progress callbacks; the job object remains the
authoritative record.
