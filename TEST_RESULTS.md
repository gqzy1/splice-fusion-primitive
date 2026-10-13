# Verification results

- Offline tests: **31 PASS**, 0 failures.
- Real onchain E2E: **NOT RUN LIVE**.
- LLM replies and consensus: **SIMULATED / MOCKED** in tests.
- Stable Studionet schema: **READ_ONLY_SCHEMA_PASS**, chain ID 61999.
- A/B complete contract bytes and frontend manifest: **SOURCE_INTEGRITY_PASS**.

Command: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -p gltest.direct.pytest_plugin tests -q`.

Tests use the official GenVM v0.2.16 SDK and storage. They cover input shape/length, permission, sender binding, two creators, invalid/self/child parents, request conflicts and idempotence, canonical lineage, model output errors, independent Validator rejection for each substantive criterion, malformed review, prompt separation, model failure before state writes and bounded pagination. The official runner-bundled cloudpickle serializes production Leader/Validator closures.

The custom consensus harness explicitly executes the production Validator BEFORE the state-writing path; its model verdict remains a fixture. These tests do not prove live multi-validator consensus, universal injection resistance, visual quality or real transaction rollback under all VM faults.
