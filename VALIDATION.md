# Local release validation

Preparation date: 2026-10-30. No NPU experiments or model generations were run during packaging.

| Check | Result |
|---|---|
| Formal V3 table | 9 models, 216 trajectories, 1,080 unique round keys |
| V3 archived round coverage | Exact match to all 1,080 formal CSV keys |
| Transfer task comparisons | 65 formal; 79 including development and location comparisons |
| Transfer timing | 101 conditions, 303 session records |
| Input scan | 600 records plus 4 out-of-contract conditions |
| ForeachNorm gates | 9 attempted, 8 baseline passes, 7 application admissions |
| Published source entries | 56,482, including 56,453 archived members and 29 loose source-derived files |
| Included original result archives | Formal V3 archive and 14 unique transfer result archives, with supporting snapshots |
| JSON parsing of scanned publication contents | 22,451 JSON files successfully parsed; no parse errors in the completed scan |
| Consolidated CSV preservation | All six CSV files byte-identical to the curated local source |
| Consolidated JSON measurements | Numeric values and their structural locations unchanged |
| Credential-prefix / service aggregation-token scan | No remaining findings for the checked patterns |
| Known local workspace path scan | No remaining findings |
| Markdown reading-layer local links | All resolved |
| Release and member SHA-256 checks | Passed using `tools/verify_artifact.py` |

The source-entry count is a file count, not an experiment count. Historical snapshots can contain the same source file more than once. Known paths and service access fields were sanitized only in published copies. Source and public hashes are both retained.

This validation establishes packaging integrity and the reported cohort counts. It does not independently rerun every statistic, certify all third-party rights, or guarantee anonymity against indirect inference. The E expansion and incomplete Opus formal cohort are excluded; the original V3 eight-operator scope remains intact.
