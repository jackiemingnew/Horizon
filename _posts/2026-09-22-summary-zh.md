---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 37 条内容中筛选出 5 条重要资讯。

---

1. [小米发布 MiMo-V2.6 开放权重模型系列，含 Flash 与 Pro 两个版本](#item-1) ⭐️ 8.0/10
2. [Bryan Cantrill 剖析 Sun Microsystems 的失败教训](#item-2) ⭐️ 8.0/10
3. [xAI 发布 Grok 4.7：参数增加 40%，价格保持不变](#item-3) ⭐️ 8.0/10
4. [Cloudflare 宣布 Python Workers 正式可用](#item-4) ⭐️ 8.0/10
5. [SemiAnalysis 深度解析：将 MoE 模型映射到推理硬件](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [小米发布 MiMo-V2.6 开放权重模型系列，含 Flash 与 Pro 两个版本](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

小米正式发布 MiMo-V2.6 系列开放权重模型，分为 Flash 和 Pro 两个版本，并将经过强化学习训练的权重以 XiaomiMiMo/MiMo-V2.6-Flash-RL 和 XiaomiMiMo/MiMo-V2.6-Pro-RL 之名发布在 Hugging Face 上，同时附上详细的技术报告。小米还公开了一个实时强化学习训练仪表盘，在模型训练期间持续对外展示进展。 此次发布让小米跻身于能够交付前沿级开放权重模型的实验室之列，而它对训练方法论的细致披露以及实时强化学习进展的公开，也抬高了业界对厂商训练透明度披露的期待。对开发者和研究者而言，这多出两个性能强劲、可自由下载的选项，能够自行部署或微调，而不必只依赖闭源 API。 Flash 版本总参数量为 309B、激活参数为 15B，Pro 版本则扩展到总参数 1.02T、激活参数 42B，可见二者均采用稀疏 MoE 架构；Flash 还包含一个 6 层音频 patch 编码器，以及用于投机解码的 5 层滑动窗口注意力 MTP 草稿模型，小米同时提供了 SGLang 部署指南。需要注意的是，尽管透明度很高，这些模型仍属于“开放权重”而非完全开放，训练数据和训练代码并未完整公布。

hackernews · volf_ · 9月21日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=49792730)

**背景**: 开放权重模型指的是训练好的参数可以公开下载的模型，任何人都能运行、修改或微调，这与只能通过 API 调用的闭源模型不同。像 MiMo-V2.6 这样的大模型通常采用混合专家（MoE）架构，每个 token 只激活一小部分参数，因此推理成本远低于总参数量所暗示的水平。强化学习（RL）后训练是让基础模型依据奖励信号继续优化推理能力、指令遵循和工具调用的阶段，而小米正是把这一阶段通过公开仪表盘展示了出来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">Introducing MiMo-V2.6 series</a></li>
<li><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL">XiaomiMiMo/MiMo-V2.6-Flash-RL · Hugging Face</a></li>
<li><a href="https://www.linkedin.com/pulse/open-weights-llms-in-depth-analysis-adoption-usage-performance-jha-kymhc">Open - Weights LLMs: In-Depth Analysis of Adoption, Usage, and...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论整体偏正面：有人称赞实时强化学习仪表盘是极佳的学习工具、技术报告也异常全面，同时也承认“开放”一词的定义仍存争议。另一些人主要从价格可负担性角度比较中美模型，分享了用 SVG 鹈鹕提示词对两个版本做的实测，并引用了具体的参数规模；还有讨论认为，凭借电力和电网建设的优势，中国长期来看可能会赢得 AI 竞赛。

**标签**: `#AI/ML`, `#LLM`, `#open weights`, `#Xiaomi`, `#model release`

---

<a id="item-2"></a>
## [Bryan Cantrill 剖析 Sun Microsystems 的失败教训](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 8.0/10

曾任 Sun Microsystems 工程师、以创造 DTrace 闻名的 Bryan Cantrill 发表了一篇题为《What Sun got wrong》的详细回顾文章，剖析了导致这家公司走向衰落的战略与技术失误。该文章在 Hacker News 上引发了热烈讨论（484 分、270 条评论），许多前客户和员工在讨论中补充了关于 Sun 销售文化、产品决策以及最终被 Oracle 收购的一手细节。 Sun 的衰落至今仍是科技行业最具教育意义的案例之一：一家在工程上确实卓越的公司——拥有 SPARC 服务器、Solaris、Java、NFS、ZFS 和 DTrace 等成果——依然可能败给更便宜、对客户更友好的竞争对手。这场讨论在当下引发共鸣，因为评论者明确将 Sun 在互联网泡沫时期的高估值与如今估值倍数居高不下的 AI 及硬件股票相类比。 评论者指出两个尤其致命的失误：一是 2002 年 Sun 短暂取消 x86 平台上的 Solaris，这让不愿被锁定在 SPARC 硬件上的客户感到失望；二是 2002 年 Sun 未能与 Google 达成交易，原因是 Sun 坚持要了解 Google 拥有多少台服务器，而 Google 认为这属于高度机密。还有人提到，Sun 的瘦客户端以及 Pine、vi 等工具虽然启动缓慢，却深受大学用户的喜爱。

hackernews · chmaynard · 9月21日 14:03 · [社区讨论](https://news.ycombinator.com/item?id=49787436)

**背景**: Sun Microsystems 是一家成立于 1982 年的美国计算机公司，以制造基于 SPARC 架构的高性能工作站和服务器、并运行其专有操作系统 Solaris 而闻名，同时还创造了 Java、NFS、ZFS 和 DTrace。在 20 世纪 90 年代末互联网泡沫的高峰期，它曾是全球市值最高的科技公司之一，但在 2000 年代举步维艰，最终于 2010 年被 Oracle 收购。Bryan Cantrill 在 Sun 工作了十余年，后来联合创办了 Oxide Computer，这使他的回顾文章具有难得的内部视角与可信度。

**社区讨论**: 讨论中既有怀旧，也有尖锐的商业批评：一位评论者回忆说，1990 年代末从 Sun 或 DEC 采购意味着被迫参加销售会议和没完没了的报价修改，以至于一台 Alpha 服务器的导轨和电源线比一台次日送达的完整 Dell 服务器还贵。另一位认为 Sun 其实从未真正对经营企业感兴趣，只是为了给造出优秀技术提供资金才勉强做销售；还有人提到自己在泡沫高峰期以每股 70 美元卖出 Sun 股票，几个月后股价跌至 7 美元，并以此警示今天的 AI 股票。

**标签**: `#Sun Microsystems`, `#tech history`, `#systems`, `#business strategy`, `#Hacker News`

---

<a id="item-3"></a>
## [xAI 发布 Grok 4.7：参数增加 40%，价格保持不变](https://x.ai/news/grok-4-7) ⭐️ 8.0/10

xAI 发布了 Grok 4.7，这是继 Grok 4.6 之后的又一前沿模型：其权重（参数）规模增加约 40%，但 API 价格维持不变，输入为每百万 token 2 美元、输出为每百万 token 6 美元。该版本比原定发布日期推迟了将近两周。 由于模型规模明显变大而单位 token 价格不变，xAI 实际上是在以“每一美元能买到多少能力”而非降价来竞争，这很可能压缩其自身利润空间，同时抬高竞争对手的门槛。对于在编程和 agentic 工作流中选择模型的开发者而言，这直接影响他们的决策，因为他们需要在 Grok 4.7 与 Anthropic 的 Opus 系列等前沿模型之间做取舍。 社区测试者反馈称 Grok 4.7 明显更慢、消耗的 token 也更多；开发者 Simon Willison 还发现，low 与 medium 两档 reasoning effort 消耗的 token 数相近，而 xhigh 反而比 high 用得更少。他表示还需要绕开中间的 OpenRouter、直接用 xAI API 重测，才能确认这些数字。

hackernews · meetpateltech · 9月21日 15:50 · [社区讨论](https://news.ycombinator.com/item?id=49788838)

**背景**: Grok 是 xAI 旗下的大语言模型系列，xAI 由 Elon Musk 于 2023 年创立，其 Grok 聊天机器人已与 X 平台整合。据公开资料，Grok 4.6 是基于 1.5 万亿参数 V9 基座预训练的模型，并引入了 AI 编程平台 Cursor 的数据，而 xAI 此后已收购 Cursor。所谓“参数”（即权重）是模型在训练中学习到的变量，参数越多通常代表容量越大，但训练与推理成本也更高。当前前沿实验室的模型发布节奏很快，社区对基准测试分数的怀疑也随之上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">XAI (company)</a></li>
<li><a href="https://www.ibm.com/think/topics/model-parameters">What are Model Parameters? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区态度褒贬不一，且以质疑为主：多位评论者指出，模型大了 40% 而价格不变意味着利润变薄，加上发布推迟，他们怀疑 Grok 4.7 是为了抢在传闻中的 Opus 5.5 之前仓促推出；有人直言 Grok 4.6 在编程和 agentic 场景中“根本不顶用”。也有更乐观的声音，欢迎发布节奏加快，并预计随着团队在大型训练任务上积累经验，Grok 5 会带来更大的跃升；此外还有开发者分享了对不同 reasoning effort 档位 token 消耗的实测数据。

**标签**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#Model Release`

---

<a id="item-4"></a>
## [Cloudflare 宣布 Python Workers 正式可用](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

Cloudflare 将 Python Workers 从测试阶段推进到正式可用（GA），开发者现在可以直接在其无服务器边缘运行时上编写和部署 Python 代码。此次发布强调了包依赖支持的改进，以及向 WebAssembly 上游社区提交的贡献，使得常用 Python HTTP 客户端能够在基于 Wasm 的运行时中正常工作。 Python 是脚本、数据工作和后端服务中最广泛使用的语言之一，边缘平台的一等支持消除了团队必须改用 JavaScript 或 Rust 才能部署到边缘的重大障碍。这也说明「在 WebAssembly 上运行 Python」正获得越来越多的动力，进而影响无服务器平台和 Python 库维护者对可移植性的思考方式。 正式版本依赖 Pyodide 与 Emscripten 工具链，并借助 urllib3 中的 JSPI 支持，让 HTTP 客户端在 WebAssembly 环境中通过 JavaScript 的 fetch API 发起请求。包管理标准化正通过 PEP 783（PyEmscripten）加以规范，不过基于 Wasm 的 Workers 的冷启动延迟问题仍未有明确答案。

hackernews · torutofu · 9月21日 13:38 · [社区讨论](https://news.ycombinator.com/item?id=49787142)

**背景**: Cloudflare Workers 是一个无服务器平台，它让代码运行在 Cloudflare 遍布全球的边缘网络上，而不是单一的集中式服务器上，从而使应用更贴近用户执行。Python Workers 通过把 Python 编译为 WebAssembly 来运行它；WebAssembly 是一种可移植的二进制指令格式，运行在基于栈的虚拟机上，目标是让高性能代码同时适用于 Web 和非 Web 环境。由于 WebAssembly 本身不包含 Python 的 C 扩展和网络层，因此需要 Pyodide、Emscripten 等项目把 Python 包桥接进这个沙箱运行时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/">Overview · Cloudflare Workers docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://grokipedia.com/page/Cloudflare_Workers">Cloudflare Workers</a></li>

</ul>
</details>

**社区讨论**: 评论区总体对这一步进展表示欢迎：一位 urllib3 维护者澄清，urllib3 中的 Pyodide/Emscripten 与 JSPI 支持来自大规模的外部贡献；Wasmer 创始人则称赞 Cloudflare 在包支持和 PEP 783 上的进展，尽管双方产品存在竞争。遗留的担忧集中在架构取舍以及基于 Wasm 的 Workers 的冷启动/启动延迟上，同时也有对标题措辞的轻松调侃。

**标签**: `#Cloudflare Workers`, `#Python`, `#WebAssembly`, `#Serverless`, `#Edge Computing`

---

<a id="item-5"></a>
## [SemiAnalysis 深度解析：将 MoE 模型映射到推理硬件](https://newsletter.semianalysis.com/p/computation-and-data-movement-for) ⭐️ 8.0/10

SemiAnalysis 发布了一篇题为《Computation and Data Movement for Inference》的技术深度解析，探讨了混合专家（MoE）模型如何被映射到推理硬件上，内容涵盖模型结构、数据流以及高效的服务策略。这篇文章并未发布新产品或新基准，而是系统性地梳理了决定 MoE 推理在生产环境中实际表现的各类系统级权衡。 MoE 已成为前沿模型的主流架构，因为它把总参数量与单 token 计算量解耦；但这一优势只有在硬件能足够快地供给正确专家时才真正兑现。随着越来越多的实验室和企业部署 Mixtral 及更大规模的前沿 MoE 模型，理解计算与数据搬运之间的平衡将直接影响服务成本、延迟以及硬件采购决策。 该分析重点讨论了专家路由及其引发的 all-to-all 通信如何重塑推理对内存带宽和互连的需求：每个 token 只激活少量专家，但完整的权重集合仍必须驻留在内存中。这使得 MoE 服务在本质上受限于内存容量与内存带宽，而非单纯受限于算力，而这一点恰恰是仅比较参数量的简单分析容易忽略的。

rss · Semianalysis · 9月21日 18:14

**背景**: 混合专家（MoE）模型把权重切分成许多独立的「专家」子网络，并通过路由器为每个 token 只选择少数几个专家，从而以接近小模型的计算成本获得大模型的知识容量。代价在于内存：所有专家都必须被存储，并且根据批大小和路由结果在系统中搬运，这正是数据搬运而非单纯浮点运算量常常主导推理耗时的原因。此前《Data Movement Is All You Need》等研究已针对 Transformer 指出类似结论，证明优化内存搬运可以带来显著加速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2007.00072">DATA MOVEMENT IS ALL YOU NEED: A CASE STUDY ON OPTIMIZING TRANSFORMERS</a></li>
<li><a href="https://localmodel.run/guides/mixture-of-experts">Mixture of experts (MoE) explained for local LLMs · localmodel.run</a></li>
<li><a href="https://medium.com/@kittikawin_ball/you-dont-need-a-phd-to-understand-mixture-of-experts-here-s-the-intuition-in-plain-english-8972d6e7ad51">You Don’t Need a PhD to Understand Mixture of Experts ... | Medium</a></li>

</ul>
</details>

**标签**: `#MoE`, `#inference`, `#hardware`, `#systems`, `#data movement`

---