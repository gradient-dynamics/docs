# Usage and storage

Studio gives organisation owners and permitted administrators a consolidated
view of compute, storage, subscription state and members.

## GPU usage

The usage dashboard shows the organisation's consumed GPU time for the current
billing period, remaining allowance and usage over time. Depending on the plan,
it can also show overage and spending-limit information.

Use project and job names that allow usage to be traced to an engineering
campaign. A stopped or failed job can still consume preparation and compute
time, so investigate repeated failures rather than resubmitting blindly.

## Storage

Storage includes uploaded geometry, generated meshes, logs, result fields,
transient series and derived assets. Large meshes and frequent transient
outputs are normally the dominant contributors.

Before deleting data, preserve the accepted geometry, mesh manifest, simulation
configuration, convergence evidence and reportable result files required by
your quality process. Project deletion removes the project's assets, jobs and
simulations and should be treated as a deliberate destructive action.

## Members and billing

The same area supports member invitations, role changes, removal and ownership
transfer. The organisation owner manages billing; invited engineering members
do not need to configure a separate plan to collaborate in the workspace.
