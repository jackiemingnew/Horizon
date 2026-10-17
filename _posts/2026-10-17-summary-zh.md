---
layout: default
title: "Horizon Summary: 2026-10-17 (ZH)"
date: 2026-10-17
lang: zh
---

> 从 34 条内容中筛选出 2 条重要资讯。

---

1. [DeepSeek 发布 V4.1-Flash-1017，编码基准成绩提升](#item-1) ⭐️ 8.0/10
2. [iPhone 18 Pro 被指实现免电脑、重启后仍生效的 untethered 越狱](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek 发布 V4.1-Flash-1017，编码基准成绩提升](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) ⭐️ 8.0/10

DeepSeek 在 Hugging Face 与自家 API 上发布了 DeepSeek-V4.1-Flash-1017，官方将其描述为 DeepSeek-V4.1-Flash 的一次小版本更新，但在推理、编码与智能体任务上带来了实质性提升。根据官方新闻页的数据，新版本在 11 项编码基准中的 10 项上超过了 Sol 5.6。 这次发布在编码助手市场上继续对 OpenAI 和 Anthropic 形成压力，而 Hacker News 上 657 分、556 条评论的讨论表明，开发者越来越看重吞吐量、延迟和透明度，而不只是基准分数。对于构建多智能体编码流水线的团队来说，一个在基准测试上有竞争力、更便宜更快的模型足以改变实际的生产选型。 根据模型卡和 OpenRouter 页面，V4.1-Flash 是一个稀疏多模态混合专家（MoE）模型，拥有 552B 参数的主干，但输入侧仅激活 8B、输出侧激活 16B 参数，支持最长一百万个 token 的上下文，并且是首个基于 DeepSeek 自研 Causal Encoder-Decoder（CED）架构的模型。社区指出，对比对象是 Sol 5.6 而非更新的 Sol 6.1，因此这一基准领先是针对上一代模型取得的。

hackernews · theykk · 10月17日 08:21 · [社区讨论](https://news.ycombinator.com/item?id=50129045)

**背景**: DeepSeek 是一家中国 AI 实验室，以发布开放权重模型著称——其权重可以直接从 Hugging Face 下载，而不必只通过付费 API 使用。混合专家（MoE）模型保留极大的总参数量，但每个 token 只经过一小部分专家，从而降低推理成本与延迟，这正是 552B 参数模型依然能跑得很快的原因。SWE-bench、HumanEval、LiveCodeBench 等编码基准通过把生成的代码放到单元测试中运行来给模型打分；文中的“Sol”和“Opus”分别指 OpenAI 与 Anthropic 的竞品前沿模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek -ai/ DeepSeek - V 4 . 1 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4.1-flash">DeepSeek V 4 . 1 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">Introducing DeepSeek - V 4 . 1 - Flash : smarter, faster, more efficient.</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同 DeepSeek 在纯基准成绩上并未明显领先 Sol 或 Gemini，但认为它“用起来”更好：token 生成速度快、首 token 延迟低，而且思维链（CoT）公开可见、不会被莫名的安全审查拦截。不过一次针对 200 多个文件改动的 C++ 代码库进行多智能体代码评审的实测削弱了这一印象：DeepSeek 通过自有 API 花了约 20 分钟才找出一个相关的 P1 问题，而 GPT 5.6 Sol 用 5 分 30 秒、GPT 6.1 Sol 用 4 分 30 秒就给出了更多相关问题，GLM 5.3 Flash 则花了一个多小时。多位用户将这次发布视为模型生态多元化价值的体现，并表示要重新用 DeepSeek 写代码。

**标签**: `#AI/ML`, `#LLM release`, `#DeepSeek`, `#coding benchmarks`, `#model comparison`

---

<a id="item-2"></a>
## [iPhone 18 Pro 被指实现免电脑、重启后仍生效的 untethered 越狱](https://x.com/calif_io/status/2111080240978223545?s=20) ⭐️ 8.0/10

研究者 @calif_io 声称在完全打补丁的 iOS 版本上为 iPhone 18 Pro 演示了公开的 untethered 越狱，重启后越狱状态依然保留且无需连接电脑；若属实，这将是自 iOS 9 以来首个公开演示的完整 untethered 越狱。其声称的攻击链由 cryptex 子系统滥用、TSS 票签欺骗和 PAC 绕过三层组成，时间点据称就在 Apple 于 9 月 14 日发布 273 个漏洞修复之后不久。 如果得到验证，这将是一个里程碑式的安全研究成果：在现代硬件上打通完整的 untethered 攻击链，直接击穿了 Apple 投入最多的三项防护——签名系统卷、服务端固件签名以及指针认证。这将牵动 Apple 的平台安全团队、越狱与漏洞利用开发者，以及所有把 iOS 当作高加固终端使用的人，也会强化这样一种论点：即便是激进打补丁的版本，仍可能存在完整攻击链。 该说法仅源自一条单源短推文，既无技术细节文章，也没有 CVE 编号或厂商、第三方的确认，因此这条三层攻击链应视为未经证实。单看每一层在理论上都说得通——cryptex 容器、TSS 票签校验和 PAC 签名指针都是真实存在且防护严密的组件——但要把三者串成在当前旗舰机型上持久生效、无需电脑的越狱，恰恰是最需要独立复现的部分。

telegram · zaihuapd · 10月17日 10:34

**背景**: 越狱就是解除 iOS 对运行未签名代码的限制；"untethered" 越狱在正常重启后依然有效、无需再从电脑上重新运行漏洞利用，因此比 tethered 或 semi-tethered 越狱困难得多。cryptex 是 Apple 用于挂载加密签名的密封辅助系统卷的机制，而 TSS（Ticket Signing Server）是 Apple 用来签发签名票据、决定设备可接受哪些固件的服务，这也正是 TSS 欺骗成为降级与持久化利用核心的原因。PAC（指针认证）是一种 ARM 缓解措施，通过对指针签名来阻止攻击者篡改指针重定向控制流，而在 A12 及之后芯片上，内核 PAC 绕过几乎是所有现代越狱的必经一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theapplewiki.com/wiki/PAC_Bypasses">PAC Bypasses - The Apple Wiki</a></li>
<li><a href="https://github.com/tihmstar/tsschecker">GitHub - tihmstar/tsschecker: a powerfull tool to check tss signing ...</a></li>
<li><a href="https://discussions.apple.com/thread/254340117">is Cryptex a standard part of the ios sys… - Apple Community</a></li>

</ul>
</details>

**标签**: `#iOS jailbreak`, `#security research`, `#exploit chain`, `#PAC bypass`, `#Apple`

---