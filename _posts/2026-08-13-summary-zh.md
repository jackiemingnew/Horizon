---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 32 条内容中筛选出 11 条重要资讯。

---

1. [“Spaghettifying DRAM”攻击：利用内存加扰解锁 CPU 隐藏区域](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Pro 0813 发布：开放权重并开放 API 访问](#item-2) ⭐️ 9.0/10
3. [DeepSeek-V4-Pro 正式版上线：强化 Agent 能力，API 实行峰谷定价](#item-3) ⭐️ 9.0/10
4. [Gemini 3.7 Flash](#item-4) ⭐️ 8.0/10
5. [Cerebras 与 OpenAI 发布 GPT-5.6 Sol Ultrafast，宣称提速 7 倍](#item-5) ⭐️ 8.0/10
6. [选择无聊的技术：创新代币的永恒论证](#item-6) ⭐️ 8.0/10
7. [DeepSeek 发布开源 Agent Harness 开发者预览版](#item-7) ⭐️ 8.0/10
8. [Worldproof 工具揭示像素指标常无法对世界模型排序](#item-8) ⭐️ 8.0/10
9. [DeepMind 发布手语转文字模型 SL2T，首发 Pixel 11](#item-9) ⭐️ 8.0/10
10. [DeepSeek 发布开源 Harness 与 V4-Pro-0813 权重](#item-10) ⭐️ 8.0/10
11. [OpenAI 预览 Ultrafast 模式，GPT-5.6 Sol 提速 14 倍](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [“Spaghettifying DRAM”攻击：利用内存加扰解锁 CPU 隐藏区域](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

安全研究员 Christopher Domas 发布了“Skitter Creek Bath Salts”工具，利用 AMD 的 DRAM 加扰机制构造地址别名，从而访问通常受保护的内存区域（如 SMRAM、PSP 私有内存和 C6 空闲状态区域）。该项目展示了一类名为“Spaghettifying DRAM”的新型 DRAM 攻击技术。 这项研究表明，原本用于防止物理探测的 DRAM 加扰机制可以被逆向工程，从而绕过 CPU 的安全屏障，可能暴露 AMD 系统上的可信内存区域。它给基于 AMD 硬件的平台（包括 Xbox 和 PlayStation 等游戏主机）带来了严重担忧，也降低了攻击者在获得内核级代码执行后的进一步利用门槛。 项目的 README 指出 AMD16h（约 2013 年的 Jaguar 架构）属于受影响家族，并提到 Zen 3 的内存控制器寄存器基地址不同，因此对新款 CPU 的支持情况尚不明确。该技术使用 z3 SMT 求解器逆向出 DRAM 加扰变换，将其变成一块“罗塞塔石碑”，用来生成能够绕过一致性内存视图中围栏和锁定的别名地址。

hackernews · matt_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**背景**: DRAM 加扰是现代内存控制器的一项特性，它在地址位到达物理 DRAM 之前对其进行置换或哈希处理，使通过探测物理线路来关联地址与数据的攻击变得更困难。知名硬件黑客 Christopher Domas 的这个项目表明，这种加扰变换可以被完整求解并被滥用为一种地址别名原语。名称“Spaghettification”源自天体物理学中的“面条化效应”，即在强引力场中物体会被拉伸成细长形状——这里用来比喻加扰后的地址空间相对于正常一致性内存视图发生了扭曲和折叠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking _everything_ on the CPU with DRAM scrambling · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spaghettification">Spaghettification - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Christopher Domas 即将在 Black Hat 上的演讲表示期待，不少人称赞他过去的逆向工程演讲非常出色。有人指出，虽然这种攻击需要 ring-0 权限，但一旦获得该权限，Xbox 和 PlayStation 等主机上的所有内容都可能暴露；还有人质疑具体哪些 CPU 世代受影响，并指出已确认的 AMD16h/Jaguar 是较老的架构，而 Zen 3 需要不同的地址计算方法。

**标签**: `#security`, `#DRAM`, `#exploit`, `#hardware`, `#research`

---

<a id="item-2"></a>
## [DeepSeek V4 Pro 0813 发布：开放权重并开放 API 访问](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 9.0/10

DeepSeek V4 Pro 0813 现已通过 OpenRouter 提供 API 访问，同时其开放权重已发布在 Hugging Face 上（1.7T 参数，893GB）。Simon Willison 注意到该模型在低、中、高推理等级下生成的图像差异非常明显。 此次发布延续了开放权重前沿模型的发展趋势，使尖端能力可以被自主部署和研究。作者观察到的推理等级差异也表明，推理强度不仅仅影响基准分数，还会实质性改变模型的行为表现。 开放权重为 893GB、1.7 万亿参数，发布在 Hugging Face 的 deepseek-ai/DeepSeek-V4-Pro-0813 仓库中。基准测试结果通过非官方渠道流传：一篇 Reddit 帖子被版主以“低质量”为由删除，随后又被转成 Hacker News 上的 ASCII 表格。

rss · Simon Willison · 8月12日 23:59

**背景**: DeepSeek 是一家中国 AI 实验室，以发布大型混合专家（MoE）语言模型而闻名，例如此前拥有 1.6T 总参数和 1M token 上下文窗口的 DeepSeek-V4-Pro。这类开放权重模型允许任何人将训练好的参数下载并运行在自己的硬件上，而 OpenRouter 则为众多此类模型提供了统一的 API 接入网关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro">DeepSeek V4 Pro - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: Simon Willison 的文章指出，基准测试信息并非官方发布，而是经由微信群流出、在 Reddit 被删除后又以 ASCII 表格形式出现在 Hacker News 上。这表明社区正在通过非正式渠道积极讨论和验证性能数据。

**标签**: `#DeepSeek`, `#LLM`, `#open-weights`, `#Hugging Face`, `#AI release`

---

<a id="item-3"></a>
## [DeepSeek-V4-Pro 正式版上线：强化 Agent 能力，API 实行峰谷定价](https://api-docs.deepseek.com/zh-cn/updates) ⭐️ 9.0/10

DeepSeek-V4-Pro 正式版已同步上线 APP、网页端和 API，调用方式不变，模型名为 deepseek-v4-pro。该版本增强了 Agent 能力，原生支持 Responses API 格式并适配 Codex，同时为 V4-Pro 和 V4-Flash 思考模式新增 low、high、max 三档。 这次更新让 DeepSeek 在采用新兴的 Responses API 标准并强化智能体工作流方面，更直接地与前沿 AI API 竞争。开发者现在可以用 DeepSeek 构建兼容 Codex 的智能体，而新的峰谷定价也可能让闲时调用大幅降价，影响 AI API 的定价方式。 新的 API 峰谷定价于 2026 年 8 月 17 日 0 时生效，闲时价格为高峰时段的一半。V4-Pro 和 V4-Flash 的思考模式新增 low、high、max 三档，并原生支持 Responses API 格式。

telegram · zaihuapd · 8月13日 11:12

**背景**: Responses API 是 OpenAI 推出的一种新的 API 原语，由 Chat Completions 演化而来，为开发者带来了持久推理、托管工具和智能体（Agent）能力。AI 智能体是半自主或全自主的系统，能够感知、推理并采取行动完成任务，并常与其他智能体或人类协作。峰谷定价类似电力峰谷电价，在非高峰时段收取更低费率，以平衡负载并降低成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/blog/responses-api">Why we built the Responses API | OpenAI Developers</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI`, `#LLM`, `#API`, `#Pricing`

---

<a id="item-4"></a>
## [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

谷歌推出 Gemini 3.7 Flash，这是一款高效的新型 AI 模型，具备强大的视觉到 HTML 转换能力，并采用入门级定价，引发了社区的广泛讨论。

hackernews · thisisauserid · 8月13日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**标签**: `#Gemini`, `#Google`, `#AI models`, `#LLM`, `#Machine learning`

---

<a id="item-5"></a>
## [Cerebras 与 OpenAI 发布 GPT-5.6 Sol Ultrafast，宣称提速 7 倍](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

Cerebras 与 OpenAI 联合发布了 GPT-5.6 Sol Ultrafast，这是一个由 Cerebras 硬件驱动的新 API 服务层级，模型运行速度最高提升 14 倍，每秒可输出多达 750 个 token。在前沿基准测试中，它号称在保持相近准确率的情况下比标准 Sol 快 7 倍，包括在 11 小时 11 分钟内答完全部 2,500 道 HLE 问题。 这一里程碑表明，专门的晶圆级硬件可以大幅加速最先进的 LLM 推理，有可能重塑企业级 AI 应用的成本与延迟权衡。此次合作也标志着 OpenAI 模型与 Cerebras 定制芯片的深度融合，可能加剧推理服务商之间的竞争。 Ultrafast 模式目前处于预览阶段，尚未公开定价，且部分性能对比基于内部数据，而非独立重跑 Artificial Analysis 测试套件。Cerebras 报告称在 GDP-Val 上实现了 5.6 倍的端到端加速且质量无损，并且比 Claude Fable 5 快 11 倍，比 Opus 4.8 的 Fast 模式快 5 倍。

hackernews · pr337h4m · 8月13日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**背景**: Cerebras 制造晶圆级处理器，例如 WSE-3，这是一款 5nm 芯片，拥有 4 万亿个晶体管和 90 万个 AI 优化核心，可以在单个芯片上容纳整个 LLM，避免多 GPU 系统的内存瓶颈。HLE（Humanity's Last Exam）和 GDP-Val 等前沿基准测试旨在评估模型在严苛推理和经济价值较高的工作任务上的表现。更快的推理速度会改变模型的使用方式，让每秒能生成更多 token，或在实际时限内实现迭代优化等技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者们态度谨慎但兴奋：多人指出 Cerebras 和 OpenAI 都没有明确表述 Ultrafast 在质量上完全等同于标准 Sol，而且没有定价信息可能意味着它相当昂贵。也有人认为速度本身就能改善推理，因为可以支持迭代与修正，并与其他模型如 Claude Fable 5 和 Opus 4.8 的吞吐量进行了有利对比。

**标签**: `#LLM inference`, `#Cerebras`, `#OpenAI`, `#GPT-5.6`, `#performance acceleration`

---

<a id="item-6"></a>
## [选择无聊的技术：创新代币的永恒论证](https://mcfunley.com/choose-boring-technology) ⭐️ 8.0/10

Dan McKinley 于 2015 年发表的《选择无聊的技术》一文在 Hacker News 上重新引发热议，其提出的“创新代币”框架再次受到关注。该文主张公司应默认使用无聊且成熟的技术，并将新颖的技术选择视为有限预算来分配。 “创新代币”概念为工程领导者提供了一种权衡新颖性与风险的具体方法，因而成为一种持久的决策启发式工具。即使在 AI 代理等新趋势下，它仍然适用，因为它帮助团队将创新投入产品价值，同时保持基础设施的可靠性。 该文章指出，每家公司大约拥有三个创新代币，每在新数据库、框架或范式上花费一个代币，就会减少可用于其他实验的代币数量。其核心思想是：应将创新投入到能让产品差异化的领域，而不是基础技术设施。

hackernews · tosh · 8月13日 17:48 · [社区讨论](https://news.ycombinator.com/item?id=49289512)

**背景**: 软件工程中的“无聊技术”理念鼓励使用成熟、可预测的工具，而非追逐新潮流，因为成熟工具能减少意外故障和维护负担。本文普及的“创新代币”比喻通过为非标准选择设定明确预算，使这一理念变得可操作。该框架在工程领导力讨论中被广泛引用，作为做出和沟通技术权衡的工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lessannoyingbusiness.com/post/innovation-tokens">Innovation Tokens - When to break from the status quo</a></li>
<li><a href="https://mattrickard.com/innovation-tokens">Innovation Tokens - Matt Rickard</a></li>
<li><a href="https://concepts.dsebastien.net/concept/innovation-tokens/">Innovation Tokens - Concepts</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论大多赞赏这篇文章的实用性，有用户称其为核心工程师思维，还有用户强调“创新代币”对解释技术权衡至关重要。但也有人提出异议：有评论者认为“创新代币”概念“武断”且“不够严谨”，工程师应基于需求、风险与收益本身来评估。另一位评论者则建议，在代理时代，团队应将所有创新代币花在代理层面，其余技术都保持“无聊”。

**标签**: `#software engineering`, `#technology strategy`, `#innovation tokens`, `#engineering culture`

---

<a id="item-7"></a>
## [DeepSeek 发布开源 Agent Harness 开发者预览版](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek 发布了 DeepSeek Harness（dsh）的开源开发者预览版，源代码已在 GitHub 上以 MIT 许可证公开。该框架具备可追踪的追加式会话日志，以及基于 Cordis 的热重载插件系统。 作为来自头部 AI 实验室的开源 agent 框架，它为开发者提供了对 agent 运行过程的完整可检查性以及模块化插件架构，这与美国闭源模型中加密或混淆追踪信息的做法形成对比。这可能推动社区驱动的 agent 工具链发展，并降低构建生产级 agent 的门槛。 该框架采用“一切皆插件”的架构，并支持在同一事件流上进行恢复、分叉、搜索和重放。当前为早期 MIT 许可的开发者预览版，预计会有粗糙之处和破坏性变更；系统基于 Cordis v4 实现插件的热加载/卸载及副作用回滚。

hackernews · bjin · 8月13日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49285244)

**背景**: Agent harness 是围绕大语言模型的软件基础设施，使模型能够作为 agent 运行，负责工具调用、记忆、状态持久化和执行环境管理。DeepSeek Harness 以开发者预览形式在 DeepSeek 官网和 GitHub 上发布，文档描述了其“一切皆插件”的设计以及轨迹（Trajectory）视图。其插件系统由 Cordis 驱动，支持在不重启进程的情况下热重载和动态启用/禁用组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>

</ul>
</details>

**社区讨论**: 讨论整体积极。有评论者指出，可追踪的追加式会话日志是“杀手级功能”，优于美国模型加密或混淆的追踪信息；论文作者回应称，该系统为插件体系增添了热重载和动态启用/禁用能力，甚至扩展到 UI 组件。另一位评论者认为 DeepSeek Harness 在设计上与 Pi Coding Agent 相似，也有人谨慎表示其对应论文“有用但并非颠覆性”。

**标签**: `#deepseek`, `#agent-harness`, `#open-source`, `#tracing`, `#plugins`

---

<a id="item-8"></a>
## [Worldproof 工具揭示像素指标常无法对世界模型排序](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/) ⭐️ 8.0/10

作者发布了开源工具 Worldproof，用于诊断世界模型，并发现 SSIM 和 PSNR 等像素指标在真实机器人 rollout 视频上通常无法对模型进行排序。在 SO-101 录制数据上，“复制最后一帧”基线获得 0.983 SSIM 和 53.9 dB PSNR，误差随预测步长保持平稳，导致所有模型得分相当。 这件事很重要，因为它揭示了世界模型评测中的一种隐藏失效模式：在真实机器人数据上，标准保真度指标可能完全没有区分度，使基准排名失去意义。它推动研究者在自己的数据上测量“可用预测窗口”，而不是照搬其他论文的默认设置。 该分析对每种配置使用 64 次 rollout，采用 Agarwal 等（2021）的四分位均值聚合和分层 bootstrap 置信区间，并使用动态区域掩码指标。在 DROID 视频上，可用预测窗口约为第 8 到 24 步；过短和过长的预测步长都会导致模型得分相等，而 LPIPS 的行为不一致，目前还没有明确解释。

reddit · r/MachineLearning · /u/georgia_bucea · 8月13日 19:58

**背景**: 世界模型（world model）是一种神经网络，给定初始上下文和一系列动作来预测未来视频帧，常用于基于模型的强化学习和机器人领域。PSNR、SSIM 等像素指标通过逐像素或亮度/对比度/结构比较图像，但当背景静止或运动较小时可能很不敏感。该帖发布在 r/MachineLearning，并附带开源代码；SO-101 是 Hugging Face LeRobot 项目的开源机械臂，DROID 是大型真实操作数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/TheRobotStudio/SO-ARM100">GitHub - TheRobotStudio/SO- ARM 100: Standard Open Arm 100</a></li>
<li><a href="https://ieeexplore.ieee.org/document/5596999/">Image Quality Metrics: PSNR vs. SSIM | IEEE Conference Publication | IEEE Xplore</a></li>

</ul>
</details>

**标签**: `#world models`, `#model evaluation`, `#robotics`, `#machine learning`, `#open source`

---

<a id="item-9"></a>
## [DeepMind 发布手语转文字模型 SL2T，首发 Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

DeepMind 发布了多语言手语转文字模型 SL2T，并首次将其落地到消费产品中——Pixel 11 的 Gboard 和 Live Transcribe 现已支持美国手语转英语，后续将扩展到更多设备和语言。 这是无障碍技术的一个重要里程碑，将手语 AI 从研究带入日常消费设备，有望帮助聋人及听障人士更便捷地交流，也为其他科技公司集成同类模型树立了先例。 该模型使用超过 10 万小时、50 多种手语的数据进行训练，在 FLEURS-ASL 基准上的零样本 BLEURT 得分达到 70。为保护隐私，它只处理手部和身体姿态关键点，而不读取原始视频。

telegram · zaihuapd · 8月13日 08:55

**背景**: 手语识别是一个具有挑战性的计算机视觉问题，因为手语依赖快速而复杂的手势和身体动作。FLEURS-ASL 是近期推出的基准，将多语言数据集 FLORES/FLEURS 扩展到美国手语；BLEURT 则是一种基于学习的评估指标，用于衡量生成文本与人类对流畅度和语义判断的吻合程度。DeepMind 通过使用姿态关键点而非完整视频，在降低隐私风险的同时保持较高的翻译质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2408.13585v1">FLEURS-ASL: Including American Sign Language in Massively ...</a></li>
<li><a href="https://github.com/google-research/bleurt">GitHub - google-research/bleurt: BLEURT is a metric for ...</a></li>
<li><a href="https://aclanthology.org/2025.naacl-long.314.pdf">FLEURS-ASL: Including American Sign Language in Massively ...</a></li>

</ul>
</details>

**标签**: `#sign language`, `#accessibility`, `#DeepMind`, `#AI model`, `#translation`

---

<a id="item-10"></a>
## [DeepSeek 发布开源 Harness 与 V4-Pro-0813 权重](https://mp.weixin.qq.com/s/mANdGRI4fO_sEbC1ECEoZQ) ⭐️ 8.0/10

DeepSeek 宣布以 MIT 协议开源发布 DeepSeek Harness，并在 Hugging Face 上开放 DeepSeek-V4-Pro-0813 权重。该 Harness 现已进入开发者预览阶段，并包含完整源代码。 此次发布提供了一个与模型无关、基于插件的智能体基础设施替代方案，可对标 Claude Code 和 Codex 背后的架构，有望降低 AI 智能体开发的门槛。这也表明 DeepSeek 持续推进核心工具和模型的开源，可能加速 AI/ML 社区的采用。 DeepSeek Harness 采用“一切皆插件”的架构，由 Cordis 驱动，并提供标准、PTC、极简和创造四种运行模式。PTC（编程式工具调用）模式允许模型生成单一程序来编排多个工具调用，从而减少来回通信。V4-Pro-0813 的 Hugging Face 页面曾短暂 404，随后已恢复。

telegram · zaihuapd · 8月13日 12:39

**背景**: 智能体 Harness 是一种框架，允许大语言模型智能体与工具交互，并管理会话、沙箱、存储和调度。DeepSeek Harness 被设计为与模型无关，开发者可以将每种能力作为可替换插件进行交换或重组。Cordis 是一个用于时空组合性的元框架，为这种插件架构提供支持。DeepSeek-V4-Pro-0813 是 DeepSeek 新发布的模型权重集，通过 Hugging Face 分发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness/tree/master">GitHub - deepseek-ai/deepseek-harness · GitHub</a></li>
<li><a href="https://venturebeat.com/technology/deepseek-harness-launches-as-open-source-rival-to-claude-code-alongside-v4-pro-on-api-with-higher-prices">DeepSeek Harness launches as open source rival to Claude Code ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI`, `#Open Source`, `#Model Release`, `#Harness`

---

<a id="item-11"></a>
## [OpenAI 预览 Ultrafast 模式，GPT-5.6 Sol 提速 14 倍](https://openai.com/index/previewing-ultrafast/) ⭐️ 8.0/10

OpenAI 预览了 Ultrafast——一种新的 API 服务层级，可让 GPT-5.6 Sol 的处理速度比标准模式快 14 倍，每秒最多输出 750 个 token。该服务由 Cerebras 提供支持，目前仅面向少数精选客户开放。 这大幅降低了 OpenAI 最强大模型的推理延迟，使其在故障响应、金融研究、客服和电商等对时间敏感的场景中更具实用性。同时，这也凸显了 Cerebras 等专用推理硬件在 AI 生态中日益重要的作用。 Ultrafast 预览版目前仅限少数精选客户使用，OpenAI 表示随着算力扩展会逐步扩大访问范围。尽管速度大幅提升，OpenAI 和 Cerebras 均表示输出质量不受任何影响。

telegram · zaihuapd · 8月13日 17:04

**背景**: Cerebras Systems 开发用于深度学习应用的半导体、超级计算机及相关软件，其中包括 AI 推理。该公司声称其硬件可提供比 NVIDIA GPU 快 15 倍的推理速度，例如以每秒 1500 多个 token 的速度运行 DeepSeek R1。Ultrafast 利用 Cerebras 的晶圆级引擎（Wafer Scale Engine）为 OpenAI 的 GPT-5.6 Sol 加速，这标志着领先 AI 实验室与专业推理硬件供应商之间的合作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT‑5.6 Sol at up to ... - OpenAI</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://www.ithinkdiff.com/openai-ultrafast-api-tier-gpt-5-6-sol-750-tokens-per-second/">OpenAI Previews Ultrafast Mode: GPT-5.6 Sol at 14x Speed</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#performance`, `#Cerebras`, `#ultrafast`

---