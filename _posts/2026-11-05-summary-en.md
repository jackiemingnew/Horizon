---
layout: default
title: "Horizon Summary: 2026-11-05 (EN)"
date: 2026-11-05
lang: en
---

> From 38 items, 10 important content pieces were selected

---

1. [Moonshot AI Open-Sources Kimi K3.1 Pro Weights](#item-1) ⭐️ 9.0/10
2. [AI Vulnerability Discovery Forces Software to Repay 40 Years of Technical Debt](#item-2) ⭐️ 8.0/10
3. [Go Proposes New encoding/json/v2 API for Faster, Stricter JSON](#item-3) ⭐️ 8.0/10
4. [Anthropic reports progress on cryptographically provable inference for LLMs](#item-4) ⭐️ 8.0/10
5. [Tencent Unveils Hy4 Open-Weight Model With Game-Dev Focus and Open-Sourced Science Models](#item-5) ⭐️ 8.0/10
6. [NKI layer megakernels cut GLM-5.3-Flash decode step from 32.2 ms to 24.2 ms on one Trainium2 box](#item-6) ⭐️ 8.0/10
7. [Looped transformers save storage, not HBM traffic, B200 profiling shows](#item-7) ⭐️ 8.0/10
8. [Oracle Cancels $7B AI Chip Lease With Tencent After US Pushback](#item-8) ⭐️ 8.0/10
9. [Huawei Tells Customers to Source Their Own HBM for Ascend 960DT](#item-9) ⭐️ 8.0/10
10. [Bluetooth HDT Standard Adopted: LE Peak Bit Rate Rises to 7.5 Mbps](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Moonshot AI Open-Sources Kimi K3.1 Pro Weights](http://platform.kimi.ai/) ⭐️ 9.0/10

Moonshot AI published the open weights of Kimi K3.1 Pro on Hugging Face — a natively multimodal agentic model with 2.8T total parameters (104B active), a ~1M-token context window, and the first release in the K3.1 line. The company simultaneously opened API access at platform.kimi.ai under the model ID kimi-k3.1-pro, compatible with both the OpenAI and Anthropic interfaces, with weights shipped in MXFP4 quantization. Open weights at the multi-trillion-parameter scale are still rare, so this gives researchers and self-hosting teams a frontier-class multimodal agent model they can inspect, fine-tune, and run without depending on a closed vendor. The dual OpenAI/Anthropic API compatibility also lowers migration costs for teams already built on those SDKs, intensifying pressure on both closed frontier labs and other open-weight challengers. Even in MXFP4 — a 4-bit microscaling format that cuts weight memory roughly to a quarter of BF16 — 2.8T parameters still occupy on the order of 1.4 TB, so self-hosting realistically requires a multi-GPU node rather than a single workstation. The 104B active parameter count keeps per-token compute moderate, but the full expert set must still be resident in memory, making VRAM capacity and interconnect bandwidth the real bottleneck.

telegram · zaihuapd · Nov 4, 15:47

**Background**: Kimi K3.1 Pro uses a Mixture-of-Experts (MoE) architecture: instead of running every parameter for each token, a router activates only a small subset of expert sub-networks, so total parameters (all experts held in memory) can be far larger than active parameters (the few used per token). MXFP4 is a 4-bit floating-point quantization scheme that shares one small exponent scale across a block of values (typically 32), preserving accuracy far better than naive 4-bit rounding while shrinking model size and speeding inference on recent accelerators. "Native multimodal" means vision is trained into the model from the start rather than bolted on afterwards, and "agentic" signals tool-calling and multi-step task execution as first-class capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi -K3 · Hugging Face</a></li>
<li><a href="https://www.kapilsharma.dev/posts/mxfp4-visualizer/">Understanding MXFP4 Quantization | Kapil Sharma</a></li>
<li><a href="https://osfoundry.io/articles/mixture-of-experts-explained">Mixture of Experts Explained: Total vs Active Parameters ...</a></li>

</ul>
</details>

**Discussion**: Commenters were split: several called the model "benchmaxxed" and argued it barely outpaces DeepSeek V4.1-Flash or scores weakly on other labs' internal benchmarks, while one practitioner pushed back saying their own testing showed a very strong open model only slightly off the frontier. Others focused on practicalities — that running it locally needs something like an 8x B300 node, and that third-party providers such as OpenRouter are already hosting it with roughly double Moonshot's endpoint throughput, hinting at room for further cost reductions.

**Tags**: `#open-weights`, `#large-language-models`, `#multimodal`, `#mixture-of-experts`, `#moonshot-kimi`

---

<a id="item-2"></a>
## [AI Vulnerability Discovery Forces Software to Repay 40 Years of Technical Debt](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability) ⭐️ 8.0/10

An IEEE Spectrum analysis argues that AI-driven vulnerability discovery is finally forcing the software industry to confront roughly 40 years of accumulated technical debt, prompting a large Hacker News debate (about 1,066 points and 634 comments). The piece frames AI not merely as a new attack tool but as an auditing force that exposes long-ignored weaknesses in existing codebases. If AI can audit code at a scale humans never could, the long-standing open-source assumption that "someone else has reviewed this code" may finally become real, and every organization maintaining legacy systems should expect a sustained wave of patching work. That shifts security spending from reactive incident response toward large-scale remediation of design-level flaws. The sharpest counterpoint in the thread is that many technical-debt items are not narrow off-by-one bugs fixable with a surgical patch, but require restructuring or redesign, so AI may produce a compulsory treadmill of "feature-neutral fix-work" rather than genuine debt repayment. Commenters also invoked Gödel, Escher, Bach to note that perfectly secure systems are impossible not just practically but in theory, meaning the goal is robustness rather than closure.

hackernews · pseudolus · Nov 4, 11:52 · [Discussion](https://news.ycombinator.com/item?id=50364336)

**Background**: Technical debt is the metaphor for shortcuts taken in software design that accumulate interest over time as future changes become harder and riskier. Vulnerability discovery traditionally relies on manual audits and fuzzing at a scale far smaller than the codebase; large language models and AI-assisted analysis tools now make it cheap to scan enormous amounts of code for weaknesses. The open-source community has long relied on Linus's Law — "given enough eyeballs, all bugs are shallow" — an assumption that in practice often went untested.

**Discussion**: The Hacker News discussion is broadly engaged but skeptical of the headline framing: the top counterargument holds that AI-driven fixing may be an endless treadmill of feature-neutral work rather than true debt payoff, and that many flaws require restructuring rather than narrow patches. Others are more optimistic, hoping that AI auditing will incidentally surface state-held zero-days and finally make real the promise of open-source review, while one thread uses Gödel, Escher, Bach to argue that no system can be made perfectly secure.

**Tags**: `#AI/ML`, `#cybersecurity`, `#technical-debt`, `#vulnerability-research`, `#software-engineering`

---

<a id="item-3"></a>
## [Go Proposes New encoding/json/v2 API for Faster, Stricter JSON](https://go.dev/blog/jsonv2) ⭐️ 8.0/10

The Go team has formally introduced a new encoding/json/v2 package (alongside encoding/json/jsontext) as a major revision of the standard library's JSON handling, targeted at Go 1.27. The v1 encoding/json package remains unchanged and existing imports keep working, but the underlying engine can be switched to v2 behavior via new configuration options. JSON handling is one of the most-used parts of Go's standard library, so a redesign affects virtually every Go service that serializes data, with the Go team reporting unmarshaling up to 10x faster. The proposal also forces the ecosystem to confront long-standing behavior quirks and migration costs across countless existing projects. Migration is not purely drop-in: v2 changes behaviors around duplicate keys, invalid UTF-8 handling, nil collections, case-insensitive field matching, and encoding of byte arrays as Base64 strings, and it drops the familiar MarshalIndent in favor of more verbose jsontext options. The Go team provides a dedicated migration guide describing how to opt into v2 safely, including options that restore legacy v1 behavior.

hackernews · olexsmir · Nov 4, 17:52 · [Discussion](https://news.ycombinator.com/item?id=50369106)

**Background**: Go's encoding/json package has been essentially unchanged since Go 1.0 and is built on reflection, which made it convenient but relatively slow and loose about malformed input. The v2 effort follows the same pattern as math/v2 and other standard-library revisions: keep the old package importable while offering a stricter, faster, and more explicitly configurable new API in a versioned subpackage. The jsontext subpackage handles low-level tokenizing and formatting, separating it from the type-mapping logic in json.

<details><summary>References</summary>
<ul>
<li><a href="https://go.dev/doc/jsonv2-migration">encoding/json/v2 Migration Guide - The Go Programming Language</a></li>
<li><a href="https://github.com/golang/go/issues/71497">encoding / json / v 2 : new API for encoding / json · Issue #71497...</a></li>
<li><a href="https://pkg.go.dev/encoding/json">json package - encoding / json - Go Packages</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly positive about the redesign, but several raised migration pain points — one lamented the removal of MarshalIndent, noting the equivalent code is complicated and non-obvious for quick scripts. Others questioned JSON's reputation as a "simple" format given how much effort every language still spends on it, and a few discussed a future where LLMs write most of the Go code while developers still value Go's performance and safety.

**Tags**: `#Go`, `#JSON`, `#standard library`, `#API design`, `#encoding/json/v2`

---

<a id="item-4"></a>
## [Anthropic reports progress on cryptographically provable inference for LLMs](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

Anthropic published research describing FlashProve, a system that allows a model provider (the prover) to cryptographically convince a user (the verifier) that a specific large Mixture-of-Experts language model actually produced a given response. The company says the approach yields a commitment of roughly 6.5 MB that covers about 16 million requests, after which the provider must commit again, with each request accompanied by a proof. Today, API customers largely take it on trust that the model they paid for is the model that answered, which makes silent model swaps, downgrades by routers, or undisclosed weight changes hard to detect. Cryptographically provable inference would give enterprises and regulated users a concrete verification mechanism, and the discussion around it is already shaping how open-weight versus closed-weight accountability gets debated. The costs are substantial: commenters cite roughly a 90–100x compute overhead, and proof checking itself takes about 17 seconds on 24 threads (21 seconds single-threaded), including the offline phase's check. The proof also only certifies that the committed weights were the ones executed — it says nothing about output quality, and GPU non-determinism remains a practical obstacle to faithful re-execution.

hackernews · ltononro · Nov 4, 17:17 · [Discussion](https://news.ycombinator.com/item?id=50368626)

**Background**: Verifiable computation lets a prover convince a verifier that a computation was carried out correctly without the verifier redoing all the work, an idea popularized by zero-knowledge proofs and blockchain "zkML" projects. Applying this to LLM inference is hard because transformer forward passes involve billions of parameters and many non-arithmetic operations, which are expensive to express as proof circuits; related systems such as Lagrange's DeepProve-1 and academic ZK-LLM work have only recently begun to cover full model inference. Anthropic's FlashProve targets Mixture-of-Experts models, where only a subset of parameters is activated per token, which changes both the proving cost and how weights must be committed to.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/provable-inference">Progress on provable inference for large language models \ Anthropic</a></li>
<li><a href="https://github.com/JamesPetrie/zkllm-entropy">GitHub - JamesPetrie/zkllm-entropy · GitHub</a></li>
<li><a href="https://lagrange.dev/blog/deepprove-1">DeepProve-1: The First zkML System to Prove a Full LLM Inference</a></li>

</ul>
</details>

**Discussion**: Discussion was mixed: one commenter, describing himself as a former MARS fellow, said the work is built on his VerInf project and complained that even the choice of the 400B Maverick model was taken with little attribution. Others questioned the economics, arguing that for open-weight models you can simply redo the computation deterministically, or get a cheaper probabilistic guarantee from several independent inference providers running the same unbatched prompt, and noted that signed responses are the fallback when weights stay closed.

**Tags**: `#provable inference`, `#LLM security`, `#cryptography`, `#zero-knowledge proofs`, `#Anthropic`

---

<a id="item-5"></a>
## [Tencent Unveils Hy4 Open-Weight Model With Game-Dev Focus and Open-Sourced Science Models](https://hy.tencent.ai/research/hy4) ⭐️ 8.0/10

Tencent announced Hy4, a next-generation Mixture-of-Experts foundation model with roughly 770B total parameters (about 49B activated per token) and a context window exceeding 1M tokens, positioning it among the strongest open-weight models available. Alongside it, Tencent open-sourced two scientific foundation models co-developed with Hy4 and Hyra 2.0: HyCell for single-cell representation learning and HyPDE for physical field modeling, while stating that model weights and system cards will be published in the coming days. A Chinese lab shipping a frontier-class open-weight model narrows the gap between freely downloadable models and closed proprietary APIs, which matters for researchers, startups and anyone who cannot or will not depend on a single vendor. The unusual specialization in game development — including engine-level adaptation for Unreal Engine, Unity and Godot — plus freely released scientific models suggest open weights are becoming a competitive distribution strategy rather than an afterthought. Tencent itself acknowledges a notable gap versus top proprietary models, particularly on internal benchmarks for research-level mathematics, long-horizon coding, model self-improvement and advanced visual question answering, and says it will keep scaling pre- and post-training. Third-party testing also hints at a cost/accuracy trade-off: in Plotly's data analytics benchmark Hy4 landed between GPT-6.1 Sol and GPT-6.1 Terra but was markedly slow, sometimes issuing dozens of queries per question.

hackernews · Philpax · Nov 4, 14:11 · [Discussion](https://news.ycombinator.com/item?id=50365780)

**Background**: Hy4 is built as a Mixture-of-Experts model, meaning only a fraction of its parameters are activated for each token, which keeps inference cheaper than a dense model of the same total size. "Open-weight" means the trained parameters are downloadable so anyone can run or fine-tune the model locally, though it is not necessarily the same as fully open-source, since training data and code may remain undisclosed. Scientific foundation models like HyCell (single-cell biology) and HyPDE (partial differential equations for physical fields) are domain-specialized models trained on scientific data rather than general text, and the game-development focus reflects an effort to tune coding ability toward engine scripting, gameplay logic and asset pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://hy.tencent.ai/research/hy4">hy . tencent .ai/research/ hy 4</a></li>
<li><a href="https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/">Tencent Launches Hy4, Joining the Ranks of the... - Tencent</a></li>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent / Hy 4-preview · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly positive, with one praising the contrast between Tencent open-sourcing tools for science and US labs restricting research use, and another calling the Unreal/Unity/Godot adaptation genuinely interesting. Several appreciated Tencent's candid admission of the gap to proprietary models, while a benchmark write-up noted Hy4 was thorough but very slow, running dozens of queries per question.

**Tags**: `#llm`, `#open-weights`, `#tencent`, `#game-development`, `#foundation-models`

---

<a id="item-6"></a>
## [NKI layer megakernels cut GLM-5.3-Flash decode step from 32.2 ms to 24.2 ms on one Trainium2 box](https://www.reddit.com/r/MachineLearning/comments/1xo0yuq/p_nki_layer_megakernels_for_glm53flash_on_aws/) ⭐️ 8.0/10

RunAnywhere open-sourced trnrt, an NKI-based inference engine that serves GLM-5.3-Flash (a 320B mixture-of-experts model with 1M-token context) on a single AWS trn2.48xlarge instance, and published a granular profile of where a decode step's time actually goes. Profiling an early build showed that in one KDA linear-attention layer at batch 1, the recurrence math was only 2% of the attention half, while the mHC pre-projection took 36%, XLA glue 33%, transposes 10% and the stream mix 10%. After rewriting each layer half as a single NKI kernel, a batch-8 decode step fell from 32.2 ms (17 October build) to 24.2 ms (1 November build), with the fused sparse-attention layer and the combined KDA plus MoE kernels each saving 3.2 ms per step. Trainium2 is a much less documented accelerator than GPUs, and there is no off-the-shelf serving path for this model class: the latest vLLM Neuron plugin registers no GLM model and NxD Inference is in maintenance mode, so this work fills a real gap for anyone trying to run large MoE models on AWS silicon. The finding that most of a decode step was framework overhead rather than model math, plus concrete rewrite rules and negative results, gives systems engineers a transferable playbook rather than a single benchmark number. The design follows three rules: keep the working set in each physical NeuronCore's 28 MiB SBUF so only layer inputs, outputs and streamed weights cross HBM; split the weight stream across both physical cores of a logical core (one program sustains 340–400 GB/s, the pair 672–708 GB/s); and move a collective inside the kernel when it blocks the next one, since XLA otherwise makes the next kernel wait for the whole all-reduce. Of the remaining 24.2 ms per batch-8 step, 6.1 ms is the memory floor, 10.0 ms is engines busy beyond it, 4.6 ms is intra-kernel waits, 2.8 ms is exposed collectives and 0.7 ms is idle — and the authors caution there is no stock-AWS or GPU baseline, no task-level eval on this build, and one remaining approximation in sparse-attention prefill that shifted next-token log-probabilities by 0.012–0.021 nats and changed the top token at 3 of 448 positions.

reddit · r/MachineLearning · /u/WildCard727 · Nov 4, 21:47

**Background**: NKI (Neuron Kernel Interface) is AWS's low-level bare-metal programming language for NeuronCore, the compute unit inside Trainium chips, giving direct control over on-chip memory and instruction scheduling rather than relying on a high-level graph compiler. SBUF is the NeuronCore's on-chip scratchpad memory, and HBM is the off-chip high-bandwidth memory that is far slower to round-trip, so kernel fusion — keeping intermediates on chip — is the main lever for latency. A megakernel fuses an entire decode step or layer into one persistent kernel launch to eliminate per-operator launch overhead and cross-kernel HBM traffic, an idea popularized by Mirage/MPK and Hazy Research work on GPUs. GLM-5.3-Flash is a 320B mixture-of-experts model, meaning only a fraction of its parameters are activated per token, and it combines KDA (linear attention with a recurrent state) with sparse attention over a 1M-token context; the many cross-chip collectives come from sharding such a large model across the 16 NeuronCores of a trn2.48xlarge.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/328113/20260928/aws-trainium-runs-real-time-ai-video-generation-without-nvidia-nki-kernel-playbook-published.htm">AWS Trainium Runs Real-Time AI Video Generation Without NVIDIA...</a></li>
<li><a href="https://theorempath.com/topics/megakernels">Megakernels . End-to-End Fused LLM Inference Kernels</a></li>
<li><a href="https://github.com/allenkchau/trainium-kernel-fusion">allenkchau/ trainium - kernel -fusion: Transformer inference on AWS ...</a></li>

</ul>
</details>

**Tags**: `#inference-optimization`, `#aws-trainium`, `#kernel-fusion`, `#mixture-of-experts`, `#llm-serving`

---

<a id="item-7"></a>
## [Looped transformers save storage, not HBM traffic, B200 profiling shows](https://www.reddit.com/r/MachineLearning/comments/1xnskvt/do_looped_transformers_save_hbm_traffic_profiling/) ⭐️ 8.0/10

A new profiled investigation (with code and raw Nsight Compute data released on GitHub) measured how Huginn-style looped transformers behave on an NVIDIA B200. In a microbenchmark, a chain of eight matmuls sharing a single 72 MiB weight ran 24% faster than the same chain with eight identical weight copies and read almost nothing from HBM, but at 288 MiB — beyond L2 capacity — the advantage disappeared; in a full Huginn Core with random weights, eight iterations took roughly eight times as long and read about eight times as much data from HBM as a single iteration. Looped architectures that reuse the same weights across iterations have become a serious scaling axis in 2025–2026 (Huginn, Ouro and others) and are often pitched as an efficiency win, so this concrete negative result clarifies that storage savings do not automatically translate into bandwidth savings. That distinction directly affects how such models are designed and how kernels must be written — for example whether recurrent weights can be kept on-chip with persistent kernels. The measurements come from a teaching implementation of Huginn Core with random weights rather than a trained model, so the numbers characterize memory behaviour rather than end-to-end inference quality. The key threshold appears to be the L2 cache: shared weights that fit there are read once and reused across iterations, while larger weight sets are re-fetched from HBM every iteration regardless of sharing.

reddit · r/MachineLearning · /u/2dayyy6 · Nov 4, 16:26

**Background**: Looped transformers reuse the same weights more than once, applying a shared layer, block or stack repeatedly to a latent state before a readout; the idea dates back to Universal Transformers in 2018 and was revived at scale by models such as Huginn. HBM is the high-bandwidth memory that holds a GPU's model weights and activations, and on memory-bound workloads the cost of moving data from HBM into on-chip caches can dominate runtime, which is why fits-in-cache versus exceeds-cache is such a sharp dividing line. Nsight Compute is NVIDIA's CUDA kernel profiler, used here to obtain per-kernel metrics such as bytes read from HBM and elapsed time.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/clutch-61/awesome-loop-transformers">GitHub - clutch-61/awesome-loop-transformers: Bilingual ...</a></li>
<li><a href="https://developer.nvidia.com/nsight-compute">Nsight Compute | NVIDIA Developer</a></li>
<li><a href="https://arxiv.org/abs/2610.23036">[2610.23036] Towards Looped Models Done Right, Part I ...</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#GPU-memory-bandwidth`, `#HBM`, `#performance-profiling`, `#LLM-efficiency`

---

<a id="item-8"></a>
## [Oracle Cancels $7B AI Chip Lease With Tencent After US Pushback](https://www.tradingview.com/news/seekingalpha:e51e68f4d094b:0-oracle-cancels-7b-ai-chip-lease-with-tencent-amid-us-concerns-ft/) ⭐️ 8.0/10

Oracle has scrapped a roughly $7 billion, five-year AI chip lease with Tencent after US officials raised concerns with the company and the Trump administration applied pressure, according to the Financial Times. The deal would have given Tencent access to as many as 100,000 advanced AI chips hosted in Oracle data centers across Southeast Asia, with an upfront payment of about 30% of the contract value. The cancellation is one of the clearest examples yet of Washington extending export-control scrutiny beyond the direct sale of chips to third-country compute arrangements, effectively closing an offshore route that Chinese AI firms had been using to access restricted hardware. It signals that US chip policy now shapes not just what Chinese companies can buy, but where and from whom they can rent compute — a constraint that could slow Chinese AI training capacity and chill similar cross-border leasing deals. The agreement was structured as a lease rather than a sale: Tencent would rent capacity in Oracle's Southeast Asian data centers rather than take ownership of the hardware, with roughly 30% paid upfront and the remainder spread over five years. The chips involved are described only as "advanced AI chips"; both Washington's export controls and Beijing's own restrictions on foreign AI hardware in domestic data centers had made them unusable inside mainland China.

telegram · zaihuapd · Nov 4, 11:01

**Background**: US export controls restrict which advanced AI accelerators — most notably Nvidia's high-end GPUs — can be sold to Chinese firms, and successive rounds of rules have also targeted onward transfers and third-country data centers used as intermediaries. Separately, Beijing has pushed domestic data centers to favor homegrown chips over foreign accelerators, meaning Tencent could not simply deploy the same hardware at home. Leasing compute housed abroad became an attractive workaround, because the Chinese firm never takes ownership of the chips; regulators are now treating those offshore arrangements as a loophole to be closed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zerohedge.com/ai/oracle-kills-7bn-tencent-ai-chip-deal-under-trump-pressure">Oracle Kills $ 7 BN Tencent AI Chip Deal Under Trump... | ZeroHedge</a></li>
<li><a href="https://nypost.com/2026/11/04/business/oracle-nixes-7b-chip-leasing-deal-with-chinas-tencent-after-trump-admin-pushback-report/">Oracle nixes $ 7 B chip leasing deal with China's Tencent after Trump...</a></li>
<li><a href="https://diesignal.com/articles/tencent-signs-7-billion-five-year-lease-for-100-000-oracle-ai-chips-18f11e57">Tencent Leases 100,000 Oracle AI Chips in $ 7 Billion Five-Year Deal</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#Oracle`, `#Tencent`, `#US-China tech`, `#export controls`

---

<a id="item-9"></a>
## [Huawei Tells Customers to Source Their Own HBM for Ascend 960DT](https://thenextweb.com/news/huawei-hbm-smuggling-samsung-sk-hynix-ascend-960dt) ⭐️ 8.0/10

According to a report from The Information relayed by The Next Web, Huawei has told some customers that its next-generation flagship AI chip, the Ascend 960DT, will rely mainly on Samsung and SK Hynix HBM, and that buyers must arrange their own memory supply because Chinese domestic HBM capacity is insufficient. A Shenzhen chip broker quoted in the report said a single HBM3E stack now costs around $4,000, up from a few hundred dollars a year earlier. The disclosure suggests that even Huawei's most advanced domestic AI accelerator is constrained by memory rather than logic, with the shortfall filled through grey-market channels. That pushes up system costs for Chinese AI data-center operators and shows how export controls on advanced memory are shaping the economics of China's AI buildout. The report describes HBM dies being re-balled onto very weak processors so the modules can be declared under processor HS codes, shipped to Hong Kong, carried into the mainland by hand, and then de-soldered with heat — a labor-intensive route that explains the roughly $4,000 per-stack price. The Ascend 960DT is the training/decode variant of Huawei's sixth-generation Ascend 960 family, sharing a microarchitecture with the prefill-focused 960PR but tuned for high memory bandwidth, so the HBM dependency is structural rather than incidental.

telegram · zaihuapd · Nov 4, 14:52

**Background**: HBM, or high-bandwidth memory, is DRAM stacked vertically into a single package and connected through wide interfaces, which lets AI accelerators feed their compute units fast enough; HBM3E is the current mainstream generation, used in parts such as Nvidia's H200. The market is dominated by Samsung, SK Hynix and Micron, while Chinese suppliers such as ChangXin are still early: TrendForce estimates Chinese vendors will hold less than 2% of the HBM market by 2027. US export controls restrict sales of advanced HBM to China, which is why supply is routed through transshipment hubs like Hong Kong. Huawei unveiled the Ascend 960 series at its HC2026 Connect conference on September 17, saying development was ahead of schedule with performance roughly doubled over the previous generation.

<details><summary>References</summary>
<ul>
<li><a href="https://mirrorfrog.com/docs/cards/huawei/ascend-960dt/">Huawei Ascend 960DT (昇腾 960DT) | AI 算力卡百科 | 233 款 AI 芯片...</a></li>
<li><a href="https://www.199it.com/archives/1860209.html">TrendForce：2027年 中 国 供应商 HBM 份额不到2%， HBM ...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2083900025302671798">华为 HC2026 公布 960DT 完整参数，2027 年 Q1 面世</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#HBM`, `#AI chips`, `#semiconductor supply chain`, `#export controls`

---

<a id="item-10"></a>
## [Bluetooth HDT Standard Adopted: LE Peak Bit Rate Rises to 7.5 Mbps](https://www.bluetooth.com/press/bluetooth-high-data-throughput-opens-a-new-chapter-in-wireless-performance/) ⭐️ 8.0/10

On November 4, the Bluetooth Special Interest Group (SIG) announced it has adopted Bluetooth High Data Throughput (HDT), an optional feature of Bluetooth Core 7.0 that raises the maximum Bluetooth LE bit rate from 2 Mbps to 7.5 Mbps — nearly a fourfold increase — while also improving capacity, energy efficiency and reliability. The first standardized use case is premium wireless audio with lossless and high-resolution support, with products expected around 2027. The bandwidth jump removes one of the biggest technical obstacles to lossless, high-resolution wireless audio, a segment where Bluetooth has lagged behind wired connections and proprietary 2.4 GHz/5 GHz links. If the 2027 timeline holds, it will reshape product planning for headphone makers, audio codec vendors and Bluetooth chip designers, and could extend LE into higher-throughput uses beyond audio. HDT is an optional feature that is designed to coexist with older devices, meaning both ends of a connection must support it to reach the higher rate, and real-world throughput will remain below the 7.5 Mbps raw PHY figure once protocol overhead is accounted for. The technology still operates in the crowded 2.4 GHz band, where interference and coexistence remain practical concerns for audio latency and stability.

telegram · zaihuapd · Nov 5, 01:39

**Background**: Bluetooth LE (Low Energy) is the power-efficient branch of Bluetooth, and its maximum over-the-air bit rate has been capped at 2 Mbps since the introduction of the 2M PHY in Bluetooth 5 back in 2016. That ceiling has been the key constraint on delivering lossless or high-resolution audio wirelessly, since formats such as 24-bit/96 kHz require considerably more sustained bandwidth than typical Bluetooth codecs can carry. The SIG has since been iterating on the core specification — Core 7.0 is the version that now packages HDT — and the PHY here refers to the physical-layer modulation scheme that determines the raw bit rate over the air.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/354478/bluetooth-sig-announces-bluetooth-high-data-throughput">Bluetooth SIG Announces Bluetooth High Data... | TechPowerUp</a></li>
<li><a href="https://www.androidauthority.com/bluetooth-hdt-lossless-wireless-audio-3731705/">Bluetooth HDT could standardize lossless wireless audio</a></li>

</ul>
</details>

**Tags**: `#Bluetooth`, `#wireless`, `#audio`, `#standards`, `#HDT`

---