# Source provenance

`contracts/creative_fusion.py` is the canonical complete source for this primitive, created for SPLICE.CLUB. No prior user project source was copied. It is a single deployable Python file with no application-local imports.

Sources consulted for public runtime APIs and constraints:

- [Official GenVM v0.2.16 source](https://github.com/genlayerlabs/genvm/tree/v0.2.16), including runner parsing, hashes and `gl.vm.run_nondet_unsafe` / `Return.calldata`.
- [Official GenVM v0.2.16 release](https://github.com/genlayerlabs/genvm/releases/tag/v0.2.16); runner hash is pinned in the contract header.
- [GenLayer Equivalence Principle](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle): independent source-grounded review for open-ended generation.
- Official npm `genlayer-js@1.1.8` package typings and implementation: Stable chain preset, public calls, write encoding and transaction receipts.
- Official `genlayer-test==0.29.2` direct runner implementation; tests explicitly compensate for its default skip of Validator execution.

The companion project includes the full canonical source unchanged. `SOURCE_SHA256.txt` records exact bytes. Code is MIT licensed. Creative record permission `PUBLIC-DERIVATION-V1` is an application permission acknowledgement, not a legal ownership certification.
