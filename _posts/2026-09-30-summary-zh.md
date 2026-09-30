---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
lang: zh
---

> 从 40 条内容中筛选出 9 条重要资讯。

---

1. [AMD 将以 82 亿美元收购李飞飞创办的 World Labs](#item-1) ⭐️ 9.0/10
2. [OpenAI 发布 GPT-6.1 Sol：以五分之一价格实现接近 Astra 的智能](#item-2) ⭐️ 8.0/10
3. [美国政府推出基于 Google Gemini 的 America.gov AI 服务平台](#item-3) ⭐️ 8.0/10
4. [隐私分析发现对话式 AI 代理泄露提示与聊天内容](#item-4) ⭐️ 8.0/10
5. [OpenAI 发布常驻智能体产品 Dots](#item-5) ⭐️ 8.0/10
6. [Anthropic：GLM-5.3 与 Claude Mythos Preview 首次跨过自主漏洞利用门槛](#item-6) ⭐️ 8.0/10
7. [甲骨文就星际之门新墨西哥数据中心发出不可抗力通知](#item-7) ⭐️ 8.0/10
8. [Cloudflare 发布面向 AI Agent 的命令行工具 cf CLI](#item-8) ⭐️ 8.0/10
9. [OpenAI 开发者大会：Dots 常驻智能体等 20 余项更新](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AMD 将以 82 亿美元收购李飞飞创办的 World Labs](https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute) ⭐️ 9.0/10

AMD 于 2026 年 9 月 28 日宣布，将以 82 亿美元收购李飞飞联合创办的物理 AI 与世界模型初创公司 World Labs。该交易仍需监管批准，预计在年底前完成，李飞飞将加入 AMD 担任执行副总裁兼首席科学家。 这是今年规模最大的 AI 收购之一，表明芯片厂商正从单纯出售算力转向掌控模型层，尤其是在物理 AI 与机器人领域。此举也显著提升了 AMD 在与英伟达争夺具身智能算力市场时的地位，并把该领域最知名的研究者之一招入半导体公司内部。 World Labs 成立仅约两年，2024 年成立时融资 2.3 亿美元，2026 年 3 月又完成据报 10 亿美元的一轮融资，因此 82 亿美元的收购价相较其上一轮私募估值溢价明显。其技术旨在让 AI 理解并模拟物理世界，包括生成用于机器人训练的仿真环境；交易尚需通过监管审查，存在延迟或被否决的可能。

telegram · zaihuapd · 9月29日 03:59

**背景**: 世界模型是一种 AI 系统，它会在内部构建对环境的表征，并预测环境在动作作用下如何变化，从而模拟物理规律、物体交互与因果关系，而不仅仅是生成文本或图像。这类模型被视为机器人、自动驾驶和交互式视频的基础，因为它能让智能体在无需大量真实世界试错的情况下进行规划与推理。World Labs 由斯坦福大学教授李飞飞联合创办，她因推动深度学习浪潮的 ImageNet 数据集而广为人知，公司主攻的正是“物理 AI”方向。AMD 是英伟达在 AI 加速器领域的主要挑战者，收购一家模型开发商意在通过软硬件与模型的深度绑定来实现差异化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fortune.com/2026/09/28/amd-acquires-world-labs-startup-fei-fei-li-8-2-billion/">AMD acquires Fei-Fei Li’s physical AI startup World Labs for $8.2 billion | Fortune</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-09-28/amd-to-buy-fei-fei-li-s-world-labs-ai-startup-for-8-2-billion">AMD to Buy Fei-Fei Li’s World Labs Startup for $8.2 Billion - Bloomberg</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>

</ul>
</details>

**标签**: `#AMD`, `#World Labs`, `#M&A`, `#World Models`, `#AI Compute`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-6.1 Sol：以五分之一价格实现接近 Astra 的智能](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 8.0/10

OpenAI 发布了 GPT-6 Sol 的升级版 GPT-6.1 Sol，声称其在智能体编程、计算机操作和专业任务上接近旗舰模型 GPT-6 Astra 的水平，而价格仅为 Astra 标准价的约五分之一。该模型已向 Plus、Pro、Business、Enterprise 和 Edu 用户开放，并可通过 OpenAI API 以 gpt-6.1-sol 的名称调用，标准价格为每百万输入 token 2 美元、缓存输入每百万 token 0.10 美元、每百万输出 token 10 美元。 此次发布加剧了前沿 AI 领域的价格战：OpenAI 将一款更便宜的中端模型定位为足以胜任严肃编程和智能体任务，从而对 Anthropic 的 Opus 5.5 以及 DeepSeek 等低成本挑战者形成压力。如果“接近 Astra”的说法站得住脚，可能会改变开发者选择模型的方式——从追求基准测试的绝对领先，转向优化单位任务成本。 OpenAI 会自动缓存 1024 个 token 及以上的提示词，且 GPT-6.1 Sol 对每次缓存提示都收取缓存写入费用，无论该缓存前缀是否被再次读取；每百万 token 0.10 美元的缓存输入价格比标准输入价格低 95%，也比 GPT-6 Sol 的缓存价格低 50%。在 Devin 的排行榜上，GPT-6.1 Sol 在低推理努力下以每任务 0.21 美元的成本取得 58.1% 的分数，高于 GPT-6 Sol 的 50.5%；在 DeepSWE v1.1 上，据称其以约五分之一的成本达到 GPT-6 Astra 的水平。

hackernews · crorella · 9月29日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49896586)

**背景**: OpenAI 的 GPT-6 系列采用分层设计：GPT-6 Astra 是旗舰模型，GPT-6 Sol 则定位在它之下，是更便宜的主力模型。GPT-6.1 Sol 在 GPT-6 Sol 发布仅七天后就将其取代，这种异常迅速的迭代被社区解读为对上一代反响不佳的回应。这里的“Astra”指的是 OpenAI 自家的 GPT-6 Astra 档位，与 Google DeepMind 用于通用 AI 助手的同名研究原型 Project Astra 无关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT - 6 . 1 Sol | OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6.1-sol">GPT - 6 . 1 Sol - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/articles/gpt-6-1-sol-replaces-gpt-6-sol-after-just-7-days-with-near-astra-intelligence">GPT-6.1 Sol replaces GPT-6 Sol after just 7 days, with near-Astra intelligence | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的反应明显分化：多位开发者表示 GPT-6 Sol 相比前代出现退步，自己已转投 Anthropic 的 Opus 5.5，其中一人怀疑 GPT-6.1 Sol 只是把此前泄露的 “Astra-Minor” 模型临时改名后仓促推出。另一些人则认为真正的大新闻是缓存价格降低 50%，这在 Codex 类工作负载中能带来可观的成本收益；也有评论者警告说，token 价格成为主要战场对行业和投资者而言是一个不祥信号。

**标签**: `#AI`, `#LLM`, `#OpenAI`, `#Model Release`, `#Pricing`

---

<a id="item-3"></a>
## [美国政府推出基于 Google Gemini 的 America.gov AI 服务平台](https://america.gov/) ⭐️ 8.0/10

美国政府正式上线 America.gov，这是一个基于 Google Gemini 构建的 AI 平台，帮助民众查找并获取联邦政府服务。Google 公开表示自己是该计划的技术合作伙伴，并称 Gemini 将帮助超过 1 亿人更快、更便捷地获取关键公共资源。 政府服务长期分散在成千上万个页面中，一个统一的对话式入口可以显著降低民众寻找正确机构或项目的门槛，同时减少被钓鱼网站欺骗的风险。这也是商业大语言模型在公共部门的又一次高调落地，将成为政府采用生成式 AI 的重要试验案例。 据社区讨论，该平台以 Gemini 为核心并叠加了安全护栏（guardrails），Google 也确认自己是该计划的技术合作伙伴之一。不过护栏的具体机制、用户数据的处理方式以及覆盖哪些联邦服务，目前尚未公开说明。

hackernews · plesiv · 9月29日 14:04 · [社区讨论](https://news.ycombinator.com/item?id=49893509)

**背景**: Gemini 是 Google DeepMind 开发的多模态大语言模型系列，于 2023 年 12 月 6 日发布，是 LaMDA 和 PaLM 2 的继任者，包含 Pro、Flash 等多个版本。大语言模型是在海量文本上训练的神经网络，能针对提示生成流畅回答，因此很适合在庞大文档集合上进行对话式检索，但也容易出错或被操纵。过去政府机构通常通过众多彼此独立的门户网站提供服务，而“护栏”（guardrails）指的是对已部署模型的输出与行为施加的限制和过滤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model ) - Wikipedia</a></li>
<li><a href="https://gemini.google.com/app">Google Gemini</a></li>

</ul>
</details>

**社区讨论**: 评论区整体对该构想持肯定态度，多位用户认为精心打造的聊天机器人正适合解决“大海捞针”式的任务，例如找到正确的政府服务，也有人惊讶于平台回答竟如此直白。有用户根据 Google 的博客公告指出其技术栈是“Gemini + 护栏”，还有人强调其最大价值在于把迷宫般的信息密集页面浓缩成一个输入框。

**标签**: `#AI`, `#Government`, `#LLM`, `#Gemini`, `#Public Services`

---

<a id="item-4"></a>
## [隐私分析发现对话式 AI 代理泄露提示与聊天内容](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf) ⭐️ 8.0/10

一篇题为《A Privacy Analysis of Web and Mobile Conversational AI Agents》的新研究论文，考察了网页端与移动端对话式 AI 助手如何处理用户数据，记录了诸如在用户真正发送消息前就部分传输提示词、以及用会话 URL 暴露完整聊天记录等追踪行为。该论文被分享到 Hacker News，获得 407 分与 129 条评论。 随着对话式 AI 助手逐渐成为搜索、编程和日常写作的默认入口，提示词与会话记录的隐私已从边缘问题变成核心的用户权益问题。论文的发现意味着用户视为私密的内容——尚未成形的想法、修改痕迹和草稿——可能早已离开本地设备，进入追踪或训练数据管道。 该分析同时覆盖网页端和移动端代理，并指出两个具体机制：一是在用户点击发送之前，部分提示数据就被送往类似 ChatGPT 的 `conversation/prepare` 这类端点；二是基于 UUID 的会话 URL 看似私密，实际上任何拿到链接的人都能读取完整对话。论文的论述框架表明，这些更像是设计取舍和工程选择，而非孤立的漏洞。

hackernews · damaru2 · 9月29日 09:03 · [社区讨论](https://news.ycombinator.com/item?id=49890226)

**背景**: 对话式 AI 代理是指 ChatGPT、Perplexity 及类似应用，用户通过浏览器或手机应用里的聊天框与它们交互。由于这些服务基于云端，每一次按键、草稿和追问都可能被传送到远程服务器并保存，而可分享的会话链接、使用分析等功能会让这些存储数据变成追踪面。这一领域的隐私研究通常关注：哪些数据离开了客户端、何时离开、以及之后谁能取回它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nngroup.com/articles/ai-prompt-structure/">Prompt Structure in Conversations with Generative AI - NN/G</a></li>
<li><a href="https://www.theregister.com/2026/02/10/ai_agents_messaging_apps_data_leak/">AI agents can spill secrets via malicious link previews • The Register</a></li>
<li><a href="https://zylos.ai/research/2026-07-18-capability-urls-no-login-access-agent-workflows/">Capability URLs: The Authentication Layer AI Agents Actually Want | Zylos Research</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍把这些发现视为对已知不良实践的印证，而非意外：有人描述观察到 ChatGPT 向 `conversation/prepare` 端点发送未完成的提示词，也有人抱怨 Perplexity 等把 URL 里的 UUID 等同于隐私，而链接实际会暴露整段对话。还有人将其与更普遍的现象联系起来——本应私密的提示词和输出流入产品数据或训练管道，并据此主张应偏向本地运行的开源模型。

**标签**: `#privacy`, `#conversational-ai`, `#web-tracking`, `#mobile-agents`, `#LLM-security`

---

<a id="item-5"></a>
## [OpenAI 发布常驻智能体产品 Dots](https://openai.com/index/introducing-dots/) ⭐️ 8.0/10

OpenAI 发布了名为 Dots 的常驻智能体（always-on agent）产品，用户可以通过 Slack、Teams 等企业协作平台向它发送消息，短信（text message）支持据称也即将推出。企业可为每个 "dot" 配置独立的身份、凭证以及对完成任务所需系统的访问权限，OpenAI 还表示计划推出承担特定职责的 "专家型 dot"（specialist Dots）。 这标志着头部实验室正把智能体从聊天窗口推进到企业系统之中，使其成为拥有凭证、长期在线的"数字员工"，可能改变采购、发票处理、客服等日常知识工作的分派方式。同时它也引发了 Hacker News 讨论中的核心疑虑——平台锁定：一个深度接入你的工具链和工作历史的智能体，远比一个 API 背后的模型更难替换。 OpenAI 表示 Dots 借鉴了公司内部在采购、发票处理、邮件营销、客户支持和商业合同等场景的早期试用经验，每个 dot 会适应新信息并根据团队反馈不断改进。公告并未说明定价、可用范围，也没有解释 Dots 与 OpenAI 现有 Codex、ChatGPT Work 之间的关系——而评论者指出，这三条产品线其实都在朝"带长期记忆的沙盒远程智能体"这一方向收敛。

hackernews · alvis · 9月29日 17:07 · [社区讨论](https://news.ycombinator.com/item?id=49896604)

**背景**: 所谓"常驻智能体"（always-on agent），指的是常驻云端持续运行、而非只回应单次提问的系统：它跨会话保存持久状态与记忆，能异步操作其他系统，实际上相当于一台替你干活的云端小电脑。这个概念处在两条趋势的交汇处——会调用工具和 API 的 LLM 智能体，以及云托管的虚拟机；目前已有多家厂商涌入，例如 Cursor 推出了"常驻"自动化功能，学术界也已有论文专门梳理这类智能体的持久记忆、状态与治理问题。从历史看，AI 订阅定价常呈现"先补贴、后收紧"的模式：先用慷慨的额度从竞争对手那里抢用户，等用户的迁移成本变高后再收紧限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-dots/">Introducing dots | OpenAI</a></li>
<li><a href="https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/">OpenAI launches Dots, its bubbly agentic avatar | TechCrunch</a></li>
<li><a href="https://arxiv.org/abs/2606.30306">[2606.30306] Always-OnAgents:A Survey of Persistent Memory, State, and Governance in LLMAgents</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论（456 分、345 条评论）整体偏批评而非宣传。评论者认为常驻智能体造成深度锁定：由于集成的平台和积累的工作历史，它实际上就是"你在云端的电脑"，很难换掉；他们抱怨 Codex、ChatGPT Work 与 Dots 之间的界限越来越模糊，并指出 OpenAI 和 Anthropic 都存在"先用慷慨订阅额度吸引用户、随后收紧限制"的老套路。还有人认为这类产品并非面向能自己折腾的技术用户，而是面向非技术人群和下一代"AI 原住民"，其中一位甚至称常驻智能体意味着"PC 时代的终结"。

**标签**: `#ai-agents`, `#openai`, `#platform-lock-in`, `#llm-products`, `#industry-news`

---

<a id="item-6"></a>
## [Anthropic：GLM-5.3 与 Claude Mythos Preview 首次跨过自主漏洞利用门槛](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/) ⭐️ 8.0/10

Anthropic 前沿红队（Frontier Red Team）在其内部二进制利用基准测试中随机抽取 100 个任务进行评测，结果显示 GLM-5.3 在 4% 的试验中成功构建了完整的控制流劫持，Claude Mythos Preview 的成功率为 6%。而更早的模型如 Claude Opus 4.6 和 GLM-5.2 则一次都未能成功，这标志着一条明确的能力门槛已被跨过。 这是首批公开信号之一，表明现成模型已能自主完成端到端的漏洞利用原语，而不只是让程序崩溃，这直接抬高了 AI 辅助网络攻击的风险。若该趋势延续，防御方将面对更快速、更低成本且更易获得的漏洞发现与利用开发能力，尤其是那些无法被集中管控的开放权重模型。 绝对成功率仍然很低（100 个任务中分别为 4% 和 6%），且该基准是 Anthropic 的内部测试而非完全公开的标准，因此跨实验室对比需谨慎解读。Anthropic 还报告称，GLM-5.3 的安全防护可被简单方法绕过（在其模拟测试中成功率为 64% 至 100%），并且其开放权重允许用户改造模型以削弱拒答行为。

rss · Simon Willison · 9月29日 22:20

**背景**: 控制流劫持是一种经典的二进制利用技术，攻击者通过操纵程序的执行路径——通常借助缓冲区溢出等内存破坏漏洞——使程序运行攻击者指定的代码。要稳定实现这一点需要串联多个高难度步骤（定位漏洞、构造 payload、绕过各种防护、最终达成代码执行），因此这类基准测试通常按“能力阶梯”分级评估，而不是简单地用“崩溃与否”作为唯一判据。Anthropic 前沿红队是专门对前沿模型进行危险能力压力测试的团队，此次结论即来自其内部的二进制利用基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.14153">ExploitBench: A Capability Ladder Benchmark for LLM Cybersecurity...</a></li>
<li><a href="https://cyberpedia.reasonlabs.com/EN/control+flow+hijacking.html">What is Control Flow Hijacking ?</a></li>

</ul>
</details>

**标签**: `#ai-safety`, `#cybersecurity`, `#llm-capabilities`, `#anthropic`, `#red-teaming`

---

<a id="item-7"></a>
## [甲骨文就星际之门新墨西哥数据中心发出不可抗力通知](https://www.bloomberg.com/news/articles/2026-09-24/oracle-cites-force-majeure-to-shield-itself-on-controversial-data-center) ⭐️ 8.0/10

甲骨文已就星际之门旗下新墨西哥州 Project Jupiter 数据中心向项目开发方发出不可抗力通知，理由是配套 2.45GW 微电网的环境与供电审批迟迟未落地，令该园区原定 2028 年投运的目标面临延期风险。该通知意味着一旦延期由外部因素造成，甲骨文可以推迟支付部分款项。 此举表明，超大型 AI 数据中心最大的瓶颈可能不是芯片或资金，而是电力与审批，并且已经动摇了市场对这些项目融资的信心。据报道，与该项目相关的约 180 亿美元银团贷款已出现折价交易，这对整个 AI 基础设施投资热潮是一个警示信号。 Project Jupiter 的核心是装机容量最高 2.45GW 的微电网——据报道采用 Bloom Energy 燃料电池而非柴油发电机，建成后将是美国最大的数据中心微电网之一，而如今卡在审批环节的恰恰就是这套供电方案。星际之门多数站点仍处于土建、审批或能源配套阶段，目前仅得克萨斯州阿比林园区投产，而得州本身也已暂停新数据中心项目的审批。

telegram · zaihuapd · 9月29日 05:46

**背景**: 星际之门（Stargate）是 OpenAI、甲骨文、软银和 MGX 于 2025 年 1 月宣布成立的 AI 基础设施合资企业，计划四年内投资最高 5000 亿美元，首期投入 1000 亿美元。Project Jupiter 是其园区之一，位于新墨西哥州 Doña Ana 县，规模达数吉瓦，由 STACK Infrastructure、BorderPlex Digital Assets 等合作方共同开发。AI 训练与推理需要巨大且持续的电力，而电网并网排队往往要等数年，因此这类项目越来越依赖自建发电与微电网。不可抗力条款是标准合同条款，允许一方在遭遇不可预见的、超出其控制的事件导致延期时免除履行义务，在这里即推迟支付部分款项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/announcing-the-stargate-project/">Announcing The Stargate Project | OpenAI</a></li>
<li><a href="https://malachi.energy/data-centers/projects/project-jupiter-nm">Project Jupiter (Stargate) Data Center (Santa Teresa, NM ): 2.2 GW...</a></li>
<li><a href="https://www.linkedin.com/posts/justinidcnova_datacenter-ai-fuelcells-activity-7454715294532653056-xxjy">Oracle & Bloom Energy Power 2 . 45 GW AI Data Center with... | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI基础设施`, `#Stargate`, `#甲骨文`, `#数据中心`, `#电力审批`

---

<a id="item-8"></a>
## [Cloudflare 发布面向 AI Agent 的命令行工具 cf CLI](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) ⭐️ 8.0/10

Cloudflare 发布了 cf CLI 的公开测试版，这是一个让开发者和 AI Agent 都能在终端中调用 Cloudflare API 的新命令行工具。与现有覆盖约 280 项操作的 Wrangler 不同，cf 直接由 API Schema 生成，覆盖超过 3,000 项 API 操作，默认以 JSON 作为输出，并支持命令搜索与引导式发现。 随着 AI Agent 逐渐成为云基础设施的一等使用者，一个以机器可读输出和自发现为核心的 CLI，能显著降低 Agent 框架此前的集成负担——过去它们不得不抓取文档或手写 API 客户端。凭借 Cloudflare 的规模与 API 覆盖面（Workers、Access、WAF、域名等），cf 有望成为自动化基础设施管理的通用接口，也会推动其他云厂商推出类似的“Agent 友好”工具。 该工具目前处于公开测试阶段，其命令体系由 Cloudflare 的 API Schema 自动生成，而非手工编写，这正是操作数量能从 280 项跃升到 3,000 项以上的原因。由于默认输出 JSON，Agent 可以程序化解析结果；Cloudflare 的示例显示，一个 Agent 可以用同一个工具创建并部署 Worker、监控服务、配置 Access 与 WAF 策略，甚至购买域名。由 Schema 生成也意味着新 API 端点能被自动纳入覆盖范围，不过测试版状态意味着接口仍可能频繁变动。

telegram · zaihuapd · 9月29日 13:46

**背景**: Cloudflare 是重要的 CDN、DNS、安全与边缘计算服务商，其无服务器平台 Cloudflare Workers 可在全球边缘网络上运行代码。该公司长期使用的命令行工具是 Wrangler，用于构建、测试和部署 Worker 项目，它面向开发者，且只覆盖 Cloudflare 产品线中相对狭窄的一部分。Cloudflare Access 属于其 Zero Trust（零信任）套件，负责基于身份感知的访问控制，WAF 则指 Web 应用防火墙。此处所说的 AI Agent，是由大模型驱动、能够自主发现工具、执行命令并根据结果采取行动的程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/wrangler/">Wrangler · Cloudflare Workers docs</a></li>
<li><a href="https://developers.cloudflare.com/workers/">Overview · Cloudflare Workers docs</a></li>
<li><a href="https://www.cloudflare.com/products/workers/">Cloudflare Workers - Global Serverless Functions Platform</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#CLI`, `#AI Agents`, `#Developer Tools`, `#API`

---

<a id="item-9"></a>
## [OpenAI 开发者大会：Dots 常驻智能体等 20 余项更新](https://openai.com/zh-Hant/index/devday-2026-recap/) ⭐️ 8.0/10

OpenAI 在其开发者大会上公布了 20 余项更新，核心是常驻伴生智能体「Dots」——可全天候自主运转、深度学习用户习惯，并主动接管长线复杂工作。同批更新还包括 GPT-6.1 Sol 模型（专精编程与电脑操控，以五分之一的价格获得接近 Astra 的智能水平）、最高提速 8 倍的「Astra Ultrafast」服务档、支持语音操控与自动修障的云端 Codex、全新的 Agents API 与 Decisions API、「Sign in with ChatGPT」第三方登录，以及 Pro 500 新套餐。 这次发布标志着 OpenAI 正从聊天助手转向可跨多个第三方应用长期驻留、自主工作的智能体软件，直接回应了 Meta 不久前推出的 Muse 智能体。通过把智能体 API、云端 Codex、跨应用身份（Sign in with ChatGPT）以及算力密集型 Pro 500 套餐打包推出，OpenAI 同时在争取开发者、借助既有 ChatGPT 订阅锁定分发渠道，并把推理算力变现。 Dots 基于 OpenAI 的 GPT-6 Astra 模型运行，会根据用户反馈不断学习，发布时可接入包括 ChatGPT、Slack、Teams 在内的 4000 多个应用；Astra Ultrafast 并非新模型，而是 GPT-6 Astra 的加速服务档，用户在模型列表中选用，Pro 500 套餐的算力额度约为 Plus 的 25 倍并独享该档位。GPT-6.1 Sol 定位低于旗舰 GPT-6 Astra，事实性错误更少、在智能体任务中更可靠地遵守显式约束与用户意图，通过 API 以 gpt-6.1-sol 名称提供，但暂未在 ChatGPT 中上线。需要说明的是，本条消息属于简短二手汇总，缺乏基准测试或一手技术文档来佐证这些说法。

telegram · zaihuapd · 9月29日 17:52

**背景**: OpenAI 的 GPT-6 一代模型按能力分档，Luna 等更轻量模型与中档的 Sol 都位于旗舰 Astra 之下；「Sol」这一档专门面向编程与电脑操控场景，因此 GPT-6.1 Sol 会出现在智能体相关产品中。所谓「常驻」或「伴生」智能体是较新的产品形态：AI 在后台持续存在、接入你的各类工具并主动发起操作，而不是被动等待指令，Meta 的 Muse 是最直接的竞争对手。「Sign in with ChatGPT」把 OpenAI 账号与订阅额度延伸到 Devin、Notion 等第三方工具，而 Agents API 与 Decisions API 则让开发者能直接在 OpenAI 基础设施上构建电脑操控型智能体或轻量级的分类、路由与动作决策能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lifehacker.com/tech/openai-just-announced-dots-its-take-on-metas-muse">OpenAI Just Announced ' Dots ,' a New Type of Personalized AI Agent</a></li>
<li><a href="https://officechai.com/ai/openai-dots/">[Liveblog] OpenAI Announces Always-On AI Agents Named Dots</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT - 6 . 1 Sol | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI Agents`, `#LLM`, `#Developer APIs`, `#Model Release`

---