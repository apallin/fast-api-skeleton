# fast-api-skeleton
Fast API Hello World Skeleton setup for testing HTTP development.

## Development

### Script Management
This repo uses Poetry and [Poe The Poet](https://github.com/nat-n/poethepoet) for running commands at the pyproject level.  Therefore, all service/project level commands can be centralized here without the need for something like a Makefile or some separate bash scripts for command management.

### Adding dependencies
Use Poetry and associated commands to add a dependency.  The `dev` group is for local dependencies and should be separate/clean from the application dependencies.

### Running tests
Run tests using Poe The Poet
```
poe test
```

### Starting the Service
For dev/local use:
```
poe serve-dev
```

Otherwise, use:
```
poe serve-prod
```
