# External resources

Use the exact checkpoint revisions and file hashes in `02_model_transfer/protocols/C正式冻结协议.json`, `D正式冻结协议.json` and `模型权重校验.json`. The links below are entry points, not substitutes for the frozen versions.

| Resource | Official entry point |
|---|---|
| Qwen2.5-VL-3B | https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct |
| Qwen2.5-VL-7B | https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct |
| InternVL2-4B | https://huggingface.co/OpenGVLab/InternVL2-4B |
| LAION CLIP | https://huggingface.co/laion/CLIP-ViT-B-32-laion2B-s34B-b79K |
| OpenAI CLIP | https://huggingface.co/openai/clip-vit-base-patch32 |
| AI2D | https://allenai.org/data/diagrams |
| MMStar | https://github.com/MMStar-Benchmark/MMStar |
| DocVQA | https://www.docvqa.org/datasets/docvqa |
| COCO | https://cocodataset.org/ |

Subset selections, sample identifiers and image checksums are retained in the execution payloads and subset manifests. Obtain missing images from the dataset provider and match these records. Some datasets require accepting access conditions. Do not infer the subset from filenames or redraw a random subset.
