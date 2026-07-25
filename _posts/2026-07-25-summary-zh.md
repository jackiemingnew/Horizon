---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> 从 25 条内容中筛选出 9 条重要资讯。

---

1. [vLLM v0.26.0 发布：支持 Inkling 模型并优化 DeepSeek-V4 性能](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5，价格仅为 Fable 5 的一半](#item-2) ⭐️ 9.0/10
3. [SGLang v0.5.16：引入 DSPark 解码和 Inkling 支持](#item-3) ⭐️ 8.0/10
4. [Android 可能限制设备端 ADB 使用](#item-4) ⭐️ 8.0/10
5. [开放权重 AI 迎来 Kubernetes 式崛起](#item-5) ⭐️ 8.0/10
6. [Opus 5 是 Anthropic 最抗提示注入的模型](#item-6) ⭐️ 8.0/10
7. [AMD 能否打破 NVIDIA 的 CUDA 护城河？Advancing AI 2026](#item-7) ⭐️ 8.0/10
8. [中国对离岸信托财产装入及收益征税新规](#item-8) ⭐️ 8.0/10
9. [苹果游说特朗普使用中国存储芯片，美光反对](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布：支持 Inkling 模型并优化 DeepSeek-V4 性能](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 9.0/10

vLLM v0.26.0 引入了对 Inkling 模型家族（975B 参数，41B 活跃参数）的全面支持，跨厂商的 DeepSeek-V4 性能显著提升（端到端 TPOT 提升最高达 2.94%），以及按 KV-cache 组灵活选择注意力后端的功能。 此版本增强了对 DeepSeek-V4 和 Inkling 等前沿模型的推理效率，使大规模部署更加实用。灵活的注意力后端和改进的推测解码降低了延迟并拓宽了硬件支持。 该版本包含来自 212 位贡献者的 411 次提交，功能包括 Inkling 的分段 CUDA 图支持、Hopper FA4 相对注意力、MTP=1 推测解码，以及生成模型的 fp32 lm_head。Rust 前端现支持多模态视频和音频。

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个用于大语言模型的高吞吐、内存高效的推理引擎。此版本增加了对 Inkling 模型的支持，这是一个拥有 975B 总参数和 1M token 上下文窗口的混合专家 Transformer，并通过专门的内核和编译器优化在 NVIDIA、AMD 和 Intel 硬件上提升了 DeepSeek-V4 的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://www.spheron.network/blog/flashattention-4-blackwell-gpu-cloud-guide/">FlashAttention-4 on GPU Cloud: Blackwell Inference... | Spheron Blog</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#DeepSeek`, `#GPU kernels`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5，价格仅为 Fable 5 的一半](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5，这款新型前沿 AI 模型的智能水平与 Claude Fable 5 相当，但价格仅为后者的一半，目前已在 Artificial Analysis 排行榜上领先。 此次发布通过大幅降低成本，使前沿 AI 能力更加易得，可能扩大开发者和企业的采用。同时也加剧了 AI 模型市场的竞争，推动其他提供商提升性价比。 Claude Opus 5 的定价与 Opus 4.8 相同，并提供了成本翻倍的“快速模式”。它在发现网络安全漏洞方面有所改进，但与其前代一样，故意未接受利用漏洞的训练。

rss · Simon Willison · 7月24日 23:48

**背景**: Anthropic 的 Claude 模型家族包含多个层级，其中'Mythos'系列最为强大。Claude Fable 5 是公开发布的 Mythos 级模型，而 Claude Mythos 5 则是受限版本。Artificial Analysis 排行榜根据综合得分对 AI 模型进行排名。“快速模式”是一种推理加速功能，使用相同的模型权重，但通过优化后端配置来加快令牌输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://llm-stats.com/benchmarks/artificial-analysis">Artificial Analysis Leaderboard - llm-stats.com</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/fast-mode">Fast mode (research preview) - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: AI 社区对 Claude Opus 5 反应积极，早期基准测试结果显示它在排行榜上领先。一些开发者赞赏其降低的成本，而另一些则对该模型改进的漏洞发现能力表示谨慎。

**标签**: `#Claude`, `#Anthropic`, `#LLM`, `#AI model`, `#release`

---

<a id="item-3"></a>
## [SGLang v0.5.16：引入 DSPark 解码和 Inkling 支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 8.0/10

SGLang v0.5.16 引入了基于置信度的投机解码方法 DSPark，在 DeepSeek-V4-Pro 上达到 383.7 tok/s，并新增了对 Inkling（一个 9750 亿参数的多模态 MoE 模型）的支持。 这些进展显著提升了 LLM 推理效率和能力，实现了更快的 token 生成并支持大型开放权重多模态模型，惠及 AI 部署领域的研究者和实践者。 DSPark 采用半自回归分块草稿，根据草稿模型的置信度动态调整验证长度；Inkling 则融合了多种注意力机制、NVFP4 MoE 和 100 万 token 的上下文窗口。

github · Qiaolin-Yu · 7月25日 00:13

**背景**: 投机解码通过使用较小的草稿模型并行提出 token，再由较大的目标模型验证，从而加速 LLM 推理。DSPark 基于置信度自适应调整验证窗口大小，进一步优化了这一过程。Inkling 是 Thinking Machines Lab 最近发布的一个开放权重多模态 MoE 模型，总参数量 9750 亿，活跃参数量 410 亿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark: Confidence-Scheduled Speculative ...</a></li>
<li><a href="https://www.lmsys.org/blog/2026-07-06-dspark-sglang">DSpark in SGLang: Speculative Decoding with Confidence-Driven ...</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#speculative decoding`, `#LLM inference`, `#MoE`, `#multimodal`, `#open source`

---

<a id="item-4"></a>
## [Android 可能限制设备端 ADB 使用](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/) ⭐️ 8.0/10

Android 正在考虑一项变更，将限制设备端 ADB（Android 调试桥）的使用，要求无线连接必须授权到特定 IP 地址。 这一变更将影响依赖无线 ADB 进行调试的开发者，可能提高安全性，但也降低了便利性，并引发了对谷歌控制开发者工具的担忧。 提议的限制将阻止来自未知 IP 地址的 ADB 连接，除非用户明确授权。该讨论仍处于 Android 工程团队的早期阶段。

hackernews · shscs911 · 7月25日 06:57 · [社区讨论](https://news.ycombinator.com/item?id=49045159)

**背景**: ADB（Android 调试桥）是一种命令行工具，允许开发者与 Android 设备通信，用于调试、安装应用和运行 shell 命令。它可以通过 USB 或无线（TCP/IP）方式运行。设备端 ADB 常被开发者用于便利，但若在不受信任的网络中保持开放，可能带来安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Android_Debug_Bridge">Android Debug Bridge - Wikipedia</a></li>
<li><a href="https://developer.android.com/tools/adb">Android Debug Bridge (adb) | Android Studio | Android Developers</a></li>
<li><a href="https://www.howtogeek.com/125769/how-to-install-and-use-abd-the-android-debug-bridge-utility/">How to Install and Use ADB, the Android Debug Bridge Utility</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：有人认为安全收益甚微，因为攻击需要启用开发者选项和远程 ADB；另一些人则认为这是进一步限制开发者能力的步骤。一些人建议像 IP 白名单这样的替代方案更平衡。

**标签**: `#Android`, `#ADB`, `#Security`, `#Developer Tools`, `#Privacy`

---

<a id="item-5"></a>
## [开放权重 AI 迎来 Kubernetes 式崛起](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

这篇文章指出，开放权重 AI 模型将效仿 Kubernetes 成为行业标准，尽管最初存在专有替代方案。 这一类比意义重大，因为它表明一个开放、可定制的人工智能平台可能成为核心，超越任何单一供应商的创新速度，从而重塑 AI 行业的竞争格局。 文章指出，正如 Kubernetes 促进了容器的广泛采用，DeepSeek 和 Qwen 等开放权重模型正在挑战专有模型，但由于权重只是数字，技术上无法按来源禁止模型。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: 开放权重 AI 模型是指将训练后的模型权重公开发布，允许任何人下载、运行和微调。这与 GPT-4 等封闭权重模型（仅通过 API 访问）形成对比。Kubernetes 是一个开源容器编排系统，尽管曾与 Docker Swarm 和 Mesos 竞争，最终成为事实标准。文章认为开放权重 AI 将走类似的道路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/open-models/">Open models by OpenAI</a></li>
<li><a href="https://www.gumloop.com/blog/open-weight-ai-models">7 best open weight AI models I've tested in 2026 - gumloop.com</a></li>

</ul>
</details>

**社区讨论**: 社区评论包括对禁止中国模型可行性的怀疑，对'核心引力'观点的赞赏，对代币经济学的困惑，以及对 OpenAI 过去开源发布的赞赏。还有建议指出，要实现真正的 Kubernetes 式地位，需要公开训练数据和协作开发。

**标签**: `#open-weight`, `#AI`, `#Kubernetes`, `#model licensing`, `#AI industry`

---

<a id="item-6"></a>
## [Opus 5 是 Anthropic 最抗提示注入的模型](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

Anthropic 的 Boris Cherny 表示，根据系统卡评估和红队演练，Opus 5 是迄今为止他们最不易受到提示注入的模型。 提示注入是大语言模型的一个关键安全漏洞，更强的抵抗能力直接提升了 AI 的安全性和可信度。这一进展可能影响行业对模型安全的标准。 这一说法得到了 Claude Opus 5 系统卡（第 73 页）的支持，其中包含了提示注入评估和对抗性红队测试结果。该模型被描述为“很难成功进行提示注入”。

rss · Simon Willison · 7月25日 00:42

**背景**: 提示注入是一种安全攻击，恶意输入会覆盖模型的预期指令，导致意外行为。系统卡是透明度文档，详细说明 AI 系统的能力、局限性和安全评估。红队演练是通过对抗性测试来发现漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.linkedin.com/pulse/system-cards-foundation-ai-transparency-sandy-dunn-uf1uc">System Cards : Foundation of AI Transparency</a></li>
<li><a href="https://en.wikipedia.org/wiki/Red_teaming">Red teaming</a></li>

</ul>
</details>

**标签**: `#prompt-injection`, `#anthropic`, `#claude`, `#generative-ai`, `#ai`

---

<a id="item-7"></a>
## [AMD 能否打破 NVIDIA 的 CUDA 护城河？Advancing AI 2026](https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing) ⭐️ 8.0/10

在 AMD 的 Advancing AI 2026 活动上，该公司公布了挑战 NVIDIA CUDA 主导地位的新举措，包括智能内核生成方法和搭载 Instinct MI455X GPU 的 Helios 机架级架构。 如果成功，AMD 的软件改进和硬件进步可能会显著削弱 NVIDIA 的软件生态系统护城河，从而可能重塑 AI 硬件格局，为客户提供更具竞争力的选择。 Instinct MI455X 配备 432GB HBM4 内存，采用 2nm 制程，峰值 MXFP8 和 MXFP4 性能可达 MI355X 的 4 倍。然而，内部开发集群仍不稳定，生产爬坡被描述为“地狱”，财务工程提供高达 105%的折扣。

rss · Semianalysis · 7月25日 00:33

**背景**: CUDA 是 NVIDIA 专有的并行计算平台，已成为 AI 工作负载的主导软件生态系统。AMD 长期以来一直难以提供有竞争力的替代方案。智能内核生成是指利用大型语言模型（LLM）自动合成和优化 GPU 内核，可能减少对手动调优 CUDA 代码的需求。Helios 机架级架构集成了 72 个 MI455X GPU、AMD EPYC CPU 和 UALink 网络，类似于 NVIDIA 的 NVL72 设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/AMD-Instinct-MI455X-Helios">AMD Launches Instinct MI455X, Helios AI Rack - Phoronix</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center">AMD takes the wraps off its Instinct MI455X AI accelerator — CDNA 5 and Helios rack-scale architecture combine to take the fight to Nvidia in the data center | Tom's Hardware</a></li>
<li><a href="https://arxiv.org/abs/2602.24286">[2602.24286] CUDA Agent: Large-Scale Agentic RL for High ... [2607.04395] NKI-Agent: Domain-Specific Fine-Tuning and ... qhy991/Awesome-LLM-Kernel-Agent - GitHub Awesome LLM-Driven Kernel Generation - GitHub KernelAgent: Hardware-Guided GPU Kernel Optimization via ... Agentic Kernel Generation - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#AMD`, `#CUDA`, `#AI hardware`, `#software ecosystem`, `#GPU competition`

---

<a id="item-8"></a>
## [中国对离岸信托财产装入及收益征税新规](https://liaoning.chinatax.gov.cn/art/2026/7/24/art_5869_7823.html) ⭐️ 8.0/10

2026 年 7 月 24 日，中国财政部和税务总局发布 2026 年第 21 号公告，要求居民个人将财产装入离岸信托时需申报纳税，信托存续期间产生的收益无论是否分配均须按年申报。 该规定封堵了高净值个人此前利用离岸信托递延或逃避税收的空间，对跨境财富管理和遗产规划产生重大影响。 税率统一为 20%，仅对增值部分（市场价值减去原值和合理费用）征税，涵盖装入、运营和清算各阶段。2023 年至 2025 年期间应缴未缴的税款可在 90 天内补缴且不加收滞纳金。

telegram · zaihuapd · 7月25日 00:31

**背景**: 离岸信托是在离岸金融中心法律下设立的信托，常被用于资产保护和税务筹划。此前中国居民通过将财产装入离岸信托并延迟分配，可暂免纳税；新规采用“穿透式”征税，即无论收益是否分配，委托人每年均需缴税。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/境外信託">境外信托 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/离岸信托/2652314">离岸信托_百度百科</a></li>
<li><a href="https://baike.baidu.com/item/财产转让所得/309814">财产转让所得_百度百科 财产转让所得个人所得税 - ailegal.baidu.com 个人所得税财产转让所得税务处理全解析 从政策解读到实操案例帮你规避... 财产转让所得应纳税额的计算_25年注会税法学习要点 个人所得税|“财产转让所得”所涉个人所得税的处理 财产转让所得交多少个税，就看这三点 - 知乎</a></li>

</ul>
</details>

**标签**: `#税务`, `#离岸信托`, `#个人所得税`, `#政策法规`, `#财富管理`

---

<a id="item-9"></a>
## [苹果游说特朗普使用中国存储芯片，美光反对](https://www.wsj.com/tech/trump-apple-micron-china-chips-784bbd3d) ⭐️ 8.0/10

苹果正游说特朗普政府，允许在海外市场销售的产品中使用中国长鑫存储和长江存储的存储芯片，而美光科技则强力阻挠。 这反映了美国两大科技巨头在供应链战略和对华关系上的重大商业与政治交锋，对全球半导体贸易具有重要影响。 近几周，苹果 CEO 库克及多名高管已向特朗普、商务部长卢特尼克和财政部长贝森特推销该方案，计划采购长鑫存储（DRAM）和长江存储（NAND 闪存）的芯片。

telegram · zaihuapd · 7月25日 04:02

**背景**: 长鑫存储（CXMT）是中国 DRAM 制造商，长江存储（YMTC）则生产 NAND 闪存。两家公司均受美国制裁，长江存储于 2022 年被列入实体清单。苹果希望采用更便宜的中国芯片以缓解成本压力，但其主要供应商美光科技出于竞争和国家安全考虑表示反对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/長江存儲">长江存储 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/长江存储科技有限责任公司/20002721">长江存储科技有限责任公司_百度百科 追赶三星、海力士！继长鑫后，长江存储宣布IPO，估值或破万亿！湖北国... 长江存储 - 维基百科，自由的百科全书 企业简介-长江存储 - YMTC 长江存储 IPO 启幕！千亿存储航母启航，五大梯队 A 股受益全梳理 2026... 又一“巨无霸”！长江存储宣布IPO _ 东方财富网</a></li>
<li><a href="https://www.jiuyangongshe.com/a/2z5j06y178w">长 鑫 存 储 上市催化！ 手握 长 期订单的10大 存 储 产业链核心标的梳理</a></li>

</ul>
</details>

**标签**: `#苹果`, `#芯片`, `#美光`, `#特朗普`, `#供应链`

---