## dj-migration-test 

Django migration test module.  

# Requirements

```text
django>=2.2.0
```

# Setup
`pip install dj-migration-test`

# Usage

For examples see the [examples](/examples) directory

# Tips

For single migrations do not use the attribute `migrate_from` the test suite will dynamical determine
the previous step.
