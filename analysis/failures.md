# Current V5 failure modes

| Failure | Status | Evidence | Next useful check |
|---|---|---|---|
| Stronghold loses to V2 | Unresolved | Final V5 0–2 on replay Stronghold and 0–2 on the differently encoded local Stronghold; extra units and total length did not win | Trace longest individual dragon and pearl uptake over time; test a general rule on fresh maps before adoption |
| Default Small loses to V3 | Unresolved | Final V5 0–2 in paired native games | Compare first elimination and longest-dragon trajectory on both sides |
| No-route split can leave a child without an escape | Known limitation | `rescue_child_box.map`: legal fallback split followed by child death; exact V2 also loses this setup | Find a case where a change improves the match result, then test it across the full map suite |
| Performance versus outside teams | Unverified | User observed V2 did best outside; supplied replay ZIPs contain V3/V4 games, not reproducible V2 outside matches | Run final V5 and exact V2 against the same outside opponents/maps on both sides |

The earlier V4-derived V5's portal and split regressions are documented in `v5_rejected_portal_report.md`. The current V5 is V2-derived and was compared directly against V2, V3, and V4.
