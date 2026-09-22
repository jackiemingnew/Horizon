---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 39 条内容中筛选出 9 条重要资讯。

---

1. [OpenAI 发布 GPT-6 Sol 与 Luna，主打更低价格](#item-1) ⭐️ 10.0/10
2. [Anthropic 发布 Claude Opus 5.5，价格明显下调](#item-2) ⭐️ 9.0/10
3. [五角大楼：过度依赖 AI 导致对伊朗学校的致命空袭](#item-3) ⭐️ 9.0/10
4. [Claude Opus 5.5、GPT-6 Sol 与 Luna 发布，掀起新一轮价格战](#item-4) ⭐️ 9.0/10
5. [vLLM v0.30.0 发布：新增 Fast Start 权重缓存与 DeepSeek-V4 支持](#item-5) ⭐️ 8.0/10
6. [Artificial Analysis 在最高推理档位下评测 Claude Opus 5.5](#item-6) ⭐️ 8.0/10
7. [阿里发布真武 V900 AI 芯片，宣称算力达 M890 三倍](#item-7) ⭐️ 8.0/10
8. [Cloudflare 宣布 Python Workers 正式全面可用](#item-8) ⭐️ 8.0/10
9. [DeepSeek 与清华发布 DSec 沙箱平台技术报告](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Sol 与 Luna，主打更低价格](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 10.0/10

OpenAI 发布了 GPT-6 Sol 和 Luna 两款 GPT-6 系列新模型，在 API 中分别以 gpt-6-sol 和 gpt-6-luna 的名称提供。Sol 定位于旗舰 GPT-6 Astra 之下、主打高性价比的高端层级，Luna 则是快速且低成本的层级；有早期评论者指出，Luna 的价格大约只有 GPT-5.6 Luna 的一半。 如今价格和使用额度已成为许多开发者在 OpenAI 与 Anthropic 之间做选择的关键因素，因此更便宜的中端模型会直接影响工具成本，以及订阅套餐能用多久。此次发布也表明 OpenAI 正在把 GPT-6 铺成 Astra、Sol、Luna 三层产品线，而不是只推出单一旗舰，这会改变团队分配日常任务与高难度任务的方式。 Sol 被描述为位于快速层 Luna 之上、旗舰 GPT-6 Astra 之下，在同等价位下比竞品模型更聪明、效果更好，并且为处理困难工作任务提供了更高的使用额度和更低的成本。由于这些模型使用 OpenAI 兼容的 chat completions 接口，开发者可以先用 GPT-6 Astra 开发，之后只需更换模型 ID 即可切换；不过 API 速率限制仍会在一定时间窗口内对请求数和 token 用量设限。

hackernews · OfficialTurkey · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**背景**: OpenAI 一直在以分层方式推进 GPT-6 世代：GPT-6 Astra 于 2026 年 9 月早些时候发布，被宣传为公司迄今最强的模型，如今 Sol 和 Luna 则分别覆盖中端和快速低价端。所谓“分层”，实际上是 API 形态和接入端点相同，但在智能水平、延迟和每 token 价格上有所取舍，因此开发者可以把简单请求路由到便宜模型，把昂贵模型留给难题。订阅套餐（例如 ChatGPT Plus 或 20x 编程套餐）中的使用额度本质上由这些每 token 成本决定，这也是价格下调会引发如此多讨论的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT‑6 Sol and Luna - OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-sol">GPT - 6 Sol - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/">OpenAI launches GPT-6 Sol and Luna, boasting lower cost and ...</a></li>

</ul>
</details>

**社区讨论**: 评论者高度聚焦于价格与使用额度：simonw 认为 Luna 价格只有 GPT-5.6 Luna 的一半“是件大事”，并贴出了 Sol、Luna 与 Astra 的 SVG“鹈鹕”生成对比图；jeffnash 则认为 Codex 明显胜过 Claude Code，主要因为重置窗口不透明、20x/5x 套餐的额度换算奇怪，而且在 20x 套餐下 ChatGPT 的使用几乎是无限的。也有人更感性——m_fayer 表示 GPT-5.6 Sol 是少数让他“合拍”的模型，担心技术上更强的后继者反而没那么顺手；leokennis 则指出，对普通人来说 ChatGPT Plus 已经近乎无限且“开箱即用”。

**标签**: `#OpenAI`, `#GPT-6`, `#LLM`, `#AI models`, `#pricing`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5.5，价格明显下调](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic 发布了新前沿模型 Claude Opus 5.5，相比 Claude Opus 5 进行了全面降价——每百万 token 的缓存读取从 0.50 美元降至 0.20 美元，输入从 5 美元降至 4 美元，输出从 25 美元降至 20 美元，缓存写入从 6.25 美元降至 5 美元。该版本还强调沟通风格更加自然，Anthropic 称早期测试者认为其写作更清晰、更易读，在长时间会话中体验更好。 据报道 Opus 5 是 OpenRouter 上支出最高的模型，因此旗舰档位降价会直接降低重度 API 用户的成本，并加大其他前沿实验室的竞争压力。此次发布也表明，Anthropic 一边公开呼吁为前沿发展“踩刹车”，一边仍在同时推进能力提升与市场采用。 公告中最具体的部分是价格表：缓存读取降至每百万 token 0.20 美元，输出降至 20 美元，这对以缓存输入为主要成本的智能体式或长上下文工作负载影响最大。Anthropic 的表述还强调可读性与“把最重要的信息放在前面”，并将更清晰的沟通同时定位为可用性收益和安全收益。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**背景**: 前沿模型（frontier model）指当前能力最强的一类大规模机器学习模型，通常展现出较强的多步推理、编程和工具调用能力。大模型 API 的价格以“每百万 token 美元”计价，并区分输入（提示）与输出（补全）token，而提示缓存（prompt caching）允许重复出现的上下文被缓存并以远低于全新输入的价格再次读取。Claude Opus 是 Anthropic 最高端、最昂贵的模型系列，因此该系列的价格变动备受 API 开发者关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://distillation.technology/learn/what-is-a-frontier-model">What Is a Frontier Model ? | Distillation Technologies</a></li>
<li><a href="https://onpremisia.com/llm-api-pricing">LLM API Pricing by Provider (2026) — Compare per - token costs</a></li>
<li><a href="https://siliconanalysts.com/data/llm-pricing">LLM API Pricing — $/ Million Tokens by Model (2026)</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的反应明显分化：一条高赞评论讽刺该公告第一行还在提醒读者 Anthropic 上周刚呼吁“为前沿发展减速”，而正文却用具体数字证明自己完全没有减速；另一些人则通过逐项对比 token 价格，对这次期待已久的降价表示欢迎。有用户表示在重度智能体任务上仍更愿意使用 DeepSeek v4.1 等更便宜的替代方案，也有人分享了针对新模型行为的具体测试。

**标签**: `#AI/ML`, `#LLM`, `#Anthropic`, `#model release`, `#pricing`

---

<a id="item-3"></a>
## [五角大楼：过度依赖 AI 导致对伊朗学校的致命空袭](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 9.0/10

五角大楼一份报告认定，过度依赖 AI 辅助目标定位促成了美军对伊朗米纳布一所学校的导弹袭击，报告指出美国"未能履行尽一切可行手段核实"该学校为军事目标的义务，且这一失误"已超出单纯疏忽的范畴"。报告称，美国"在明知存在击中民用物体重大风险的情况下仍指示打击该校建筑，并对可能发生的后果采取了鲁莽态度"。 这是首批被官方认定与大规模平民伤亡有关的军用 AI 工具案例之一，把关于致命性自主武器和 AI 伦理的抽象争论变成了具体的问责危机。此事很可能加剧外界对五角大楼 AI 采购流程、Palantir 等承包商，以及当算法影响致命决策时究竟由谁承担法律责任这一问题的审视。 报道援引官员的话称，米纳布该地点因数据过时被登记为伊斯兰革命卫队设施，随后与其他候选目标一并被输入 Maven 系统，最终作为推荐结果输出；据称部分用户以为 Maven 会标出情报中的过时记录或矛盾之处，但该系统并非为此设计。Project Maven 官方定位是"人在回路"的决策辅助，而非自主武器系统，因此机器输出与人类判断之间的界线究竟在哪里，仍是一个悬而未决的问题。

hackernews · devonnull · 9月22日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49806430)

**背景**: Project Maven（正式名称为"算法战跨职能小组"）是美国国防部于 2017 年启动的计划，旨在加快机器学习与数据集成在情报、监视、目标获取与侦察流程中的应用；该计划目前由国家地理空间情报局（NGA）管理，整合无人机、卫星及其他传感器数据，为人类分析员标记潜在目标。谷歌在 2018 年因内部抗议退出该项目，后续参与整合的承包商包括 Palantir、Anduril、亚马逊云服务（AWS），以及于 2026 年退出的 Anthropic。五角大楼曾称 Maven 为 2024 年在伊拉克、叙利亚和也门的空袭提供了目标支持。此事也进一步卷入围绕致命性自主武器系统的长期国际争论——这类系统被设计为在极少或没有人工干预的情况下，依据预设约束搜索并攻击目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Maven">Project Maven</a></li>
<li><a href="https://www.cnas.org/events/project-maven">Project Maven: Artificial Intelligence in Warfare | CNAS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapon">Lethal autonomous weapon</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者大多不认同把"AI"当作根本原因，有人根据报告细节认为 AI"其实并不像是罪魁祸首"，也有人指责那些在不了解 AI 盲点的情况下就全盘拥抱它的官员。多位评论者强调责任必须由人承担：正如一人所言，"AI 无法在法庭上受审"，因此每一次致命行动都需要有负责的人类。还有人批评五角大楼与 Palantir 之间相互推责，质问为何导致无辜者死亡的决定会被当作一次搞砸的企业 SaaS 系统上线来处理。

**标签**: `#AI ethics`, `#military AI`, `#accountability`, `#Project Maven`, `#lethal autonomous weapons`

---

<a id="item-4"></a>
## [Claude Opus 5.5、GPT-6 Sol 与 Luna 发布，掀起新一轮价格战](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5.5，大约一小时后 OpenAI 发布了 GPT-6 Sol 和 GPT-6 Luna，Simon Willison 撰文给出了初步体验。GPT-6 Luna 的定价为每百万 token 输入 0.10 美元、输出 0.50 美元，仅为 GPT-5.6 Luna 的一半；GPT-6 Sol 相比 GPT-5.6 Sol 也有类似降幅，而 Claude Opus 5.5 同样降价至每百万 token 输入 4 美元、输出 20 美元。 前沿模型的同步发布与大幅降价，标志着大模型市场的价格战全面升级，开发者如今能以远低于去年的成本在顶级模型之上构建应用。这也给竞争对手带来直接压力：Grok 4.7 原本以每百万 token 输入 2 美元、输出 6 美元的低价定位，如今其输入价格已被 GPT-6 Sol 追平。 需要注意的一个细节是，GPT-5.6 系列计划在 11 月涨价 25%，因此 GPT-6 实际上只是 GPT-5.6 促销价的一半，而非最终价格的一半。以 0.10/0.50 美元的定价，GPT-6 Luna 是 OpenAI 有史以来最便宜的模型之一，仅高于能力弱得多的 GPT-4.1 Nano（0.10/0.40 美元）和 GPT-5 Nano（0.05/0.40 美元）；此外 GPT-5.6 Terra 与 GPT-6 Sol 同价，Willison 认为继续使用 Terra 的理由已经不复存在。

rss · Simon Willison · 9月22日 23:46

**背景**: Simon Willison 是一位广受关注的开发者与博主，他的文章常被当作评估新大模型的参考，而他也以「让模型生成一幅骑自行车的鹈鹕 SVG」这一别致的定性测试来横向比较模型。文中引用的价格是每百万 token 的费用，并分为输入、缓存输入和输出三档，这是业界比较各家 API 成本的标准方式。这两次发布出现在一个模型发布异常密集的一周里，同期还有 xAI 的 Grok 4.7 以及小米开源的 MiMo v2.6 Flash/Pro 全模态系列，后者是其强化学习研究的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Jun/6/six-months-in-llms/">The last six months in LLMs, illustrated by pelicans on bicycles - Simon Willison's Weblog</a></li>
<li><a href="https://github.com/simonw/pelican-bicycle">LLM benchmark: Generate an SVG of a pelican riding a bicycle - GitHub</a></li>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo-V2.6 | Xiaomi</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Anthropic`, `#OpenAI`, `#AI pricing`, `#model releases`

---

<a id="item-5"></a>
## [vLLM v0.30.0 发布：新增 Fast Start 权重缓存与 DeepSeek-V4 支持](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM 发布了 v0.30.0，这是一个包含 762 个提交、来自 315 位贡献者（其中 104 位是新贡献者）的大型版本。该版本引入了名为 “Fast Start” 的常驻式单 GPU 权重缓存守护进程，新增了 DeepSeek-V4.1-Flash、DeepSeek-V4-Flash-Vision-Exp、GLM-5.3-Flash、K2-Horizon、Cohere Compass 等大量模型支持，并带来 DeepSeek-V4 CPU 后端、Gumbel-max 水印、HiSparse 主机侧 KV 缓存以及一系列 Model Runner V2 性能优化。 vLLM 是目前使用最广泛的开源大模型推理与服务平台之一，因此这些改动会很快传导到生产环境、强化学习训练流程和自托管部署中。尤其是 Fast Start 直接针对推理引擎的冷启动延迟，而新的 CPU 后端与更广的模型覆盖则扩大了团队可服务的硬件范围与模型架构范围。 Fast Start 将量化后、按张量并行切分的权重常驻在 GPU 显存中，使重启的引擎可以通过 CUDA IPC 以 `--load-format ipc_cache` 方式直接映射这些权重，而无需从磁盘重新加载，并且现在也支持 FP4 权重与多节点张量并行。在性能方面，在 CUDA 图捕获期间冻结垃圾回收使 H200 上的捕获时间从 12 秒降至 2 秒、引擎初始化时间从 28.9 秒降至 8.2 秒；DeepSeek-V4 的 CPU 后端则依赖 AVX512/AMX 内核来执行稀疏 MLA、indexer、mHC 与压缩器算子。

github · khluu · 9月22日 05:20

**背景**: vLLM 是一个开源的大语言模型推理服务引擎，它以 PagedAttention 式的 KV 缓存管理而闻名，并常与 FP8、MXFP8、NVFP4 等量化格式配合使用以降低显存占用——例如 MXFP8 对每 32 个元素组成的块共享一个 2 的幂次缩放因子。现代推理服务还依赖面向 DeepSeek 类架构的 FlashMLA 等高度优化注意力内核、用于把模型切分到多张 GPU 上的张量并行（TP），以及用于消除逐步启动开销的 CUDA 图。本次发布还涉及 DeepSeek 的 Engram 条件记忆查表机制——它可在其他层计算的同时从主机 DRAM 预取数据，以及 HiSparse 这类在显存紧张时把 KV 缓存页溢出到固定主机内存的特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvidia.github.io/cudnn-frontend/mxfp8-attention-scaling/">How Scales Are Applied in MXFP8 Attention - nvidia.github.io</a></li>
<li><a href="https://www.deepep.org/en/flashmla">FlashMLA</a></li>
<li><a href="https://generativeai.pub/deepseeks-engram-the-lookup-table-that-eats-transformer-layers-90b5f6a99a90">DeepSeek’s Engram : The Lookup Table That Eats... | Generative AI</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#model-serving`, `#release`, `#ai-infrastructure`

---

<a id="item-6"></a>
## [Artificial Analysis 在最高推理档位下评测 Claude Opus 5.5](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 8.0/10

Artificial Analysis 发布了 Claude Opus 5.5 在“max”推理档位下的评测页面，同时还有“xhigh”档位和默认“medium”档位的独立页面。该评测很快在 Hacker News 上引发讨论（约 216 分、62 条评论），焦点集中在其智能水平、成本以及与开源权重模型相比的基准可靠性。 这次评测进一步激化了业内的争论：当开源权重模型在许多基准上已接近前沿水平、成本却低得多时，闭源前沿模型是否还值这个溢价。它也凸显出，决定实际效果和单任务开销的已不仅是模型本身，还有推理投入档位的选择。 评论者 simonw 指出，在 max 档位下，模型两次在解答“画一只骑自行车的鹈鹕的 SVG”这样一个简单提示时耗尽了 128,000 token 的预算，却仍处于推理过程中；而 hglaser 则引用数据称，在同等高投入档位对比下，其单任务成本约为 Opus 5 的一半。由于依据的是第三方独立评测页面而非官方发布公告，这些数字应被视为某一家评测机构的阶段性快照。

hackernews · theanonymousone · 9月22日 16:51 · [社区讨论](https://news.ycombinator.com/item?id=49804316)

**背景**: Artificial Analysis 是一家独立评测机构，持续发布语言、图像、视频和语音模型的评测结果，并用一个综合的 Intelligence Index 对模型进行排名。所谓“max”推理档位，是指允许模型在作答前花费远更多的内部推理 token 预算的配置，通常能提升难题上的表现，但也会增加延迟和成本。开源权重模型指的是训练后的参数被公开可供下载的模型，任何人都能自行部署和微调，这与仅通过 API 提供的闭源模型形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://www.everydev.ai/tools/artificial-analysis">Artificial Analysis - AI Model Benchmarking Platform | EveryDev.ai</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open - Weights Model ? | AI21</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏向怀疑与分歧：cmiles8 认为前沿模型只比开源权重方案略好，价格却高出约 100 倍；breckenedge 则担心模型厂商的基准成绩在发布数周后会回退，而用户此时早已切换过去。也有人持正面看法，hglaser 称赞其单任务成本比 Opus 5 大约减半；linuxrebe1 则表示自己已退回使用 Opus 4.8，因为 Opus 5 常常中途迷失任务、跑题。

**标签**: `#AI`, `#LLM`, `#Claude`, `#benchmarks`, `#pricing`

---

<a id="item-7"></a>
## [阿里发布真武 V900 AI 芯片，宣称算力达 M890 三倍](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 8.0/10

在 2026 云栖大会上，阿里平头哥发布号称最强国产 AI 芯片的真武 V900，宣称算力达到上一代真武 M890 的 3 倍，单一集群可扩展至 50 万卡。阿里 CEO 吴泳铭同时表示，自研 M890 超节点已支撑 2 万亿参数大模型推理，本季度将在阿里云规模化上架；Qwen 计划训练 5 至 10T 参数新模型，阿里云目标到 2032 年全球数据中心规模超过 20GW。 这一发布让阿里成为横跨芯片、云与大模型的全栈 AI 玩家，在国产大规模算力竞赛中直接挑战英伟达的主导地位以及华为昇腾的演进路线。如果 50 万卡集群与万亿参数路线图得以落地，将改变中国 AI 实验室在高端 GPU 出口受限背景下训练与部署前沿模型的方式。 新芯片是规划中 50 万卡广域超节点集群的底座，该集群算力规划达 1GW、通信延迟目标为 6 微秒，采用 NPO 光模块、HPN 8.0 网络与 CPFS 存储系统，目标是支撑十万亿级 MoE 模型训练。上一代真武 M890 是训推一体 AI 芯片，已应用于磐久 AL128 节点服务器，其 128 卡超节点通信时延达百纳秒级，并已成功适配 2.4 万亿参数的旗舰模型 Qwen3.8。

telegram · zaihuapd · 9月22日 03:30

**背景**: 超节点（SuperPod）是一种为构建大规模 AI 算力集群而设计的技术架构，最早由英伟达提出，其核心是通过高速互联协议把多个计算节点紧密耦合，形成逻辑上单一、物理上分布、具备大带宽、低时延与内存统一编址特征的计算系统；运行万亿参数模型需要把参数分散到几十甚至上百张高速互联的加速卡上。平头哥是阿里自研芯片的半导体部门，云栖大会则是阿里云每年发布芯片、云与模型路线图的旗舰活动。2026 年的发布正值与华为的竞争加剧之际，后者也已公布算力规模超过 50 万卡的昇腾超节点集群。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chooseai.net/news/7318/">阿里云计划建 50 万卡广域超节点集群：1GW 算力、6 微秒通信延迟-Choo...</a></li>
<li><a href="https://www.ithome.com/0/952/644.htm">阿里云发布“真武 M890”AI 芯片及 128 卡超节点服务器，可支持海量 Agent 并发推理 - IT之家</a></li>
<li><a href="https://www.qbitai.com/2026/07/457694.html">阿里云：真武芯片超节点已成功适配Qwen3.8，上线百炼提供推理服务</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Alibaba`, `#semiconductors`, `#cloud computing`, `#LLM infrastructure`

---

<a id="item-8"></a>
## [Cloudflare 宣布 Python Workers 正式全面可用](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

Cloudflare 宣布 Python Workers 正式全面可用（GA），Python 由此成为其开发者平台上与 JavaScript 并列的一级支持语言。该运行时原生支持 FastAPI、Django、Flask 等主流 Python Web 框架，可直接运行 PostgreSQL 等数据库以及 LangChain 等 AI 编排库，并无缝接入 Workers AI、R2、D1 等 Cloudflare 服务。 这为庞大的 Python 开发者群体扫除了一个重要障碍——过去他们要么用 JavaScript/TypeScript 重写逻辑，要么把 Python 跑在更重的容器化 Serverless 平台上。此举增强了 Cloudflare 在边缘计算与 Serverless 领域相对 AWS Lambda、Vercel 的竞争力，让团队可以用极少的改动就把现有 Python 框架和 AI 技术栈部署到边缘节点。 开发者通过 Python Workers 专用命令行工具 pywrangler 安装依赖并部署 Worker，Cloudflare 还在 python-workers-examples 仓库中提供了示例项目。D1 提供边缘端 Serverless SQLite 式数据库，R2 提供兼容 S3 API 且免出口流量的对象存储，Workers AI 提供托管推理能力，这些服务如今都可以直接从 Python 代码中调用。

telegram · zaihuapd · 9月22日 04:00

**背景**: Cloudflare Workers 是一个 Serverless 平台，它把应用代码运行在 Cloudflare 遍布全球的边缘网络上，而非集中在单一区域，传统上以 JavaScript 和 WebAssembly 为主要语言。Python 支持大约在两年前以公开测试形式推出，底层基于 Pyodide——即编译为 WebAssembly 的 CPython，使 Python 能够运行在 Workers 运行时中。此次进入 GA 意味着该功能被视为生产可用、足够稳定，并获得了官方正式支持而不再是实验性状态。FastAPI、Django、Flask 是 Python 生态中常用的 Web 框架，LangChain 则是构建大语言模型应用的常用库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/python-workers-ga/">Python Workers are now generally available | Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/workers/languages/python/">Write Cloudflare Workers in Python · Cloudflare Workers docs</a></li>
<li><a href="https://developers.cloudflare.com/r2/">Overview · Cloudflare R 2 docs</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#Serverless`, `#Python`, `#Edge Computing`, `#Workers AI`

---

<a id="item-9"></a>
## [DeepSeek 与清华发布 DSec 沙箱平台技术报告](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI 与清华大学联合发布了《DeepSeek Elastic Compute（DSec）》技术报告，公开了一套每天服务约 300 万个沙箱实例、用于支撑大规模智能体训练与评测的沙箱基础设施。该平台通过统一 SDK 提供 FnCall、容器、Firecracker microVM 和完整 VM 四种后端，并与强化学习框架深度协同，将有状态的 rollout 执行与可抢占的 GPU 训练解耦。 随着 AI 实验室从静态模型训练转向需要执行代码、与真实环境交互的智能体系统，沙箱吞吐量成为关键扩展瓶颈；DSec 展示了一套可支撑数十万并发沙箱的生产级设计。这份报告也让更广泛的 AI 基础设施社区得以具体了解前沿实验室如何构建和运营智能体强化学习背后的执行层。 单个生产单元约由 160 个节点组成，峰值并发超过 38 万个沙箱，创建速度超过每秒 5000 个；单节点可高密度承载 3200 个容器或 800 个 microVM。平台基于 3FS 分布式文件系统按需加载 EROFS 镜像，取代传统 Docker 全量拉取，报告称任务完成时间快 1.7 倍、磁盘写入减少 57%，内存共享与回收机制还使峰值内存占用下降约 40%。

telegram · zaihuapd · 9月22日 04:45

**背景**: 智能体训练要求模型在隔离环境中真正执行代码、浏览网页或操作软件，因此每个训练样本都需要一个可丢弃的执行沙箱。Firecracker 是一种轻量级虚拟机监控器，其 microVM 兼具硬件级隔离与接近容器的启动速度；EROFS 则是为不可变镜像和容器/应用沙箱镜像设计的只读 Linux 文件系统。3FS 是 DeepSeek 开源的分布式文件系统，专为 AI 训练与推理所需的高吞吐、低延迟场景打造。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://erofs.docs.kernel.org/en/latest/">Overview — EROFS filesystem project</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker - microvm / firecracker : Secure and fast microVMs...</a></li>
<li><a href="https://winbuzzer.com/2025/04/20/deepseeks-open-source-3fs-distributed-file-system-promises-efficiency-and-better-scaling-for-ai-workloads-xcxwbn/">DeepSeek's Open Source 3 FS Distributed File System Promises...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#agent training`, `#sandbox`, `#reinforcement learning`, `#distributed systems`

---