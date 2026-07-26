# Community Grant Signals -- Pointer

Chet's discovery and monitoring skills both read grant and funding signals as one of
their scanning sources (see `scanning.sources` in `core/config.template.json`). The
capability to search for and score community and grant funding signals already exists as
its own public skill in this repo -- see `Skills/community-grant-radar` for the grant
and contract radar capability.

Use `Skills/community-grant-radar` to source and score grant or contract signals, then
feed anything that resolves to a named, bounded group into
`Skills/cluster-discovery/` here.
