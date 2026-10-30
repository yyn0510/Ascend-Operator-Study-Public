# Part 1: V3 foundation-model evaluation

Formal cohort: 9 generator models, 8 operators, 3 trajectories per model–operator pair and 5 rounds per trajectory. Total: 216 trajectories and 1,080 rounds. A round may fail before submission; it remains in the denominator.

## Consolidated results

| File | Unit |
|---|---|
| [v3_rounds.csv](tables/v3_rounds.csv) | One scheduled round |
| [v3_trajectories.csv](tables/v3_trajectories.csv) | One five-round trajectory |
| [v3_models.csv](tables/v3_models.csv) | Generator model |
| [v3_operators.csv](tables/v3_operators.csv) | Operator |
| [v3_round_scores_wide.csv](tables/v3_round_scores_wide.csv) | Wide-form round scores |
| [v3_op_means_wide.csv](tables/v3_op_means_wide.csv) | Model/operator summaries |

The JSON files in `tables/` preserve the source whitelist, correctness audit and reporting-selection calculations. [Protocol description](docs/裸基模评测流程.md) provides the original Chinese explanation.

`score` is the recorded platform composite score; `passed_cases` and `total_cases` describe correctness. Keep submission, evaluation, parsing and failure-status fields when interpreting zero scores. Use the recorded source/protocol flags rather than inferring success from a nonempty response. Provider and returned-model fields are preserved as recorded identities, not independently established model architecture claims.

## Evidence and code

`evidence/records-*.zip` together cover the formal source archive. Each ZIP is independent, not a multipart ZIP requiring concatenation. Original experiment/trajectory/round paths are retained. They include recorded requests, responses, parser outcomes, feedback, platform results and generated/submission projects where those exist. A missing submission project in a failed round is not automatically an export omission.

`code/harness-*.zip` contains the archived harness, configurations, task/reference snapshots and statistical scripts. These are historical execution snapshots; configure their environment before rerunning. External platform access is not bundled.

Best historical composite score, final-round score, best fully correct composite score and best valid speed among fully correct rounds are distinct selections. A best-versus-final difference alone does not establish a causal disadvantage of feedback. This study has no matched independent-sampling control establishing that claim.

The incomplete Opus experiment and later E model-transfer experiment are outside this part. V3's original Mish, Exp, MaskedScale and ForeachAddcdivScalar generation records are intentionally retained.
