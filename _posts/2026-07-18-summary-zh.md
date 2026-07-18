---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 38 条内容中筛选出 13 条重要资讯。

---

1. [GPT-5.6 解决凸优化三十年未解猜想](#item-1) ⭐️ 9.0/10
2. [LG 显示器通过 Windows Update 静默安装软件](#item-2) ⭐️ 9.0/10
3. [Kimi K3 达到前沿 AI 水平，引发蒸馏争议](#item-3) ⭐️ 9.0/10
4. [台积电 A14 制程超预期：良率与性能逼近 90%](#item-4) ⭐️ 9.0/10
5. [回归式 JPEG 利用网络延迟实现播放](#item-5) ⭐️ 8.0/10
6. [Stack Overflow 衰退图引发关于 AI 与政策的辩论](#item-6) ⭐️ 8.0/10
7. [再见，自行车棚：可逆决策与 MD5crypt](#item-7) ⭐️ 8.0/10
8. [明目张胆的 AI 垃圾竟赢得 DeepMind Kaggle 大奖？](#item-8) ⭐️ 8.0/10
9. [豆包手机放弃 GUI 自动化，转向 MCP 协议集成 AI](#item-9) ⭐️ 8.0/10
10. [Meta 拟向 Anthropic 出租 AI 算力，潜在交易额 100 亿美元](#item-10) ⭐️ 8.0/10
11. [SpaceX 与五角大楼谈判提供数十亿美元 AI 算力](#item-11) ⭐️ 8.0/10
12. [特朗普政府拟设类似 FINRA 的 AI 审查机构](#item-12) ⭐️ 8.0/10
13. [旧金山责令苹果谷歌下架 AI“脱衣”应用](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-5.6 解决凸优化三十年未解猜想](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 9.0/10

据报道，GPT-5.6 的 Sol 版本通过一次提示，解决了凸优化中一个长期未解决的猜想，涉及 oracle 复杂度问题。 这表明大型语言模型能够为高级数学做出实质性贡献，可能加速发现进程，并将研究重点从‘易摘的果实’问题转移开来。 该猜想涉及球域上 Lipschitz 函数的凸优化 oracle 复杂度，其证明已在 Reddit 上经过领域专家验证。使用的模型是 GPT-5.6 Sol，而非功能最强的 Ultra 版本。

hackernews · mbustamanter · 7月18日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48957779)

**背景**: 凸优化是数学优化的一个分支，其中目标函数和约束条件都是凸的。Oracle 复杂度衡量为达到所需精度而向 oracle（例如梯度计算）进行查询的次数。这个三十年的差距指的是某些凸问题类别中 oracle 复杂度上下界之间的差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出这一贡献是真实的但较为小众，并质疑此类 AI 成就是否会让研究者过时——有人认为这将推动研究者专注于真正新颖的方法。一条评论澄清成功的是 Sol Pro 而非 Ultra，并讨论了其背后的多智能体架构。

**标签**: `#AI`, `#mathematics`, `#convex optimization`, `#GPT-5.6`, `#breakthrough`

---

<a id="item-2"></a>
## [LG 显示器通过 Windows Update 静默安装软件](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 9.0/10

将某些 LG 显示器连接到 Windows 电脑后，系统会通过 Windows Update 自动安装推广 McAfee 订阅的软件，且无需用户同意。 这构成了严重的安全和隐私漏洞，因为该软件以完全系统权限运行、开机自启动，且在没有任何用户交互的情况下被安装，影响大量使用 LG 显示器的 Windows 用户。 即使显示器之前已连接过，该问题也会发生，且软件会在每次系统启动时安装。解决办法包括在组策略或设备安装设置中禁用自动下载与设备相关的应用程序。

hackernews · baranul · 7月18日 10:21 · [社区讨论](https://news.ycombinator.com/item?id=48956688)

**背景**: Windows Update 可以自动为检测到的硬件安装驱动程序和相关软件。显示器被识别为设备，制造商可以提供包含额外软件的驱动程序包。这一机制类似于曾经允许恶意软件通过 USB 驱动器传播的自动运行漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent">LG monitors silently install software through Windows Update ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对此感到愤怒，指出该软件实际上是恶意软件，且没有沙箱保护。多位用户提供了通过组策略或设备安装设置的解决方法。关于责任在于 LG 还是允许自动安装的微软，存在争议。

**标签**: `#security`, `#windows`, `#privacy`, `#supply chain`, `#lg`

---

<a id="item-3"></a>
## [Kimi K3 达到前沿 AI 水平，引发蒸馏争议](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 9.0/10

中国初创公司 Moonshot AI 发布了 Kimi K3，这是一个拥有 2.8 万亿参数的模型，其性能与 OpenAI 和 Anthropic 的前沿模型持平，据 2026 年 7 月 17 日报道。 这一进展挑战了美国前沿实验室的领先地位，并引发了对知识蒸馏方法的担忧，可能重塑全球 AI 竞争格局，并引发关于开放权重模型访问的地缘政治辩论。 Kimi K3 拥有 100 万标记的上下文窗口，定价为每百万输入/输出标记 3/15 美元，在性能和成本上直接与 GPT-5.6 Sol 和 Claude Opus 4.8 竞争。

hackernews · sbochins · 7月18日 17:32 · [社区讨论](https://news.ycombinator.com/item?id=48960218)

**背景**: 知识蒸馏是一种技术，通过训练较小的“学生”模型来模仿较大的“教师”模型，从而实现成本高效的部署。GPT-5 和 Claude 等前沿模型是闭源的，但 Kimi K3 的开放权重访问引发了关于其是否通过蒸馏这些闭源模型达到同等水平的辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html">China's Moonshot AI unveils Kimi K3 that rivals OpenAI, Anthropic - CNBC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者们表达了不同的观点：有人认为蒸馏是不可避免的，并非“攻击”，而另一些人则指出使用限制问题，并质疑 K3 的真实成本效益。关于政府监管和地缘政治风险的担忧也很突出，有人将其比作早期的 Napster 时代。

**标签**: `#AI`, `#distillation`, `#frontier models`, `#open-source`, `#geopolitics`

---

<a id="item-4"></a>
## [台积电 A14 制程超预期：良率与性能逼近 90%](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers) ⭐️ 9.0/10

台积电宣布其 A14（1.4 纳米级）制程过去三个月进展迅速，器件性能和 256 Mb SRAM 良率均接近 90%，而 4 月份分别为 85%和 80%以上。 这一里程碑表明 A14 有望在 2028 年下半年量产，可能为下一代 AI、高性能计算和智能手机芯片带来显著优于当前 N2 节点的性能和能效提升。 与 N2 相比，A14 预计在同功耗下性能提升 10%至 15%，同频下功耗降低 25%至 30%，逻辑晶体管密度提高 23%，部分原因在于其采用第二代 GAA 纳米片晶体管。

telegram · zaihuapd · 7月18日 05:00

**背景**: A14 是台积电的 1.4 纳米级节点，将继 N2（2 纳米级）之后推出。它采用全环绕栅极（GAA）纳米片晶体管，相比 FinFET 具有更好的静电控制能力，从而实现进一步微缩。台积电的 N2 工艺使用第一代 GAA，而 A14 利用第二代 GAA，基于 N2 的经验积累。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.patsnap.com/resources/blog/articles/gaa-transistors-at-2nm-nanosheet-architecture-explained/">GAA transistors at 2nm: nanosheet architecture explained | PatSnap</a></li>
<li><a href="https://semiengineering.com/new-transistor-structures-at-3nm-2nm/">New Transistor Structures At 3nm/2nm</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#TSMC`, `#A14`, `#chip manufacturing`, `#AI`

---

<a id="item-5"></a>
## [回归式 JPEG 利用网络延迟实现播放](https://maurycyz.com/projects/bad_jpeg/) ⭐️ 8.0/10

该项目创建了一种渐进式 JPEG 图像，在加载过程中显示一系列低质量帧的动画，仅依赖网络延迟作为计时机制。 这一巧妙技巧重新利用了渐进式 JPEG 解码，用于隐写术、进度条或恶搞等创意应用，同时突出了图像编码中被忽视的特性。 每个动画帧被编码为渐进式 JPEG 的一个独立扫描；浏览器在数据到达时依次解码扫描，从而产生动画效果。播放速度无法控制，并随网络条件变化。

hackernews · vitaut · 7月18日 03:14 · [社区讨论](https://news.ycombinator.com/item?id=48954851)

**背景**: 渐进式 JPEG 通过多次扫描加载图像，首先显示模糊的低分辨率版本，然后每次后续扫描后变清晰。与从上到下加载的基线 JPEG 不同，渐进式 JPEG 允许早期感知整个图像。回归式 JPEG 项目利用这一行为，通过将每个帧编码为一个扫描来创建动画。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ionos.com/digitalguide/websites/web-design/progressive-jpeg/">Progressive JPEGs | An introduction to image compression - IONOS</a></li>
<li><a href="https://elementor.com/blog/progressive-jpegs/">Progressive JPEGs: What They Are & How They Boost Web Performance</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这种创意荒诞性，并提出了用于隐写术以绕过内容过滤器的建议。Retr0id 提到类似的工作使用了交错 PNG（adam7）。一些人建议通过服务器端定时分块发送来控制播放。

**标签**: `#jpeg`, `#image-encoding`, `#hacker-culture`, `#novelty`, `#compression`

---

<a id="item-6"></a>
## [Stack Overflow 衰退图引发关于 AI 与政策的辩论](https://data.stackexchange.com/stackoverflow/query/1953768#graph) ⭐️ 8.0/10

一个 Stack Exchange 数据浏览器的图表显示了 Stack Overflow 活动随时间明显下降，社区评论在讨论原因究竟是 AI 工具（如 ChatGPT）还是平台自身的排他性政策。 这很重要，因为 Stack Overflow 一直是开发者的基石，其衰退影响了程序员寻求帮助和分享知识的方式，可能将生态系统转向 AI 驱动的答案或更包容的平台。 图表显示活动在 2014 年左右达到顶峰，早于现代 AI 工具的普及。一些评论者指出，在 2021 年被 Prosus 收购后，衰退加速了。

hackernews · secretslol · 7月18日 11:12 · [社区讨论](https://news.ycombinator.com/item?id=48956949)

**背景**: Stack Overflow 是一个面向程序员的问答平台，用户可以提问和回答技术问题。长期以来，其严格的版规和较高的新手门槛被批评为阻碍了参与。最近 AI 的进步（如 ChatGPT）提供了直接答案，减少了对传统论坛的需求。

**社区讨论**: 评论者意见不一：一些人指责 AI 取代了答案来源，而另一些人则认为 Stack Overflow 本身的守门人文化和缺乏社区氛围赶走了用户。有几人指出衰退早在 AI 成为主流之前就已开始，并以 2014 年的峰值和 2021 年的收购为关键事件。

**标签**: `#stackoverflow`, `#ai-impact`, `#community`, `#decline`, `#data-analysis`

---

<a id="item-7"></a>
## [再见，自行车棚：可逆决策与 MD5crypt](https://queue.acm.org/detail.cfm?id=3818307) ⭐️ 8.0/10

这篇文章反思了软件开发中的自行车棚现象，引入了可逆决策的概念来缓解该问题，并向 PHK 的 MD5crypt 算法及其他贡献致敬。 它为技术团队提高决策效率提供了实用智慧，并强调了早期开源贡献对密码哈希等基础安全基础设施的持久影响。 文章讨论了可逆决策（可以轻松撤销的决定）应快速做出，无需大量辩论，而不可逆决策则需要更仔细的考虑。它还追溯了 MD5crypt 的历史，这是一种 1994 年在 FreeBSD 中引入的密码哈希方案。

hackernews · Ygg2 · 7月18日 17:27 · [社区讨论](https://news.ycombinator.com/item?id=48960155)

**背景**: 自行车棚现象源自帕金森琐碎定律，指人们倾向于在琐碎且容易理解的问题上花费过多时间，而忽视更重要但复杂的问题。MD5crypt 是一种密码哈希算法，它使用 MD5 结合盐值和多次迭代来安全存储密码，是早期加强密码存储以抵御暴力攻击的尝试之一，早于 bcrypt 和 scrypt。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.urbandictionary.com/define.php?term=bikeshedding">Urban Dictionary: bikeshedding</a></li>
<li><a href="https://en.wikipedia.org/wiki/MD5">MD5 - Wikipedia</a></li>
<li><a href="https://www.onlinehashcrack.com/guides/cryptography-algorithms/md5crypt-a-comprehensive-analysis-of-its-use-in-cryptography.php">md5crypt: A Comprehensive Analysis of Its Use in Cryptography</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了可逆决策的实用性，有人指出用钱解决自行车棚问题可以解决问题。还有人赞扬了 PHK 创建的 MD5crypt。一位用户最初对文章感到恼火，但在重读后欣赏其深度。一些人开玩笑说，用 JIRA 票务涂鸦取代了物理上的自行车棚。

**标签**: `#software engineering`, `#bikeshedding`, `#decision-making`, `#open source`, `#password hashing`

---

<a id="item-8"></a>
## [明目张胆的 AI 垃圾竟赢得 DeepMind Kaggle 大奖？](https://www.reddit.com/r/MachineLearning/comments/1uzyf66/did_blatant_ai_slop_just_win_a_25k_usd_deepmind/) ⭐️ 8.0/10

一位 Reddit 用户声称，在一场 DeepMind 赞助的关于认知 AI 基准测试的 Kaggle 比赛中，大奖得主包含无意义内容和毫无根据的声明，并提供了方法缺陷和代码错误的证据。 这引发了对高知名度 AI 竞赛和同行评审过程诚信性的严重质疑，可能削弱 AI 社区对基准开发与奖项分配的信任。 据报道，获奖提交物是要求格式大小的十倍，分析显示其包含无意义的数字生成和不合理的声明。组织者辩称评审具有主观性。

reddit · r/MachineLearning · /u/TheWerkmeister · 7月18日 15:10

**背景**: Kaggle 是一个数据科学竞赛平台，DeepMind 等赞助商会提供奖金。本次比赛名为“衡量 AGI 进展——认知能力”，要求参赛者设计新的基于认知科学的 AI 基准测试。获胜者通过评审流程选出，该流程有时可能缺乏严谨性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kaggle">Kaggle - Wikipedia</a></li>
<li><a href="https://ai.plainenglish.io/why-todays-ai-benchmarks-are-broken-and-what-deepmind-s-200k-hackathon-is-doing-about-it-44407812a1d4">Why Today’s AI Benchmarks Are Broken — and What...</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#Kaggle`, `#DeepMind`, `#competition controversy`, `#peer review`

---

<a id="item-9"></a>
## [豆包手机放弃 GUI 自动化，转向 MCP 协议集成 AI](https://www.latepost.com/news/dj_detail?id=3648) ⭐️ 8.0/10

豆包手机宣布放弃对微信、淘宝等头部应用使用 GUI 自动化（读取屏幕并模拟点击），转而要求这些超级应用提供 MCP（模型上下文协议）服务来实现 AI 智能体集成。同时，该手机的备货量从 3 万台提升至数十万台。 这一战略转变从脆弱、依赖平台的自动化转向开放协议标准，与苹果、谷歌采用类似框架整合 AI 智能体的趋势一致。它迫使超级应用开放数据和操控权限，可能重塑移动 AI 生态格局。 豆包手机助手软件于 2025 年 7 月 15 日获得生成式人工智能服务备案，首次技术预览版于 2025 年 12 月发布，但此前因微信、淘宝等平台封禁而被迫下线相关功能。该公司现正将产量从最初的 3 万台提升至“数十万台”。

telegram · zaihuapd · 7月18日 00:29

**背景**: GUI 自动化（图形用户界面自动化）允许 AI 智能体通过读取屏幕内容并模拟点击来操作手机应用，类似人类使用手机的方式。但这种方式不稳健，且可能被应用开发者封禁。MCP（模型上下文协议）由 Anthropic 于 2024 年 11 月推出，是一种开放标准，允许 AI 系统以结构化方式直接连接外部工具和数据源，使集成更可靠、更安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#MCP`, `#mobile operating systems`, `#AI integration`, `#ecosystem strategy`

---

<a id="item-10"></a>
## [Meta 拟向 Anthropic 出租 AI 算力，潜在交易额 100 亿美元](https://www.nytimes.com/2026/07/17/technology/meta-anthropic-ai-computing-power.html) ⭐️ 8.0/10

Meta 正与 AI 初创公司 Anthropic 谈判，拟以约 100 亿美元的价格向其出租 AI 算力，租期两年，按月付款，双方均可提前退出。 这笔交易凸显了 AI 算力的极度稀缺性，以及 Meta 将其巨额基础设施投资变现的策略，可能重塑大型科技公司之间 AI 算力的分配方式。 该方案由 Anthropic 于 2026 年 6 月提出，谈判仍处于早期阶段，未必能最终成交。Meta 今年计划投入高达 1450 亿美元，其中大量用于 AI 和数据中心建设。

telegram · zaihuapd · 7月18日 01:14

**背景**: AI 算力，尤其是用于训练大型语言模型的算力，目前需求极高且供应紧张。Meta 和 Google 等公司正在建设大型数据中心，而 Anthropic 等 AI 初创公司需要大量算力但缺乏自有基础设施。向科技巨头租用闲置算力正成为一种常见安排。

**标签**: `#AI`, `#Meta`, `#Anthropic`, `#cloud computing`, `#infrastructure`

---

<a id="item-11"></a>
## [SpaceX 与五角大楼谈判提供数十亿美元 AI 算力](https://www.wsj.com/tech/ai/spacex-in-talks-to-provide-computing-power-for-pentagons-ai-push-15e752e4) ⭐️ 8.0/10

SpaceX 正与美国国防部谈判，拟提供数据中心算力以运行人工智能模型，交易金额可能高达数十亿美元。 若最终达成，这将是 SpaceX 从发射服务扩展到国家安全云计算领域的重要一步，可能重塑国防 AI 格局，并挑战亚马逊、微软等现有供应商。 谈判仍在进行中，存在破裂可能；SpaceX 近期已与 Anthropic 和谷歌签署类似算力协议，并计划大幅扩展云计算业务。

telegram · zaihuapd · 7月18日 01:44

**背景**: 五角大楼正加速获取云计算能力，以支持国家安全和日常作战中的 AI 应用。该部门近期已批准 SpaceX、亚马逊、谷歌、微软和甲骨文等公司在机密环境中使用其 AI 模型及相关技术。SpaceX 以其 Starlink 卫星网络闻名，正利用其基础设施进军云计算市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://t.me/jinxw/795412">禁闻网 – Telegram</a></li>
<li><a href="https://www.nbd.com.cn/articles/2026-02-27/4271111.html">Anthropic拒向 五 角 大 楼 妥协；谷歌Nano Banana...</a></li>

</ul>
</details>

**标签**: `#AI算力`, `#SpaceX`, `#国防`, `#云计算`, `#五角大楼`

---

<a id="item-12"></a>
## [特朗普政府拟设类似 FINRA 的 AI 审查机构](https://www.bloomberg.com/news/articles/2026-07-17/us-considers-creating-finra-like-watchdog-to-vet-top-ai-models) ⭐️ 8.0/10

特朗普政府正考虑设立一个类似 FINRA 的独立监管机构，负责审查顶尖人工智能模型的安全性。该提案由财政部长斯科特·贝森特牵头制定，目前正由白宫幕僚长苏茜·威尔斯审阅，旨在回应华尔街和硅谷的关切。 此举或将建立由行业参与的正式 AI 安全监管框架，让金融和科技行业在安全标准制定方面拥有更大发言权。也可能回应了 AI 公司与政府近期在模型发布上的争议。 拟议的机构将向 SEC 汇报，类似于 FINRA。该计划与 Google DeepMind 首席执行官德米斯·哈萨比斯提出的行业资助独立监管机构建议方向一致。但总统特朗普尚未审阅该方案，内容可能调整。

telegram · zaihuapd · 7月18日 05:45

**背景**: 金融业监管局（FINRA）是一家私营自律组织，在美国证券交易委员会（SEC）的监督下监管经纪公司和交易市场。拟议中的 AI 监管机构将类似 FINRA，是一个由行业资助的独立机构，旨在实现 AI 安全领域的自律管理。这种模式意在结合行业专业知识和政府监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FINRA">FINRA</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#government policy`, `#Trump administration`, `#AI safety`

---

<a id="item-13"></a>
## [旧金山责令苹果谷歌下架 AI“脱衣”应用](https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/) ⭐️ 8.0/10

旧金山市检察长邱信福要求苹果和谷歌从其应用商店中下架数十款“脱衣”应用，并威胁若不遵守将采取法律行动并处以民事罚款。 这一举措开创了先例，要求主要科技平台对托管非自愿深度伪造应用负责，凸显了 AI 生成合成媒体带来的日益增长的法律和伦理挑战。 信函称，苹果和谷歌明知这些应用利用 AI 技术未经同意将照片中的人物“脱衣”并从中获利，可能面临民事处罚。苹果已下架三款应用并终止相关开发者账号，谷歌则暂停了五款 Play 商店应用。

telegram · zaihuapd · 7月18日 08:45

**背景**: 深度伪造技术利用机器学习创建逼真但虚假的图像和视频，通常未经同意。“脱衣”应用是一种特定的深度伪造色情内容，通过数字方式修改照片使对象看似裸体，引发严重的隐私和同意问题。科技透明项目此前已多次警告此类应用在苹果和谷歌应用商店中普遍存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deepfake">Deepfake - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nudify_apps">Nudify apps</a></li>
<li><a href="https://www.techtransparencyproject.org/articles/nudify-apps-widely-available-in-apple-and-google-app-stores">TTP - Nudify Apps Widely Available in Apple and Google App Stores</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#deepfakes`, `#app store regulation`, `#privacy`, `#platform accountability`

---