---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> 从 31 条内容中筛选出 4 条重要资讯。

---

1. [新 AI 击败人类顶级 Stratego 棋手，训练对局数减少约 34 倍](#item-1) ⭐️ 8.0/10
2. [Greg Kroah-Hartman 拆解 Anthropic Mythos 内核漏洞宣称](#item-2) ⭐️ 8.0/10
3. [Google Research 发布 Cogentic，用多智能体协调系统发现新数学证明](#item-3) ⭐️ 8.0/10
4. [Claude Code 新增基于 TypeScript 的 mods 自定义功能](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [新 AI 击败人类顶级 Stratego 棋手，训练对局数减少约 34 倍](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 8.0/10

一个新的 AI 系统击败了历史上最强的人类 Stratego（斯特拉特戈）棋手，攻克了这个长期抵抗强力 AI 的不完全信息博弈难题。该成果发表在《Nature》期刊（s41586-026-11036-y），并配有 arXiv 预印本（2511.07312）；据称该系统使用的训练对局数比 DeepMind 的 DeepNash 少约 34 倍。 不完全信息博弈是 AI 的艰难前沿：最优着法取决于玩家无法观察到的信息，因此经典的向前搜索方法会失效。而这次以极低的训练成本取得远强于以往的 Stratego 智能体，说明这类方法可能迁移到谈判、安全博弈等真实世界中信息不公开的战略场景。 Stratego 在 10×10 的棋盘上进行，每方 40 枚棋子，可能的初始布阵超过 10^33 种；双方都能看到对方棋子的位置，但在交战揭示之前并不知道它们是什么。由于一步棋的价值取决于隐藏信息，智能体无法依赖通常的“我这样走、对手就会那样走”的搜索方式；据报告，这项工作的关键突破是样本效率的大幅提升，而不仅仅是棋力更强。

hackernews · PaulHoule · 10月2日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49933740)

**背景**: Stratego 是一种类似国际象棋的两人策略桌面战争游戏，每方 40 枚棋子通过编号表示军官与士兵的等级，另有炸弹和军旗。它与扑克一样，是经典的不完全信息基准问题；在国际象棋和围棋等完全信息博弈中行之有效的技术（例如蒙特卡洛树搜索结合自我对弈）在此类游戏中往往失效。DeepMind 在 2022 年推出的 DeepNash 是此前机器在 Stratego 上的最高水平，但它需要极其庞大的自我对弈对局才能达到顶级人类水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stratego">Stratego - Wikipedia</a></li>
<li><a href="https://deepmind.google/blog/mastering-stratego-the-classic-game-of-imperfect-information/">Mastering Stratego , the classic game of imperfect information</a></li>
<li><a href="https://www.zmescience.com/science/ai-beats-humans-stratego/">This AI Finally Beat the Best Humans at One of the Last Board Games ...</a></li>

</ul>
</details>

**社区讨论**: 评论区总体热情高涨，许多人分享了童年玩 Stratego 的回忆——有人当年碾压身边所有人，也有人发现朋友的棋子被偷偷做了标记来作弊。最有价值的观点来自一位评论者，他认为样本效率的提升（对局数比 DeepNash 少约 34 倍）才是关键，因为在不完全信息博弈中，最优着法取决于你无法知道的信息，导致向前搜索根本无法进行；也有人打趣说自己本打算亲手做出第一个必胜机器人。

**标签**: `#AI`, `#game-playing`, `#imperfect-information`, `#reinforcement-learning`, `#research`

---

<a id="item-2"></a>
## [Greg Kroah-Hartman 拆解 Anthropic Mythos 内核漏洞宣称](https://www.youtube.com/watch?v=NnV_cWeoo5Q) ⭐️ 8.0/10

在 Kernel Recipes 2026 题为“Security in the LLM Age”的演讲中，Linux 内核稳定分支维护者 Greg Kroah-Hartman 逐条检视了 Anthropic 声称其 Mythos 模型发现 79 个 Linux 内核漏洞的说法，指出这份清单最终只相当于约一小时的真实内核开发工作量。他展示的分类显示：24 项完全没有细节、只有“某个东西崩溃了”，14 项根本不是漏洞，3 项数据是编造的，15 项在最新版本中已被修复（其中 11 项由其他开发者修复、4 项由 Anthropic 修复），真正需要修复的只有 20 项。 这场演讲来自内核开发领域最具公信力的人物之一，是对当下 AI 驱动的漏洞披露浪潮罕见的、有据可依的反驳，也直接冲击了“前沿模型危险到必须限制发布、同时又可作为安全突破来宣传”的叙事。它对内核维护者、安全工程师以及所有评估基于大模型的漏洞扫描方案的人都很重要，因为低质量或早已修复的报告会浪费稀缺的维护者时间，并扭曲公众对软件风险的认知。 在真正需要修复的 20 项中，Kroah-Hartman 指出有 7 项基于“恶意文件系统镜像”这一前提，另有 2 项需要攻击者已经具备注入数据的能力，也就是说许多发现在现实威胁模型中并不能远程利用。他还指出，该方法本质上是对内核开发者数十年已有补丁做模式匹配，再套用到其他地方以检查同一修复是否被普遍应用，而 Anthropic 并未向最初修复这些 CVE 的开发者致谢。

hackernews · usernomdeguerre · 10月2日 02:51 · [社区讨论](https://news.ycombinator.com/item?id=49929391)

**背景**: Greg Kroah-Hartman 是 Linux 内核 stable 与 longterm 稳定分支的维护者，也是贡献最多的内核开发者之一，因此他的评价分量很重。Kernel Recipes 是知名的年度 Linux 内核开发者会议，而 CVE 是被公开披露的安全漏洞的标准编号标识。Anthropic 的 Mythos 是被该公司称为过于危险、不宜公开释放的前沿模型，而它把“发现 79 个内核漏洞”作为其安全能力的证据来宣传，Kroah-Hartman 的演讲正是对此进行检视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://imiel.dev/blog/anthropic-mythos-disclosure-ledger-2026-teardown">1,611 Bugs Found, 27 Fixed: Anthropic 's Fire Hose... | Imiel Visser</a></li>
<li><a href="https://webdinavia.com/blog/anthropic-mythos-model">Anthropic 's Mythos Model Deemed Too Dangerous for Public</a></li>
<li><a href="https://vuldb.com/article/llm-generated-cve-descriptions-undermine-security-data-quality-and-trust">LLM Generated CVE Descriptions Undermine Security Data Quality...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者普遍赞赏 Kroah-Hartman 的坦率，不少人直接引用了幻灯片中的分类数据，并把整件事总结为“一小时的内核开发工作量”。反复出现的批评是：Anthropic 的做法是对此前内核开发者补丁的模式匹配，却没有引用最初修复这些 CVE 的人；评论者还认为，一边以安全为由宣称模型危险到不能公开发布，一边在真实安全产出上如此有限，这种反差十分刺眼。

**标签**: `#LLM security`, `#kernel development`, `#AI safety`, `#vulnerability disclosure`, `#open source`

---

<a id="item-3"></a>
## [Google Research 发布 Cogentic，用多智能体协调系统发现新数学证明](https://arxiv.org/abs/2609.40324v1) ⭐️ 8.0/10

Google Research 公布了 Cogentic，这是一套基于 Gemini 的多智能体自动证明发现系统，采用“证明—验证”循环：多个独立证明器分头探索不同方向，另设专门组件进行对抗式验证，被确认的结果则写入一个可持续复用的验证账本。据报道，该系统在在线学习、拍卖理论和机制设计三个领域的 5 个开放问题上产出了新结果，全部由领域专家独立验证，并在配套论文中展开论述。 如果属实，这意味着大模型不再只解决教科书或竞赛题目，而是开始在理论计算机科学的开放研究问题上贡献真正的新结果；它也暗示“多智能体编排＋对抗式验证”可能成为可信 AI 辅助研究的标准架构。其影响最大的是理论计算机科学、机器学习理论以及 AI for Mathematics 领域的研究者——在这一领域，瓶颈早已不是生成候选论证，而是可靠地检验它们。 一个关键设计是反馈闭环：通过验证的引理会被提升进一个持久化账本，而失败的尝试以及验证器的批评意见会写入后续的任务简报，使进展可以跨轮次累积。据报道，该系统仅从问题陈述出发、不需要专家提示，并且还把推理效率作为优化目标。不过这条消息来自一条简短的电报式帖子，没有任何讨论，且 arXiv 编号（2609.40324）看起来不太寻常，因此在读到论文原文之前，这些结论应视为未经验证。

telegram · zaihuapd · 10月2日 12:04

**背景**: 自动定理证明传统上依赖 Coq、Lean 这类交互式证明助手，每一步都要经过机器检查。近年来的大模型工作把语言模型与这类检查器结合起来，但成功案例多集中在已知问题或对已有证明的形式化上，而非开放问题。Cogentic 属于较新的多智能体路线：不是让一个模型给出答案，而是并行运行多个智能体，额外加入一个专门“找错”、以推翻结论为目标的对抗式验证器，并维护一份记录“已成立／未成立”的账本。文中提到的在线学习、拍卖理论与机制设计，都属于理论计算机科学领域，那里的一条新定理通常意味着数月的人类研究投入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.40324">Cogentic: Multi - Agent Orchestration for Automated Proof Discovery</a></li>
<li><a href="https://agihunt.info/en/e/1a0f9cea5c8b68af181e13c5f80">Google 's Cogentic Multi - Agent System Tackles… · AGI Hunt</a></li>
<li><a href="https://academy.dair.ai/papers/cogentic-multi-agent-orchestration-for-automated-proof-discovery-2609.40324?ref=symbolika.ai">Cogentic: Multi-Agent Orchestration for Automated Proof Discovery</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#AI for mathematics`, `#theorem proving`, `#Google Research`, `#Gemini`

---

<a id="item-4"></a>
## [Claude Code 新增基于 TypeScript 的 mods 自定义功能](https://claude.com/blog/claude-code-mods) ⭐️ 8.0/10

Anthropic 为 Claude Code 推出了 mods 功能：开发者只需编写少量 TypeScript 代码，就能改写提示词、新增界面元素或替换内置功能。Mods 随插件一起分发，目前已支持 CLI 和桌面版，部分内置功能已改为以 mods 形式实现，官方还计划继续迁移更多功能。 对于目前使用最广泛的 AI 编程工具之一来说，这是一次重要的可扩展性里程碑：原本写死的内置功能变成了用户可替换的插件，团队因此能够按自己的工作流定制 agent 的行为。这也说明“一切皆插件”的架构正在成为各家 agent harness 的竞争常态，DeepSeek Harness 的类似设计就是一例。 Mods 与 Claude Code 拥有相同权限，且没有沙箱隔离，因此官方明确提醒用户只安装来自可信来源的 mods；用户也可以直接让 Claude 自己编写 mods。由于 mods 能够替换内置功能，安装来源不可信的 mods 实际上就等于赋予了它与工具本身同等的信任级别。

telegram · zaihuapd · 10月2日 12:32

**背景**: Claude Code 是 Anthropic 推出的 agent 式命令行编程工具，可以读取和修改文件、执行命令并在开发者本机上完成编程任务。像 mods 这样的扩展层让第三方和用户无需等待 Anthropic 发布新版本，就能改变 agent 的默认行为。DeepSeek 开源的 agent harness——DeepSeek Harness 正是基于类似的“一切皆插件”架构构建的，因此其团队才会把两种设计相提并论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://www.deepseek.com/en/harness/">DeepSeek Harness | Explore the limits of intelligence</a></li>
<li><a href="https://deepseekharness.dev/">DeepSeek Harness - AI Agent Framework Installation & Usage Guide</a></li>

</ul>
</details>

**社区讨论**: 功能发布后，DeepSeek Harness 团队负责人崔添翼在 X 上引用 Anthropic 员工的帖子表示祝贺，并阐释了该功能与 DeepSeek Harness“一切皆插件”设计的相似性。社区反应整体正面，有群友调侃说“好的设计心有灵犀”。

**标签**: `#AI coding tools`, `#Claude Code`, `#Anthropic`, `#extensibility`, `#developer tools`

---