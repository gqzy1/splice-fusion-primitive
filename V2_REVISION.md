# SPLICE-V2 safety revision

Status: candidate, not deployed. Source SHA256: `4a92361b30f2b504ec02e699a816bab78cac47504dafafa9a2ca158c947f07b1`. Runtime pin unchanged: `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.

V1's three observed parse failures motivate strict whole-document JSON handling. The exact historical failed text is not recoverable, so this revision does not claim that fences caused all three errors. The successful third-round candidate still lacked majority agreement; its private review texts are also unavailable. V2 improves checkable grounding rather than promising a pass rate.

- Accept a whole JSON object or one complete JSON/unlabelled fence; reject empty/prose/concatenated/truncated data, duplicate keys and nonfinite/float tokens. Keep exact candidate fields, types and limits. No extraction, coercion, repair or JSON-mode parameter.
- Preserve distinctive features from both authors and require causal interaction in actual description/features. Generation and review have distinct roles.
- Each independent reviewer chooses one full original feature from its specific parent, plus a quoted span from a specific candidate field. Positive reviews must pass deterministic source-index/quote and candidate-field/index/quote binding. The interaction also quotes the candidate. Bridge is excluded as evidence.
- Four semantic flags must all be actual true booleans; errors, uncertainty and negative judgments fail closed. Valid citations establish existence, not truth of the semantic claim: a dishonest all-true model can still misjudge an unrelated existing span. Independent semantic assessment and later real-model testing remain essential.
- Error codes: MODEL_FORMAT_ERROR, CANDIDATE_STRUCTURE_ERROR, REVIEW_STRUCTURE_ERROR, REFERENCE_INVALID, VALIDATOR_NEGATIVE, MODEL_CALL_ERROR, LEADER_EXECUTION_ERROR, CANDIDATE_INVALID, CONSENSUS_NOT_COMPLETED. Diagnostics emit only a bounded code; no raw reply/prompt. A boundary exception means execution did not complete, not a reconstructed platform vote result.
- No writes occur in nondeterministic closures. Business save follows completed consensus. Successful sender-namespaced requests remain idempotent. Public methods/parameters/returns and PUBLIC-DERIVATION-V1 remain unchanged. New records use SPLICE-V2; old storage is not migrated.

V1 code is archived unchanged. Old address 0x49FA79fB4Ff5C924F9FbA0a2E16558E3A7Db8D38 and its successful seeds remain V1-only evidence. V2 address is null. Source diff is in V2_CONTRACT_DIFF.patch.

## Validation

41 direct tests PASS using genlayer-test 0.29.2 and official v0.2.16 SDK/storage, with a harness that explicitly invokes production validators. Model/consensus remain MOCK. Production closures serialize with the official cloudpickle dependency.

Stable 61999 read-only schema signatures equal V1. A sentinel probe demonstrated actual module execution and exposed v0.2.16-x86_64-linux-release. The same read-only schema path passed 30 runtime helper assertions on the temporary source plus test appendix. Expected sentinel exceptions verify observation; they are not failed chain transactions. LLM/Web calls are zero. This verifies parser/reference functions in the pinned GenVM schema stage, not actual multi-validator consensus.

The actual runtime returned the diagnostic marker in stdout during a schema-stage probe. Future transaction/validator receipt visibility is NOT VERIFIED. REAL MODEL NOT VERIFIED; REAL ONCHAIN NOT VERIFIED.

## Future acceptance

A separately authorized batch needs at most four writes including failures: new deployment, author A seed, author B seed, one fusion. Each is manually signed, leaderOnly=false, zero-fee precheck, immediate stop on failure/unknown/nonzero fee. No writes are authorized by this revision. Do not merge, publish or submit Portal here.
