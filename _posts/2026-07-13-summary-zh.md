---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> 从 19 条内容中筛选出 6 条重要资讯。

---

1. [Telegram 的 t.me 域名被暂停，引发猜测](#item-1) ⭐️ 8.0/10
2. [洛杉矶警局因隐私担忧终止 Flock 监控合同](#item-2) ⭐️ 8.0/10
3. [DOOMQL：完全由 SQLite 查询驱动的类《毁灭战士》游戏](#item-3) ⭐️ 8.0/10
4. [CoT 是缩放陷阱；潜在推理是下一波](#item-4) ⭐️ 8.0/10
5. [Reddit 辩论：什么是持续学习？](#item-5) ⭐️ 8.0/10
6. [开源工具按研究兴趣过滤 arXiv 论文](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Telegram 的 t.me 域名被暂停，引发猜测](https://www.whois.com/whois/t.me) ⭐️ 8.0/10

Telegram 用于短链接的 t.me 域名已被暂停，WHOIS 查询显示其状态代码已禁用。 这一中断影响了全球数百万 Telegram 用户，并引发了对该平台依赖 GoDaddy 作为注册商的担忧，后者有采取不透明域名操作的历史。 该域名的状态代码包括 clientRenewProhibited 和 serverDeleteProhibited，ICANN 文档表明这些代码通常在法律纠纷期间或删除待定时使用。

hackernews · Tiberium · 7月13日 19:52 · [社区讨论](https://news.ycombinator.com/item?id=48897878)

**背景**: Telegram 目前因各种指控在俄罗斯、法国和印度面临法律和监管调查。t.me 域名是 Telegram 用于分享内容的短链接。

**社区讨论**: 社区评论对 Telegram 使用以不透明著称的 GoDaddy 表示惊讶，并指出此次暂停可能与印度对考试作弊的调查有关。一位用户强调了使用重定向而非直接第三方域名链接的重要性。

**标签**: `#Telegram`, `#domain suspension`, `#ICANN`, `#GoDaddy`, `#regulatory investigation`

---

<a id="item-2"></a>
## [洛杉矶警局因隐私担忧终止 Flock 监控合同](https://techcrunch.com/2026/07/13/lapd-lets-contract-with-surveillance-giant-flock-expire-citing-serious-concerns-over-civil-liberties-and-privacy/) ⭐️ 8.0/10

洛杉矶警局以对公民自由和隐私的严重担忧为由，允许与 Flock Safety 的合同到期。然而，摄像头仍在运行并继续收集数据，Flock 可将这些数据出售给其他机构。 这一决定凸显了执法监控与公民自由之间的紧张关系，并揭示了一个漏洞：即使合同终止，私人监控基础设施依然存在。这凸显了监管向政府机构提供数据的私营公司数据收集的挑战。 Flock Safety 拥有摄像头和杆柱，因此即使没有 LAPD 合同，摄像头仍继续记录数据，并可出售给 CHP、LASB、FBI 和 Palantir 等其他实体。LAPD 也可能通过非正式途径访问数据，使合同到期在很大程度上流于形式。

hackernews · forks · 7月13日 15:11 · [社区讨论](https://news.ycombinator.com/item?id=48893947)

**背景**: Flock Safety 是一家专门提供自动车牌识别（ALPR）系统的监控公司，该系统捕获车牌数据、照片和位置信息。ALPR 技术被执法机构用于追踪车辆，但引发了关于大规模监控和隐私的担忧。LAPD 的决定反映了关于公共安全与隐私权平衡的更广泛争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.cnet.com/home/security/when-flock-comes-to-town-why-cities-are-axing-the-controversial-surveillance-technology/">When Flock Surveillance Comes to Your Town: Everything to Know ... - CNET</a></li>

</ul>
</details>

**社区讨论**: 评论者对合同终止的影响表示怀疑，指出 Flock 摄像头仍在运行，其他机构可获取数据。有用户指出尽管有监控，累犯率仍很高，质疑其有效性。另一人认为，政府购买其本身无法合法收集的数据应属非法。

**标签**: `#surveillance`, `#privacy`, `#civil liberties`, `#Flock`, `#LAPD`

---

<a id="item-3"></a>
## [DOOMQL：完全由 SQLite 查询驱动的类《毁灭战士》游戏](https://simonwillison.net/2026/Jul/13/doomql/#atom-everything) ⭐️ 8.0/10

Peter Gostev 发布了 DOOMQL，这是一个类《毁灭战士》的游戏，其中 SQLite 通过 SQL 查询处理所有游戏逻辑，包括移动、碰撞、敌人 AI 和渲染。该游戏作为 Python 终端脚本运行，并使用递归 CTE 在 SQLite 中实现了完整的光线追踪器。 该项目展示了 SQLite 作为完整游戏引擎的极其新颖的用途，拓展了数据库能力的边界。它激励软件工程师创造性地思考数据库在传统角色之外的用途，并展示了 SQL 进行复杂计算的能力。 该游戏作为 Python 终端脚本实现，可使用 `uv run host/doomql.py` 运行。它会创建一个 SQLite 数据库，可用 Datasette 进行探索，Simon Willison 使用 Datasette Apps 构建了一个带小地图的实时刷新网页界面。渲染通过一个巨大的 SQL 查询完成，该查询使用递归 CTE 实现了光线追踪。

rss · Simon Willison · 7月13日 22:34

**背景**: SQLite 是一种轻量级嵌入式 SQL 数据库引擎，广泛应用于应用程序的数据存储。递归 CTE（公用表表达式）允许 SQL 查询执行迭代计算，此处用于光线追踪。uv 工具是用 Rust 编写的超快 Python 包管理器，用于运行该项目。Datasette 是一个探索和发布 SQLite 数据库的工具，而 Datasette Apps 允许用户构建自定义的 HTML/JavaScript 应用来查询数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forum.openmw.org/viewtopic.php?t=7193">SQLite based approach to storing game world state - openmw.org</a></li>
<li><a href="https://github.com/astral-sh/uv">GitHub - astral-sh/uv: An extremely fast Python package and project manager, written in Rust. · GitHub</a></li>
<li><a href="https://medium.com/@dieggo.filipe/uv-the-new-python-package-manager-you-need-to-know-491a147af74c">UV: The New Python Package Manager You Need to Know! | by Diego Lima | Medium</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#game-development`, `#python`, `#novel-approach`, `#doom`

---

<a id="item-4"></a>
## [CoT 是缩放陷阱；潜在推理是下一波](https://www.reddit.com/r/MachineLearning/comments/1uviru5/chain_of_thought_is_a_scaling_trap_the_next_wave/) ⭐️ 8.0/10

一个 Reddit 帖子认为链式思维推理是一个昂贵的接口人工产物，而不是可扩展路径，并提出 LLM 推理的下一波将转向潜在空间，采用 Coconut、HRM 和 RecursiveMAS 等方法。 这一讨论突出了当前 LLM 推理的一个关键限制——自回归 token 生成效率低且不可信——并指向新兴的潜在推理方法，这些方法可以大幅降低成本和延迟，同时提高推理深度，但也引入了新的治理挑战。 帖子指出了 CoT 的两个实际问题：可信度和系统成本，然后调研了潜在推理方法：Coconut 使用连续潜在步骤，HRM 将规划与执行分离，RecursiveMAS 在代理之间传递潜在嵌入。BDH 旨在结合潜在迭代与有原则的状态管理，在数独上无需 CoT 即可达到 97.4%的准确率。

reddit · r/MachineLearning · /u/meowsterpieces · 7月13日 17:50

**背景**: 链式思维推理迫使 LLM 生成中间文本步骤，可解释但昂贵且可能不可信。潜在推理方法在连续向量空间中进行内部计算，无需生成 token，从而降低成本并允许更深层次的递归，但失去了对推理过程的直接可见性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ht0324.github.io/blog/2025/Coconut/">Continuous Latent Reasoning for LLMs ( COCONUT ) - Review</a></li>
<li><a href="https://github.com/sapientinc/HRM-Text">GitHub - sapientinc/HRM-Text: HRM-Text is a 1B text generation model based on the HRM architecture, strengthened by task completion and latent space reasoning. · GitHub</a></li>
<li><a href="https://recursivemas.github.io/">Recursive Multi-Agent Systems</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#LLM reasoning`, `#chain-of-thought`, `#latent reasoning`, `#AI research`

---

<a id="item-5"></a>
## [Reddit 辩论：什么是持续学习？](https://www.reddit.com/r/MachineLearning/comments/1uvm2p4/whats_your_take_on_continual_learning_d/) ⭐️ 8.0/10

Reddit 上的一场讨论质疑了持续学习的定义和重要性，引用了 Dario Amodei 关于 2026 年实现持续学习的预测和 Demis Hassabis 关于它是通往 AGI 最重要未突破难题的主张。 持续学习被广泛认为是通向 AGI 的关键瓶颈，但其定义仍存在争议，导致研究和行业混乱。澄清持续学习的真正要求可能会加速实现更通用 AI 的进展。 讨论指出持续学习经常与灾难性遗忘、在线学习、终身学习或元学习混淆，并质疑瓶颈是架构性的、数据相关的，还是评估和基准测试的根本问题。

reddit · r/MachineLearning · /u/watercolorer2024 · 7月13日 19:47

**背景**: 持续学习旨在使 AI 模型能够顺序学习而不遗忘先前知识，解决稳定性-可塑性困境。灾难性遗忘是指神经网络在学习新数据时迅速丢失旧信息，这是一大挑战。元学习，即“学会学习”，是一个相关但不同的概念，专注于优化学习过程本身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Catastrophic_forgetting">Catastrophic forgetting</a></li>
<li><a href="https://en.wikipedia.org/wiki/Meta-learning_(computer_science)">Meta-learning (computer science) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#continual learning`, `#AGI`, `#catastrophic forgetting`, `#AI research`, `#machine learning`

---

<a id="item-6"></a>
## [开源工具按研究兴趣过滤 arXiv 论文](https://www.reddit.com/r/MachineLearning/comments/1uvcdf7/hundreds_of_papers_hit_arxiv_every_day_and_maybe/) ⭐️ 8.0/10

一位开发者创建了 Research Radar，这是一个开源工具，能自动获取 arXiv 论文，根据用户自定义的研究兴趣进行评分，并将最相关的论文摘要整理成每日摘要。 该工具解决了研究人员信息过载的常见痛点，每天节省 30-60 分钟，仅呈现相关论文，且其领域无关的设计使其适用于机器学习、物理、生物等多个领域。 Research Radar 使用两阶段评分系统：一个廉价模型用于摘要浏览，一个强模型用于全文深度阅读，成本已在仓库中基准测试。它支持多种模型，包括 Claude、Codex 或通过 Ollama/vLLM 运行本地模型。

reddit · r/MachineLearning · /u/usedtobreath · 7月13日 13:59

**背景**: arXiv 是一个预印本仓库，每天有数千篇论文发布，研究人员很难跟上相关工作的最新进展。许多人使用 RSS 订阅或新闻通讯，但这些往往突出热门内容而非个性化内容。Research Radar 通过根据用户指定的兴趣对论文进行评分，自动完成过滤和摘要生成过程。

**标签**: `#arXiv`, `#research tool`, `#NLP`, `#open source`, `#machine learning`

---