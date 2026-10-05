---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 24 条内容中筛选出 3 条重要资讯。

---

1. [Strata 让 125B 的 Qwen3.8-Flash-Next 在 RTX 4090 上跑到 124 tokens/秒](#item-1) ⭐️ 8.0/10
2. [为什么更多开发者不“使用平台”？](#item-2) ⭐️ 8.0/10
3. [ARC-AGI-3 的 Kaggle 最高分据称 30 天内从 7% 跃升至 56%](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Strata 让 125B 的 Qwen3.8-Flash-Next 在 RTX 4090 上跑到 124 tokens/秒](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

Hacker News 上的一则热帖介绍了 Strata —— 由 GitHub 用户 Niko1221 开发的开源推理运行时，它能让 125B 参数的 Qwen3.8-Flash-Next 模型在单张消费级 RTX 4090 上运行。一位评论者（snehesht）报告称，在 4090 搭配 128GB DDR5 内存和 Ryzen 7950X3D 的配置下达到 124 tokens/秒，与帖子宣称的 100+ tokens/秒一致。 在几千美元级别的硬件上（而非租用数据中心 GPU）运行 125B 参数的多模态 MoE 模型，大幅降低了本地化、隐私友好型大模型部署的门槛。同时，这也让一个持续争论升温：为了塞进消费级显存预算而进行激进量化，究竟要牺牲多少质量。 Strata 看起来是专门为 Qwen3.8-Flash-Next 调优的运行时，而不是通用推理引擎，其性能依赖于 KV-cache 管理、CUDA 限制以及 Windows 调度上的权衡。关键在于，一位评论者的 50 张图像视觉基准测试显示，Strata 的坐标中位误差为 154.8 像素，而完全相同的 GGUF 与视觉适配器权重在 llama.cpp 上运行仅为 46.5 像素，说明不同运行时之间存在明显的精度差异。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: Qwen3.8-Flash-Next 是阿里巴巴开源的权重多模态混合专家（MoE）模型，作为未来 Qwen4 架构的实验性预览版发布，因此其 125B 参数中每个 token 只会激活一小部分。量化技术把模型权重压缩为更低精度的格式（如 4-bit、3-bit），使得远超单张显卡显存容量的模型仍能加载，通常做法是从系统内存中流式读取权重。Strata 的卖点在于：其特有的量化与卸载方案让这种规模的模型能在单张消费级显卡上交互式使用，不过更低的位宽普遍被认为会带来质量下降。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md">Strata /docs/DETAILS.md at main · Niko1221/ Strata · GitHub</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/Qwen3.8-Flash-Next · Hugging Face</a></li>
<li><a href="https://www.digitalocean.com/community/tutorials/model-quantization-large-language-models">Understanding Model Quantization in Large Language ... | DigitalOcean</a></li>

</ul>
</details>

**社区讨论**: 社区情绪分歧明显：a11r 等怀疑者认为低于 4-bit 的量化会导致质量显著退化，jacquesm 则警告 Strata 链接正在各大 LLM 论坛被刷屏，热度未必能挺过蜜月期。另一方面，snehesht 和 AntiRush 给出了亮眼的实测数据（4090 上 124 tokens/秒；RTX 6000 Pro 上 Q4 量化解码 255 tokens/秒），但 Jackson__ 的测试显示 Strata 在相同权重下的视觉精度远落后于 llama.cpp，令基准测试的可信度受到质疑。

**标签**: `#LLM inference`, `#quantization`, `#consumer hardware`, `#Qwen`, `#model optimization`

---

<a id="item-2"></a>
## [为什么更多开发者不“使用平台”？](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/) ⭐️ 8.0/10

Nolan Lawson 探讨了为什么开发者常常选择框架而非原生 Web 平台 API，引发了一场关于 Web Components、React 和浏览器 API 可用性的详细社区讨论。

hackernews · vinhnx · 10月4日 04:10 · [社区讨论](https://news.ycombinator.com/item?id=49950554)

**标签**: `#web development`, `#web components`, `#React`, `#browser APIs`, `#Hacker News discussion`

---

<a id="item-3"></a>
## [ARC-AGI-3 的 Kaggle 最高分据称 30 天内从 7% 跃升至 56%](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

r/MachineLearning 上一篇帖子称，Kaggle 上 ARC-AGI-3 的最高分数在约 30 天内从约 7% 上升到 56%，这些成绩由能够在本地运行的小型模型配合评测 harness 取得。发帖人还注明所附排行榜截图已经有些过时。 ARC-AGI 系列基准专门设计用来抵抗记忆化、衡量人类占优的抽象推理能力，因此小型本地模型配合 harness 就能接近甚至超过普通人水平，会挑战人们对基准难度与模型规模关系的既有认知。这也说明脚手架与评测 harness 工程本身（而不只是模型原始能力）就能带来巨大分数提升，从而改变我们解读排行榜结果的方式。 由于 Kaggle 规则只允许参赛者使用可本地运行的小型模型，这一成绩并非来自前沿超大模型；分数的跃升可能部分源于评测 harness、提示与脚手架工程或测试时计算，而不完全是模型能力的质变。帖子所依据的只是发帖人承认已过时的排行榜截图，因此具体数值和提升幅度的可靠性仍需谨慎看待。

reddit · r/MachineLearning · /u/we_are_mammals · 10月4日 10:24 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**背景**: ARC-AGI（Abstraction and Reasoning Corpus for Artificial General Intelligence）是 François Chollet 提出的基准，其任务要求从少量示例中归纳出新颖的抽象规则，而不是依赖记忆。ARC-AGI-3 是其交互式版本，智能体需要探索全新环境、即时确立目标、构建可适应的世界模型并持续学习，100% 意味着智能体在每个游戏中都能以接近人类的效率完成。所谓 eval harness 是指端到端运行评测的基础设施，负责提示、工具调用、输出解析与打分；Kaggle 则是举办机器学习竞赛的平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://arcprize.org/arc-agi/2">ARC-AGI-2</a></li>
<li><a href="https://github.com/EleutherAI/lm-evaluation-harness">GitHub - EleutherAI/lm-evaluation-harness: A framework for ...</a></li>

</ul>
</details>

**标签**: `#ARC-AGI`, `#benchmarks`, `#reasoning`, `#LLM-evaluation`, `#Kaggle`

---