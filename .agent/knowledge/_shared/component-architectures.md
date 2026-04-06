# Neops Component Architectures

Consolidated architecture reference for all neops platform components.

## Workflow Engine (NestJS/TypeScript)

### Workflow Definition (YAML)

Top-level fields: `label`, `package`, `name`, `majorVersion`/`minorVersion`/`patchVersion`, `seedEntity` (device|interface|group|global), `description`, `parameterSchema`, `acquire[]`, `type: workflow`, `steps[]`.

Step types: `functionBlock` (execute registered FB), `workflow` (inline nested), `workflowReference` (reference another definition — not yet implemented).

Parameters use `{{ jmesPath }}` interpolation against the execution context. Conditions (`condition.jmes`) skip steps; assertions (`assert.jmes`) fail execution.

### Blackboard & Job Lifecycle

`PENDING` → `POLLED` (assigned to worker) → `PUSHED` (result received). Job types: `ACQUIRE`, `EXECUTE`, `ROLLBACK`.

Worker API: `/workers/register` (POST), `/workers/:uuid/ping` (POST heartbeat), `/function-blocks/register` (POST), `/blackboard/job` (POST poll), `/blackboard/job/result` (POST push).

Worker states: ONLINE → UNREACHABLE (2min no ping) → OFFLINE (6min) → deleted (24h). Stuck jobs (>12min POLLED) auto-failed.

### Pure/Idempotent Semantics

Engine tracks `isPureExecution` and `isIdempotentExecution` across steps. Failed workflow with only pure steps → `FAILED_SAFE`. Non-pure failure → `FAILED_UNSAFE`. Auto-retry for pure/idempotent is planned but not implemented; retry count is hardcoded to 3 in `job-executor.ts`.

### Configuration

Database: PostgreSQL (host port 5434 default, container 5432). CMS: GraphQL endpoint. Port: 3030. Schema: `GET /schema`. Swagger: `/api`. Health: `/health/`. Local dev: `docker-compose.yml` at repo root (engine + postgres + monitor app). Build override: `docker-compose.build.yml` for local source builds.

## Worker SDK (Python 3.12+)

### Function Block System

```python
class FunctionBlock(Generic[ParamsT, ResultDataT], ABC):
    async def run(params, context) -> FunctionBlockResult[ResultDataT]
    async def acquire(params) -> FunctionBlockAcquireResult
    async def rollback(params, context, result_from_failed) -> FunctionBlockRollbackResult
```

Registration via `@register_function_block(Registration(name, package, version, run_on, fb_type, is_pure, is_idempotent))`. ParamsT: Pydantic model (`extra="ignore"`). ResultDataT: Pydantic model (`extra="forbid"`).

### Worker Architecture

Hybrid sync/async: main loop (async) handles heartbeat/polling/API; FBs execute sync in `ThreadPoolExecutor(max_workers=1)`. Sequential job processing. Blocking detector warns on sync calls in async loop.

Config: `URL_BLACKBOARD`, `DIR_FUNCTION_BLOCKS`, `WORKER_NAME`. Entry point: `neops_worker`.

### Connection System (Three Layers)

1. **Capability interfaces**: abstract method contracts (e.g., `DeviceInfoCapability.get_version()`)
2. **ConnectionProxy**: user-facing API, composes capabilities via inheritance, delegates to plugin at runtime
3. **ConnectionPlugin**: platform/library implementations. Resolution: platform → connection_type → library → capabilities

Base plugins: Scrapli, Netmiko, Napalm, NETCONF, RESTCONF, API. ProxyMeta metaclass generates fallback methods raising `NotImplementedForThisPlatform`.

### Data & Context

WorkflowContext holds entity state (devices, groups, interfaces). Change tracking via deep-copy snapshot at init; `compute_db_updates()` diffs current vs. snapshot to generate `EntityCreateDto`/`EntityPatchDto`/`EntityDeleteDto`.

## CMS (Django/GraphQL)

### Data Models

- **Device**: hostname, ip, username, password (encrypted), platform (FK), groups (M2M), connection_state (NEW|UNREACHABLE|NOSSH|AUTHFAILURE|OK), facts/checks (JSON auto-aggregated), soft-deletable, lockable
- **Interface**: name, ifindex, device (FK CASCADE), state (UP|DOWN|ADMIN_SHUTDOWN|ERROR_DISABLED), neighbor (self one-to-one), facts/checks
- **DeviceGroup**: name (unique), title, devices (M2M), facts/checks
- **Facts/Checks**: versioned records (key, value JSON, valid_till, purge_at), auto-aggregated into parent entity

### Integration Pattern (Acquire → Execute → Unlock)

1. Engine calls `getAndLockResources` GraphQL mutation → CMS locks entities, resolves Elasticsearch queries
2. Locked entities serialized as DTOs → passed to workers as job context
3. Workers modify entities in memory → compute diff
4. Diff sent as `dbUpdates` in job result → engine aggregates
5. Engine calls `unlockResources` with aggregated updates → CMS applies atomically

Authentication: JWT with RS256, JWKS at `/.well-known/jwks.json`, role-based permissions (BitField).

## Remote Lab (FastAPI)

Session-based lab allocation: `POST /session` → wait in FIFO queue → `ACTIVE` → use lab → `DELETE /session`. Heartbeat required (300s timeout). One lab at a time per session.

Lab lifecycle: upload topology (`POST /lab`), topology hash comparison for reuse, reference counting for shared labs, release/destroy.

Worker SDK integration via pytest fixtures: `remote_lab_fixture("tests/topologies/simple_iol.yml")`. Available topologies: `simple_iol` (2 Cisco IOL), `simple_frr` (2 FRRouting). `RemoteLabDevice.to_neops_device()` converts lab devices to `DeviceTypeDto`.

Config: `REMOTE_LAB_URL` (unset = local mode), `REMOTE_LAB_REQUEST_TIMEOUT` (30s), `REMOTE_LAB_SESSION_TIMEOUT` (300s).
