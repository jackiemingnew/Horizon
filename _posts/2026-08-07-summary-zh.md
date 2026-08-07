---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> 从 35 条内容中筛选出 12 条重要资讯。

---

1. [OpenAI 新模型 Astra 或达关键网络攻击能力，发布恐推迟](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Flash 0731 发布：速度更快、成本更低、支持本地运行](#item-2) ⭐️ 8.0/10
3. [科技从业者普遍悲伤，对职业失去信心](#item-3) ⭐️ 8.0/10
4. [Oracle 禁止 OpenJDK 使用 AI 生成代码](#item-4) ⭐️ 8.0/10
5. [App Store 拒稿：开发者因不存在的塔罗牌功能被拒](#item-5) ⭐️ 8.0/10
6. [用批处理、算子融合与 SIMD 让 Postgres 分析提速 300 倍](#item-6) ⭐️ 8.0/10
7. [2027 年内存产能据报道已售罄，AI HBM 需求成主因](#item-7) ⭐️ 8.0/10
8. [新墨西哥州法院裁定 Meta 因损害儿童心理健康赔偿 5.67 亿美元](#item-8) ⭐️ 8.0/10
9. [SpaceX 2027 年 10GW 算力或带来 3000 亿美元 ARR](#item-9) ⭐️ 8.0/10
10. [Gemini 长期受挫，或令 Google Cloud 短期受益](#item-10) ⭐️ 8.0/10
11. [美国审查中国 AI 企业海外获取英伟达芯片渠道](#item-11) ⭐️ 8.0/10
12. [sub2api 曝 OAuth 高危漏洞：仅凭邮箱即可接管账户](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 新模型 Astra 或达关键网络攻击能力，发布恐推迟](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/) ⭐️ 9.0/10

OpenAI 于 2026 年 8 月 7 日披露，其即将推出的模型 Astra 在内部评估中可能达到预备框架下的“关键”网络安全能力阈值。初步结果显示其在代理编码与网络安全方面进展显著，无法排除达到关键能力的可能性，因此扩大了安全测试范围并可能导致发布推迟。 如果 Astra 达到关键阈值，它可能无需人工干预即可自主发现并利用加固真实系统中的零日漏洞，或仅凭高层目标策划并执行端到端的新型网络攻击，从而带来严重的国家安全风险。这一进展可能重塑 AI 安全实践，影响监管监督，并左右全球前沿 AI 模型的发布时间表。 OpenAI 已暂停不符合强化安全要求的 Astra 相关内部活动，并实施了隔离测试环境、加密增强和通用监控等措施。公司将与政府机构和 AI 安全组织合作开展第三方测试。相比之下，此前 GPT-5.6-Sol 等模型在同一网络安全评估中仅被评为“高”。

telegram · zaihuapd · 8月7日 16:44

**背景**: OpenAI 预备框架是一套用于跟踪、评估和防范前沿 AI 可能带来的灾难性风险的结构化流程，网络安全是其核心追踪类别之一。代理编码（Astra 评估中突出的能力）指的是 AI 系统能够在最少人工干预的情况下规划、编写、测试和修改代码，这种能力既能提升生产力，也可能加剧网络威胁。该框架定义了低、中、高、关键等递进的能力等级，其中“关键”代表最高风险层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/updating-our-preparedness-framework/">Our updated Preparedness Framework - OpenAI</a></li>
<li><a href="https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf">Preparedness Framework - cdn.openai.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#cybersecurity`, `#frontier AI`, `#model evaluation`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 0731 发布：速度更快、成本更低、支持本地运行](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 8.0/10

DeepSeek 于 2026 年 7 月 31 日在官方 API 上公开测试发布了 V4 Flash 0731，该模型也出现在 ARC Prize 的结果页面上。早期用户反馈称，它是相比上一个 Flash 预览版的重大升级，在速度、成本效益和本地可用性方面都有显著提升。 此次发布意义重大，因为它让前沿级大语言模型足够便宜、足够快，可支持日常 agent 工作流，甚至能在高端 GPU 上本地部署。这可能会推动 AI/ML 从业者转向 DeepSeek，作为 Claude、GPT 等专有模型的高性价比替代方案。 据 lmstudio.ai 介绍，V4 Flash 0731 是一个 284B 参数的混合专家模型，激活参数为 13B，上下文窗口为 100 万 token。有用户在 2x RTX Pro 6000 Blackwell 上测得约 8k token/s 的预填充速度和单流约 250 token/s；另有用户表示，在 12 个并发流下每天花费不到 5 美元。

hackernews · tosh · 8月7日 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49214008)

**背景**: DeepSeek 是一家以发布性能强劲、成本有竞争力的大语言模型而闻名的中国 AI 实验室。V4 Flash 是介于预览版与完整版 V4 Pro 之间的快速高效型号；据官方网站介绍，V4-Flash API 已进入公开测试阶段，增强了 agent 能力，V4-Pro 暂时保持不变。ARC Prize 是一个用抽象推理基准评估 AI 系统的项目，其网站收录了该模型的测试结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepseek.com/en/index.html">DeepSeek</a></li>
<li><a href="https://lmstudio.ai/models/deepseek-v4-flash">DeepSeek V4 Flash - lmstudio.ai</a></li>
<li><a href="https://www.orcarouter.ai/blog/deepseek-v4-flash-official-release">DeepSeek V4 Flash: Cheap, Verbose, Matches V4 Pro at Math</a></li>

</ul>
</details>

**社区讨论**: 评论大多积极：LaurensBER 表示它“几乎可以处理所有事情”，成本低到可以忽略；ak_t 认为它比预览版“高出一个档次”，并称赞本地推理速度。但也有用户如 nylonstrung 反映出现无限循环、不调用工具等回归问题；另有用户提到自己 Claude 账号被封这一无关话题，因此并非所有反馈都是一致的。

**标签**: `#DeepSeek`, `#AI`, `#LLM`, `#ARC Prize`, `#Model Release`

---

<a id="item-3"></a>
## [科技从业者普遍悲伤，对职业失去信心](https://www.noemamag.com/why-is-everyone-in-tech-so-sad/) ⭐️ 8.0/10

《Noema》杂志的一篇文章探讨了科技从业者中普遍的悲伤情绪和对职业失去信心的现象，将其与印刷工等历史性行业的衰落相类比。文章着重指出有毒的网络环境对心理健康的损害，并引发了 409 条评论的讨论。 这篇文章捕捉到了整个行业的一种重要情绪，并引发了关于科技行业倦怠、工作文化以及科技职业可持续性的实质性讨论。它与许多感到幻灭的从业者产生共鸣，可能影响行业如何应对心理健康和工作满意度问题。 文章将科技行业的潜在衰落与延续数世纪的印刷行业相类比，后者因技术变革而消失。社区评论还提到 90 年代上网是为了逃避现实、如今下线是为了逃避网络这一反差，以及在没有独立经济来源的情况下难以转向所谓“脚踏实地”的职业。

hackernews · RickJWagner · 8月7日 12:42 · [社区讨论](https://news.ycombinator.com/item?id=49209539)

**背景**: 科技行业长期以来与乐观和高回报联系在一起，但如今许多从业者面临倦怠、裁员和意义感缺失。网络曾经是连接的地方，如今却变得充满敌意，加剧了心理健康问题。印刷行业等历史案例展示了当一个职业失去社会和经济基础时会发生什么。

**社区讨论**: 评论大多与文章主题产生共鸣，一位用户将科技的可能衰落比作印刷工的命运，另一位则指出网络毒性加剧。有人表达深深的幻灭感，也有人提醒说，没有经济保障，离开科技行业去从事“脚踏实地”的工作只是一种虚假的逃避。

**标签**: `#tech burnout`, `#mental health`, `#tech industry`, `#work culture`, `#community discussion`

---

<a id="item-4"></a>
## [Oracle 禁止 OpenJDK 使用 AI 生成代码](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code) ⭐️ 8.0/10

Oracle 发布了一项临时政策，禁止向 OpenJDK 提交包含由大型语言模型部分或全部生成内容的社区贡献。该政策发布在 openjdk.org/legal/ai，理由是法律与人工审查方面的顾虑，最终版本正由 Oracle 的法务团队起草。 该政策影响使用最广泛的开源 Java 平台之一，可能为开源项目如何处理 AI 生成代码开创先例。值得注意的是，Oracle 同时在大举投资 AI，这凸显了企业 AI 战略与法律风险管理之间的张力。 有评论者指出，该政策适用于社区提交，可能并不约束 OpenJDK 核心开发者。Oracle 表示，限制是为了应对“本就有限的人类审查者时间”并规避法律风险，最终政策仍由律师撰写中。

hackernews · delduca · 8月7日 17:36 · [社区讨论](https://news.ycombinator.com/item?id=49213754)

**背景**: OpenJDK 是 Java 平台标准版（Java SE）的免费开源实现，由 Sun Microsystems 于 2006 年启动，后来随公司被 Oracle 收购。它托管官方 JDK 源代码，贡献者既包括 Oracle 付费开发者，也包括更广泛的社区，因此 AI 生成代码带来了来源与法律责任方面的顾虑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenJDK">OpenJDK - Wikipedia</a></li>
<li><a href="https://openjdk.org/">OpenJDK</a></li>
<li><a href="https://www.azul.com/blog/what-is-openjdk/">What is OpenJDK & What is it Used For? | Azul</a></li>

</ul>
</details>

**社区讨论**: 评论者认为此举是法律策略，有人说 Oracle 是“一家挂着科技业务的律所”，希望保留对“AI 洗白”代码提起诉讼的能力。也有人指出政策范围似乎针对社区提交而非核心开发者；还有人认为，鉴于 Oracle 过去在 Java 版权问题上的纠纷，这一做法是明智的。

**标签**: `#OpenJDK`, `#Oracle`, `#AI-generated code`, `#Open Source`, `#Legal Policy`

---

<a id="item-5"></a>
## [App Store 拒稿：开发者因不存在的塔罗牌功能被拒](https://daringfireball.net/2026/08/app_store_rejection_of_the_week_dark_hours) ⭐️ 8.0/10

Daring Fireball 报道称，开发者 Godier 的 App 被苹果 App Store 拒绝，理由是审核人员声称该应用包含一项实时塔罗牌解读功能——然而该应用根本没有塔罗、星座或任何占星功能。即使逐级申诉至 App 审核委员会，委员会仍以同样错误的事实认定维持了最初的拒绝决定。 这一事件凸显了 App Store 审核流程的任意性和不透明性，执行标准似乎不一致，开发者几乎没有有效的申诉途径。这件事影响重大，因为数百万开发者依赖苹果平台，而反复无常的拒绝会给应用开发带来实际成本并产生寒蝉效应。 此次拒绝的理由是该应用具备一项实际并不存在的“实时塔罗牌解读功能”，而 App 审核委员会在申诉后仍明确确认了这一错误认知。评论者将此与 Co-Star 等以占星为核心且曾获得 App Store“编辑精选”的应用进行对比，并提到目前 App Store 提交审核停滞不前的报告。

hackernews · _da_ · 8月7日 18:59 · [社区讨论](https://news.ycombinator.com/item?id=49214863)

**背景**: App Store 审核流程是苹果对 iOS 应用的把关机制，每个应用在分发前都必须经过人工审核，而审核指南往往宽泛且执行不一致。开发者常把这个过程形容为“拜占庭式的官僚体系”，在上诉时，做出裁决的甚至可能是导致最初拒稿的同一套错误理解。由于应用商店事实上是大多数用户获取移动软件的唯一渠道，这类决定对开发者产生了格外大的影响。

**社区讨论**: 评论者大多对这一裁决感到愤怒又觉得好笑，DrJokepu 逐字引用了审核委员会荒谬的理由。szidev 指出明显的双重标准：占星应用 Co-Star 曾获“编辑精选”。MerrimanInd 认为由两家巨头把关应用分发是技术行业里“缓慢蔓延的腐烂”，并提到 Keep Android Open 运动；aliasxneo 和 guessbest 则补充说，审核结果随机，通过时间从一天到两周不等，而且目前有些开发者根本看不到任何审核通过。

**标签**: `#app-store`, `#ios`, `#developer-experience`, `#review-process`, `#platform-gatekeeping`

---

<a id="item-6"></a>
## [用批处理、算子融合与 SIMD 让 Postgres 分析提速 300 倍](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 8.0/10

pgrust（一个实验性的 Postgres Rust 重实现）的作者发表了一篇详细技术文章，展示了批处理、算子融合和 SIMD 如何让 Postgres 查询执行在分析负载下提速数百倍。文章还介绍了 pgrust 早期的正确性工作，包括对超过 1000 个函数与 PostgreSQL 进行形式化验证和差分模糊测试。 这项工作表明，Postgres 传统的一次处理一行的执行模型仍有巨大的性能提升空间。如果这些技术被证明可行，可能推动主流 Postgres 或其衍生系统达到专用列式、向量化分析数据库的性能水平。 优化后的查询引擎通过批处理在每次操作中处理多行，融合相邻算子以减少逐元组开销和物化，并利用 SIMD 指令开发数据级并行。作者强调，pgrust 的首要目标是正确性，而非单纯的原始速度，其通过形式化证明和差分模糊测试来保证与 PostgreSQL 的逻辑一致。

hackernews · poly2it · 8月7日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49208535)

**背景**: 传统 Postgres 采用一次一行、基于迭代器（Volcano 风格）的模型执行查询，每个算子逐个物化元组并向上传递，带来了大量 CPU 和内存开销。批处理将多行分组为向量，算子融合把多个算子合并为一次遍历以减少中间物化，而 SIMD 让单条 CPU 指令一次处理多个数据值。这些技术在现代列式与向量化数据库中已经很常见，但干净地应用到像 Postgres 这样的行式引擎仍然很困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/">Rebuilding Postgres for 300x faster analytics: batching, operator ...</a></li>
<li><a href="https://www.infoq.com/articles/columnar-databases-and-vectorization/">Columnar Databases and Vectorization - InfoQ</a></li>
<li><a href="https://www.starrocks.io/blog/deep-dive-how-starrocks-built-a-high-performance-vectorized-engine">Deep Dive: How StarRocks Built a High-Performance Vectorized Engine</a></li>

</ul>
</details>

**社区讨论**: 作者回应了大家可能关心的信任问题，表示正确性是第一优先级，形式化验证和差分模糊测试目前已覆盖超过 1000 个函数。有评论者仍对 pgrust 能否替代 Postgres 本身表示怀疑，认为关键在于机构信任和长期连续性，而非技术优劣。另一些人则对自适应规划表示兴奋，并提议将 pgrust 嵌入二进制以替代 SQLite/Turso；还有评论者提出用 ramfs/tmpfs 运行 Postgres 来提升速度的实用技巧。

**标签**: `#postgres`, `#performance`, `#rust`, `#query-engine`, `#SIMD`

---

<a id="item-7"></a>
## [2027 年内存产能据报道已售罄，AI HBM 需求成主因](https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out) ⭐️ 8.0/10

行业报告显示，2027 年的内存产能已被全部预订一空，主要原因是 AI 加速器使用的高带宽内存（HBM）需求激增。这一短缺使当前的供应紧张延续，并引发整个硬件和软件供应链的担忧。 2027 年之前的内存供应紧张可能拖慢 AI 硬件部署，并推高智能手机、笔记本电脑和游戏机等消费电子产品的价格。由于内存是整个计算行业的基础组件，此次短缺将产生广泛的经济和技术连锁反应。 HBM 的生产尤其消耗晶圆：在同一技术节点下，生产等量比特的 HBM 所需晶圆供应大约是 DDR5 的三倍，因此 HBM 产能爬坡会直接限制非 HBM 产品的供应增长。行业报告已指出 2026 年 HBM 供应全部售罄，如今据报道 2027 年产能也紧随其后售罄。

hackernews · inigyou · 8月7日 07:58 · [社区讨论](https://news.ycombinator.com/item?id=49207236)

**背景**: 高带宽内存（HBM）是一种 3D 堆叠 DRAM 接口，旨在为 AI 加速器和高性能计算提供极高的带宽。其生产主要由 SK 海力士、三星和镁光等内存三巨头主导，而随着 AI 模型对内存容量需求不断增大，HBM 需求急剧攀升。由于 HBM 芯片采用堆叠封装，裸片比普通 DRAM 更大，因此消耗了不成比例的晶圆产能，挤压了 PC 和服务器所用传统 DDR5 内存的产量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://enkiai.com/ai-market-intelligence/ai-supply-chain-crisis-2026-the-new-hbm-bottleneck/">AI Supply Chain Crisis 2026: The New HBM Bottleneck</a></li>
<li><a href="https://www.datagravity.dev/p/the-memory-triopoly">The Memory Triopoly - by Chris Zeoli - Data Gravity</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了多种实际关切：有人指出 HBM 与 DDR5 之间的晶圆权衡，有人担心需要囤积集成内存的微控制器，还有人提醒这可能对消费产品产生通胀效应。部分评论者也表示，由于 AI 给内存和存储供应带来压力，他们对于采用 AI 持谨慎态度。

**标签**: `#memory`, `#HBM`, `#AI hardware`, `#supply chain`, `#semiconductors`

---

<a id="item-8"></a>
## [新墨西哥州法院裁定 Meta 因损害儿童心理健康赔偿 5.67 亿美元](https://www.theguardian.com/technology/2026/aug/06/new-mexico-court-meta) ⭐️ 8.0/10

2026 年 8 月 6 日，新墨西哥州法院裁定 Meta 须支付 5.67 亿美元（部分报道称金额高达 9.42 亿美元）用于青少年心理健康项目，并须针对未成年用户做出整改。法院认定 Meta 违反了新墨西哥州的公共妨害法（NMSA 1978 § 30-8-1）。 这是美国州级法院针对社交媒体平台损害儿童心理健康开出的最大罚单之一，表明各州可借助公共妨害法追究科技公司责任。此案可能鼓励其他州提起类似诉讼，并促使 Meta 重新设计面向未成年人的算法与保护机制。 关于赔偿金额的报道并不一致：《卫报》和路透社报道为 5.67 亿美元，而《华尔街日报》标题为 9.42 亿美元；有评论者指出，按 Meta 在美加收入和新墨西哥州人口比例计算，9.42 亿美元这一数字相当可观。除罚款外，Meta 还被要求对未成年用户的使用体验做出整改，且该判决可能会被上诉。

hackernews · boplicity · 8月7日 00:06 · [社区讨论](https://news.ycombinator.com/item?id=49204352)

**背景**: Meta 旗下拥有 Facebook、Instagram 和 WhatsApp，其中 Instagram 的 Reels 和 TikTok 等短视频功能因算法推送容易让年轻用户上瘾而受到批评。公共妨害法通常用于整治危害公共健康或安全的行为，将其适用于社交媒体是一种较新的法律路径。新墨西哥州人口约 210 万，属于小州，因此数亿美元的判决对该州而言尤为重大。

**社区讨论**: 评论者大多认为这笔罚款仅占 Meta 全球收入的一小部分，但也有人指出，对于一个人口刚过 200 万的州来说，9.42 亿美元实际上非常庞大。其他人详细列出了本案涉及的新墨西哥州公共妨害法（NMSA 1978 § 30-8-1），并分享了自己沉迷 Instagram Reels 和 TikTok 的经历，有人形容它们“相当于网上的海洛因”。还有人认为，随着多国着手限制未成年人使用社交媒体，这一判决会进一步加剧 Meta 的财务与监管压力。

**标签**: `#Meta`, `#social media`, `#mental health`, `#regulation`, `#legal`

---

<a id="item-9"></a>
## [SpaceX 2027 年 10GW 算力或带来 3000 亿美元 ARR](https://newsletter.semianalysis.com/p/spacex-10gw-in-2027-why-its-real) ⭐️ 8.0/10

SemiAnalysis 预测，SpaceX 将在 2027 年部署 10GW（100 亿瓦）的 AI 算力，每年可产生高达 3000 亿美元的经常性收入（ARR）。微软预计将成为最大的承购方，这可能推动 Azure 云业务实现三位数增长。 这一预测将 SpaceX 的基础设施建设与 AI 推理经济性联系起来，表明大规模算力可以按每 GW 每年约 1000 亿美元（$100B/GW/year）的速度变现。如果微软成为主要承购方，将加剧云与 AI 领域的竞争，并使 Azure 获得重要的供给优势。 文章基于“每 GW 每年 1000 亿美元”的推理收入假设，并提到微软“2026 年 10GW 觉醒”作为前奏。这一预测具有投机性，要验证 SpaceX 的落地速度以及承购协议的落实情况。

rss · Semianalysis · 8月7日 20:08

**背景**: AI 推理是在训练完成后，让模型将学到的知识应用于新数据并产出结果，这个过程需要大规模的云端计算设施。在容量协议中，承购方（offtaker）是指承诺购买项目未来产出的买方，这种安排可以降低融资风险并保障收入。在此语境下，微软将作为 SpaceX 计划中算力容量的主要承购方。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.ibm.com/blog/AI-inference-explained">What is AI inferencing? - IBM Research</a></li>
<li><a href="https://www.investopedia.com/terms/o/offtake-agreement.asp">Understanding Offtake Agreements in Project Financing What Is An "Offtaker" In A Solar PPA Project? | Rob Freeman The state of BESS offtakes in the NEM: Tolls, revenue swaps ... Modern BESS offtake agreements: A guide for project ... Key considerations in battery storage offtake agreements What Are BESS Offtake and Optimization Agreements?</a></li>
<li><a href="https://scienceinsights.org/what-is-an-offtaker-in-energy-roles-and-ppas/">What Is an Offtaker in Energy? Roles and PPAs</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#AI Infrastructure`, `#Cloud Computing`, `#Microsoft Azure`, `#Inference`

---

<a id="item-10"></a>
## [Gemini 长期受挫，或令 Google Cloud 短期受益](https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking) ⭐️ 8.0/10

SemiAnalysis 的分析文章指出，DeepMind 的 Gemini 模型遇到的困难是长期战略失利，却可能为 Google Cloud 带来短期收益。文章将 Gemini 的困境重新定位为对谷歌云业务的一种潜在利好。 这之所以重要，是因为谷歌的 AI 战略在云计算和 AI 市场备受关注；即使 Gemini 表现不佳，GCP 仍可能承接对 AI 算力的需求。同时，这也凸显了内部模型研发与云基础设施变现之间的张力。 文章聚焦于 DeepMind 与 Google Cloud Platform 之间的战略互动，认为前沿模型上的长期失利不一定妨碍基础设施在短期内获利。摘要和正文中没有提供关于模型性能或 GCP 具体数字的详细说法。

rss · Semianalysis · 8月7日 02:32

**背景**: Gemini 是 Google DeepMind 推出的大语言模型系列，与 OpenAI 的 GPT 系统及其他前沿 AI 模型竞争。GCP（Google Cloud Platform）通过 Google Cloud 销售云计算服务，包括 TPU、GPU 等 AI 加速器。该分析认为，即使 Gemini 在模型竞赛中表现欠佳，企业仍可能涌向 GCP 采购算力，从而使云业务成为谷歌 AI 雄心的一种财务对冲。

**标签**: `#AI`, `#Google Cloud`, `#Cloud Computing`, `#Strategy`, `#Gemini`

---

<a id="item-11"></a>
## [美国审查中国 AI 企业海外获取英伟达芯片渠道](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 8.0/10

美国商务部工业与安全局（BIS）已启动系统性审查，调查中国 AI 企业如何在海外获取和使用英伟达芯片，包括通过租用他国算力进行远程访问的方式。此次审查部分源于月之暗面最近发布的 Kimi K3 模型性能表现，一名白宫官员曾公开指控该模型非法获取英伟达芯片。 此次审查可能重塑全球 AI 供应链和云计算格局，因为美国出口管制可能从实体芯片出货扩展到对海外算力资源的远程访问。若付诸实施，将直接影响中国 AI 企业、国际云服务商以及英伟达在关键市场的业务。 据报道，BIS 正在整理两份名单：一份是涉嫌将受限芯片走私入境中国的黑市所在地名单，另一份是中国企业远程租用芯片的国家名单。然而，限制远程访问的合法性尚存疑问，美国众议院两党法案拟明确授予该权力，但预计会遭到英伟达等科技公司反对。

telegram · zaihuapd · 8月7日 11:18

**背景**: 美国对华实施先进英伟达芯片出口管制，旨在限制中国 AI 能力，但中国企业一直寻求变通方案，包括利用海外子公司或租用由英伟达 GPU 驱动的境外云计算服务。月之暗面的 Kimi K3 模型拥有 2.8 万亿参数和 100 万 token 上下文窗口，近期其性能逼近美国同行，引发美方更严格的审视。另外，新加坡和美国当局正在调查英伟达客户 Megaspeed 涉嫌通过马来西亚向中国用户销售芯片，据报阿里巴巴通过一家新加坡壳公司参与其中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2025/10/10/singapore-us-investigate-nvidia-client-megaspeed-export-controls-violation.html">Singapore, U.S. investigate Nvidia client Megaspeed - CNBC</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#AI`, `#semiconductors`, `#export-controls`, `#US-China`, `#Nvidia`

---

<a id="item-12"></a>
## [sub2api 曝 OAuth 高危漏洞：仅凭邮箱即可接管账户](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 8.0/10

sub2api v0.1.171 及之前版本被披露存在 CVSS 8.8 的严重 OAuth 账户接管漏洞。攻击者只要知道受害者的注册邮箱，就能把自己的 OAuth 身份绑定到受害者账户，无需密码、验证码或用户交互，即可完全控制其 API 密钥、账单余额与订阅配额。 这是一个利用门槛极低的高危漏洞，可对用于拼车共享 Claude、OpenAI、Gemini 等订阅的开源 AI API 中转服务造成完整账户接管。受影响用户的付费配额和账单余额可能被盗，该漏洞也反映出 AI 工具生态中 OAuth 实现的普遍风险。 漏洞位于 OAuth pending session 交换流程中：existingUser 分支不校验密码和验证码，攻击者可将目标用户 ID 设为受害者并完成 OAuth 身份绑定。此后攻击者每次 OAuth 登录都会解析为受害者账户；公开报告中未确认 v0.1.171 之后是否有修复版本。

telegram · zaihuapd · 8月7日 14:59

**背景**: sub2api 是一个开源的一站式中转服务，将 Claude、OpenAI、Gemini、Antigravity 等 AI 订阅统一接入，支持拼车共享以降低成本并方便团队管理 API 用量。OAuth 是常见的授权框架，但若 pending session 或账户绑定流程实现不安全，就可能被滥用来将攻击者身份绑定到受害者账户，这是 OAuth 账户接管攻击中的常见模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Wei-Shaw/sub2api/issues/5350">OAuth Account Takeover via Pending Exchange Bypass in sub2api</a></li>
<li><a href="https://github.com/Wei-Shaw/sub2api">GitHub - Wei-Shaw/sub2api: Sub2API 一站式开源中转服务，让 Claude、Openai 、Gemini、Grok订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。</a></li>
<li><a href="https://desecurity.github.io/hacktricks/pentesting-web/oauth-to-account-takeover.html">OAuth to Account takeover - HackTricks</a></li>

</ul>
</details>

**标签**: `#security`, `#OAuth`, `#vulnerability`, `#account takeover`, `#sub2api`

---