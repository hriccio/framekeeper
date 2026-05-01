# MRL Core Is Separate From Packs

MRL core should not be confused with one implementation pack.

## Meaning

The refinement loop, artifact chain, and evaluation discipline belong to MRL
core. The pack supplies the implementation defaults that sit on top of that
core.

## Related Episodes

- [Packs Define Implementation Defaults](../episodes/046-packs-define-implementation-defaults.md)
- [Python DDD Monolith Is A Selected Pack](../episodes/047-python-ddd-monolith-is-a-selected-pack.md)

## Notes

- keep core and pack separate
- do not let a pack pretend to be the loop itself
- make the selected pack explicit
