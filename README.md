# Confidence-Scheduled Decoding

**Lab report:** Confidence Scheduling Specifies Scalable LLM Serving  
**Primary paper:** arXiv:2606.19348v1, *DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation*  
**Source links:**
- Paper: https://arxiv.org/html/2606.19348v1
- DeepSpec: https://github.com/deepseek-ai/DeepSpec
- Model card: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark

## Engineering statement

Verification is not a fixed cost. It is a schedulable engineering resource.

DSpark turns confidence estimates into scheduling signals: draft tokens are proposed in blocks, prefix survival probabilities estimate which tokens are worth verifying, and a hardware-aware scheduler allocates target-model verification budget toward tokens with the highest expected throughput return.

## Notebook roadmap

| Notebook | Theme | Status |
|---|---|---|
| 00 | Context | scaffold |
| 07 | Verification Resource | scaffold |
| 13 | Confidence Scheduling | scaffold |
| 17 | Semi-Autoregression | scaffold |
| 23 | Throughput Objective | scaffold |
| 29 | Hardware-Aware Scheduling | scaffold |
| 37 | Operating Regimes | scaffold |
| 43 | Resource Allocation | scaffold |
| 49 | Adaptive AI Infrastructure | scaffold |

## Core relation

```text
Throughput = Accepted Tokens × Steps/sec
```

Confidence scheduling maximizes useful verification.

## Repo structure

```text
confidence-scheduled-decoding/
├── data/                         # reference paper / small local inputs
├── figures/                      # infographic and notebook figures
├── notebooks/                    # executable notebooks
├── report_pages/                 # static notebook HTML pages, e.g. 00.html
├── results/                      # generated outputs
├── scripts/                      # helper scripts
├── src/confidence_scheduled_decoding/
├── requirements.txt
└── README.md
```
