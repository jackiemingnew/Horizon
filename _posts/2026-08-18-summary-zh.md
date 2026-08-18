---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
lang: zh
---

> 从 30 条内容中筛选出 4 条重要资讯。

---

1. [Mojo🔥现已开源](#item-1) ⭐️ 9.0/10
2. [亚马逊税：广告驱动的搜索如何侵蚀消费者信任](#item-2) ⭐️ 8.0/10
3. [Linux 7.3 改进显存耗尽时的性能表现](#item-3) ⭐️ 8.0/10
4. [Qwen 3.8 27B 在 Artificial Analysis 获 52 分，追平 GPT-5.6 Luna](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mojo🔥现已开源](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 9.0/10

Mojo 编程语言的编译器和工具链现已根据 Apache 2 许可开源，紧随其 1.0 版本的发布。

rss · Simon Willison · 8月18日 21:39

**标签**: `#Mojo`, `#open source`, `#programming languages`, `#compiler`, `#AI`

---

<a id="item-2"></a>
## [亚马逊税：广告驱动的搜索如何侵蚀消费者信任](https://seths.blog/2026/08/the-amazon-tax/) ⭐️ 8.0/10

Seth Godin 的博客文章指出，亚马逊的搜索结果如今优先展示赞助广告和亚马逊自身利益，而非对购物者最有利的产品。Hacker News 上的讨论反映出用户对搜索结果质量下降和广告充斥的普遍不满。 亚马逊是数百万消费者默认的商品搜索引擎，搜索结果质量下降会在大规模上影响购买决策。这削弱了用户对平台的信任，并引发了对平台经济的更广泛质疑：市场通过变现搜索意图而非服务用户来获利。 亚马逊的 A9 算法过去主要根据相关性和销售表现对商品进行排名，但现在 Sponsored Products（赞助商品）广告位占据了搜索结果的大部分。评论者反映，大约四分之三的搜索结果都是赞助广告；此外，A10 算法体系进一步加强了转化率和外部流量的权重。

hackernews · herbertl · 8月18日 13:22 · [社区讨论](https://news.ycombinator.com/item?id=49345263)

**背景**: 亚马逊的搜索引擎并非中立的发现工具，而是一个零售收入引擎。A9/A10 算法综合关键词相关性、销售速度、转化率和广告投入来对商品排序。这促使卖家付费投广告才能突围，正如评论区有人指出的那样，即使产品优质但评论较少也需如此。结果是广告主导搜索结果、自然流量可见度不断缩小的循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://salesduo.com/blog/amazon-a9-search-engine-guide/">Amazon A9 Algorithm: How Amazon’s Search Engine Works (2026)</a></li>
<li><a href="https://www.repricerexpress.com/amazons-algorithm-a9/">Understanding Amazon's A9 Algorithm: Boost Your Product Rankings</a></li>
<li><a href="https://feedvisor.com/university/a9-search-engine/">Amazon A9 Algorithm: How It Works & How to Rank (2026)</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者大体同意这种批评，并分享了自己把购物从亚马逊转移开的个人经历。有人怀念搜索曾意味着准确定位商品的年代，也有人从经济学角度分析平台如何将信噪比下降变现。一位卖家视角的评论反驳说，广告是新优质产品突围的唯一途径。

**标签**: `#Amazon`, `#e-commerce`, `#search`, `#platform-economics`, `#consumer-behavior`

---

<a id="item-3"></a>
## [Linux 7.3 改进显存耗尽时的性能表现](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 8.0/10

根据 pixelcluster.dev 的报道，Linux 7.3 通过更好地处理 GPU 显存超售（overcommit），改善了显存耗尽时的性能表现。这一改动引发了社区强烈关注，许多用户希望它能尽快合入主线内核。 这一改动意义重大，因为当前显存耗尽时往往会导致性能急剧下降甚至系统卡死，尤其是在显存有限的设备上。更好的超售处理有望改善游戏、AI 推理和桌面响应速度，同时也会给 Nvidia 带来压力，促使其在闭源驱动中支持显存换页（paging）。 内核的超售行为由 vm.overcommit_memory 及相关 sysctl 参数控制，其中启发式（heuristic）模式会拒绝明显过大的分配，同时仍允许一定程度的超售。社区成员指出，虚拟内存碎片化仍然是个问题，而且 Nvidia 的闭源驱动似乎完全不支持 GPU 显存换页。

hackernews · flaburgan · 8月18日 07:51 · [社区讨论](https://news.ycombinator.com/item?id=49342719)

**背景**: 内存超售（memory overcommit）是一种内核技术，允许进程预留比物理内存更多的虚拟内存，前提是大部分已分配内存最终不会被真正使用；当实际不够时，Linux 依靠回收机制和 OOM killer 来应对。VRAM 超售将同样的思路应用到显存上，但显存一旦耗尽，性能影响往往非常严重。Linux 内核文档描述了多种超售记账模式，从启发式处理到严格禁止超售模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kernel.org/doc/Documentation/vm/overcommit-accounting">The Linux kernel supports the following overcommit handling modes</a></li>
<li><a href="https://www.baeldung.com/linux/memory-overcommitment-oom-killer">Linux Memory Overcommitment and the OOM Killer | Baeldung on Linux</a></li>
<li><a href="https://gitlab.com/MaxIV/kubernetes/mortalgpu/-/tree/main">Files · main · MaxIV / kubernetes / MortalGPU · GitLab</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体正面，用户称赞文章清晰，并感叹 Linux 内核改进速度之快与 Windows 更新形成鲜明对比。Nvidia 用户对闭源驱动完全不支持显存换页感到沮丧；还有人争论到底该由内核还是应用程序决定内存对 VRAM 的粘性。此外，有人提出内核是否应偶尔整理虚拟内存碎片，也有评论者指出低层性能工程在很大程度上有赖于年轻的跨性别者的贡献。

**标签**: `#linux`, `#kernel`, `#vram`, `#memory-management`, `#performance`

---

<a id="item-4"></a>
## [Qwen 3.8 27B 在 Artificial Analysis 获 52 分，追平 GPT-5.6 Luna](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 8.0/10

Qwen 3.8 27B 这个紧凑的开源权重模型在 Artificial Analysis Intelligence Index 上得分 52，追平了 GPT-5.6 Luna (max)，仅比 GLM-5.2（753B）和 DeepSeek V4 Pro 0813（1.7T）低 1 分。Simon Willison 于 2026 年 8 月 17 日报道了这一结果。 只有 27B 参数的模型追平了规模大得多的旗舰模型，说明参数效率正在快速提升，有望降低高性能 AI 部署的成本和硬件门槛。这也可能加剧竞争，因为前沿级别的能力可以被放进小得多的模型中。 Artificial Analysis Intelligence Index v4.1.1 综合了 GDPval-AA v2、Terminal-Bench v2.1、SciCode、GPQA Diamond 和 Humanity's Last Exam 等基准。对比模型规模大得多：GLM-5.2 有 753B 参数，DeepSeek V4 Pro 0813 有 1.7T 参数，而 Luna 的规模未公开。

rss · Simon Willison · 8月17日 23:58

**背景**: Artificial Analysis Intelligence Index 是一个独立合成的指标，用于衡量大语言模型的“聪明程度”，其评测范围已从问答数据集扩展到智能体任务和长上下文推理。Qwen 是阿里巴巴的开源权重大模型系列，Qwen 3.8 27B 是其最新的 27B 参数版本之一，可通过 Hugging Face 和 Ollama 获取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://ollama.com/library/qwen3.8:27b">qwen 3 . 8 : 27 b</a></li>

</ul>
</details>

**标签**: `#ai`, `#llms`, `#qwen`, `#benchmark`, `#efficiency`

---