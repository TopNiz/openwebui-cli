# Roadmap

## Product vision

Deliver a safe, scriptable Open WebUI administration client that works both as a Python library and as a self-documenting command-line tool.

## Milestone 0.1.0 — Administration MVP

The initial `0.1.0a1` proof-of-concept increment implements the three sprints below. Future alpha increments will incorporate feedback before a stable `0.1.0` release.

### Sprint 0 — Repository and governance

- public GitHub repository;
- pinned OpenAPI source and provenance;
- contribution, security, issue, and pull-request guidance;
- milestone and issue backlog.

### Sprint 1 — Generated client and runtime foundation

- reproducible OpenAPI Generator configuration;
- generated Python client and endpoint documentation;
- installable package and `owui` entry point;
- URL/profile/authentication resolution;
- safe API errors and JSON output;
- system configuration read and patch commands.

### Sprint 2 — User administration and user settings

- list, inspect, create, and update users;
- current-user settings read and patch commands;
- default permission read and patch commands;
- confirmation and dry-run behavior for mutating commands;
- unit tests for the high-level library and CLI.

### Sprint 3 — Documentation, global skill, and release readiness

- complete README installation and examples;
- embedded help for every command and subcommand;
- CI for formatting, linting, typing, tests, build, and generated-client drift;
- global Pi skill backed by the CLI;
- compatibility and security documentation;
- versioned GitHub pre-release.

## Later backlog

- knowledge-base and document management;
- model export/import/synchronization;
- groups and granular access grants;
- chat convenience commands;
- tool-server administration;
- audit and analytics exports;
- shell completion and additional credential stores;
- compatibility testing across supported Open WebUI releases.

## Definition of done

A milestone item is done when its code, tests, user-facing help, and documentation are included in a pull request; automated checks pass; no credential is committed; and the pull request links the corresponding issue.
