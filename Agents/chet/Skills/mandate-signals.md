# Mandate Signals -- Pointer

Chet's discovery and monitoring skills both read mandate and compliance signals as one
of their scanning sources (see `scanning.sources` in `core/config.template.json`). The
capability to search for and score those signals already exists as its own public skill
in this repo -- see `Skills/mandate-mapping` for the mandate-search capability
(configuration, scoring rubric, and scoring examples).

Use `Skills/mandate-mapping` to source and score mandate or compliance signals, then
feed anything that resolves to a named, bounded group into
`Skills/cluster-discovery/` here.
