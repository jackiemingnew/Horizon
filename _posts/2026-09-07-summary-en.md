---
layout: default
title: "Horizon Summary: 2026-09-07 (EN)"
date: 2026-09-07
lang: en
---

> From 33 items, 8 important content pieces were selected

---

1. [LG Smart TVs Caught Logging Audio and Snooping on Devices](#item-1) ⭐️ 8.0/10
2. [OpenAI Reveals Recursive Self-Improvement Push and Coding Agent Use](#item-2) ⭐️ 8.0/10
3. [TPU Inference Externalization Full Steam Ahead via InferenceX](#item-3) ⭐️ 8.0/10
4. [Optuna Team Releases Rustuna: Rust-Based Hyperparameter Optimization](#item-4) ⭐️ 8.0/10
5. [LLM-guided Program Evolution Breaks 10 Circle-Packing Records](#item-5) ⭐️ 8.0/10
6. [KV Cache as an Agent Runtime: A New Way to Make LLMs Interactive](#item-6) ⭐️ 8.0/10
7. [Measuring LLM Performance Drift with 31,352 Repeated Benchmark Runs](#item-7) ⭐️ 8.0/10
8. [China's Supreme Court Issues 24-Article Judicial Interpretation on AI Disputes](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LG Smart TVs Caught Logging Audio and Snooping on Devices](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 8.0/10

Reports reveal that LG Smart TVs log audio even when the screen is off and actively snoop on other devices connected to the local network. The findings point to serious privacy violations affecting an estimated 216 million LG televisions. With an estimated 216 million LG TVs in homes, this kind of covert data collection affects tens of millions of households worldwide. It also shows that consent in smart-TV terms of service is often meaningless, prompting calls for stronger regulation. LG's contract terms reportedly require owners to inform household members and guests that their voices may be captured and processed. Some users avoid the issue by disabling all network functions or physically unplugging the TV's Wi-Fi/BT chip.

hackernews · treve · Sep 7, 00:22 · [Discussion](https://news.ycombinator.com/item?id=49592375)

**Background**: Smart TVs commonly include microphones and always-on voice assistants, but how captured audio is used is often buried in lengthy privacy policies. LG's reported behavior goes further by scanning local network devices, which can reveal information about phones, computers, and other connected hardware. For many users, the only practical protections are hardware-level disconnection or refusing network access entirely.

**Discussion**: Commenters are outraged, with several pointing out that LG's terms may run afoul of all-party wiretap laws because guests never consent to being recorded. Others share workarounds such as unplugging the Wi-Fi/Bluetooth chip on LG OLED TVs, and some note that people who refused smart-TV features were previously ridiculed for being paranoid.

**Tags**: `#privacy`, `#security`, `#smart-tv`, `#lg`, `#surveillance`

---

<a id="item-2"></a>
## [OpenAI Reveals Recursive Self-Improvement Push and Coding Agent Use](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

OpenAI published a report, 'Research acceleration: The view inside OpenAI,' alongside a companion essay by Chief Scientist Jakub Pachocki, framing recursive self-improvement (RSI) as its new focus on the path to AGI. The report shows OpenAI researchers rapidly adopted coding agents in 2026, with median daily AI spend per researcher climbing to roughly $600 by late August. This marks one of the clearest public statements from OpenAI that recursive self-improvement is a practical research direction rather than a speculative concept. It also highlights how coding agents have become essential infrastructure inside frontier AI labs, a trend that will likely shape how software is developed across the industry. The report uses the acronym RSI without expanding it, implying it is now common internal vocabulary. Simon Willison notes that the steepest rise in agent-related spend began in late July, speculating that it coincided with employee access to the model later released as GPT-6 Astra.

rss · Simon Willison · Sep 6, 23:57

**Background**: Recursive self-improvement (RSI) is a hypothesized process in which an artificial general intelligence rewrites its own code, potentially leading to an intelligence explosion and superintelligence. Coding agents are AI tools that can autonomously write, debug, and refactor code, understanding multi-file context and executing multi-step tasks, unlike basic autocomplete assistants. Agentic engineering is a methodology that integrates such AI helpers into existing development workflows; the term builds on the earlier concept of 'vibe coding' popularized by OpenAI co-founder Andrej Karpathy in 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is Agentic Engineering? | IBM</a></li>
<li><a href="https://agentic.ai/best/coding-agents">21 Best AI Coding Agents in 2026 — Agentic.ai</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AGI`, `#AI research`, `#coding agents`, `#recursive self-improvement`

---

<a id="item-3"></a>
## [TPU Inference Externalization Full Steam Ahead via InferenceX](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 8.0/10

A new SemiAnalysis report says Google's TPU inference externalization, labeled 'InferenceX,' is progressing rapidly and delivers up to 50% better performance per dollar. The report points to a growing customer base and next-gen TPUs such as Ironwood and TPUv8i as evidence that the CUDA moat is starting to erode. This challenges Nvidia's long-held dominance in AI inference, as CUDA's software ecosystem has historically been a formidable lock-in. If TPU inference externalization continues to gain traction, it could give cloud customers a more cost-effective alternative and accelerate multi-cloud AI strategies. The article highlights 'up to 50% better performance per dollar' and the 'rapid externalization' of Google's TPU stack, alongside a growing customer base. It also references Ironwood and TPUv8i, tying near-term TPU hardware advancements to the inference push.

rss · Semianalysis · Sep 7, 20:00

**Background**: Tensor Processing Units (TPUs) are Google's custom ASICs designed to accelerate machine-learning training and inference workloads. Ironwood, announced in April 2025, is Google's seventh-generation TPU aimed at inference, while TPUv8i is the inference-focused variant of the eighth-generation TPU family introduced at Google Cloud Next 2026. Nvidia's CUDA software stack has been a powerful moat for over a decade, locking developers into its ecosystem; rivals have struggled to match its maturity. 'InferenceX' appears to be the label for Google's broader push to make its TPU inference stack more widely accessible externally.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam">TPU Inference Externalization Full Steam Ahead - InferenceX</a></li>
<li><a href="https://www.panabee.com/news/why-is-cuda-such-a-powerful-moat-for-nvidia-nvda">Why is CUDA Such a Powerful Moat for Nvidia (NVDA)? | NVDA ...</a></li>
<li><a href="https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/">Ironwood: The first Google TPU for the age of inference</a></li>

</ul>
</details>

**Tags**: `#TPU`, `#inference`, `#CUDA`, `#AI hardware`, `#cloud computing`

---

<a id="item-4"></a>
## [Optuna Team Releases Rustuna: Rust-Based Hyperparameter Optimization](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 8.0/10

The Optuna team released Rustuna, a high-performance Rust implementation of Optuna that keeps the familiar API while requiring zero Python dependencies. The project is available on GitHub and was announced via the Optuna Medium blog. Rustuna gives Rust-native machine learning workflows a direct, memory-efficient way to use Optuna's hyperparameter search without Python bindings. Its zero-dependency design also reduces supply chain attack surface, addressing a key security concern in modern ML tooling. Familiar Optuna concepts, such as studies and trials, are preserved, which should ease migration for existing Optuna users. As of this announcement, Optuna has not published detailed performance benchmarks or a compatibility matrix for Rustuna.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**Background**: Optuna is a widely used open-source hyperparameter optimization framework that automates the search for optimal model settings such as learning rates or regularization coefficients. Hyperparameter optimization is a key part of AutoML, because the choice of hyperparameters heavily influences model performance. Software supply chain attacks target trusted dependencies to inject malicious code, making reduced dependency trees an important security improvement. Rust's memory safety and performance make it an attractive language for reimplementing Python-based ML infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/optuna/optuna">GitHub - optuna / optuna : A hyperparameter optimization framework</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperparameter_optimization">Hyperparameter optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#hyperparameter optimization`, `#Optuna`, `#machine learning`, `#performance`

---

<a id="item-5"></a>
## [LLM-guided Program Evolution Breaks 10 Circle-Packing Records](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

An author used an LLM to iteratively evolve an optimization algorithm, improving best-known solutions for 10 values of N in the range 101–114 on the Packomania csqv benchmark by 2.4%–5.4%. The entire run cost only $27.72 and took 15 iterations. This demonstrates that LLM-guided program evolution can autonomously discover algorithms that outperform human-designed approaches on a recognized optimization benchmark. It highlights a low-cost, verifiable path for AI-driven algorithmic and scientific discovery. The system, called Discovery Loop, starts from a simple seed solver, lets the LLM propose changes informed by a scoreboard and prior attempts, and scores each candidate with an independent verifier. Packomania independently accepted the new records; the paper, code, and solutions have been made publicly available.

reddit · r/MachineLearning · /u/SIGH_I_CALL · Sep 7, 16:54

**Background**: Circle packing is a classic geometry optimization problem that arranges circles inside a unit square without overlaps, often maximizing the sum of radii for a given number of circles N. Packomania maintains a well-known database of best-known solutions for such benchmarks. LLM-guided program evolution takes a different route from direct LLM problem solving: it lets the LLM iteratively rewrite a solver program, testing each change against an independent verifier. This allows the search to improve the algorithm itself rather than just a single solution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.05093">[2609.05093] LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28</a></li>
<li><a href="https://en.wikipedia.org/wiki/Circle_packing">Circle packing - Wikipedia</a></li>
<li><a href="http://www.packomania.com/cciuneq/">The best known solutions of benchmark instances for ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#program evolution`, `#optimization`, `#AI research`, `#benchmark`

---

<a id="item-6"></a>
## [KV Cache as an Agent Runtime: A New Way to Make LLMs Interactive](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

A Yandex Research blog post proposes using direct modifications to the KV cache during inference as a lightweight agent runtime, instead of retraining or replacing models. The idea extends the lab’s Hogwild! Inference and AsyncReasoning work, and the post includes a preview of a Qwen-based agent interactively playing Doom. This positions inference/runtime design as a distinct axis for improving agent capabilities, sitting between external harnesses and costly model retraining. If it works broadly, researchers can get more interactive, responsive LLM behavior by manipulating state already available during decoding. The KV cache stores intermediate key/value representations from attention, and the post treats that memory as agent-controllable state. Earlier work shown as grounding includes Hogwild! Inference, where parallel LLM instances share one attention cache, and AsyncReasoning, which lets reasoning models think and write concurrently; the future-work demo reportedly uses a Qwen3.8-27B agent in a Doom environment.

reddit · r/MachineLearning · /u/_puhsu · Sep 7, 09:03

**Background**: In transformer LLMs, autoregressive generation repeatedly recomputes attention over earlier tokens; a KV cache avoids that by caching key and value tensors, substantially speeding up inference. Modern LLM agents usually combine a fixed pretrained model with an external 'harness' for prompting, tool use, or planning, because changing model weights is expensive. The authors argue that modifying inference state such as the KV cache gives a third, cheaper way to steer behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/not-lain/kv-caching">KV Caching Explained: Optimizing Transformer Inference Efficiency</a></li>
<li><a href="https://arxiv.org/abs/2504.06261">[2504.06261] Hogwild! Inference: Parallel LLM Generation via Concurrent Attention</a></li>
<li><a href="https://arxiv.org/html/2512.10931v1">Asynchronous Reasoning: Training-Free Interactive Thinking LLMs</a></li>

</ul>
</details>

**Tags**: `#KV cache`, `#LLM agents`, `#inference`, `#machine learning research`, `#interactive AI`

---

<a id="item-7"></a>
## [Measuring LLM Performance Drift with 31,352 Repeated Benchmark Runs](https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/) ⭐️ 8.0/10

The author presents a longitudinal benchmarking methodology that uses 31,352 repeated score observations across 49 models to detect LLM performance drift. The analysis found a within-day standard deviation of 2.80 points and a between-day standard deviation of 8.43 points, roughly a 3:1 ratio. Leaderboard-style benchmark results treat model quality as a stable snapshot, which can mislead practitioners when API-served models change over time. By quantifying how much scores vary between days, this work makes a case for continuous longitudinal evaluation instead of one-time comparisons. The methodology keeps benchmark configurations versioned, uses repeated execution-based evaluation rather than LLM judges, tracks serving/version metadata when available, and runs change detection over the resulting time series. The author also separates availability failures from valid task outcomes and acknowledges confounders such as task composition, sampling, missingness, and provider behavior.

reddit · r/MachineLearning · /u/ionutvi · Sep 7, 07:44

**Background**: Traditional LLM benchmarks are snapshots: a model is evaluated once and that score is treated as a stable property. However, API-served models can change because of infrastructure, configuration, or version updates without a public release. Longitudinal benchmarking turns snapshots into a time series so genuine model drift can be separated from ordinary variability. The numbers in this post highlight that between-day differences are about three times larger than within-day noise, suggesting temporal effects deserve scrutiny.

<details><summary>References</summary>
<ul>
<li><a href="https://data-today.net/llm-performance-drift-benchmark-variance/">LLM performance drift : why your benchmark scores... | Data Today</a></li>
<li><a href="https://toloka.ai/blog/llm-observability/">LLM observability</a></li>
<li><a href="https://www.traceloop.com/">Traceloop - LLM Reliability Platform</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmarking`, `#measurement`, `#evaluation`, `#model drift`

---

<a id="item-8"></a>
## [China's Supreme Court Issues 24-Article Judicial Interpretation on AI Disputes](https://www.cnr.cn/news/20260907/t20260907_527806795.shtml) ⭐️ 8.0/10

On September 7, the Supreme People's Court of China issued a 24-article judicial interpretation on artificial intelligence disputes. It clarifies that unauthorized AI-generated replicas of identifiable faces or voices can constitute infringement of personality rights, that algorithmic price discrimination may trigger liability, and that punitive damages may be supported when AI impersonation is used to induce consumption. This provides China's first systematic judicial standards for civil disputes involving AI, giving developers, platforms, and users clearer legal expectations. It could reshape compliance for facial recognition, recommendation algorithms, voice synthesis, and autonomous driving, and strengthen legal responses to deepfakes and algorithmic discrimination. The interpretation has five parts and 24 articles, covering AI face-swapping, algorithmic price discrimination, unauthorized endorsement by impersonation, autonomous driving, and intellectual property. It also regulates AI-assisted 'network kaihe' and 'human flesh search' practices that infringe on natural persons' privacy rights.

telegram · zaihuapd · Sep 7, 09:32

**Background**: In China, judicial interpretations issued by the Supreme People's Court are normative documents with legal binding force, designed to guide lower courts in applying statutes. AI face-swapping uses deep synthesis to replace a person's face or voice in video, and without consent such acts may violate personality rights. 'Algorithmic price discrimination' — colloquially known as 'big data killing familiarity' — refers to platforms using user behavior data to charge different prices for the same product or service to different customers. 'Network kaihe' is a Chinese internet term for illegally obtaining and publicly exposing personal information such as names, addresses, and ID numbers, often described as an escalated form of doxxing.

<details><summary>References</summary>
<ul>
<li><a href="http://gongbao.court.gov.cn/Details/b1a7af04dadc864fc2b87fd9bbe4dc.html">最高人民法院印发《关于修改〈最高人民法院关于司法解释工作的规定〉的决定》的通知 - 中华人民共和国最高人民法院公报</a></li>
<li><a href="https://baike.baidu.com/item/开盒/58943997">开盒（网络热词）_百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/128561235">大数据杀熟是什么？ - 知乎 - 知乎专栏</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#China law`, `#deepfakes`, `#algorithmic fairness`, `#privacy`

---