---
layout: default
title: "Horizon Summary: 2026-10-25 (ZH)"
date: 2026-10-25
lang: zh
---

> 从 29 条内容中筛选出 3 条重要资讯。

---

1. [俄勒冈警方为一名警员的记录报价 250 万美元、需 21 年工时](#item-1) ⭐️ 8.0/10
2. [Cerebras 详解如何在自家芯片上部署万亿参数模型](#item-2) ⭐️ 8.0/10
3. [Brotli 高危漏洞 CVE-2026-111497（CVSS 9.2）波及 Python HTTP 组件](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [俄勒冈警方为一名警员的记录报价 250 万美元、需 21 年工时](https://theintercept.com/2026/10/01/oregon-police-misconduct-public-records-cost-fee/) ⭐️ 8.0/10

据 The Intercept 报道，俄勒冈州尤金市警察局告知一家当地新闻媒体，要完成其针对一名警员的公共记录查阅申请，至少需要 44,816 个工作人员工时，费用约为 2,484,599.04 美元。这相当于一名员工约 21 年的全职工作量，而申请所涉及的只是一名警员。 用一个高得离谱的报价，机构就能在不正式拒绝申请的情况下事实上拒绝提供记录，从而把记者和普通公民挡在公共监督之外。如果这种做法成为常态，那么即便法律条文上保障查阅权，公众查阅政府记录这一新闻自由与警察问责的基石也会被实质性地侵蚀。 44,816 个工时的报价折算下来约等于 21 年不间断的全职工作，而美元估算精确到美分，即 2,484,599.04 美元——这种精确程度让人觉得该报价是精心计算出来的，而非粗略估计。申请所涉的只是一名警员的记录，与索取范围之窄相比，这一估算规模显得格外刺眼。

hackernews · tdeck · 10月25日 18:04 · [社区讨论](https://news.ycombinator.com/item?id=50234232)

**背景**: 公共记录法——包括联邦层面的《信息自由法》(FOIA) 以及各州的对应法规，例如俄勒冈州的公共记录法——赋予公众和媒体索取政府文件的权利。这类法律通常允许机构就检索和脱敏处理所需的人工工时与复制成本收费，这便制造了一个漏洞：机构在纸面上遵守了法律，却开出一个任何申请人都付不起的价码。记者通常会以公共利益为由申请减免费用，一些地区也设定了收费上限或法定答复期限，但执行力度差异很大。

**社区讨论**: 评论者将此案视为一种更普遍模式的一部分：有人描述自己向学区申请记录后，对方数月来每月只挤出一点点材料，且看不到尽头；也有人把美国制度与英国法定的 30 天答复期限作对比，并警告德国官员（尤其是延斯·施潘）正推动改革，试图让这类高得令人望而却步的收费合法化。还有人举出更夸张的先例：2015 年美国国防部曾对一项 FOIA 申请估算需要 1500 万个工时、花费 6.6 亿美元，相当于 1700 多年的工作量。

**标签**: `#public-records`, `#FOIA`, `#government-transparency`, `#press-freedom`, `#policy`

---

<a id="item-2"></a>
## [Cerebras 详解如何在自家芯片上部署万亿参数模型](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras) ⭐️ 8.0/10

Cerebras 发布技术博客，详细介绍了其如何在晶圆级硬件上部署万亿参数的前沿 AI 模型，并解释了模型各层如何流经芯片上的处理核心。该文章在 Hacker News 上引发热议（348 个赞、127 条评论），讨论焦点在于这种方案在现实中是否真的可用。 以极高吞吐量服务万亿参数模型是 AI 基础设施中最困难的问题之一，而 Cerebras 的晶圆级方案是相对多 GPU 集群的一条真正不同的路径。如果该方案能够规模化落地，就可能重塑推理的经济性，并为企业提供比 GPU 云更快的选择。 Cerebras 的 CS-3 系统基于 Wafer Scale Engine 3，这是一颗采用 5nm 工艺、拥有 4 万亿个晶体管和 90 万个 AI 优化核心的芯片，而较新的 CS-4 则集成了三颗 WSE-3 Turbo 处理器。评论者提出的一个关键限制是，要达到这样的速度需要极其庞大的硬件，因此可用容量有限，且所服务的模型往往比前沿模型落后数月。

hackernews · gmays · 10月25日 01:33 · [社区讨论](https://news.ycombinator.com/item?id=50227356)

**背景**: Cerebras 制造的 AI 芯片与 Nvidia GPU 截然不同：它不把硅晶圆切割成许多独立芯片，而是保留整片晶圆作为一颗巨型处理器，从而获得巨大的片上内存带宽，并避免多 GPU 集群的网络瓶颈。万亿参数模型体量极大，通常必须拆分到大量 GPU 上，导致推理又慢又贵。Wafer Scale Engine 3 是该设计的第三代产品，也是 Cerebras 推理云服务的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/chip">Cerebras WSE-3 Turbo | Wafer-Scale AI Chip</a></li>
<li><a href="https://developer.nvidia.com/blog/demystifying-ai-inference-deployments-for-trillion-parameter-large-language-models/">Demystifying AI Inference Deployments for Trillion Parameter ...</a></li>

</ul>
</details>

**社区讨论**: 评论者看法分歧：一些人称赞这项技术，但认为 Cerebras 缺乏足够资金和制造能力来满足需求，因此只能靠低价套餐让用户体验，同时提供较旧的模型。另一些人则为该策略辩护，预计几个月内就能以更低成本和数倍速度获得接近前沿的模型；也有人指出可用的模型（如 GPT-OSS 120B）虽然速度快，但准确性不足以满足需求，还有一位有专业合作经验的评论者称该公司技术卓越但团队能力令人费解地不足。

**标签**: `#AI`, `#hardware`, `#inference`, `#Cerebras`, `#large language models`

---

<a id="item-3"></a>
## [Brotli 高危漏洞 CVE-2026-111497（CVSS 9.2）波及 Python HTTP 组件](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 8.0/10

Brotli 解码器漏洞 CVE-2026-111497（最初以 Node2Shell 名称披露，后被称为 HTTP2Shell）影响 Brotli 1.0.3 至 1.2.0 版本，CVSS 4.0 评分为 9.2。修复版本为 Python 侧的 Brotli 1.2.1、brotlicffi 1.2.1.0，以及 Node.js 22.23.4、24.22.1 和 26.12.1。 Brotli 是浏览器与服务器协商使用的核心 HTTP 压缩格式，因此存在漏洞的解码器处于大量已部署的 Node.js 与 Python Web 技术栈的请求处理路径上。未认证攻击者只要能够发送特制的压缩流即可触发内存损坏，因此任何运行这些运行时或其内嵌库的用户都需要尽快修补。 该漏洞利用后可能造成内存损坏、敏感数据泄露、进程崩溃，甚至可能执行任意代码；据称该问题于今年 2 月被发现。漏洞位于解码器而非编码器，这意味着即使服务器或客户端自身从不进行压缩，只要它们解压攻击者提供的 Brotli 内容就会暴露在风险之中。

telegram · zaihuapd · 10月25日 02:42

**背景**: Brotli 是谷歌于 2015 年发布的开源无损压缩算法，重点面向 HTTP 压缩场景，通过结合 LZ77 式回溯引用、霍夫曼编码以及内置静态字典，实现比 gzip 更高的压缩比。由于它是 HTTP 的标准内容编码之一，浏览器与服务器会透明地解码 Brotli 数据流；而 brotlicffi 这类库提供 CFFI 绑定，使 Python 程序能够直接调用参考 C 实现。CVSS 是由 FIRST 维护的业界通用漏洞评分框架，取值 0 到 10 分，其 4.0 版本进一步细化了攻击复杂度与可被利用条件的描述方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/Brotli">Brotli - 维基百科，自由的百科全书</a></li>
<li><a href="https://pypi.org/project/brotlicffi/">Python CFFI bindings to the Brotli library</a></li>
<li><a href="https://www.first.org/cvss/v4-0/cvss-v40-specification.pdf">CVSS v4.0 Specification - 2024-06-18 - FIRST</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#brotli`, `#nodejs`, `#python`

---