---
layout: default
title: "Horizon Summary: 2026-10-27 (ZH)"
date: 2026-10-27
lang: zh
---

> 从 40 条内容中筛选出 8 条重要资讯。

---

1. [OpenAI 宣称指数时间假说不成立，并给出杨–米尔斯与 QCD 证明](#item-1) ⭐️ 9.0/10
2. [预印本声称证伪了指数时间假设](#item-2) ⭐️ 9.0/10
3. [Anthropic 提交 S-1 上市申请，披露巨额算力采购承诺](#item-3) ⭐️ 9.0/10
4. [OpenAI 发布 GPT-6.1 Terra：定位中端、价格大幅下调](#item-4) ⭐️ 8.0/10
5. [微软向约四分之一员工提供大规模自愿离职买断方案](#item-5) ⭐️ 8.0/10
6. [西北大学用单正电子量子回旋仪将单个正电子囚禁数月](#item-6) ⭐️ 8.0/10
7. [马斯克称 SpaceX 完成 400 亿美元 GPU 债务融资，并预言 neocloud 大洗牌](#item-7) ⭐️ 8.0/10
8. [Anthropic：违规用户贡献了公司 5%–7% 的收入](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 宣称指数时间假说不成立，并给出杨–米尔斯与 QCD 证明](https://openai.com/index/building-scientific-understanding-with-academic-communities/) ⭐️ 9.0/10

OpenAI 公布了三项与学术界合作完成的研究成果：一个确定性算法，可在 (n+m)^{O_k(1)}·2^{n/(log n)^{1/2+o(1)}} 时间内精确统计任意 k-CNF 公式的可满足赋值个数——该复杂度属于次指数级，因此否定了指数时间假说（ETH）。此外，OpenAI 称其模型分别于 2026 年 9 月 9 日和 9 月 18 日生成了杨–米尔斯存在性与 QCD 的自然语言证明，其中杨–米尔斯的工作一直推迟到 2026 年 10 月 16 日完成 Lean 形式化后才对外发布。 ETH 是细粒度复杂性与参数化复杂性中大量困难性结论和下界证明所依赖的核心假设，因此若否定成立，相关文献将被迫大面积重新审视。物理方面的声明更为惊人：其目标属于千禧年大奖难题量级的开放问题，且据称已在 Lean 中完成机器验证，这意味着 AI 系统可能开始参与基础科学的发现，而不仅是辅助日常研究。 2^{n/(log n)^{1/2+o(1)}} 的运行时间仍是超多项式的，因此否定 ETH 本身并不等于证明 P = NP，它只打破了「不存在次指数时间算法」这一具体的困难性假设。这些声明极其重大，目前主要依据 OpenAI 自己的公告；不过杨–米尔斯结果已完成 Lean 形式化，至少为该结论提供了部分可机器检验的证据。

hackernews · jonluca · 10月26日 21:35 · [社区讨论](https://news.ycombinator.com/item?id=50251344)

**背景**: 指数时间假说由 Impagliazzo 与 Paturi 于 1999 年提出，其内容是 3-SAT 无法在 2^{o(n)} 的次指数时间内求解；它比 P ≠ NP 更强，常被用来论证许多现有算法本质上已是最优。计算复杂性理论总体上按问题所需的时间和存储资源对其进行分类，而 P 与 NP 之争正是该领域的核心开放问题之一，也是千禧年大奖难题之一。Lean 是一个交互式证明助手，证明需用形式逻辑书写，以便计算机逐步检验每一个推理；正因如此，一份完成的 Lean 形式化被视为比自然语言论证强得多的证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exponential_time_hypothesis">Exponential time hypothesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computational_complexity_theory">Computational complexity theory</a></li>
<li><a href="https://www.datacamp.com/blog/openai-math-breakthroughs-what-the-latest-results-mean">OpenAI's AI Math Breakthroughs: What the Latest Results... | DataCamp</a></li>

</ul>
</details>

**社区讨论**: 评论者大多震惊不已，有人表示自己原本绝不相信 ETH 会被推翻，并感叹各类长期猜想接连倒下的速度令人恍如隔世（「2026 年真是诡异」）。有讨论追问否定 ETH 是否会在实质上让人更倾向于相信 P = NP，也有人指出论文作者之一就在讨论区中现身，同时还有人对杨–米尔斯与 QCD 的声明之大胆表示谨慎。

**标签**: `#AI for science`, `#mathematics`, `#computational complexity`, `#physics`, `#OpenAI`

---

<a id="item-2"></a>
## [预印本声称证伪了指数时间假设](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) ⭐️ 9.0/10

一篇题为《指数时间假设是错的》的预印本被发布在 OpenAI 于 GitHub 上的公开数学仓库中，声称推翻了指数时间假设（ETH）——即 1999 年提出、至今未被证明的“3-SAT 无法在次指数时间内求解”这一假设。该论文标注日期为 2026 年 10 月 25 日，并与另外两项分别属于数学、计算机科学和物理学的新发现一同公布。 ETH 是一个承重式的困难性假设：大量条件性下界都建立在它之上，用来论证许多现有算法已经接近最优，覆盖参数化复杂度、细粒度算法，甚至包括“除非 SETH 不成立，否则自注意力必须是平方时间”这类结论。如果该证明成立，那么一大批“不存在更好算法”的论断将失去依据，这将是复杂度理论中的范式转移。 论文本身也提醒，形如 2^o(n) 的运行时间界在一般多项式时间归约下并不能传递（这种传递需要 2^{n^o(1)} 形式的界），因此该结果并不意味着一般 NP 问题存在次指数时间算法。换言之，它并不是对 NP ⊆ SUBEXP 的证明，而且最坏情况下的渐近界对实际的 SAT 求解影响甚微。

hackernews · vok · 10月26日 21:59 · [社区讨论](https://news.ycombinator.com/item?id=50251661)

**背景**: 在计算复杂度理论中，由 Impagliazzo 与 Paturi 于 1999 年提出的指数时间假设认为：求解 3-SAT（判断一个 3-CNF 布尔公式是否存在可满足赋值）至少需要 2^{s₃n} 的时间，其中 s₃ > 0 为某常数，也就是说不存在 2^o(n) 的次指数算法。ETH 比 P ≠ NP 更强：它能推出 P ≠ NP，但反过来不成立。更强的一个版本是强指数时间假设（SETH），它对子句长度不受限制的 k-SAT 作出类似断言，被广泛用于推导具体问题的紧下界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exponential_time_hypothesis">Exponential time hypothesis - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Strong_Exponential_Time_Hypothesis">Strong Exponential Time Hypothesis</a></li>
<li><a href="https://web.stanford.edu/class/cs354/scribe/lecture17.pdf">Lecture 17: The Strong Exponential Time Hypothesis</a></li>

</ul>
</details>

**社区讨论**: 评论者称这一结果令人惊叹且出人意料，但同时谨慎地限定其适用范围：有人指出 ETH 被证伪并不意味着 NP 问题可以在次指数时间内求解，因为 2^o(n) 的界无法通过多项式时间归约传递。也有人追问，若 SETH 不成立，是否意味着自注意力可以做到次平方时间、大模型推理会更便宜；还有人询问该方法对 SAT 求解器是否有近期可用之处，并感叹这类复杂度类分离结果极为罕见。

**标签**: `#complexity-theory`, `#exponential-time-hypothesis`, `#theoretical-computer-science`, `#SAT-solving`, `#algorithms`

---

<a id="item-3"></a>
## [Anthropic 提交 S-1 上市申请，披露巨额算力采购承诺](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm) ⭐️ 9.0/10

Anthropic 已向美国证券交易委员会（SEC）提交 S-1 注册声明，这是其迈向公开上市的第一步，文件披露了约 1140 亿美元对 Google、1100 亿美元对 AWS、1610 亿美元对 Broadcom、1200 亿美元对 SpaceX 的算力采购承诺。文件同时显示营收快速增长，有评论者指出每 1 美元算力支出对应的收入已从 2025 年第一季度的约 0.40 美元升至如今的约 2.08 美元。 这是外界首次得以详细审视一家头部前沿实验室的财务结构，使原本高度保密的业务变成投资者和竞争对手可以真正检视的对象。由于 Anthropic 的承诺横跨多家超大规模云厂商和芯片供应商，其资产负债表实际上反映出整个人工智能基础设施建设是如何被融资的，以及整个行业押注了多大的需求增长。 这些承诺异常集中且横跨多个供应商，既包括两家超大规模云厂商（Google、AWS），也包括定制芯片合作伙伴 Broadcom 和一个非传统的算力来源（SpaceX）。文件的风险因素部分也提到了开源与开放权重模型，但社区读者指出，相对于一些人认为中国开放权重实验室带来的威胁，这些提及显得相当稀少。

hackernews · SiNTEx · 10月26日 13:04 · [社区讨论](https://news.ycombinator.com/item?id=50242939)

**背景**: S-1 是公司在首次公开募股（IPO）前向 SEC 提交的注册声明，需披露其商业模式、财务状况、风险因素以及重大合同义务；通常先以保密方式提交，随后在上市前公开。对人工智能实验室而言，最具分量的披露是算力合同，因为训练和运行前沿模型需要提前数年锁定海量的 GPU 与数据中心容量。Anthropic 是 Claude 系列模型的开发商，也是 Claude Code 的打造者，后者是一款在软件行业迅速普及的智能体式编程工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/s/sec-form-s-1.asp">What Is SEC Form S-1? Filing Steps & Amendment Guidelines</a></li>
<li><a href="https://penchan.co/en/market/ai/anthropic/compute-and-supply-chain/">Anthropic's Compute Gamble: Three Clouds , Three Chips... | Penchan</a></li>
<li><a href="https://presenc.ai/research/ai-compute-commitments-tracker-2026">AI Compute Commitments Tracker 2026 | Presenc AI</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（1459 分、1426 条评论）聚焦于这些承诺背后的需求是否可持续：一位高赞评论者认为，Anthropic 的押注只有在收入增长约十倍时才成立；另一位则警告称，收入激增高度集中于 AI 编程领域，而该领域的采用速度不太可能延续过去一年的复合增速。还有人强调算力回本经济性的显著改善，并批评招股书低估了中国开放权重模型作为竞争风险的分量。

**标签**: `#anthropic`, `#ipo`, `#sec-filing`, `#ai-industry`, `#business-strategy`

---

<a id="item-4"></a>
## [OpenAI 发布 GPT-6.1 Terra：定位中端、价格大幅下调](https://openai.com/index/introducing-gpt-6-1-terra/) ⭐️ 8.0/10

OpenAI 发布了 GPT-6.1 Terra，这是 GPT-6.1 系列中定位低于 GPT-6.1 Sol 的中端模型，定价为每百万输入 token 1.00 美元、每百万缓存输入 token 0.05 美元、每百万输出 token 5.00 美元。这一定价延续了 OpenAI 此前从 GPT-5.6 Sol 到 GPT-6.1 Sol 约 75%的降价轨迹，使 Terra 的价格约为 Sol 的一半。 此次发布重新划定了 OpenAI 自家产品线内部的价格与性能阶梯，使中端模型的价格低到足以承载过去只能交给小模型或竞争对手的高并发智能体与编程任务。这也被普遍解读为对 Claude Sonnet 5.5 等竞品的直接施压，因为决定开发者最终部署哪个模型的，越来越多是单位任务成本而非单纯的基准分数。 GPT-6.1 Terra 支持文本与图像输入，拥有 100 万 token 的上下文窗口，官方强调其在理解截图和屏幕内容方面尤为擅长，并继承了 GPT-6 系列的对齐改进——OpenAI 称它比 GPT-5.6 Terra 更能保持在任务范围内并如实说明局限。问题在于定位：社区对 TerminalBench 4.0 单位任务成本数据的分析发现，很难看出开发者在该场景下为何要选择 Terra 而非 Sol。

hackernews · meetpateltech · 10月26日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=50248124)

**背景**: OpenAI 以天体命名模型层级：Luna 是小尺寸、低成本档，Terra 是中端档，Sol 是大模型档，Astra 则是比 Sol 更大的档位。在这一阶梯中，“.1”后缀通常代表一次更新，主要带来更低价格和更好的对齐表现，而非新的能力上限。“推理 token”是模型在给出答案前用于内部思考的隐藏 token，按输出计费并增加延迟，因此开发者会关注“none”“low”“medium”等不同推理档位实际消耗多少思考量。TerminalBench 是一个智能体终端任务基准，由它推算出的单位任务成本，正越来越多地被用来判断更便宜的模型在真实使用中是否真的更经济。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/openai/gpt-6.1-terra">GPT - 6 . 1 Terra - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/models/gpt-6-1-terra">GPT - 6 . 1 Terra (max) - Intelligence, Performance... | Artificial Analysis</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-1-terra/">Introducing GPT - 6 . 1 Terra | OpenAI</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者认为此次发布技术上扎实，但战略定位模糊。minimaxir 指出 Terra 仍是尴尬的“中间孩子”——夹在明显变强的小模型 Luna 和明显变便宜的大模型 Sol 之间，并称 TerminalBench 4.0 的单位任务成本结果让人难以论证为何选 Terra 而不选 Sol；Someone1234 把混乱归因于命名体系，认为自从 Sol-6.1 开始超越 Astra、且 Terra 一度被下架后，这套层级就失去了自洽性；simonw 则提供了实测数据，显示“none”和“low”推理档完全没有消耗推理 token——甚至“low”比“none”更便宜——而“medium”消耗了 496 个推理 token 却未返回可见的推理轨迹。

**标签**: `#openai`, `#llm`, `#model-release`, `#pricing`, `#ai`

---

<a id="item-5"></a>
## [微软向约四分之一员工提供大规模自愿离职买断方案](https://www.seattletimes.com/business/microsoft/microsoft-offers-mass-buyouts-for-roughly-a-quarter-of-its-workforce/) ⭐️ 8.0/10

据《西雅图时报》报道，微软正向约四分之一的员工提供大规模买断（自愿离职补偿）方案，这一自愿离职计划的规模在微软这种体量的公司中相当罕见。社区评论者估算这可能涉及约 6 万名员工，不过讨论中并未出现微软官方确认的具体人数。 对全球最大软件公司之一四分之一员工开放自愿离职，是大型科技企业仍在收缩而非扩张的强烈信号，也可能促使其他大型雇主以类似方式精简人员。与此同时，大量经验丰富的工程师会在同一时间段涌入本地及远程就业市场，其影响远超微软本身。 该方案名义上是自愿的，但评论者指出它制造了两难处境：接受买断的员工要和自己大量同事争夺新工作，而拒绝的人如果接受方案的人数不足，仍可能面临裁员。时机也颇为引人注目——据报道，买断方案出台不到一周前，微软总裁布拉德·史密斯刚在领英视频中公开表示公司“始终支持自己的员工”。

hackernews · doctorzook · 10月26日 15:35 · [社区讨论](https://news.ycombinator.com/item?id=50245524)

**背景**: 买断（即自愿离职补偿方案）是向愿意主动离开的员工提供现金与福利的方案。相比直接裁员，公司更青睐这种方式，因为它能降低法律风险、避免强制解雇，对公司形象冲击也更小。买断通常面向满足特定工龄、年龄或岗位条件的员工；当公司认为现有人员超出业务需要时，它便成为一种严肃的降本工具。与其它大型云计算与软件公司一样，微软正把支出向 AI 基础设施倾斜，这给较老或增长较慢的业务部门的人员编制带来压力。

**社区讨论**: Hacker News 上的讨论十分热烈，且以质疑为主。一位前微软 L63 级员工描述了自己在 18 个月里经历的频繁重组、工作量不足和团队臃肿，认为裁员确有其现实依据；其他人则强调收到买断方案者的两难处境，并批评方案出台时机与高管“我们支持自己的员工”的表态相矛盾。还有评论者警告说，自愿离职往往会带走最有市场竞争力的员工，另有人以微软的 H-1B 招聘做法质疑其“员工过剩四分之一”的说法。

**标签**: `#Microsoft`, `#layoffs`, `#tech industry`, `#workforce`, `#Hacker News`

---

<a id="item-6"></a>
## [西北大学用单正电子量子回旋仪将单个正电子囚禁数月](https://www.wired.com/story/scientists-trapped-an-antimatter-particle-for-months-to-study-its-secrets/) ⭐️ 8.0/10

美国西北大学 Gerald Gabrielse 团队利用单正电子量子回旋仪，在接近绝对零度的真空环境中依靠电磁场（彭宁阱）将单个正电子——即电子的反物质对应体——囚禁了数月，且过程中并未使粒子湮灭，因此可以对同一个粒子反复测量。据美国物理学会评估，该新装置有望把反物质测量精度提升约 30 倍。 电子与正电子磁矩的高精度比对是对 CPT 对称性（标准模型的基石之一）最严格的检验之一，因此约 30 倍的精度提升有可能揭示物质与反物质对磁场的响应是否完全一致。一旦未来测出两者的差异，描述物质与反物质行为的定律就需要改写，这也关系到宇宙为何几乎不存在反物质这一根本问题。 在这种状态下，正电子表现得类似一个具有离散量子能级（回旋能级与自旋翻转）的“人造原子”，科学家可以精确地驱动并观测这些能级，从而把此前在单个电子上实现的技术拓展到了反物质。目前实验尚未发现正电子与电子之间存在意外的差异，而长时间囚禁正是实现反复、高精度磁矩测量的关键前提。

telegram · zaihuapd · 10月26日 06:06

**背景**: 反物质粒子一旦与普通物质接触就会湮灭，因此通常寿命极短、极难研究。彭宁阱（Penning trap）利用静电场与静磁场在超低温真空中将带电粒子长期悬浮，Gabrielse 实验室自 2005 年起就用这类装置测量单个质子、反质子和电子的磁矩。所谓“量子回旋仪”，是指被囚禁的单个粒子只占据离散量子能级的 regime（体系），从而能以极高精度读出其磁矩，也就是“g 因子”。比较电子与正电子的 g 因子是对 CPT 对称性的检验——该对称性预言粒子与反粒子应具有完全相同的质量和磁矩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eurekalert.org/news-releases/1147987">Scientists trap and tame a single particle of antimatter... | EurekAlert!</a></li>
<li><a href="https://phys.org/news/2026-10-positron-cyclotron-key-standard.html">'One-positron cyclotron ' could test a key prediction of the Standard.....</a></li>
<li><a href="https://link.aps.org/doi/10.1103/Physics.19.132">Physics - A Quantum Cyclotron for Antimatter</a></li>

</ul>
</details>

**标签**: `#physics`, `#antimatter`, `#positron`, `#quantum measurement`, `#research`

---

<a id="item-7"></a>
## [马斯克称 SpaceX 完成 400 亿美元 GPU 债务融资，并预言 neocloud 大洗牌](https://www.bloomberg.com/news/articles/2026-10-25/musk-says-spacex-closed-40-billion-debt-deal-blasts-neoclouds) ⭐️ 8.0/10

马斯克表示 SpaceX 已完成 400 亿美元债务融资，用于购买英伟达 GPU 支撑其 AI 业务，但知情人士称定价谈判仍在进行，截至纽约上周日晚这笔债务尚未完成定价。他同时在发言中预言，200 多家 neocloud 算力租赁公司将遭遇“孔雀鱼式”的倒闭潮与整合，并称 SpaceX 不会收购其中任何一家。 这笔 400 亿美元的 GPU 抵押融资一旦落地，将成为 AI 基础设施领域规模最大的资本市场交易之一，意味着火箭公司的发射与星链信用被转化为 AI 算力的杠杆。马斯克对 neocloud 的唱衰则释放信号：随着超大规模云厂商和资金雄厚的运营方吸纳产能与定价权，单纯的 GPU 租赁商业模式可能被挤压。 这笔债务拟由表外实体以私募方式发行，高盛与阿波罗参与其中，相关 GPU 据称将于明年第一、二季度到货。这一区别很重要：具有约束力的融资承诺与实际完成定价、正式关闭的债券发行属于不同阶段，而报道称定价尚未完成。

telegram · zaihuapd · 10月26日 06:40

**背景**: 所谓“neocloud”（新云）是专门面向人工智能和高性能计算出租 GPU 算力的新型云服务商，定位是 AWS、Azure、Google Cloud 的补充而非替代。由于 GPU 价格昂贵且折旧迅速，这类公司常以债务融资采购，有时通过特殊目的实体把芯片放在表外持有。在 AI 资本开支持续扩张时这种结构可行，但一旦租赁价格下滑或芯片代际更替快于预期，运营方就会暴露风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ic.work/article/spacex-apollo-40b-gpu-financing-deal-vera-rubin">SpaceX敲定Apollo牵头400亿美元租赁锁定英伟达Vera Rubin - ic.work</a></li>
<li><a href="https://m.21jingji.com/article/20260813/herald/4fb4841bde3087f180defb71d3e2ce6d.html">两大 Neocloud 龙头爆火！ 算 力 租 赁 概念梳理 - 21财经</a></li>
<li><a href="https://wallstreetcn.com/articles/3784441">马斯克称SpaceX已完成400亿美元 GPU ...</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#AI infrastructure`, `#GPU financing`, `#Nvidia`, `#neoclouds`

---

<a id="item-8"></a>
## [Anthropic：违规用户贡献了公司 5%–7% 的收入](https://www.reuters.com/technology/artificial-intelligence/why-anthropic-is-turning-away-some-users-2026-10-22/) ⭐️ 8.0/10

据报道，Anthropic 在招股书中披露，被认定违反其使用政策或商业条款的客户贡献了公司本年前九个月收入的 5% 至 7%。据 Reuters 报道，Anthropic 已切断部分付费账户的访问权限，并指控其中一些账户与中国 AI 实验室有关联、利用 Claude 的输出训练自有模型；公司还表示第三季度强化的防御措施将蒸馏提取量降低了 90% 至 99%。 这一披露首次量化了前沿 AI 实验室能从被视为滥用的使用行为中获得多少收入，也表明一家主要实验室愿意为了知识产权和国家安全而放弃这笔钱。这对 Anthropic 的 IPO 叙事以及整个 API 生态都具有意义——蒸馏执法可能会重塑模型厂商监管自身客户的方式。 Anthropic 表示，公司在第三季度主动放弃了“可观的收入和数万亿 token 的付费流量”，并封禁了数万个相关账号。蒸馏之所以难以根除，是因为它只需要对模型进行普通的查询访问即可完成，而过于激进的防御又可能损害正当付费用户的使用体验。

telegram · zaihuapd · 10月26日 16:43

**背景**: 模型蒸馏是指通过在大模型的输出上训练，把一个能力强的大模型的行为迁移到另一个模型中；在此语境下，指的是利用 Claude 这类商业 API 生成训练数据来训练竞争对手的模型，这通常违反服务条款。Anthropic 此前已发布关于检测和防范蒸馏攻击的研究，其在 2026 年 9 月发布的威胁报告中也描述了多家中国实验室针对 Claude 开展的大规模提取行动。招股书是公司在首次公开募股前提交的披露文件，因此收入与风险细节才会公开浮现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/distillation-defenses">Strengthening our defenses against distillation attacks</a></li>
<li><a href="https://www.scientificamerican.com/article/what-is-ai-model-distillation-and-why-is-it-so-hard-to-stop/">What is AI model distillation, and why is it so hard to stop?</a></li>
<li><a href="https://betterstack.com/community/guides/ai/anthropic-threat-report-2026/">Anthropic's September 2026 Threat Report: Illicit ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI policy`, `#model distillation`, `#AI industry`, `#IPO`

---