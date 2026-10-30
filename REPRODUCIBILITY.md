# Reproduction and verification

## 1. Offline integrity checks (no accelerator)

Run `python tools/verify_artifact.py` from a downloaded checkout. It verifies release-file SHA-256 hashes, ZIP integrity, published-member hashes, formal V3 cohort size and transfer summary counts. It does not rerun model inference or independently regenerate every reported statistical estimate.

Use `python tools/find_evidence.py --query <candidate-or-source-name>` to locate entries in the member index. Each result reports `archive.zip::member/path` or a loose repository path. `source_sha256` refers to the pre-sanitization source; `sha256` refers to published bytes. Historical embedded manifests remain original evidence and may therefore differ from sanitized copies. Use the release manifests for public-file integrity checks.

ZIP parts are independently readable with Python `zipfile` or a standard ZIP application. Prefer extraction into a short path on Windows because historical nested paths are long. Do not merge unrelated payloads into the same directory: A/B/C/D are different execution snapshots with files bearing the same names.

## 2. Recompute recorded results

Use the six V3 CSVs and archived statistics scripts for round/trajectory summaries. Original platform logs are preserved where recorded; parser failures and non-submissions must remain in the cohort. For transfer, locate the summary's source identifier in the member index, inspect predictions, references and run settings, then use the matching archived scoring implementation. Do not substitute a different answer parser or ANLS boundary rule.

Archive records may contain historical source paths. `PUBLIC_WORKSPACE` and `PUBLIC_HOME` are publication placeholders, not existing directories. Run/job identifiers and dataset sample identifiers are intentionally retained to connect the evidence.

## 3. Execute on an NPU

The release contains execution snapshots, not a newly tested one-command installer. No NPU experiment was rerun while preparing this release. Restore the matching Torch/TorchNPU/CANN/device configuration from environment records, obtain the pinned public checkpoints and dataset images, then configure the archived workers and paths. Restore the exact fixed subset order and preprocessing; do not replace the subset with the first N images of a dataset.

V3 regeneration additionally needs model-provider credentials and access to the original evaluation service. Historical model/API availability and service behavior are external dependencies; offline evidence verification does not require them. All credentials must be supplied locally and kept out of Git.

For transfer, build the fixed source candidate, recheck the original benchmark, enforce real-input admission, then run task evaluation and complete-path timing under the archived protocol. Do not rerun failed-admission candidates as though they were admitted, or treat a manually repaired diagnostic kernel as an original generated success.
