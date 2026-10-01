---
layout: default
title: "Horizon Summary: 2026-10-01 (ZH)"
date: 2026-10-01
lang: zh
---

> 从 34 条内容中筛选出 7 条重要资讯。

---

1. [DeepSeek 开源华为昇腾平台基础组件](#item-1) ⭐️ 9.0/10
2. [谷歌发布前沿模型 Gemini 4 Argon，仍处早期预览阶段](#item-2) ⭐️ 8.0/10
3. [团队公开推翻"不用 MCP"立场，引发激烈讨论](#item-3) ⭐️ 8.0/10
4. [32 位研究者联合发布现代 NLP 分词综述](#item-4) ⭐️ 8.0/10
5. [Cloudflare 宣布进军公共证书颁发机构市场](#item-5) ⭐️ 8.0/10
6. [Kimi K3 经 Baseten 接入 OpenAI Codex 企业付费通道](#item-6) ⭐️ 8.0/10
7. [Reddit 将停用 RSS 订阅并关闭公开 API 访问](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek 开源华为昇腾平台基础组件](https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww) ⭐️ 9.0/10

2026 年 9 月 30 日，DeepSeek 正式开源面向华为昇腾算力平台的一整套基础组件，涵盖 TileLang 高级语言编译工具链、高性能计算库与分布式通信库，并明确表示这些组件与其此前面向英伟达（GPU）平台开源的组件一一对应。本次开源包括 DeepGEMM Ascend、DeepEP Ascend、TileKernels、FlashMLA 和 DeepSelect，DeepSeek 还表示正与华为联合推进昇腾 950 的 128 卡超节点方案。 这是一次直指英伟达 CUDA 生态壁垒的软件栈布局：DeepSeek 把其在 GPU 上使用的同一套编译工具链、算子库和通信原语移植到昇腾，显著降低了开发者和模型团队将工作负载迁移到国产硬件上的成本。对国产 AI 生态而言意义更大，因为阻碍非英伟达加速器落地的往往不是芯片峰值算力，而是成熟可用的高性能开源软件库。 DeepSeek 称相关组件在多项测试中性能接近硬件上限；DeepGEMM Ascend  reportedly 与 DeepGEMM 完全 API 兼容，支持 BF16、FP8、FP4 GEMM、MQA logits 以及 MegaMoE，开发者可以沿用与其他平台相同的 API 与开发流程。需要留意的是，本次信息来源为一段简短的聚合摘要，缺乏技术细节与社区讨论，因此性能宣称与具体开源范围尚未经过独立验证。

telegram · zaihuapd · 9月30日 03:09

**背景**: 昇腾是华为的 AI 加速器产品线，其软件栈 CANN 长期以来成熟度远不及英伟达的 CUDA，这也是国内多数 AI 训练与推理仍跑在英伟达 GPU 上的原因。本次开源中的 TileLang 是由北京大学团队主导、2025 年 1 月开源的高性能 AI 算子领域特定语言（DSL），它基于“Tile（张量分块）”抽象，让开发者以接近数学公式的方式描述计算意图，由编译器自动完成循环优化与内存调度。DeepEP 是面向专家并行（MoE 模型所需的 all-to-all dispatch/combine 通信核）的通信库，DeepGEMM 则是高性能 GEMM 算子库，二者最初都是为英伟达 GPU 打造的。昇腾 950 是华为的下一代芯片，而“超节点”指的是高度互联的多卡集群形态，这里是 128 卡配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepGEMM-Ascend">GitHub - deepseek-ai/DeepGEMM-Ascend: DeepGEMM-Ascend: clean ...</a></li>
<li><a href="https://zglg.work/ai/news/zh/2026-09-30-deepseek-open-sources-ascend-infrastructure-tilelang-deepgemm-and-deepep">DeepSeek开源昇腾基础组件：TileLang、DeepGEMM与DeepEP同批落地 | zg...</a></li>
<li><a href="https://baike.baidu.com/item/TileLang/67440655">TileLang - 百度百科</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Huawei Ascend`, `#open source`, `#AI infrastructure`, `#compilers`

---

<a id="item-2"></a>
## [谷歌发布前沿模型 Gemini 4 Argon，仍处早期预览阶段](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) ⭐️ 8.0/10

谷歌发布了 Gemini 4 Argon，称其是面向真实世界编程、企业知识工作与网络防御的新一代前沿模型，定位在 2026 年 9 月前陆续推出的 Gemini 3.8 系列之上。关键在于该模型尚未全面开放：谷歌表示会继续收集早期测试者的反馈并迭代安全护栏，之后才会尽快向开发者、企业和消费者开放 Argon。 这次发布是今年以来前沿实验室快速交替领先的又一个例证，动摇了曾经颇具影响力的“赢家通吃”理论——即最先取得领先的实验室将永不失去优势。对企业和开发者而言，这进一步说明能力领先地位已分散于超大规模云厂商、新兴云厂商和初创公司之间，因此工作流设计应确保模型供应商可以随时替换。 谷歌明确列出了三大目标领域——软件工程、法律等企业知识工作，以及网络防御——并提到 Argon 智能体正在谷歌内部承担将 C/C++ 代码库迁移到 Rust 的工作。由于 Argon 仍属早期预览，官方定价与公开基准成绩尚未最终确定，而“迭代安全护栏”的说法也意味着正式发布前访问条件可能还会变化。

hackernews · bradleyg223 · 9月30日 20:04 · [社区讨论](https://news.ycombinator.com/item?id=49913571)

**背景**: 前沿模型指的是某一时点最先进的通用人工智能系统，通常以超大规模参数以及处理复杂多步推理和智能体工作流的能力来界定。谷歌的 Gemini 系列是其旗舰模型产品线，每一代数字版本都接替上一代；而“早期预览”发布是业界常见做法，即先向特定测试者和合作伙伴展示模型，再向公众开放。谷歌将 Argon 的定位聚焦于编程、企业知识工作和网络防御，反映出各实验室当前认为前沿能力最具商业价值、最易落地的需求方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon - The Keyword</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/google-gemini-4-argon-ai.html">Google rolls out Gemini 4 Argon, its most advanced model - CNBC</a></li>
<li><a href="https://www.datacamp.com/blog/gemini-4-argon">Gemini 4 Argon: Benchmarks, Pricing, and Access | DataCamp</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论热度极高（约 921 分、631 条评论），且内容相当有深度。一条被广泛引用的经历称，Gemini 3.8 Flash 自主地用 GDB 附加到 GPU 驱动、逆向工程内核队列 ioctl 并编写 LD_PRELOAD C 垫片，从而让 ROCm 版的 llama.cpp 跑起来，评论者认为这是能力真正跃升的证据；另一条高赞观点则认为，Dario Amodei 关于“集中化”的赢家通吃论已被如今分散的竞争格局所证伪。也有人调侃谷歌又一次“发布了尚未发布的模型”，而最实用的建议是让模型与供应商都保持可替换，从而让智能本身变成一种商品。

**标签**: `#AI`, `#LLM`, `#Google Gemini`, `#model-release`, `#AI-competition`

---

<a id="item-3"></a>
## [团队公开推翻"不用 MCP"立场，引发激烈讨论](https://earendil.com/posts/you-said-no-mcp/) ⭐️ 8.0/10

一篇题为《You said no MCP》的文章作者团队公开推翻了自己此前对 Model Context Protocol（MCP）的坚决否定，并解释了如今转而支持这一标准的理由。这次"反转"在 Hacker News 上引发了 610 分、340 条评论的热议，讨论很快演变成一场关于 MCP 与基于 CLI 的智能体工具孰优孰劣的大辩论。 这次公开反转之所以重要，是因为今年早些时候 MCP 曾被大量有影响力的声音宣判"已死"，并把命令行工具捧为赢家，却常常忽视 MCP 在安全性、可观测性、部署与运维上的优势。如果更多团队跟进，MCP 作为 AI 智能体默认集成层的地位——而非临时拼接的 CLI 封装——可能会在整个开发者工具生态中得到进一步巩固。 文章与评论者都承认，MCP 在当前形态下并非性能最优、也谈不上稳健与统一，但他们认为普适性和终端用户的兼容性才是决定性因素——有人将其类比为 USB-C、NVMe 和 HDMI：这些技术虽有缺陷却极为成功。还有评论者引用了 Armin Ronacher 的观察：人们捍卫强烈观点时，常用的往往是早已过时的论据。

hackernews · yarapavan · 9月30日 09:55 · [社区讨论](https://news.ycombinator.com/item?id=49906637)

**背景**: Model Context Protocol 是 Anthropic 于 2024 年 11 月推出的开放标准与开源框架，旨在统一大语言模型等 AI 系统与外部工具、数据源和工作流的连接方式，常被形容为"AI 的 USB-C 接口"。此后它被 OpenAI、Google DeepMind 等主要 AI 厂商采纳。与之相对的另一条路线是基于 CLI 的智能体工具：AI 智能体在终端中运行，直接访问文件系统、shell 和开发工具，能够自主编辑文件、运行测试并提交代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://github.com/bradAGI/awesome-cli-coding-agents">Awesome CLI Coding Agents - GitHub</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的情绪褒贬兼有，但整体偏向支持这次反转：gk1 称赞团队愿意公开改变长期坚持的信念，并引用 Armin Ronacher 关于"过时论据"的观点；CharlieDigital 则认为这个结论早在今年 3 月就已显而易见，并批评那些宣称 MCP 已死的意见领袖。alin23 表示自己在编程之外也大量使用 MCP，将其嵌入 rcmd、Clop、Lunar 等 macOS 应用，使其即便搭配本地模型也能用自然语言完成配置；_fw 则总结出一种务实态度：MCP 或许不够理想，但"有总比没有好"，因为它兼容性广，而且会随着时间不断改进。

**标签**: `#MCP`, `#AI agents`, `#developer tooling`, `#LLM integration`, `#Hacker News discussion`

---

<a id="item-4"></a>
## [32 位研究者联合发布现代 NLP 分词综述](https://www.reddit.com/r/MachineLearning/comments/1wuccjf/tokenization_a_survey_for_modern_nlp_r/) ⭐️ 8.0/10

在大约八个月的时间里，32 位分词研究者合作完成了他们所称的现代 NLP 领域最全面的分词综述，内容涵盖算法、评估、多语言性、编码方式与理论，并已通过 alphaXiv 公开发布。该综述还探讨了可能取代分词器的方案，例如潜空间分词（latent tokenization）与视觉分词（visual tokenization），并涉及受限生成（constrained generation）、token healing 以及分词器安全等相邻议题。 分词虽然几乎影响所有 NLP 任务，却长期被视为研究不足的环节，因此这份由多方合作完成的综述把算法、评估方法、多语言表现与安全风险整合在一起，有望成为从业者与入门者的标准参考入口。它同时表明，学界正在认真讨论是否应当用潜空间或视觉表示彻底取代离散的子词分词器。 该综述属于文献综合而非提出新模型或新基准，因此其价值在于梳理和比较现有方法，而不是报告新的实验结果。除核心分词算法外，它还专门讨论了若干密切相关的议题，例如受限生成、token healing（在推理阶段修复提示词边界处分词痕迹的方法）以及分词带来的安全问题。

reddit · r/MachineLearning · /u/mcmcmcmcmcmcmcmcmc_ · 9月30日 18:13

**背景**: 分词是把原始文本切分为子词单元（即 token）的预处理步骤，语言模型实际读取和预测的正是这些 token，常用算法包括 BPE、WordPiece 和 Unigram 语言模型。由于模型并不直接看到字符，token 边界会影响到词表大小、多语言公平性，乃至提示词行为与输出格式。token healing 针对的是一个已知问题：当提示词在某个 token 中间结束时，模型生成的第一个 token 会被不自然地切开；而受限生成则强制解码器输出符合语法、正则表达式或结构化模式的文本。较新的研究还在探索潜空间 token——即无法直接对应自然语言词的可学习向量——作为固定离散词表的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://guidance.readthedocs.io/en/latest/example_notebooks/tutorials/token_healing.html">Token healing — Guidance latest documentation</a></li>
<li><a href="https://insertchat.com/glossary/constrained-generation">Constrained Generation in nlp - InsertChat</a></li>
<li><a href="https://arxiv.org/pdf/2505.12629">Enhancing Latent Computation in Transformers with Latent Tokens</a></li>

</ul>
</details>

**标签**: `#NLP`, `#tokenization`, `#survey`, `#language modeling`, `#machine learning`

---

<a id="item-5"></a>
## [Cloudflare 宣布进军公共证书颁发机构市场](https://blog.cloudflare.com/cloudflare-certificate-authority/) ⭐️ 8.0/10

Cloudflare 宣布计划成为公共证书颁发机构（CA），已申请加入 Chrome、Apple、Microsoft 和 Mozilla 的根证书计划，并与 GlobalSign 签署协议以收购一个被广泛信任的根证书。目前尚未开始签发证书，但 Cloudflare 表示将优先支持基于 ACME 的自动化签发与续期，并计划在 2027 年第一季度签发生产级默克尔树证书（MTC），以服务后量子时代的互联网。 Cloudflare 本身就为互联网上相当大比例的流量终止 TLS 连接，拥有受信任的根证书意味着它可以绕过第三方 CA 直接签发证书，这有望为其客户简化 PKI 流程，并在价格与自动化层面给现有 CA 厂商带来压力。其“ACME 优先”和后量子路线图还可能推动整个行业更快接受默克尔树证书以及更短有效期的证书模式。 默克尔树证书（MTC）是一种正在 IETF 标准化的新型 X.509 证书形式（草案 draft-ietf-plants-merkle-tree-certs），它把类似证书透明度（CT）的公共日志记录直接集成进证书，从而即使采用体积庞大的后量子签名算法，也能将证书和日志开销保持在较低水平。由于该计划仍依赖各根证书计划的审批以及从 GlobalSign 收购根证书，时间表仍可能变化，目前用户尚无法使用其签发服务。

telegram · zaihuapd · 9月30日 06:26

**背景**: 证书颁发机构（CA）是一种受信任的实体，负责对 TLS 证书进行数字签名；浏览器和操作系统只有在证书能够链接到其根存储中已信任的根证书时才会接受它。要进入 Chrome 根存储或 Mozilla CA 计划这类项目，需要经历漫长的审计与审查流程，因此从 GlobalSign 收购一个现成的受信任根证书，是一条被广泛认可的捷径。ACME（RFC 8555）是为 Let's Encrypt 设计的协议，可实现证书签发与续期的自动化；而后量子密码学则指能够抵御未来量子计算机攻击的算法，但其密钥和签名体积很大，给 TLS 证书带来了新的效率难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/">draft-ietf-plants-merkle-tree-certs-06 - Merkle Tree Certificates</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment">Automatic Certificate Management Environment - Wikipedia</a></li>
<li><a href="https://www.encryptionconsulting.com/education-center/merkle-tree-certificates/">Merkle Tree Certificates (MTC) Explained</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#Certificate Authority`, `#PKI`, `#ACME`, `#Post-Quantum`

---

<a id="item-6"></a>
## [Kimi K3 经 Baseten 接入 OpenAI Codex 企业付费通道](https://36kr.com/newsflashes/4005691489112198) ⭐️ 8.0/10

美国 AI 基础设施公司 Baseten 宣布，企业用户现可在 OpenAI 的编程工具 Codex 中调用 Kimi K3，相关推理费用直接计入企业已有的 OpenAI 采购承诺额度，无需另行开通新供应商的采购流程。这使 Kimi K3 成为首个进入 OpenAI 企业付费结算体系的中国开源模型。 企业 AI 采购正日益向少数几份大额承诺消费合同集中，因此允许通过既有的 OpenAI 采购承诺为中国开源模型付费，能大幅降低已把预算锁定在 OpenAI 的企业尝试新模型的门槛。这也标志着中国大模型与美国企业采购体系之间出现了新一层的互通，对 Moonshot AI、Baseten、OpenAI 以及企业模型采购方都具有影响。 Kimi K3 是 2026 年 7 月 16 日发布的 2.8 万亿参数混合专家（MoE）开源权重模型，其自定义许可证要求年收入超过 2000 万美元的推理服务商分享最高 30% 的收入，而 Baseten 本身就是推理服务商，这一条款因此值得关注。值得注意的是，模型的路由与计费均由 Baseten 提供，而非来自 OpenAI 与 Moonshot AI 之间的直接商业协议。

telegram · zaihuapd · 9月30日 11:23

**背景**: Kimi 是中国公司 Moonshot AI 的大语言模型系列，其旗舰 K3 被称为迄今发布过的最大开源权重模型，性能可与 OpenAI、Anthropic 的前沿模型竞争。OpenAI Codex 是 OpenAI 的编程智能体，2025 年 4 月以 Codex CLI 形式发布，如今还可通过 ChatGPT 网页版、桌面应用以及多种 IDE 集成使用。Baseten 是一家 AI 推理平台，按用量提供模型部署、推理与训练服务的云定价。许多大型企业通过“承诺消费”（committed spend）协议采购 AI，即预付一笔最低金额，所有符合条件的用量都从该额度中扣减——Baseten 此次正是搭上了这一机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K3">Kimi K3</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Baseten">Baseten</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Kimi K3`, `#OpenAI Codex`, `#Enterprise AI`

---

<a id="item-7"></a>
## [Reddit 将停用 RSS 订阅并关闭公开 API 访问](https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/) ⭐️ 8.0/10

Reddit 宣布将于 11 月 13 日停止支持 RSS 订阅，并计划在 2027 年 3 月前关闭公开 API 访问，理由是其已成为大规模抓取与自动化滥用（尤其是 AI 机器人）的主要渠道。公司建议版主转向使用 Discord Relay，并通知第三方应用与机器人开发者必须在 2027 年 1 月 12 日前完成注册，否则将被移除 API 访问权限。 RSS 与公开 API 是第三方 Reddit 客户端、版务机器人、内容存档项目以及学术研究的基础设施，一旦取消，大量并非由 Reddit 官方构建的工具将直接失效。这也延续了平台为应对 AI 训练爬虫而收紧数据访问的行业趋势，使开放、可机读的网页生态进一步收缩。 RSS 是一种轻量、公开规范的 XML 格式，任何阅读器无需认证即可轮询，因此取消它等于切断了无需抓取、低带宽的 Reddit 内容跟进方式。关键节点是 2027 年 1 月 12 日的 API 注册截止日期，随后在 2027 年 3 月彻底关闭公开 API；而版务工作流将改用 Discord Relay 这一封闭的、基于聊天工具的替代方案，取代原有的开放订阅标准。

telegram · zaihuapd · 10月1日 00:27

**背景**: RSS（Really Simple Syndication）让网站把更新发布为标准 XML 文件，订阅阅读器会定期检查并把更新内容下载到用户界面，因此长期是新闻聚合和自建机器人的基础设施。Reddit 的公开 API 对开发者起着类似作用，支撑着移动客户端、版务工具和数据研究流水线；早在 2023 年，Reddit 推出 API 收费并导致多款第三方应用关停时就已引发大规模抗议。Discord Relay 类工具则把内容推送到 Discord 服务器和频道中，提供受控、需认证的分发渠道，取代任何人都能读取（包括 AI 爬虫）的开放订阅源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/RSS">RSS - 维基百科，自由的百科全书 - zh.wikipedia.org</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2017735765103236977">RSS 原理介绍：从零理解信息订阅的本质 - 知乎</a></li>
<li><a href="https://getrelaybot.com/">Relay · Discord support without the panel</a></li>

</ul>
</details>

**标签**: `#Reddit`, `#Public API`, `#RSS`, `#AI Scraping`, `#Platform Policy`

---