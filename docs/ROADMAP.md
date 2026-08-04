# Roadmap

## Product vision

Deliver a safe, scriptable Open WebUI administration client that works both as a Python library and as a self-documenting command-line tool.

## Milestone 0.1.0 — Administration MVP

The initial `0.1.0a2` proof-of-concept increment implements the three sprints below. Future alpha increments will incorporate feedback before a stable `0.1.0` release.

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

## CLI coverage program

### Goal and scope

Bring `owui` to command-level parity with the **525 operations across 476 paths** captured in the pinned Open WebUI 0.11.0 OpenAPI 3.1 description. This is parity with that exact snapshot, not a compatibility promise for later Open WebUI releases.

Parity does not mean exposing unsafe raw HTTP calls. Each operation must have a discoverable command, typed or schema-validated input, structured JSON output, and a safety classification. Read operations are non-mutating; mutations require a preview when meaningful and explicit `--yes` confirmation. Destructive or irreversible routes require a resource read/identity check before execution.

### Development priorities

| Priority | Focus | Why first |
|---|---|---|
| P0 | Endpoint inventory, shared command framework, authentication, error handling, safety policy, and compatibility tests | Makes every later command consistent, testable, and safe. |
| P1 | Identity, configuration, files, knowledge, retrieval, models, and integrations | Covers administrator workflows and the resources that unblock most user-facing features. |
| P2 | Chats, prompts, folders, notes, memories, channels, groups, and sharing | Covers everyday collaborative content and lifecycle operations. |
| P3 | Functions, tools, pipelines, automations, tasks, terminals, audio/images, and evaluations | Covers extension and operational workflows with higher security impact. |
| P4 | Analytics, notifications, calendars, utilities, OpenAI-compatible routes, and remaining untagged operations | Closes the long tail and completes the coverage matrix. |

### Delivery timeline

The schedule is indicative for one active maintainer. Each alpha release is gated by a reviewed endpoint matrix and targets the pinned Open WebUI 0.11.0 specification.

| Window | Release target | Scope and outcome |
|---|---|---|
| Aug 2026 | `0.1.0a4` | **Foundation:** publish the machine-readable operation matrix (`operationId`, path, method, tag, CLI command, safety class, test status); add shared list/get/create/update/delete command primitives; add dry-run and read-before-write conventions; add OpenAPI drift and command-coverage CI. |
| Sep–Oct 2026 | `0.1.0a5` | **Administration and identity:** complete `auths`, `users`, `configs`, permissions, groups, and access-grant operations. Add import/export where the API supports it. |
| Nov–Dec 2026 | `0.1.0a6` | **Knowledge and files:** complete `files` (14 operations), `knowledge` (35), and `retrieval` (16), including controlled deletion and post-operation verification. |
| Jan–Feb 2027 | `0.1.0a7` | **Models and integrations:** complete `models` (15), `ollama` (46), `openai` (12), `functions` (17), `tools` (15), and `pipelines` (8). Protect connection credentials and destructive synchronization actions. |
| Mar–Apr 2027 | `0.1.0a8` | **Content and collaboration:** complete `chats` (50), `prompts` (15), `folders` (11), `notes` (12), `memories` (11), `channels` (28), and sharing/group workflows. |
| May 2027 | `0.1.0a9` | **Operations and extensions:** complete `automations` (8), `tasks` (10), `terminals` (8), `audio` (6), `images` (6), `evaluations` (15), and relevant notifications. |
| Jun 2027 | `0.1.0a10` | **Parity and hardening:** complete analytics, calendars, utilities, skills, untagged routes, and any remaining operations; publish a coverage report showing 525/525 mapped operations; run compatibility and security review. |
| After parity | `0.2.0` | Validate against the next supported Open WebUI release, regenerate the client, publish a spec-diff migration guide, and begin stable-release criteria. |

### Per-domain implementation order

1. Add the endpoint matrix and classify every operation as read, reversible mutation, destructive mutation, or credential-sensitive mutation.
2. Implement read/list/get commands before matching mutations.
3. Add schema validation and JSON-file input for complex payloads; avoid large JSON values in shell arguments.
4. Add dry-run, confirmation, resource identity checks, and read-after-write verification for each mutation class.
5. Add fixture-based contract tests for every operation and a disposable-instance integration suite for mutations.
6. Document each command in embedded help and the CLI reference before marking its matrix row complete.

### Coverage gates

A release may claim a domain complete only when every operation in that OpenAPI tag is mapped to a CLI command or an explicitly documented, reviewed exception. CI must fail if an OpenAPI operation disappears from the matrix, a mapped command is removed, or the generated client differs from the pinned specification.

## Definition of done

A milestone item is done when its code, tests, user-facing help, endpoint-matrix entry, and documentation are included in a pull request; automated checks pass; no credential is committed; mutations have the required safety controls; and the pull request links the corresponding issue.
