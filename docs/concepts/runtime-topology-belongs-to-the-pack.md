# Runtime Topology Belongs To The Pack

Runtime shape is a pack decision, not an MRL core decision.

## Meaning

Whether the system is a single runtime, a client/server pair, or something else
belongs in pack guidance. That keeps the semantic model stable while letting
implementation vary when needed.

## Related Episodes

- [Packs Define Implementation Defaults](../episodes/046-packs-define-implementation-defaults.md)
- [Python DDD Monolith Is A Selected Pack](../episodes/047-python-ddd-monolith-is-a-selected-pack.md)

## Notes

- keep runtime shape explicit
- let the pack describe topology
- avoid hiding topology in core docs
