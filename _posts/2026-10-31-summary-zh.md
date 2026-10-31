---
layout: default
title: "Horizon Summary: 2026-10-31 (ZH)"
date: 2026-10-31
lang: zh
---

> 从 34 条内容中筛选出 9 条重要资讯。

---

1. [篡改版 Claude Code 扩展混入 Cursor 市场，向用户注入攻击者 SSH 密钥](#item-1) ⭐️ 8.0/10
2. [Northflank 遭安全入侵，引发对多租户 SaaS 连环攻击的担忧](#item-2) ⭐️ 8.0/10
3. [约 1GB Qwen 权重中运行 NES 模拟器](#item-3) ⭐️ 8.0/10
4. [Tangled 发布基于 AT Protocol 的联邦化、可自托管代码托管平台](#item-4) ⭐️ 8.0/10
5. [研究员披露 Azure 五个可完全跨租户入侵的漏洞](#item-5) ⭐️ 8.0/10
6. [AI 不会取代 SRE，而是在让其技能退化](#item-6) ⭐️ 8.0/10
7. [NES 6502 模拟器被烘焙进 Qwen3.5-4B 权重](#item-7) ⭐️ 8.0/10
8. [DeepSeek 二轮融资据报达 1055 亿元，估值超 6155 亿元](#item-8) ⭐️ 8.0/10
9. [苹果 Apple 智能 11 月 4 日在中国开启测试，接入阿里千问](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [篡改版 Claude Code 扩展混入 Cursor 市场，向用户注入攻击者 SSH 密钥](https://phorion.io/blog/offical-claude-code-vsx-compromise/) ⭐️ 8.0/10

一名恶意行为者利用对 Cursor 市场的发布权限，上架了一份被篡改的 Claude Code VS Code 扩展，该扩展会悄悄把一把标记为 “svc-telemetry” 的攻击者公钥追加到用户的 ~/.ssh/authorized_keys 文件中。Anthropic 工程师 Felix Rieseberg 确认，这只是第三方市场上的篡改副本，并非 Anthropic 系统被攻破；Cursor 则表示该恶意版本在周四约太平洋时间凌晨 2:27 至下午 1:35 之间在线。 这是一起典型的针对广泛使用的 AI 编程工具的扩展市场供应链攻击，说明从二级注册表安装知名品牌的插件，可能让攻击者获得对开发者机器的持久远程访问权限。任何通过 Cursor 市场或 Open VSX 而非微软官方市场安装 Claude Code 扩展的用户，都应检查自己的 SSH 配置。 恶意载荷本身很简单：被篡改的版本只是往 authorized_keys 里添加了一把 SSH 公钥，从而让攻击者无需密码即可登录受影响机器。macOS 用户可用 `grep -qs svc-telemetry ~/.ssh/authorized_keys && echo "svc-telemetry key found" || echo "No key found; machine not impacted"` 自检；评论者指出，究竟哪些注册表受影响目前仍不太明确，但微软官方市场上的版本被认为是干净的。

hackernews · _chall · 10月30日 07:09 · [社区讨论](https://news.ycombinator.com/item?id=50300683)

**背景**: VS Code 扩展通常通过微软的 VS Code 市场分发，但 Cursor、VSCodium 等 IDE 无法直接使用该注册表，因此转而依赖 Open VSX 以及自建市场。由于扩展以编辑器进程的完整权限运行，恶意扩展可以读写 ~/.ssh/authorized_keys 等文件，而该文件列出了允许通过 SSH 登录某账户的公钥。过去几年里，通过扩展注册表实施的供应链攻击——包括仿冒名称、发布者账号被劫持、构建产物被篡改——已成为开发者面临的反复出现的安全威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://danielraffel.me/2026/01/05/i-built-a-vs-code-cursor-extension-to-open-agents-in-the-editor-area/">I built a VS Code / Cursor extension to open Agents in the Editor Area</a></li>
<li><a href="https://labs.cloudsecurityalliance.org/research/csa-research-note-vscode-extension-supply-chain-breach-20260/">VSCode Marketplace Poisoning: How 18 Minutes Breached GitHub</a></li>

</ul>
</details>

**社区讨论**: 讨论很大程度上是在澄清事实：一位 Anthropic 工程师强调，Anthropic 的系统与员工笔记本均未被攻破；评论者则指出早期报道的偏差，援引 Phorion 的原始报告和 Cursor 官方博客，以确定约 11 小时的暴露窗口。还有人提供了具体的检测命令，并争论微软官方市场的版本是否也受影响，主流看法是 Open VSX／Cursor 渠道才是攻击入口。

**标签**: `#security`, `#supply-chain-attack`, `#vs-code-extensions`, `#ai-coding-tools`, `#cursor-marketplace`

---

<a id="item-2"></a>
## [Northflank 遭安全入侵，引发对多租户 SaaS 连环攻击的担忧](https://status.northflank.com/) ⭐️ 8.0/10

总部位于英国、基于 Kubernetes 的 PaaS 服务商 Northflank 通过其状态页披露了一起安全入侵事件，在 Hacker News 上引发热议（354 分、272 条评论）。有评论者指出，这至少是自 9 月以来针对多租户“即服务”厂商的第六起重大攻击，此前 PingCAP/TiDB、Fireworks AI、Zeabur、OpenCode Console 和 Railway 均曾中招。 这一连串事件被解读为多租户 SaaS 模式的结构性风险，而非单纯的运气不佳——单个漏洞或配置错误就可能一次性暴露所有租户的数据。有评论者认为，这会促使企业客户回流到超大规模云厂商，因为使用体验上的“更好用”无法替代安全性。 所附链接仅为状态页，攻击入口、受影响范围、客户数据是否泄露等技术细节仍不明确；有评论者观察到，该厂商似乎并不具备访问客户代码或二进制文件的能力。讨论中还提出了诸如加密环境变量、把解密密钥硬编码进已部署二进制文件等变通做法，但前提是攻击者无法触达运行中的应用。

hackernews · js4ever · 10月30日 15:10 · [社区讨论](https://news.ycombinator.com/item?id=50305025)

**背景**: Northflank 是一家总部位于英国的平台即服务（PaaS）厂商，在底层使用 Kubernetes 的同时提供开发者友好的工作流，功能包括基于 Git 的部署、托管数据库、预览环境和 GPU 支持。多租户——即众多客户共享同一套基础设施——正是这类平台成本低、易运维的原因，但 OWASP 指出，单个漏洞或配置错误就可能导致数据跨越租户边界泄露。AWS、Azure、Google Cloud 等超大规模云厂商是另一类选择，它们在安全上投入更深，代价是运维复杂度更高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://northflank.com/blog/what-is-paas-hosting">What is PaaS hosting? Benefits and how it works | Blog — Northflank</a></li>
<li><a href="https://europeanstack.com/software/northflank">Northflank Review 2026 | EuropeanStack</a></li>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html">Multi Tenant Security - OWASP Cheat Sheet Series</a></li>

</ul>
</details>

**社区讨论**: 讨论整体充满警觉：一位高赞评论者列举了自 9 月以来针对多租户厂商的六起闪电式攻击，称其为“一场正在上演的信息安全紧急事件”。其他人分享了把解密密钥硬编码进二进制文件来加密环境变量等防御技巧，预测企业客户将回流到超大规模云厂商，并担忧未来技术手段的安全防护将不再可行、零信任与行为层面的摩擦会成为常态；也有人只是好奇 Northflank 究竟是什么。

**标签**: `#security`, `#saas`, `#infrastructure`, `#cloud`, `#incident-response`

---

<a id="item-3"></a>
## [约 1GB Qwen 权重中运行 NES 模拟器](https://github.com/dbreunig/nesformer) ⭐️ 8.0/10

一位开发者发布了 nesformer，一个可运行的任天堂娱乐系统（NES）模拟器，它并非传统确定性程序，而是构建在约 1GB 的 Qwen 模型权重之中。 该项目表明 LLM 权重能够编码并执行一个具有状态的重要程序，引发了对将虚拟机、解释器和工具直接嵌入模型、而非只依赖外部工具调用的讨论。 据报道，该模拟器比真实 NES 硬件慢 150–290 倍；讨论指出它不仅模拟 CPU，还通过 gated DeltaNet 式架构在模型内模拟 RAM，作者称可工作的权重和代码仅由两次提示生成。

hackernews · dbreunig · 10月30日 16:40 · [社区讨论](https://news.ycombinator.com/item?id=50306442)

**背景**: NES 是 8 位游戏机，其游戏依赖精确的 CPU、图形和内存行为，因此模拟器通常是复现这些电路行为的确定性程序。Qwen 是阿里云推出的开放权重语言模型系列，而神经网络权重通常是驱动预测的学习参数，并非用于精确执行程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://playground.tensorflow.org/">A Neural Network Playground</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者对这个黑客项目表示赞赏，并对将小型虚拟机、Python 解释器或 Unix 工具编译进模型权重、再通过矩阵乘法执行的想法很感兴趣。同时，许多人强调巨大的效率差距：确定性程序便宜数千倍，150–290 倍的减速说明当前基于 LLM 的模拟多么不实用。评论者还惊讶于该项目不仅模拟 CPU，还模拟了 RAM。

**标签**: `#LLMs`, `#emulation`, `#Qwen`, `#neural-network-weights`, `#Hacker News`

---

<a id="item-4"></a>
## [Tangled 发布基于 AT Protocol 的联邦化、可自托管代码托管平台](https://tangled.org/blog/forge/) ⭐️ 8.0/10

Tangled 正式推出基于 AT Protocol 的联邦化代码托管平台，此次发布包含定稿的 lexicon、全面重构的架构与界面、组织（organizations）支持，并让整套系统或其中部分组件的自托管变得更容易。团队表示私有仓库将在接下来的两周内逐步上线。 它为开发者提供了一种代码托管新选择：仓库和身份可以迁移，而不是被单一服务商锁定；lexicon 的定稿也为其他代码托管平台与 Tangled 互通打开大门，而不必各自成为孤岛。这实际上是在检验 AT Protocol 的数据模型能否从社交网络延伸到开发者工具领域。 Tangled 支持使用 Bluesky 账号登录并沿用其社交关系图，其架构围绕 lexicon 定义的记录构建，因此“issue、PR 和评论记录究竟归属仓库作用域还是用户作用域”这一问题会直接影响互通能力。其背后的公司是一家芬兰初创企业，已融资 380 万欧元；项目仍处于早期阶段，私有仓库尚未全面开放。

hackernews · zlliang · 10月30日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=50305573)

**背景**: AT Protocol（ATproto）是一套用于去中心化发布的开放协议，是 Bluesky 以及更广泛的“ATmosphere”互通应用生态的基础；与基于 ActivityPub 的网络不同，它强调身份与数据的可迁移性，用户可以在不同服务之间转移。它的模式系统名为 lexicon，用 JSON 定义记录类型和 RPC 方法，使彼此独立的应用能够就数据格式达成一致并实现互通。通过定义代码托管相关的 lexicon，Tangled 让仓库、issue 和发布等内容运行在社交应用所用的同一套联邦数据模型中，这也是自托管与跨平台兼容成为本次发布核心的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atproto.com/guides/lexicon">Lexicons - AT Protocol</a></li>
<li><a href="https://nordictech.news/p/tangled-eur-3-8m-federated-github-alternative">Tangled Raises EUR 3.8M to Build a Federated GitHub Rival</a></li>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 整体反响积极：有用户计划把副项目从自托管的 Gitea 迁到 Tangled，仅保留 GitHub 用于可发现性和防止命名空间被抢注，并希望有 git-bug 桥接以同步 issue。另一位评论者追问定稿的 lexicon 是否已将 issue、PR 和评论记录从用户作用域移到仓库作用域，因为他自建的代码托管平台 juju.bi 希望充当 Tangled 的“knot server”。还有人提出界面意见，认为首页与时间线信息过于杂乱，建议个人主页的活动图表改用 GitHub 那种方块网格样式。

**标签**: `#federated-software`, `#code-forge`, `#at-protocol`, `#git`, `#self-hosting`

---

<a id="item-5"></a>
## [研究员披露 Azure 五个可完全跨租户入侵的漏洞](https://www.binarysecurity.no/posts/2026/10/one-root-case) ⭐️ 8.0/10

Binary Security 的一名安全研究员发布了一份详细报告，披露了 Microsoft Azure 中五个不同的跨租户入侵漏洞，其中包括路径遍历（path traversal）和不安全直接对象引用（IDOR）缺陷，可被用来访问其他客户的资源。该文章围绕一个“根因案例”展开，将这五个问题追溯到共同的底层访问控制弱点，而非把它们当作孤立漏洞来看待。 租户隔离是公有云最根本的信任边界，因此跨租户漏洞影响的往往不止单个受害者，而可能是平台上所有拥有付费账户的客户。由于 Azure 承载了大量企业的身份、存储和应用托管业务，这些发现对任何运行多租户工作负载或依赖 Entra ID 进行身份认证与授权的组织都有直接影响。 这些漏洞源于对用户提供的对象标识符缺乏充分的访问控制校验，而报告中“为资源名称添加随机性”的缓解建议被社区批评为近似于安全上的模糊化（security by obscurity），而非真正的授权修复。评论者还指出一个相关的独立问题：当攻击者知道另一个客户的租户 ID 时，login.microsoftonline.com 的 adminconsent 流程末尾回调是可以伪造的，而微软文档中“不要使用租户 ID 来认证用户”的警告只有在确实存在替代认证途径时才真正有用。

hackernews · swq115 · 10月30日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50301854)

**背景**: 公有云本质上是多租户的：众多客户共享同一套基础设施，但通过租户 ID、订阅 ID 和资源名称等标识符在逻辑上相互隔离。跨租户漏洞指攻击者能够从一个租户突破这种隔离，读取或篡改另一个租户的数据，因此云厂商把隔离工程视为最高级别的安全投入。本文提到的两类缺陷都非常经典：IDOR 是指应用直接信任 URL 或参数中传入的对象标识符，却不校验调用方是否拥有该对象；路径遍历则是利用“../”之类的序列访问预期目录之外的文件或接口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://owasp.org/projects/cloud-tenant-isolation">OWASP Cloud Tenant Isolation</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/IDOR">Insecure Direct Object Reference (IDOR) - Security | MDN</a></li>
<li><a href="https://www.systemshardening.com/articles/cross-cutting/multi-tenancy-security-patterns/">Multi-Tenancy Security Patterns: Isolation, Data Separation ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多赞赏这位研究员的工作，同时对 Azure 的隔离记录表达了更广泛的不安，有人认为 Azure 在跨租户泄露数量上似乎远超竞争对手，并质疑企业为何仍纷纷迁移过去。还有人提出了关于利用其他租户 ID 伪造 adminconsent 回调的具体担忧，并指出这些路径遍历和 IDOR 问题很可能自相关功能诞生之初就已存在。

**标签**: `#cloud-security`, `#azure`, `#vulnerability-research`, `#multi-tenancy`, `#access-control`

---

<a id="item-6"></a>
## [AI 不会取代 SRE，而是在让其技能退化](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) ⭐️ 8.0/10

SigNoz 通讯刊发的一篇观点文章提出，AI 智能体在站点可靠性工程（SRE）中更可能造成工程师技能退化，而不是直接取代他们；文章以航空业作类比，指出美国联邦航空管理局（FAA）即使自动驾驶完全可用，也强制要求飞行员完成一定的手动飞行时长。作者建议 SRE 团队同样可以指定某些故障场景——即便是 AI 能够处理的——作为人类练手的机会。该文在 Hacker News 上引发了约 498 分、376 条评论的大规模讨论。 这场讨论触及了运维与 DevOps 领域的核心担忧：如果依赖自主 AI 智能体完成告警分诊与故障修复，那么当自动化失效时，SRE 赖以生存的深度系统理解力可能会被削弱。这对所有引入 AI SRE 工具的组织都很重要，因为团队当下如何安排人工演练与人工监督，将决定他们日后是否还具备排查全新故障的专业能力。 文章的核心主张是一种刻意设计的“手动飞行时长”类比：即便 AI 能更快解决某些故障，也要保留一部分交由人类处理，以对应 FAA 那类让飞行员保持熟练度的规定。其代价是在生产系统中人为制造低效；此外该文属于观点评论而非实证研究，因此“技能退化”的论断主要依靠类比和个案，而非数据测量。

hackernews · dorianniemiec · 10月30日 15:52 · [社区讨论](https://news.ycombinator.com/item?id=50305693)

**背景**: 站点可靠性工程（SRE）是由 Google 开创的一门学科，把软件工程方法应用于基础设施与运维，高度强调自动化和基础设施即代码，以保障大型服务的高可用与高性能。AI SRE 智能体则是更新的一层：这类系统借助对告警、遥测数据、代码变更和故障历史的上下文推理，在无需人工逐步指导下完成告警分诊、根因分析和引导式修复。技能退化（deskilling）在自动化研究中是一个被长期关注的现象：当人类把任务交给机器后，会逐渐丧失在机器失效时进行干预所需的手工操作能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Site_reliability_engineering">Site reliability engineering</a></li>
<li><a href="https://www.augmentcode.com/guides/ai-sre-ai-powered-site-reliability-engineering">AI SRE: The 2026 Guide to AI-Powered Site Reliability Engineering</a></li>
<li><a href="https://rootly.com/blog/building-trust-with-ai-agents-in-site-reliability-engineering">Building trust with AI agents in site reliability engineering</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上认同这一担忧，但对其含义看法不一。有人称赞航空业的类比非常恰当，认为在复杂度不断提升时，这是防止人为失误最值得借鉴的行业；一位初创公司工程师则反驳说，Claude 在 AWS CLI 调试上已比自己快约 10 倍，而另一位评论者坚称 AI 生成的应用中根本不存在真正的“理解”。还有一种有力的反向观点认为，“Terraform 也让我们技能退化了”，却没人要求手工配置基础设施，因此团队应推动 AI 实现自动检测与自动修复，从而迈向五个 9 的可用性。

**标签**: `#AI/ML`, `#SRE`, `#DevOps`, `#automation`, `#skill-atrophy`

---

<a id="item-7"></a>
## [NES 6502 模拟器被烘焙进 Qwen3.5-4B 权重](https://simonwillison.net/2026/Oct/30/nesformer/) ⭐️ 8.0/10

Drew Breunig 发布了 nesformer 项目，将可运行的 NES 6502 CPU 模拟器编码进 Qwen3.5-4B 的权重中，使《超级马里奥兄弟》等 NES ROM 能在模型内部缓慢运行。 这是一个具体但不实用的实验，用来检验多少计算可以被嵌入 LLM 参数而不是交给外部工具；它把 qwenputer 的 RISC-V CPU 实验扩展到了 NES 模拟。 该模拟器运行非常缓慢，无法达到 NES 的标准时钟速度；Breunig 表示它是用 Claude Opus 5.5 的提示词构建的，并且据称使用了 Christopher Pow 多年前发布的 nestest 一致性测试套件来验证 NES CPU。

rss · Simon Willison · 10月30日 21:59

**背景**: NES 使用的是源自 6502 的 CPU，而模拟器通常用软件复现其指令行为。qwenputer 展示了可以把 CPU“编译”进模型权重，而不是作为外部程序运行；nesformer 把这一思路应用到了 NES 的 CPU 上。Qwen3.5-4B 是阿里巴巴 Qwen 系列中约 40 亿参数的模型，因此该演示值得注意，因为它只占相对较小的参数预算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MOS_Technology_6502">MOS Technology 6502 - Wikipedia</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-4B">Image-Text-to-Text model with 5B parameters. Download, explore files...</a></li>
<li><a href="https://github.com/divagr18/qwenputer">GitHub - divagr18/ qwenputer : A computer, compiled into the weights...</a></li>

</ul>
</details>

**社区讨论**: 可见的 Hacker News 讨论主要集中在 Breunig 分享他使用的 Claude Opus 5.5 提示词原文，其中包括阅读 qwenputer 文章并探索模拟 NES 芯片和 RAM 的指令。该讨论帖具有技术深度，不过从摘录中看不出明确的共识，只能看出大家对这一实验很感兴趣。

**标签**: `#LLM`, `#emulation`, `#retro-computing`, `#prompt-engineering`, `#hacker-news`

---

<a id="item-8"></a>
## [DeepSeek 二轮融资据报达 1055 亿元，估值超 6155 亿元](https://www.theinformation.com/articles/behind-deepseeks-16-billion-funding-chinese-tech-titans-state-players) ⭐️ 8.0/10

据 The Information 报道，DeepSeek 完成了规模约 1055 亿元人民币的第二轮融资，估值突破 6155 亿元人民币，参投方近 30 家。其中腾讯出资 100 亿元，宁德时代及董事长曾毓群合计出资 100 亿元，长鑫存储、中芯国际、美团、vivo、小红书等也在投资方名单之中。 若消息属实，这将成为中国 AI 初创公司史上规模最大的融资之一，也说明国内最大的互联网平台、芯片厂商与电池供应商正共同押注同一家前沿实验室。国资背景资金占比从首轮的约 2% 跃升至本轮的约 27%，表明前沿大模型能力已被视为具有战略意义的基础设施，而不再只是纯粹的市场化风险投资。 上述数字来自 The Information 的付费报道，DeepSeek 及各投资方均未予以确认，因此融资规模与估值都应视为尚未证实的消息。首轮融资于今年 6 月完成，规模约 510 亿元，意味着二轮体量约为首轮的两倍；投资方结构异常多元，横跨云计算与互联网平台、DRAM 与晶圆代工企业以及消费应用公司。

telegram · zaihuapd · 10月30日 12:37

**背景**: DeepSeek 是一家总部位于杭州的 AI 实验室，脱胎于量化投资机构幻方量化，以开源发布 V3、R1 等模型而闻名——这些模型以远低于西方的训练成本达到了接近的性能水平。长鑫存储（CXMT）是中国最大的 DRAM 内存芯片厂商，也是国产存储产业摆脱对三星、SK 海力士和美光依赖的核心力量；中芯国际则是中国大陆最大的晶圆代工厂。这两家公司都处于国资引导资金涌入 AI 与半导体的大潮之中，代表性基金包括规模 3440 亿元的国家集成电路产业投资基金三期，以及专门设立的国家人工智能产业投资基金。这些名字出现在 DeepSeek 的股东名单上，说明这笔交易的意义不只在于财务回报，更在于锁定国内的算力与存储供应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bybit.com/zh-MY/learn/stocks/deepseek-company-overview-valuation-ipo">什么是 DeepSeek ？ 公 司 概况、 估 值 与 IPO 前 景 跟单 | Bybit Learn</a></li>
<li><a href="https://zh.wikipedia.org/zh-sg/长鑫存储">长 鑫 存 储 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.sohu.com/a/851045638_121798711">600亿大手笔！国家人工智能产业投资基金成立，推动AI与半导体融合发展...</a></li>

</ul>
</details>

**标签**: `#AI funding`, `#DeepSeek`, `#China tech`, `#LLM industry`, `#state investment`

---

<a id="item-9"></a>
## [苹果 Apple 智能 11 月 4 日在中国开启测试，接入阿里千问](https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/) ⭐️ 8.0/10

苹果宣布首批 Apple 智能功能——包括实时翻译、照片消除工具和写作工具——将于 11 月 4 日随最新 iOS 开发者 Beta 版在中国开启测试，并于 12 月随 iOS 27.3 正式版面向中国用户推出。苹果同时与阿里巴巴合作，由千问（通义千问）模型为符合条件的用户在 Siri、写作工具和视觉智能中提供支持。 中国是苹果第二大市场，而 Apple 智能自 2024 年发布以来一直未能落地中国，使 iPhone 在与华为、小米等大力押注 AI 的国产对手竞争时处于劣势。引入本土合作伙伴的大模型来驱动 Siri 和系统级功能，为海外 AI 产品进入中国市场提供了一个可参照的模板，对阿里巴巴千问生态也是一次重要的胜利。 此次上线仅涵盖首批功能，不包含下一代 AI 版 Siri，其他苹果平台（iPad、Mac、Vision Pro）的支持则需在获得必要审批后才会推出。使用资格限于在中国购买支持 Apple 智能的 iPhone 的用户，或设备定位与 Apple 账户国家/地区均设置为中国的用户。

telegram · zaihuapd · 10月30日 21:44

**背景**: Apple 智能是苹果为其各操作系统提供的端侧与云端 AI 功能的统称，包括写作工具、通知摘要以及视觉智能——后者让用户按下相机控制按键即可识别物体、翻译文字或查询屏幕上内容的相关信息。由于中国监管要求生成式 AI 服务必须经过审批、且通常由持牌的国内厂商提供支持，苹果无法直接把自家模型或海外版与 ChatGPT 的集成搬到中国。千问（通义千问）是阿里云推出的大语言与多模态模型家族，既以开放权重形式发布，也提供企业级 API，因此成为 Siri 和写作辅助功能顺理成章的本土合作方。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.alibabacloud.com/en/solutions/generative-ai/qwen?_p_lc=1">Qwen - Alibaba Cloud</a></li>
<li><a href="https://support.apple.com/guide/iphone/learn-visual-intelligence-iph12eb1545e/ios">Learn about what’s around you with Visual Intelligence on ...</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#China`, `#Alibaba Qwen`, `#iOS`, `#AI localization`

---