---
layout: default
title: "Horizon Summary: 2026-07-25 (EN)"
date: 2026-07-25
lang: en
---

> From 25 items, 9 important content pieces were selected

---

1. [vLLM v0.26.0 Released with Inkling Support and DeepSeek-V4 Optimization](#item-1) ⭐️ 9.0/10
2. [Anthropic Launches Claude Opus 5 at Half the Price of Fable 5](#item-2) ⭐️ 9.0/10
3. [SGLang v0.5.16: DSPark Decoding and Inkling Support](#item-3) ⭐️ 8.0/10
4. [Android May Restrict On-Device ADB Usage](#item-4) ⭐️ 8.0/10
5. [Open-weight AI mirrors Kubernetes' rise](#item-5) ⭐️ 8.0/10
6. [Opus 5 is Anthropic's most prompt injection resistant model](#item-6) ⭐️ 8.0/10
7. [Can AMD Break NVIDIA's CUDA Moat? Advancing AI 2026](#item-7) ⭐️ 8.0/10
8. [China Imposes Tax on Offshore Trust Transfers and Income](#item-8) ⭐️ 8.0/10
9. [Apple Lobbies Trump to Use Chinese Memory Chips, Micron Opposes](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 Released with Inkling Support and DeepSeek-V4 Optimization](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 9.0/10

vLLM v0.26.0 introduces full support for the Inkling model family (975B parameters, 41B active), significant DeepSeek-V4 performance improvements across vendors (up to 2.94% end-to-end TPOT improvement), and a flexible attention backend selection per KV-cache group. This release enhances inference efficiency for cutting-edge models like DeepSeek-V4 and Inkling, making large-scale deployment more practical. The flexible attention backend and improved speculative decoding lower latency and broaden hardware support. The release includes 411 commits from 212 contributors, with features such as piecewise CUDA graph support for Inkling, Hopper FA4 relative attention, MTP=1 speculative decoding, and fp32 lm_head for generation models. The Rust frontend now supports multimodal video and audio.

github · khluu · Jul 25, 10:38

**Background**: vLLM is a high-throughput, memory-efficient inference engine for large language models. This version adds support for the Inkling model, a Mixture-of-Experts transformer with 975B total parameters and 1M token context window, and improves performance for DeepSeek-V4 across NVIDIA, AMD, and Intel hardware through specialized kernels and compiler optimizations.

<details><summary>References</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://www.spheron.network/blog/flashattention-4-blackwell-gpu-cloud-guide/">FlashAttention-4 on GPU Cloud: Blackwell Inference... | Spheron Blog</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#DeepSeek`, `#GPU kernels`

---

<a id="item-2"></a>
## [Anthropic Launches Claude Opus 5 at Half the Price of Fable 5](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 9.0/10

Anthropic has released Claude Opus 5, a new frontier AI model that matches the intelligence of Claude Fable 5 at half the price, and is currently leading the Artificial Analysis leaderboard. This release makes frontier-level AI capabilities more accessible by significantly reducing cost, potentially expanding adoption among developers and enterprises. It also intensifies competition in the AI model market, pushing other providers to improve performance-per-dollar. Claude Opus 5 is priced the same as Opus 4.8 and offers a 'fast mode' at twice the cost. It has improved at finding cybersecurity vulnerabilities but was deliberately not trained on exploitation, similar to its predecessor.

rss · Simon Willison · Jul 24, 23:48

**Background**: Anthropic's Claude model family includes multiple tiers, with the 'Mythos' series being the most powerful. Claude Fable 5 is a publicly released Mythos-class model, while Claude Mythos 5 is a restricted version. The Artificial Analysis leaderboard ranks AI models on a composite score. 'Fast mode' is an inference acceleration feature that uses the same model weights but optimizes backend configuration for faster token output.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://llm-stats.com/benchmarks/artificial-analysis">Artificial Analysis Leaderboard - llm-stats.com</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/fast-mode">Fast mode (research preview) - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: The AI community has reacted positively to Claude Opus 5, with early benchmark results showing it leading the leaderboard. Some developers appreciate the reduced cost, while others express caution about the model's improved vulnerability-finding abilities.

**Tags**: `#Claude`, `#Anthropic`, `#LLM`, `#AI model`, `#release`

---

<a id="item-3"></a>
## [SGLang v0.5.16: DSPark Decoding and Inkling Support](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 8.0/10

SGLang v0.5.16 introduces DSPark confidence-driven speculative decoding, achieving 383.7 tok/s on DeepSeek-V4-Pro, and adds support for Inkling, a 975B-parameter multimodal MoE model. These advancements significantly improve LLM inference efficiency and capability, enabling faster token generation and supporting a massive open-weights multimodal model, benefiting researchers and practitioners in AI deployment. DSPark uses semi-autoregressive block drafting with variable verification length based on the draft model's confidence, while Inkling features a mixture of attention mechanisms, NVFP4 MoE, and a 1M-token context window.

github · Qiaolin-Yu · Jul 25, 00:13

**Background**: Speculative decoding accelerates LLM inference by using a smaller draft model to propose tokens that a larger target model verifies in parallel. DSPark improves this by adaptively sizing the verification window based on confidence. Inkling is a recently released open-weights multimodal MoE model from Thinking Machines Lab with 975B total parameters and 41B active parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark: Confidence-Scheduled Speculative ...</a></li>
<li><a href="https://www.lmsys.org/blog/2026-07-06-dspark-sglang">DSpark in SGLang: Speculative Decoding with Confidence-Driven ...</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**Tags**: `#speculative decoding`, `#LLM inference`, `#MoE`, `#multimodal`, `#open source`

---

<a id="item-4"></a>
## [Android May Restrict On-Device ADB Usage](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/) ⭐️ 8.0/10

Android is considering a change that would restrict on-device ADB (Android Debug Bridge) usage, requiring wireless connections to be authorized to a specific IP address. This change would impact developers who rely on wireless ADB for debugging, potentially improving security but also reducing convenience and raising concerns about Google's control over developer tools. The proposed restriction would block ADB connections from unknown IP addresses unless the user explicitly authorizes the connection. This is still in early discussion within the Android engineering team.

hackernews · shscs911 · Jul 25, 06:57 · [Discussion](https://news.ycombinator.com/item?id=49045159)

**Background**: ADB (Android Debug Bridge) is a command-line tool that allows developers to communicate with an Android device for debugging, installing apps, and running shell commands. It can operate over USB or wirelessly via TCP/IP. On-device ADB is often used by developers for convenience but can pose a security risk if left open on untrusted networks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Android_Debug_Bridge">Android Debug Bridge - Wikipedia</a></li>
<li><a href="https://developer.android.com/tools/adb">Android Debug Bridge (adb) | Android Studio | Android Developers</a></li>
<li><a href="https://www.howtogeek.com/125769/how-to-install-and-use-abd-the-android-debug-bridge-utility/">How to Install and Use ADB, the Android Debug Bridge Utility</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some argue the security benefit is minimal since the attack requires developer options and remote ADB to be enabled, while others see it as a step toward locking down developer capabilities. Some suggest alternatives like IP whitelisting are more balanced.

**Tags**: `#Android`, `#ADB`, `#Security`, `#Developer Tools`, `#Privacy`

---

<a id="item-5"></a>
## [Open-weight AI mirrors Kubernetes' rise](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

The article argues that open-weight AI models will become the industry standard, drawing a parallel to how Kubernetes became the dominant container orchestration platform despite initial proprietary alternatives. This analogy is significant because it suggests that an open, customizable AI platform could become the center of gravity, outpacing any single vendor's innovation and reshaping the competitive dynamics of the AI industry. The article notes that just as Kubernetes enabled widespread container adoption, open-weight models like DeepSeek and Qwen are challenging proprietary models, though technical bans on models by origin are considered infeasible because weights are just numbers.

hackernews · tknaup · Jul 25, 14:49 · [Discussion](https://news.ycombinator.com/item?id=49048034)

**Background**: Open-weight AI models are those where the trained model weights are publicly released, allowing anyone to download, run, and fine-tune them. This contrasts with closed-weight models like GPT-4, where access is only via API. Kubernetes is an open-source container orchestration system that became the de facto standard despite competition from Docker Swarm and Mesos. The article posits a similar trajectory for open-weight AI.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/open-models/">Open models by OpenAI</a></li>
<li><a href="https://www.gumloop.com/blog/open-weight-ai-models">7 best open weight AI models I've tested in 2026 - gumloop.com</a></li>

</ul>
</details>

**Discussion**: Community comments include skepticism about banning Chinese models, praise for the 'center of gravity' assertion, confusion over tokenomics, and appreciation for past open-source releases from OpenAI. There is also a suggestion that true Kubernetes-like status would require public training data and collaborative development.

**Tags**: `#open-weight`, `#AI`, `#Kubernetes`, `#model licensing`, `#AI industry`

---

<a id="item-6"></a>
## [Opus 5 is Anthropic's most prompt injection resistant model](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

Boris Cherny, from Anthropic, stated that Opus 5 is their least prompt injectable model yet, based on system card evaluations and red teaming exercises. Prompt injection is a critical security vulnerability in large language models, and increased resistance directly enhances AI safety and trustworthiness. This development could influence industry standards for model security. The claim is supported by the Claude Opus 5 System Card (page 73), which includes prompt injection evaluations and adversarial red teaming results. The model is described as 'very hard to prompt inject successfully.'

rss · Simon Willison · Jul 25, 00:42

**Background**: Prompt injection is a security exploit where malicious inputs override a model's intended instructions, causing unintended behavior. System cards are transparency documents that detail an AI system's capabilities, limitations, and safety evaluations. Red teaming involves adversarial testing to uncover vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.linkedin.com/pulse/system-cards-foundation-ai-transparency-sandy-dunn-uf1uc">System Cards : Foundation of AI Transparency</a></li>
<li><a href="https://en.wikipedia.org/wiki/Red_teaming">Red teaming</a></li>

</ul>
</details>

**Tags**: `#prompt-injection`, `#anthropic`, `#claude`, `#generative-ai`, `#ai`

---

<a id="item-7"></a>
## [Can AMD Break NVIDIA's CUDA Moat? Advancing AI 2026](https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing) ⭐️ 8.0/10

At AMD's Advancing AI 2026 event, the company unveiled new initiatives to challenge NVIDIA's CUDA dominance, including the agentic kernel generation approach and the Helios rack-scale architecture with Instinct MI455X GPUs. If successful, AMD's software improvements and hardware advancements could significantly reduce NVIDIA's software ecosystem moat, potentially reshaping the AI hardware landscape and offering more competitive choices for customers. The Instinct MI455X features 432GB of HBM4 memory and is manufactured on a 2nm process, with peak MXFP8 and MXFP4 performance up to 4x the MI355X. However, internal development clusters remain unstable, and production ramp has been described as 'hell,' with discounts of up to 105% from finance engineering.

rss · Semianalysis · Jul 25, 00:33

**Background**: CUDA is NVIDIA's proprietary parallel computing platform that has become the dominant software ecosystem for AI workloads. AMD has long struggled to offer a competitive alternative. Agentic kernel generation refers to using large language models (LLMs) to automatically synthesize and optimize GPU kernels, potentially reducing the need for hand-tuned CUDA code. The Helios rack-scale architecture integrates 72 MI455X GPUs with AMD EPYC CPUs and UALink networking, similar to NVIDIA's NVL72 design.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/AMD-Instinct-MI455X-Helios">AMD Launches Instinct MI455X, Helios AI Rack - Phoronix</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center">AMD takes the wraps off its Instinct MI455X AI accelerator — CDNA 5 and Helios rack-scale architecture combine to take the fight to Nvidia in the data center | Tom's Hardware</a></li>
<li><a href="https://arxiv.org/abs/2602.24286">[2602.24286] CUDA Agent: Large-Scale Agentic RL for High ... [2607.04395] NKI-Agent: Domain-Specific Fine-Tuning and ... qhy991/Awesome-LLM-Kernel-Agent - GitHub Awesome LLM-Driven Kernel Generation - GitHub KernelAgent: Hardware-Guided GPU Kernel Optimization via ... Agentic Kernel Generation - emergentmind.com</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#CUDA`, `#AI hardware`, `#software ecosystem`, `#GPU competition`

---

<a id="item-8"></a>
## [China Imposes Tax on Offshore Trust Transfers and Income](https://liaoning.chinatax.gov.cn/art/2026/7/24/art_5869_7823.html) ⭐️ 8.0/10

China's Ministry of Finance and State Taxation Administration issued Announcement No. 21 of 2026 on July 24, requiring resident individuals to declare and pay tax on property transferred into offshore trusts and on trust income, whether distributed or not. This regulation closes tax loopholes previously used by high-net-worth individuals to defer or avoid taxes through offshore trusts, significantly impacting cross-border wealth management and estate planning. The tax rate is a flat 20% on the appreciation (market value minus original cost and reasonable expenses) at each stage—transfer, operation, and liquidation. A 90-day grace period with no late penalties applies for non-compliance during 2023–2025.

telegram · zaihuapd · Jul 25, 00:31

**Background**: An offshore trust is a trust established under the laws of a foreign jurisdiction, often used for asset protection and tax planning. Previously, Chinese residents could avoid current taxation by placing assets in offshore trusts and delaying distributions; the new rule applies a 'look-through' approach, taxing the settlor annually on trust income regardless of distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/境外信託">境外信托 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/离岸信托/2652314">离岸信托_百度百科</a></li>
<li><a href="https://baike.baidu.com/item/财产转让所得/309814">财产转让所得_百度百科 财产转让所得个人所得税 - ailegal.baidu.com 个人所得税财产转让所得税务处理全解析 从政策解读到实操案例帮你规避... 财产转让所得应纳税额的计算_25年注会税法学习要点 个人所得税|“财产转让所得”所涉个人所得税的处理 财产转让所得交多少个税，就看这三点 - 知乎</a></li>

</ul>
</details>

**Tags**: `#税务`, `#离岸信托`, `#个人所得税`, `#政策法规`, `#财富管理`

---

<a id="item-9"></a>
## [Apple Lobbies Trump to Use Chinese Memory Chips, Micron Opposes](https://www.wsj.com/tech/trump-apple-micron-china-chips-784bbd3d) ⭐️ 8.0/10

Apple has been lobbying the Trump administration to allow the use of Chinese memory chips from CXMT and YMTC in products sold outside the U.S., while Micron is actively opposing the move. This reflects a major business and political clash between two U.S. tech giants over supply chain strategy and China relations, with implications for global semiconductor trade. Apple CEO Tim Cook and other executives have pitched the plan to Trump, Commerce Secretary Lutnick, and Treasury Secretary Bessent in recent weeks, proposing to source chips from CXMT (DRAM) and YMTC (NAND Flash).

telegram · zaihuapd · Jul 25, 04:02

**Background**: ChangXin Memory Technologies (CXMT) is a Chinese DRAM manufacturer, while Yangtze Memory Technologies (YMTC) produces NAND Flash. Both companies are under U.S. sanctions; YMTC was added to the Entity List in 2022. Apple seeks to use cheaper Chinese chips to ease cost pressure, but Micron, a key Apple supplier, opposes due to competition and national security concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/長江存儲">长江存储 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/长江存储科技有限责任公司/20002721">长江存储科技有限责任公司_百度百科 追赶三星、海力士！继长鑫后，长江存储宣布IPO，估值或破万亿！湖北国... 长江存储 - 维基百科，自由的百科全书 企业简介-长江存储 - YMTC 长江存储 IPO 启幕！千亿存储航母启航，五大梯队 A 股受益全梳理 2026... 又一“巨无霸”！长江存储宣布IPO _ 东方财富网</a></li>
<li><a href="https://www.jiuyangongshe.com/a/2z5j06y178w">长 鑫 存 储 上市催化！ 手握 长 期订单的10大 存 储 产业链核心标的梳理</a></li>

</ul>
</details>

**Tags**: `#苹果`, `#芯片`, `#美光`, `#特朗普`, `#供应链`

---