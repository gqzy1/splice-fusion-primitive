# V2 validation

- Contract regression: 41/41 tests passed on 2026-10-14 using genlayer-test 0.29.2 and the pinned official GenVM v0.2.16 SDK runner. LLM and consensus responses are mocked; these tests cover parsing, bounded schemas, source-field citation binding, immutable snapshots, request idempotence, fail-closed rejection and lineage storage.
- `python scripts/verify_evidence.py`: PASS. Source hash matches the recorded deployment bytes; all four finalized successful receipts, zero reported fees, parent hashes, input identity and request fingerprint verified.
- Existing real deployment: four finalized transactions; one successful native AI fusion. [Onchain evidence](ONCHAIN_EVIDENCE.md).
- Real read-only SDK recheck: finalized T04 MAJORITY_AGREE / SUCCESS, get_lineage(3) and list_works(1,30) read successfully on 2026-10-14. No new writes.

The offline SDK version does not prove the exact deployed GenVM node binary version. Mock rejection fixtures are not a real-model accuracy benchmark. One successful real fusion is a bounded example.
