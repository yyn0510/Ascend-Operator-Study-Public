# Part 2: Generated operators in real models

Fixed original implementations of GELU, SwiGLU, ForeachNorm and Sigmoid are evaluated in Qwen2.5-VL-3B, Qwen2.5-VL-7B, InternVL2-4B, LAION CLIP ViT-B/32 and OpenAI CLIP ViT-B/32. Not every operator is applied to every host.

## Consolidated data

| File | Scope |
|---|---|
| [Readable task tables](docs/任务结果表.md) | Human-readable task comparisons |
| [AI2D](tables/AI2D_任务与条件对照.json) | 22 formal comparisons plus 8 development conditions |
| [MMStar](tables/MMStar_任务与条件对照.json) | 10 formal comparisons |
| [DocVQA](tables/DocVQA_任务与条件对照.json) | 10 formal comparisons |
| [COCO retrieval](tables/COCO_任务与条件对照.json) | 23 formal comparisons plus 6 replacement-location conditions |
| [Complete-path timing](tables/模型完整路径计时.json) | 101 conditions, 303 independent-session records |
| [Input scans](tables/真实输入扫描.json) | 600 measured/checked records: 576 valid timings and 24 numerical admission failures; 4 additional out-of-contract conditions |
| [ForeachNorm evidence](tables/ForeachNorm准入与故障定位.json) | Admission, three independent reproductions, 3 versions × 7 diagnostic points |

There are 65 formal task comparisons, or 79 rows when the development and location comparisons are included. These are not 79 independent candidates. There are 33 unique candidate attempts, 32 original-benchmark passes and 31 real-input admissions. ForeachNorm alone is 9 → 8 → 7.

AI2D tests diagram question answering; MMStar tests multimodal multiple-choice reasoning; DocVQA tests document question answering; COCO is used for image–text retrieval, not detection in this release. Fixed task subsets: AI2D 1,000 evaluation items; MMStar 63 development and 1,241 evaluation items; DocVQA 1,000 evaluation items; COCO 1,000 images and 5,002 captions. Development subsets and input scans are separately recorded.

## Traceability

`evidence/` holds result records; `audits/` holds supporting calculations; `protocols/` holds frozen protocols; `code/` holds frozen execution payloads without images or weights; `candidates/` holds candidate source packages; `data/` holds existing subset manifests. Early supporting evidence is in `support/`.

Archive names preserve batch/run identities so that source fields in consolidated rows remain searchable. Some files recur in historical snapshots; repeated copies are not additional experiments. Use `../tools/find_evidence.py` from the repository root with a source filename, candidate identifier or run identifier.

For the ForeachNorm case, the original candidate passes 20/20 baseline cases but fails real-input admission. Three original-candidate reproductions confirm the execution failure. Controlled original/rebuild/diagnostic comparisons support a tail-zero-fill alignment defect; the manually changed version is diagnostic only. Earlier logs stating that localization was pending remain historical records, superseded by the final mechanism data.

## Interpretation

No change in aggregate accuracy does not imply identical per-item outputs or equivalence. DocVQA uses the recorded local ANLS-style implementation, not an unqualified claim of exact official-score equivalence. Timing inputs are controlled separately from task evaluation; preserve wrapper costs and the distinction between candidate/native and candidate/wrapper latency ratios. Values greater than one in a *latency ratio* mean slower execution, whereas values greater than one in a *speedup* mean faster execution.

Historical GELU reference-chain qualifications are preserved in `audits/`; do not infer that every historical performance reference has independently verified identical API semantics. The subsequent E four-operator expansion is excluded.
