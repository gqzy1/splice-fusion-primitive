# Verified onchain evidence — SPLICE-V2

Network: Stable Studionet · Chain ID 61999 · RPC https://studio.genlayer.com/api.

Contract: [0x834f53cf56AE590F63cee321eE1A8CE566F3E9c4](https://explorer-studio.genlayer.com/address/0x834f53cf56AE590F63cee321eE1A8CE566F3E9c4). Source SHA256: `4a92361b30f2b504ec02e699a816bab78cac47504dafafa9a2ca158c947f07b1`.

Evidence export: 2026-10-14T15:37:42.009Z. The original export is preserved byte-for-byte in [SPLICE_V2_EVIDENCE.json](evidence/SPLICE_V2_EVIDENCE.json).

| Step | Operation | Transaction | Status | Receipt-reported fee |
| --- | --- | --- | --- | --- |
| T01 | Deployment | [0x4f5813763ed7f8486e82c64fbbb571c2f5198154360e9d8a9ed8c31cab6faaf4](https://explorer-studio.genlayer.com/tx/0x4f5813763ed7f8486e82c64fbbb571c2f5198154360e9d8a9ed8c31cab6faaf4) | FINALIZED | 0 |
| T02 | Seed #1 | [0x3edea0fd1448a77efcd11a7fb006812079ad3bbac841c9db87798d0c046221f4](https://explorer-studio.genlayer.com/tx/0x3edea0fd1448a77efcd11a7fb006812079ad3bbac841c9db87798d0c046221f4) | FINALIZED | 0 |
| T03 | Seed #2 | [0x057c9fa58cd5282f09968b3435a4d4efe6de95ab645ba6596d76a8026b7a3bf4](https://explorer-studio.genlayer.com/tx/0x057c9fa58cd5282f09968b3435a4d4efe6de95ab645ba6596d76a8026b7a3bf4) | FINALIZED | 0 |
| T04 | AI fusion #3 | [0xa49f25baa0e1e97a2b1065b516e1f40f9eee60d2231e9eb6275355f932dc4db8](https://explorer-studio.genlayer.com/tx/0xa49f25baa0e1e97a2b1065b516e1f40f9eee60d2231e9eb6275355f932dc4db8) | FINALIZED | 0 |

## Real fusion

Prism Beetle (#1) + Echo Loom (#2) → Prismatic Resonator Beetle (#3).

The saved child retains parent IDs [1, 2], both contributor addresses, both canonical parent SHA256 hashes and the versioned input SHA256. T04 reports MAJORITY_AGREE; final-round votes were 3 AGREE, 1 DISAGREE and 1 IDLE. This is majority consensus, not unanimous agreement. Successful execution and saved-work readback are separate checks from consensus status.

The human then confirmed visible preservation of each source feature and a causal interaction. This was a separate human semantic review, not an additional validator vote or onchain proof. The nested `semanticStatus` field describes the earlier readback stage; the top-level human `semantic` record and final status describe the completed review.

Receipt-reported network fee was zero for these four transactions. This is historical evidence, not a guarantee of future network pricing. The exact GenVM node binary version remains unverified. Offline SDK runner v0.2.16 is not evidence of the deployed node version. One real accepted fusion does not establish model accuracy across all inputs.
