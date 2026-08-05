# Client and availability

```{py:module} gradientdynamics
:no-index:
```

## Availability

The Python SDK is a design preview and cannot yet be installed from PyPI.
Approved integration partners receive an environment-specific service URL,
organisation-scoped credentials, permitted operations, capacity limits and a
versioned schema directly from Gradient Dynamics.

When generally available, installation is expected to follow the conventional
Python workflow:

```console
$ python -m pip install gradientdynamics
```

## Client

````{py:class} Client(*, token: str, environment: str = "production", timeout: float = 30.0)

Entry point for the Gradient Dynamics object model.

Credentials belong to an organisation and should be supplied through a secret
store or environment variable, never committed to source code or notebooks.

```{py:attribute} projects
:type: ProjectCollection

Collection used to create, list and retrieve projects visible to the current
organisation.
```

```{py:attribute} organisation
:type: Organisation

The authenticated organisation, including enabled capabilities and quota
summaries.
```

```{py:method} from_environment(*, environment: str = "production") -> Client
:classmethod:

Create a client from the planned `GRADIENT_DYNAMICS_TOKEN` environment
variable and configured service environment.
```

```{py:method} close() -> None

Close pooled network resources owned by the client.
```
````

### Context-manager use

```python
from gradientdynamics import Client

with Client.from_environment() as gd:
    for project in gd.projects.list():
        print(project.id, project.name)
```

## Authentication and versions

Preview and production environments can have separate credentials and data.
The eventual client will attach authentication automatically, record the API
and deployment versions returned with each result, and reject unknown breaking
schema versions rather than silently discarding fields.

Self-service credentials, a stable public base URL and token lifecycle will be
published with the general-availability SDK.
