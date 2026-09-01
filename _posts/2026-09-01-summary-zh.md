---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> 从 44 条内容中筛选出 11 条重要资讯。

---

1. [Anthropic 发布 Claude Fable 5.1 和 Mythos 5.1，写作更优、缓存读取更便宜](#item-1) ⭐️ 9.0/10
2. [Google Play 禁止 AnkiDroid 链接到 Open Collective 捐赠页面](#item-2) ⭐️ 8.0/10
3. [Jujutsu 创造者 Martin von Zweigbergk 加入 ERSC](#item-3) ⭐️ 8.0/10
4. [小型 Transformer 仅训练 1.5 小时，在 ARC 基准上超越众多 LLM](#item-4) ⭐️ 8.0/10
5. [苹果在 OpenAI 诉讼中出示取证证据](#item-5) ⭐️ 8.0/10
6. [Python 3.15.0 候选版本 2 发布，进入 10 月正式版前的最后阶段](#item-6) ⭐️ 8.0/10
7. [Wrapture：用 monkeypatching 统一追踪与测试的新 Python 库](#item-7) ⭐️ 8.0/10
8. [韩国万亿主权 AI 投资：英伟达受益，SK 海力士受损](#item-8) ⭐️ 8.0/10
9. [2026 年潜在推理格局：BDH-CQ、HRM/TRM 与 Coconut](#item-9) ⭐️ 8.0/10
10. [EvoUndo：验证 LLM 智能体自我进化的可恢复性](#item-10) ⭐️ 8.0/10
11. [Virtualizor 更新设施遭 BGP 劫持，恶意更新植入 root 后门](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Fable 5.1 和 Mythos 5.1，写作更优、缓存读取更便宜](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

Anthropic 发布了 Claude Fable 5.1 和 Claude Mythos 5.1，这是 Claude 模型系列的最新成员。新模型在写作质量、更低的缓存读取价格以及科学推理能力方面均有提升。 此次发布通过将缓存读取价格降低 75%来削减推理成本，增强了 Anthropic 在大语言模型市场的竞争力，可能给其他厂商带来压力。这也表明 Anthropic 持续聚焦长时运行代理任务和科学领域，有望扩大在企业与科研场景中的应用。 降价主要来自缓存读取价格从每百万 token 1 美元降至 0.25 美元，使 Fable 5.1 的缓存读取成本仅为 Opus（0.5 美元）的一半。此次发布还包含三项破坏性变更，似乎是修复了无意间泄露思维链（chain-of-thought）的问题；随附的系统卡详细说明了安全评估情况。

hackernews · denysvitali · 9月1日 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49525378)

**背景**: Claude Mythos 是 Anthropic 最强大的大语言模型系列；Claude Fable 是公开发布的“Mythos 级”模型，带有额外安全防护，而 Mythos 本身仍为受限访问。据行业估计，Mythos 约有 8 万亿参数，Fable 5 约有 5 万亿参数。系统卡（system card）是一份结构化文档，披露 AI 系统的架构、防护措施和安全评估信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos</a></li>
<li><a href="https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1">What's new in Claude Fable 5.1 - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极。一位 Anthropic 内部人士称赞 Fable 5.1 的写作风格更自然、更听从指令，并预期科学领域会有进展。另一名用户指出，撇开 Terminal-Bench-Science 的结果，其他基准上的改进看似有限；还有人讨论了定价动态以及三项破坏性变更是为修复思维链泄露问题。

**标签**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#Model Release`

---

<a id="item-2"></a>
## [Google Play 禁止 AnkiDroid 链接到 Open Collective 捐赠页面](https://github.com/ankidroid/Anki-Android/issues/21656) ⭐️ 8.0/10

知名开源闪卡应用 AnkiDroid 报告称，Google Play 不再允许其链接到 Open Collective 捐赠页面。该政策执行在 GitHub issue 中被记录，引发了开发者与开源倡导者的讨论。 这一决定威胁到了这一广泛使用的开源项目的重要资金来源，体现了应用商店政策如何对独立软件的可持续性施加控制。同时，它也引发了人们对平台垄断及 FOSS 项目财务脆弱性的担忧。 Google Play 政策要求支付必须通过其计费系统进行，并声明对免税捐赠有例外。AnkiDroid 通过 Open Collective 获得的捐赠不可抵税，因为该项目归属于 Open Source Collective（一个 501(c)(6) 实体），而非 501(c)(3) 慈善机构，这可能是 Google 禁止外部链接的原因。

hackernews · hexa555 · 9月1日 10:11 · [社区讨论](https://news.ycombinator.com/item?id=49520022)

**背景**: AnkiDroid 是一款基于间隔重复学习系统 Anki 的开源 Android 闪卡应用，在 Google Play 上有数百万次下载。Open Collective 是一个众筹与财务管理平台，许多开源项目用它来收取和管理捐赠。Google Play 历来执行严格的支付政策，2019 年曾因 WireGuard VPN 应用链接到外部支付选项而将其临时下架——这一案例常被引用来说明 Google 对应用分发的控制力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open_Collective">Open Collective - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Android_app_stores">List of Android app stores</a></li>
<li><a href="https://github.com/ankidroid/Anki-Android">GitHub - ankidroid/Anki-Android: AnkiDroid: Anki flashcards on Android. Your secret trick to achieve superhuman information retention. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对 AnkiDroid 表示同情并批评 Google 的执法行为，还回忆了 2019 年 WireGuard 被下架等类似事件。一些人澄清了免税捐赠的细微差别：Open Source Collective 是 501(c)(6) 实体，捐赠不可抵税，这可能是 Google 采取行动的原因。还有人表达了对该应用的感谢，部分人表示将改用 Linux 手机以摆脱 Google 的控制。

**标签**: `#Android`, `#Open Source`, `#Google Play`, `#Donations`, `#App Store Policy`

---

<a id="item-3"></a>
## [Jujutsu 创造者 Martin von Zweigbergk 加入 ERSC](https://ersc.io/blog/martin-joins-ersc) ⭐️ 8.0/10

Jujutsu 版本控制系统的创造者 Martin von Zweigbergk 已加入 ERSC（East River Source Control）。该公司还宣布其存储产品将于本月晚些时候进入私人测试阶段。 这一事件标志着版本控制领域的一次重大动向，因为 Jujutsu 被视为极具前景的下一代兼容 git 的工具。ERSC 正将自己定位为 GitHub 的竞争对手，因此拥有这样一位关键开发者将可能影响代码托管和开发者工作流的未来。 von Zweigbergk 将继续以 Apache 2.0 许可证担任 jj 项目的核心维护者。ERSC Storage 将于本月晚些时候进入私人测试阶段，但该公司与 GitHub 的整体差异化优势仍在讨论之中。

hackernews · steveklabnik · 9月1日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=49525297)

**背景**: Jujutsu（jj）是一个用 Rust 编写的版本控制系统，可以与 git 仓库协同工作，提供撤销、自动 rebase 等特性以及更简单的命令集。ERSC（East River Source Control）是一家旨在构建与 GitHub 竞争的代码托管平台的公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ersc.io/blog/martin-joins-ersc">East River Source Control Names Jujutsu Creator Martin von... // ERSC</a></li>
<li><a href="https://github.com/jj-vcs/jj">jj-vcs/jj - Jujutsu—a version control system</a></li>

</ul>
</details>

**社区讨论**: 评论者对 jj 的用户体验和撤销功能持乐观态度，但一些人质疑 ERSC 相比 GitHub 的价值主张。有评论者指出，既然 jj 兼容 git，ERSC 需要证明自己如何解决 GitHub 的缺点，而不只是提供一个新方向盘。

**标签**: `#jujutsu`, `#version-control`, `#ersc`, `#developer-tools`, `#announcement`

---

<a id="item-4"></a>
## [小型 Transformer 仅训练 1.5 小时，在 ARC 基准上超越众多 LLM](https://mvakde.github.io/blog/44-on-arc-1/) ⭐️ 8.0/10

博客作者 M. Vakde 描述了一种从头训练的小型自回归 Transformer，仅用 1.5 小时就在 ARC 基准上取得了有竞争力的成绩，超过了众多更大的 LLM。作者强调这不是 LLM，并说明无需大规模扩展也能解决复杂推理任务。 这一成果挑战了 AI 领域传统的规模扩展假设，表明一个小型、专门训练的模型可以在关键推理基准上超越庞大的 LLM。这可能重新激发人们对小型模型、高效训练方法和新型架构的兴趣，而不是简单地增加算力。 该模型是一个从头训练的小型自回归 Transformer（并非 LLM），据称在 Kaggle 上达到了前五名的成绩。作者认为“在评估谜题上训练”不等于“在测试标签上训练”，因为 ARC 是一个元学习基准，允许从评估谜题中学习。

hackernews · porridgeraisin · 9月1日 09:52 · [社区讨论](https://news.ycombinator.com/item?id=49519939)

**背景**: ARC（抽象与推理语料库）基准由 François Chollet 提出，由基于网格的视觉谜题组成，旨在衡量通用智能而非简单的模式识别。以往在 ARC 上取得好成绩通常需要大规模 LLM 或具有巨大训练成本的复杂架构。这一结果表明，借助合适的架构和训练策略，小型 Transformer 也能取得有竞争力的成绩，可能使这一重要基准的研究变得更加普及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Abstraction_and_Reasoning_Corpus">Abstraction and Reasoning Corpus</a></li>
<li><a href="https://deepgram.com/learn/arc-llm-benchmark-guide">ARC Benchmark Guide for Evaluating LLMs | Deepgram</a></li>
<li><a href="https://arcprize.org/">ARC Prize</a></li>

</ul>
</details>

**社区讨论**: 在 Hacker News 的讨论中，作者（evilmathkid）澄清该模型不是 LLM，而是一个小型自回归 Transformer，引发了关于样本效率以及“在评估谜题上训练”是否算作弊的辩论。一些评论者称赞这一成果（如“听起来这是你美好的一天，Kaggle 前五”），另一些人则要求更简单的解释，并讨论该方法的有效性。总体情绪是好奇和基本支持，但也有人对方法论提出质疑。

**标签**: `#AI`, `#machine-learning`, `#transformers`, `#ARC-benchmark`, `#LLMs`

---

<a id="item-5"></a>
## [苹果在 OpenAI 诉讼中出示取证证据](https://9to5mac.com/2026/08/31/apple-openai-forensic-macbook-evidence/) ⭐️ 8.0/10

苹果在对 OpenAI 的诉讼中出示了取证证据，指控前员工刘先生下载了苹果保密的电路原理图，并在.OpenAI 的工作中使用了这些原理图。据称，证据包括通过 iCloud 同步的 MacBook 和 Mac mini 上的文件。 该案可能为以下问题开创先例：人工智能模型在训练中学习了商业秘密后，是否会造成该秘密“不可逆转且持续扩散的使用”。同时，它也引发了关于公司设备上云同步数据隐私的重要问题。 苹果发现刘先生使用该原理图，是因为他在一台 Mac mini 上使用过它，而该设备通过 iCloud 同步到了他从苹果带走的 MacBook 上；苹果目前要求获取这台 Mac mini。据称，刘先生得知苹果内部调查后，曾发送指示要求销毁证据，并且他在使用 LTspice 运行仿真时表示，自己的 AI“代理”学会了操作该工具。

hackernews · colinprince · 9月1日 20:19 · [社区讨论](https://news.ycombinator.com/item?id=49527573)

**背景**: 商业秘密法保护机密商业信息不被未经授权使用或披露。在人工智能时代，将商业秘密输入 AI 模型引发了新的法律问题：模型学到的知识是否构成盗用。此外，iCloud 同步可能模糊个人数据与公司数据的界限，因为一台设备上的文件可能会自动出现在另一台设备上。

**社区讨论**: 评论者对苹果的论点很感兴趣，即 AI 从商业秘密中学习可能导致不可逆的传播，并称这是一次影响深远的法律检验。其他人则对雇主访问同步到公司设备上的个人信息表示隐私担忧。一位评论者开玩笑说，希望出现一种“AI 洗白”的 MacBook Linux 驱动程序。

**标签**: `#Apple`, `#OpenAI`, `#trade-secrets`, `#privacy`, `#litigation`

---

<a id="item-6"></a>
## [Python 3.15.0 候选版本 2 发布，进入 10 月正式版前的最后阶段](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 8.0/10

发布经理 Hugo van Kemenade 宣布了 Python 3.15.0 候选版本 2 的发布，这标志着在 10 月稳定版发布前进入了最终的候选版本阶段。从现在开始，候选版与正式版之间只允许进行明确的 bug 修复。 这一公告表明 Python 3.15 已接近生产就绪，促使第三方维护者测试其项目并发布兼容的 wheel 包。这有助于确保更广泛的生态系统在新版本发布当天就做好准备。 该候选版本尚不可用于 GitHub Actions；维护者可以使用 allow-prereleases 和 check-latest 标志来自动测试最新的 RC，并最终测试稳定版。针对 3.15.0 候选版本构建的 wheel 包将与未来的 3.15 版本保持兼容。

rss · Simon Willison · 9月1日 14:59

**背景**: 候选版本（RC）是功能已完成的版本，在正式发布前只接受 bug 修复。Python 二进制 wheel 是预构建的分发包，无需编译即可安装，Python 打包用户指南指出 pip 和 uv 优先使用 wheel。RC 阶段是 Python 生态系统验证兼容性并准备 wheel 包的关键窗口，正如 Simon Willison 此前在正式版发布后才发现问题所展示的那样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://packaging.python.org/specifications/binary-distribution-format/">Binary distribution format - Python Packaging User Guide</a></li>
<li><a href="https://realpython.com/python-wheels/">What Are Python Wheels and Why Should You Care? – Real Python</a></li>
<li><a href="https://teamhub.com/blog/understanding-the-significance-of-release-candidate-in-software-development/">What is Release Candidate in Software Development ?</a></li>

</ul>
</details>

**标签**: `#Python`, `#Release Candidate`, `#Software Development`, `#Ecosystem`

---

<a id="item-7"></a>
## [Wrapture：用 monkeypatching 统一追踪与测试的新 Python 库](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 8.0/10

Graham Dumpleton 发布了 Wrapture，一个基于 wrapt 风格 monkeypatching 的 Python 库，将追踪与测试统一起来。它支持基于配置的 OpenTelemetry 追踪，并可作为 unittest.mock 的替代方案来实现行为覆盖。 它通过一套一致的 API 统一了可观测性与测试这两个常见开发工作流。相对于 unittest.mock，它为代码插桩提供了一种更透明的新替代方案；而且这个由资深维护者主导的 AI 辅助开发过程也颇具示范意义。 Wrapture 还很年轻——才发布几个星期——其全部代码和文档都是在 Graham 指导下由 AI 助手撰写的。它支持完全基于 TOML 配置的追踪接入方式，并提供了用于在测试中 stub 函数的 binding API。

rss · Simon Willison · 8月31日 23:59

**背景**: Monkeypatching 指的是在运行时动态修改或扩展代码。wrapt 是 Graham Dumpleton（他还以 mod_wsgi 和 New Relic 的 Python agent 闻名）开发的 Python 模块，提供透明对象代理，用于构建装饰器、包装器和 monkeypatching 工具。Wrapture 在这些思想之上，将其同时应用到追踪（通过 OpenTelemetry）和测试（作为 unittest.mock 的替代方案）中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/wrapt/">wrapt · PyPI</a></li>
<li><a href="https://github.com/GrahamDumpleton/wrapt">GitHub - GrahamDumpleton/wrapt: A Python module for decorators, wrappers and monkey patching. · GitHub</a></li>
<li><a href="https://stackoverflow.com/questions/5626193/what-is-monkey-patching">python - What is monkey patching? - Stack Overflow</a></li>

</ul>
</details>

**标签**: `#Python`, `#testing`, `#tracing`, `#monkeypatching`, `#wrapt`

---

<a id="item-8"></a>
## [韩国万亿主权 AI 投资：英伟达受益，SK 海力士受损](https://newsletter.semianalysis.com/p/koreas-trillion-dollar-sovereign) ⭐️ 8.0/10

韩国正投入数万亿美元发展主权 AI，并举办全国性 AI 竞赛以选拔本土基础模型。SemiAnalysis 分析认为，这一格局重塑利好英伟达，同时损害 SK 海力士，并给三星带来压力。 主权 AI 是全球趋势，各国都希望掌控自身 AI 基础设施、数据和模型。韩国的做法表明，政府主导的 AI 投资如何改变半导体巨头的竞争格局，而开源模型在其中扮演关键角色。 韩国科学技术信息通信部已选定 LG AI Research、SK Telecom、Upstage、Naver Cloud 和 NC AI 来构建本土基础模型。竞赛还引入公民评分，获胜者将为免费国家 AI 服务提供支撑。

rss · Semianalysis · 9月1日 20:14

**背景**: 主权 AI 指的是国家对其 AI 全栈（算力、数据、模型和人才）的掌控力，而非依赖外国供应商。韩国此举是全球大趋势的一部分，各国政府资助本国 AI 领军者以减少对美中技术的依赖。以竞赛形式选拔 AI 冠军颇为罕见，该过程向公民开放，并强调开源模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>
<li><a href="https://koreatechtoday.com/korea-picks-five-national-champions-to-lead-sovereign-ai-push/">Korea Picks Five National Champions to Lead Sovereign AI Push</a></li>
<li><a href="https://www.techtimes.com/articles/323429/20260806/korea-opens-citizen-lottery-pick-national-ai-champion-starting-friday.htm">Korea Opens Citizen Lottery To Pick National AI Champion ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Semiconductors`, `#Sovereign AI`, `#Nvidia`, `#Korea`

---

<a id="item-9"></a>
## [2026 年潜在推理格局：BDH-CQ、HRM/TRM 与 Coconut](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/) ⭐️ 8.0/10

一篇 Reddit 分析将潜在推理方法划分为至少五个家族，涵盖 Coconut、Soft Thinking、Abstract-CoT、循环深度模型、HRM/TRM 及 BDH-CQ。该分析认为，未来进展可能更依赖在连续隐藏状态中推理的架构，而非显式思维链。 这一综合分析指出，可能偏离可读思维链——而思维链是当前许多可解释性和评估工作的基础。效率与可追溯性之间的权衡可能影响未来大语言模型的架构与安全实践。 该帖子根据任务获取方式（上下文、记忆或梯度优化）以及中间计算发生的位置（语言标记、抽象标记或连续潜在状态）来区分潜在推理家族。它特别强调了基于 Dragon hatchling 架构的 BDH-CQ，该模型在 ARC-AGI-1 上报告了超越已发表成本-精度帕累托前沿的结果，并显示出高达 6000 亿参数的扩展律。

reddit · r/MachineLearning · /u/Typical-Scene-5794 · 9月1日 15:14

**背景**: 潜在推理是思维链（CoT）提示的一种替代方法，模型反复变换其连续隐藏状态，仅解码最终答案，而不用语言表达中间步骤。关键论文包括 Coconut（arXiv 2412.06769），它将最后一个隐藏状态作为下一个输入嵌入反馈；HRM/TRM（arXiv 2510.04871）则使用微小的递归网络进行推理。BDH-CQ（arXiv 2608.09888）将上下文学习与循环潜在推理相结合，使推理时的演示能够更新模型记忆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2608.09888">BDH-CQ: In-Context Learning with Recurrent Latent Reasoning | alphaXiv</a></li>
<li><a href="https://arxiv.org/abs/2412.06769">[2412.06769] Training Large Language Models to Reason in a Continuous Latent Space</a></li>
<li><a href="https://arxiv.org/pdf/2510.04871">Less is More: Recursive Reasoning with Tiny Networks</a></li>

</ul>
</details>

**标签**: `#latent reasoning`, `#chain-of-thought`, `#LLM architectures`, `#AGI research`, `#continual learning`

---

<a id="item-10"></a>
## [EvoUndo：验证 LLM 智能体自我进化的可恢复性](https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/) ⭐️ 8.0/10

EvoUndo 是一个新框架，用于表示、综合、诊断并独立验证 LLM 智能体自我修改的可恢复性。在跨越 600 个未见任务的测试中，它识别出 197 个未能通过可恢复性验证的能力提升型突变，而扩展恢复演算恢复了其中 191 个，而标准修复策略为 0 个。 这解决了 AI 安全中一个关键开放问题：如何让 LLM 智能体在不冒不可逆有害变化风险的情况下自我改进。通过协同设计验证、状态接地和恢复语言表达能力，EvoUndo 为更安全的自主智能体提供了一条路径。 该框架使用类型化效应系统来定义恢复语言，并通过“接地-表现力”干预来分离两个瓶颈。在 gpt-oss-120b 主干上，精确定址诊断将丰富语言下的恢复率降至 133/143，而 Qwen3.8-27B 复现保留了主要效应但未保留这种负交互，表明该现象依赖模型。

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · 9月1日 19:17

**背景**: LLM 智能体越来越多地在运行时修改自己的提示、工具、中间件、资源和执行框架以提升能力。然而，成功的突变可能留下持久影响，在与创建时不同的状态下无法安全逆转。可恢复性是指修改可以在没有副作用的情况下被撤销。EvoUndo 将该概念形式化，并提供了验证框架，协同设计了验证、状态接地和恢复语言表达性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28363">[2608.28363] EvoUndo: Recoverability-Constrained Self ...</a></li>
<li><a href="https://arxiv.org/pdf/2608.28363v1">EvoUndo: Recoverability-Constrained Self-Evolution for LLM ...</a></li>
<li><a href="https://huggingface.co/papers/2608.28363">Paper page - EvoUndo : Recoverability -Constrained Self-Evolution for...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#self-evolution`, `#recoverability`, `#AI safety`, `#machine learning`

---

<a id="item-11"></a>
## [Virtualizor 更新设施遭 BGP 劫持，恶意更新植入 root 后门](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 8.0/10

2026 年 8 月 28 日至 30 日，攻击者劫持了 Virtualizor 更新基础设施的 BGP 路由，并通过有效 TLS 证书投递了恶意更新包。官方确认仅少量在窗口期更新的系统被植入 root 后门，并强调这是分发链路被劫持，而非软件代码漏洞。 这是一起严重的供应链攻击：攻击者借助 BGP 劫持，用合法 TLS 证书对恶意更新进行签名，使其看起来完全可信。该事件还表明，不仅是代码漏洞，底层路由基础设施被劫持同样能让众多主机商使用的服务器管理平台被植入后门。 独立取证显示，恶意更新会写入 root SSH 密钥、安装 Java 载荷并建立持久化服务；AlbaHost 在 34 台 hypervisor 中发现 5 台存在被入侵指标。Softaculous 则表示目前没有证据表明其他产品受到影响。

telegram · zaihuapd · 9月1日 06:05

**背景**: BGP（边界网关协议）是互联网上在不同自治系统之间转发流量的路由协议；BGP 劫持是指攻击者篡改路由表并广播虚假路由，使原本发往合法 IP 前缀的流量被导向攻击者控制的基础设施。Virtualizor 是 Softaculous 开发的一款基于 Web 的 VPS 管理面板，其更新服务器是主机商用来安装补丁的可信端点。一旦这些路由被劫持，更新通道就可能被投毒，同时仍能出示有效 TLS 证书，使恶意版本与官方版本几乎无法区分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/virtualizor-compromise/">BGP Hijack Diverts Softaculous Traffic to Deliver Malicious Virtualizor ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/BGP_hijacking">BGP hijacking</a></li>
<li><a href="https://en.wikipedia.org/wiki/Softaculous">Softaculous</a></li>

</ul>
</details>

**标签**: `#BGP hijacking`, `#supply chain attack`, `#rootkit`, `#Virtualizor`, `#security`

---