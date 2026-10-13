# Deployment boundary

The contract has not been deployed. No address, deployment hash, successful fusion transaction or live E2E result is claimed.

The allowed network is Stable Studionet only: chain 61999, https://studio.genlayer.com/api. Source dependency: official GenVM v0.2.16 runner `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`.

After separate authorization, the minimum successful demonstration requires four transactions:

1. Deploy the exact canonical source (empty constructor).
2. Wallet A registers a seed with explicit derivation permission.
3. Wallet B registers a distinct seed with explicit derivation permission.
4. Fuse the two seeds with a new request token.

Reads require no transactions. Verify finalized agreement, successful execution and actual `get_request` / `get_work` / `get_lineage` responses before adding a verified demo. Record source SHA256 and real hashes. Never use a private key in frontend code. Failed consensus is not a successful example.

A fuller minimal safety acceptance run adds two rejecting calls (missing parent and self-fusion), for six total transactions. Additional failed or retry transactions require a separately bounded allowance. Offline tests cannot pre-guarantee semantic consensus success.
