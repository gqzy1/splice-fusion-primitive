# Creative Fusion Lineage Primitive

Two independently authored idea seeds become one new, consensus-accepted creation. The primitive binds the generated object to immutable parent records, their real wallet contributors, a versioned input identity and an explicit public derivation permission.

**SPLICE-V2 is deployed on Stable Studionet (61999).** Four recorded transactions are FINALIZED. Work #3, Prismatic Resonator Beetle, preserves parent seeds #1 and #2 and their two wallet contributors. See [ONCHAIN_EVIDENCE.md](ONCHAIN_EVIDENCE.md).

Contract: `0x834f53cf56AE590F63cee321eE1A8CE566F3E9c4` · [Explorer](https://explorer-studio.genlayer.com/address/0x834f53cf56AE590F63cee321eE1A8CE566F3E9c4) · [Wallet-free verified example](https://gqzy1.github.io/splice-club/?w=1).

## Mechanism

1. `create_seed` records name, short description, 1–3 distinctive features, category and sender. Public derivation must be explicitly accepted.
2. `fuse` requires two existing seeds from different creator addresses. Parent order is canonicalized by ID. V2 stops at depth 1.
3. The Leader creates a bounded JSON candidate from an in-memory snapshot of both immutable parents.
4. Each Validator reads the same parents and exact proposed candidate and makes an independent semantic LLM call. It checks distinctive feature preservation for each parent, an actual interaction between them, and safe fictional content. A candidate's own bridge statement is not proof.
5. Only an accepted candidate reaches deterministic storage. Parent IDs, creators, content hashes, input SHA256, caller, version and permission are saved with the work.

The reusable capability is **creation plus provenance**, rather than a general acceptance service. The primitive owns input registration, native generation, grounded verification and append-only lineage together. No payments, tokens, NFTs, royalty claims or legal ownership assertions are included.

## Interfaces

| Method | Kind | Purpose |
| --- | --- | --- |
| `create_seed(name, description, features, category, allow_derivation, request_id)` | write | Register contribution; returns work ID |
| `fuse(parent_a, parent_b, request_id)` | write | Generate and commit accepted child; returns work ID |
| `get_work(work_id)` | view | Complete JSON work |
| `get_lineage(work_id)` | view | Work and complete parent records |
| `list_works(start, limit)` | view | ID-based pagination, maximum 30 |
| `get_request(creator, request_id)` | view | Resolve idempotent request to work ID; zero if absent |
| `total()` | view | Number of stored works |

Example arguments (illustrative inputs, not existing onchain objects):

```python
create_seed("Moon Laundry", "A laundromat folds moonlight to clean forgotten memories.",
            ["folds moonlight", "cleans forgotten memories"], "object", True, "seed-request-a")
# A second address creates its own seed. Once both IDs really exist:
fuse(first_id, second_id, "fusion-request-a")
```

## Safety and equivalence

Names: 2–48 characters; seed descriptions: 20–360; seed features: 1–3 strings of 3–80 characters. Fusion descriptions: 20–480; exactly three features of 3–100; bridge: 15–240. Control characters are rejected. Maximum 10,000 works; maximum depth 1; no update/delete method. Both parents must be depth-zero licensed seeds, so cycles cannot occur.

Requests are namespaced by actual sender. Reusing a successful token with the same normalized input returns the existing ID without another LLM call. Conflicting token reuse is rejected. A new token intentionally permits another interpretation of the same pair. Addresses prove wallet contribution, **not distinct real humans**.

Equivalence concerns validity of the Leader candidate, not byte-for-byte reproduction by other models. All four Validator criteria must independently pass; malformed verdicts, errors or uncertainty fail closed. Model or consensus errors occur before state writes. GenLayer provides transaction atomicity; offline tests prove the pre-save failure paths, not a live network rollback under every VM fault.

Prompts treat seed and candidate strings as untrusted serialized data, below immutable protocol instructions. This reduces instruction confusion but cannot guarantee universal prompt-injection resistance. Offline rejection fixtures do not measure real-model robustness or aesthetics.

## Run offline tests

Python 3.12+:

```sh
python -m pip install -r requirements-dev.txt
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -p gltest.direct.pytest_plugin tests -q
```

Tests load the **official GenVM v0.2.16 runner and SDK/storage** through `genlayer-test==0.29.2`. The first run downloads the official release archive. No local network, node or wallet is started. LLM replies and consensus are mocked. Because direct mode normally skips Validators, the test harness invokes the actual production Validator before returning accepted candidates; it also checks production closure serialization.

## Stable-only environment

Chain ID **61999**, RPC **https://studio.genlayer.com/api**. Runner dependency is pinned in the source header to the runner from official GenVM v0.2.16. JS integration uses **genlayer-js 1.1.8** in the companion project. No other network is supported. The deployment and one real AI fusion were finalized on Stable. Exact GenVM node binary version is not verified; the pinned offline SDK runner version is a separate fact. One accepted example does not measure universal model accuracy.

See [SOURCE_PROVENANCE.md](SOURCE_PROVENANCE.md), [ORIGINALITY.md](ORIGINALITY.md), [TEST_RESULTS.md](TEST_RESULTS.md), [DEPLOYMENT.md](DEPLOYMENT.md). MIT License.
