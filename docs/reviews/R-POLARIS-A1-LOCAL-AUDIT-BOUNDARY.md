# Polaris A1 local-audit boundary check

Date: 2026-08-31

Question: can an owner-attended ceremony append its audit record to a
root-owned local file that the Syzygy/agent principal can read but cannot
write?

## Result

[Observed] The process principal is Unix user `tze` (`uid=1000`). Interactive
`sudo` requires owner input; non-interactive `sudo -n` is unavailable.

[Observed] The same principal belongs to the `docker` group and can access the
Docker daemon. Docker-daemon access is host-root-equivalent: the principal can
start a container with a host bind mount and alter a nominally root-owned host
path. Therefore a file under `/var/lib/syzygy` or `/var/log/syzygy` would still
be inside the untrusted principal's effective write reach.

[Observed] Neither local audit directory existed during this check. No
directory, file, permission, container or external state was created or
changed.

## Consequence

A root-owned file on this host does not satisfy RFC3-16(a)'s independently
kept audit-trail boundary. A conforming A1 mechanism needs an owner-attended
write to a device, account or service whose write authority is unavailable to
the `tze`/Codex/Docker principal, while Syzygy retains read/verification access
to the resulting act record.

[Unknown] No such external write boundary has been selected or authorized for
this POC. Until one exists, PWB-REQ-005 requires zero Butlers body reads and a
project-model Unknown.
