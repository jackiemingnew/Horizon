---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> 从 37 条内容中筛选出 6 条重要资讯。

---

1. [库克卸任苹果 CEO，特努斯接棒聚焦 AI](#item-1) ⭐️ 9.0/10
2. [谷歌从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](#item-2) ⭐️ 8.0/10
3. [NAT：互联网中心化的原罪？](#item-3) ⭐️ 8.0/10
4. [滑动窗口注意力在长上下文推理上胜过线性注意力](#item-4) ⭐️ 8.0/10
5. [OpenClaw 2.0 发布史上最大更新，汇集逾 1.6 万个拉取请求](#item-5) ⭐️ 8.0/10
6. [DeepSeek 发布 V4 系列首款多模态模型 V4-Flash-Vision-Exp](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [库克卸任苹果 CEO，特努斯接棒聚焦 AI](https://www.bloomberg.com/news/articles/2026-08-30/apple-s-new-ceo-john-ternus-takes-reins-from-tim-cook-focusing-on-ai) ⭐️ 9.0/10

8 月 31 日，蒂姆·库克卸任苹果 CEO，约翰·特努斯于 9 月 1 日接任。现年 51 岁的硬件工程老将特努斯将优先推动 AI 功能落地，包括延期的 Siri 升级；苹果还计划在 9 月 9 日发布会上推出首款折叠屏 iPhone。 此次换帅标志着全球最具影响力的科技公司之一苹果正式将 AI 作为战略核心。折叠屏 iPhone 将开创重要的新品类别，而这次过渡也可能重塑苹果在生成式 AI 领域的竞争方式。 报道称，首款折叠屏 iPhone 将配备 12GB 内存，并深度整合 Siri AI，可结合屏幕、日历与相机信息理解现实场景。库克将继续担任执行主席，以确保过渡期的连续性。

telegram · zaihuapd · 8月31日 10:21

**背景**: 苹果是全球最大、最具影响力的科技公司之一，以 iPhone、Mac 和服务著称。CEO 更替在苹果十分罕见，而此次更替恰逢行业竞相拥抱 AI 之际，Siri 在生成式 AI 功能上已被竞争对手甩在身后。

**标签**: `#Apple`, `#CEO transition`, `#Artificial Intelligence`, `#Tim Cook`, `#John Ternus`

---

<a id="item-2"></a>
## [谷歌从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

谷歌已从 Chrome 网上应用店移除所有剩余的 Manifest V2 扩展，包括广受欢迎的广告拦截器 uBlock Origin。这标志着向 Manifest V3 过渡的完成，该过渡始于多年前的宣布。 这一变化影响了数百万依赖 uBlock Origin 等强大 MV2 广告拦截器的用户，可能使他们更容易受到侵入性广告和恶意内容的影响。这也引发了对谷歌对网络的控制以及基于 Chromium 的浏览器中广告拦截技术未来的担忧。 Manifest V3 用 Service Worker 替代了 MV2 中长期存在的后台页面，并限制远程代码执行，从而限制了扩展的过滤能力。虽然 uBlock Origin 有一个名为 uBlock Origin Lite 的 MV3 版本，但它使用 declarativeNetRequest 规则，其灵活性不如 Firefox 中可用的完整拦截引擎。

hackernews · twapi · 8月31日 21:10 · [社区讨论](https://news.ycombinator.com/item?id=49514878)

**背景**: Manifest V2 是 Chrome 扩展的旧规范，允许长期运行的后台页面和广泛的网络请求访问权限。谷歌于 2020 年宣布将逐步淘汰 MV2，转而采用 MV3，后者旨在改善隐私、安全和性能。uBlock Origin 是一款免费开源的内容拦截器，使用动态过滤来阻止广告和恶意域名；它在仍支持类似 MV2 API 的 Firefox 上效果最佳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V3 | Chrome for Developers</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V2 support timeline | Chrome for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论反映出对谷歌的强烈不满和不信任。许多用户建议改用 Firefox，指出 uBlock Origin 在那里表现更好，并且任何一家公司都不应如此控制网络。还有人强调，广告拦截现在是一个安全问题，尤其是对于可能被恶意广告欺骗的技术水平较低的用户。

**标签**: `#Chrome`, `#Manifest V3`, `#adblock`, `#privacy`, `#uBlock Origin`

---

<a id="item-3"></a>
## [NAT：互联网中心化的原罪？](https://dreamstation.systems/personal/ntppost.html) ⭐️ 8.0/10

一篇发表于 dreamstation.systems 的博客文章认为，网络地址转换（NAT）是互联网中心化的根本原因之一。这场讨论因 Linux NAT 的原始实现者 Rusty Russell 出面分享其一手的决策经验而备受关注。 这场辩论挑战了关于网络中立和端到端连接的传统假设，展示了一个务实的工程修补如何促成了当今以客户端-服务器为主导的互联网。它也凸显了 IPv4 地址节约、运营商级 NAT（CGNAT）与用户托管服务能力之间的张力。 Rusty Russell 解释说，他在 Linux NAT 实现中为了避免端口预留而将一个 IP 地址塞入更多连接，只要远程地址允许区分；这导致来自不同地址的入站流量无法路由。评论者指出，普通家用 NAT 尚可接受，而运营商级 NAT（CGNAT）被普遍视为对用户自由更严重的威胁。

hackernews · robinpie · 8月31日 02:23 · [社区讨论](https://news.ycombinator.com/item?id=49504905)

**背景**: 网络地址转换（NAT）将多个私有 IP 地址映射到一个公共 IP 地址，这一技术被广泛采用以应对 IPv4 地址耗尽。NAT 还可以通过阻止未经请求的入站连接充当基础防火墙，但它破坏了原本定义互联网的端到端原则。这使一些人认为，NAT 助长了客户端-服务器模式，并让个人更难运行随时可访问的服务器，从而推动互联网走向以数据中心为中心的中心化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Network_address_translation">Network address translation - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/computer-networks/network-address-translation-nat/">Network Address Translation (NAT) - GeeksforGeeks</a></li>
<li><a href="https://www.ietf.org/archive/id/draft-nottingham-avoiding-internet-centralization-01.html">Centralization and Internet Standards</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：有人同意 NAT 是对开放互联网的早期打击，并让用户习惯了客户端-服务器的思维；也有人认为只有运营商级 NAT（CGNAT）真正有害，普通 NAT 保护了数以百万计的不安全设备。Rusty Russell 对设计权衡的坦诚回顾为争论双方都增添了分量，语气中带有对意外后果的遗憾。

**标签**: `#NAT`, `#internet architecture`, `#centralization`, `#networking`, `#commentary`

---

<a id="item-4"></a>
## [滑动窗口注意力在长上下文推理上胜过线性注意力](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/) ⭐️ 8.0/10

一篇新的 arXiv 预印本（2608.28444）指出，带注意力汇（attention sinks）的滑动窗口注意力（SWA）在 Needle-in-a-Haystack 和 BABILong 等长上下文推理基准上，性能比线性注意力变体高出 2 到 10 倍。作者认为，从后训练到线性注意力的研究路线没有与更简单的基线进行恰当比较，并建议改用 SWA。 这一发现挑战了当前业界将大量后训练算力投入到线性注意力模型的趋势。如果得到验证，它表明一个简单、快速且内存高效的基线在长上下文推理上可能更优，从而可能节省大量资源。 论文重点研究带注意力汇的 SWA——这些特殊标记用于吸收多余注意力并稳定滑动窗口生成。论文称线性注意力“可能显示出一些前景”，但可能需要在从头训练或大量后训练后才能比肩 SWA，作者“强烈建议改用 SWA”。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 8月31日 16:35

**背景**: 标准 softmax 注意力在序列长度上的计算成本是二次方的，这使得长上下文处理非常昂贵。滑动窗口注意力将每个 token 限制为只关注局部窗口内的内容，从而把成本降到线性，而注意力汇（保留早期 token）有助于稳定生成。线性注意力变体也旨在降低复杂度，但通常需要后训练或从头训练才能保持性能。像 BABILong 这样的基准会测试模型在长上下文中跨多个事实进行推理的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.28444v1">Sliding - window beats linear attention</a></li>
<li><a href="https://carnotresearch.medium.com/let-the-chaos-sink-in-481c8a37471e">Let the Chaos Sink In. Balancing attention in transformers | Medium</a></li>
<li><a href="https://arxiv.org/abs/2406.10149">[2406.10149] BABILong : Testing the Limits of LLMs with Long ...</a></li>

</ul>
</details>

**标签**: `#attention`, `#long-context`, `#LLM`, `#efficient transformers`, `#research`

---

<a id="item-5"></a>
## [OpenClaw 2.0 发布史上最大更新，汇集逾 1.6 万个拉取请求](https://openclaw.ai/blog/openclaw-2-accidentally) ⭐️ 8.0/10

OpenClaw 于 8 月 30 日发布了史上最大更新 2.0 版，汇集了来自 933 名贡献者（其中 569 人为首次参与）的逾 1.6 万个拉取请求。该版本对安装、消息、记忆、技能、模型、浏览器、插件与安全等环节进行了全面改造，并新增了支持多人协作的共享云端会话。 此次发布对于开源 AI 助手领域而言是一个重要里程碑，展现了强大的社区活力和全面革新的用户体验。贡献规模之大（约占项目迄今全部拉取请求的一半）表明 OpenClaw 社区已经变得非常活跃和繁荣。 为准备这次更新，项目团队近七周未发布新版本；新版简化了安装流程，重建了浏览器端体验，并新增了共享云端会话，使团队可以接管正在进行的工作。此次更新覆盖记忆、技能、模型、安全等所有核心领域，并且 OpenClaw 运行在用户自己的机器上，通过用户已有的聊天应用即可使用。

telegram · zaihuapd · 8月31日 04:38

**背景**: OpenClaw 是一款免费开源的自主任 AI 代理，通过大型语言模型（LLM）执行任务，并以消息平台作为其主要用户界面。拉取请求是 Git 和 GitHub 等分布式版本控制系统中允许贡献者提出、审查和合并代码更改的机制；如此大量的拉取请求表明该项目拥有广泛的协作开发。OpenClaw 旨在提供一个在本地运行并与用户已有聊天应用集成的开源 AI 助手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw</a></li>
<li><a href="https://openclaw.ai/">OpenClaw — Open -Source AI Assistant</a></li>
<li><a href="https://tbreak.com/openclaw-2-0-rebuilt-browser-app/">OpenClaw 2.0: rebuilt browser app, shared sessions</a></li>

</ul>
</details>

**标签**: `#OpenClaw`, `#software release`, `#AI assistant`, `#open source`, `#major update`

---

<a id="item-6"></a>
## [DeepSeek 发布 V4 系列首款多模态模型 V4-Flash-Vision-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) ⭐️ 8.0/10

DeepSeek 在 Hugging Face 发布了 DeepSeek-V4-Flash-Vision-Exp，这是 V4 系列首款实验性多模态模型，基于 V4-Flash 架构加入视觉模块并进行持续训练。其多模态 agent 基准 ApexBench 得分从 26.2 提升至 36.5，文本 agent 任务表现基本持平。 这一更新意义重大，因为它首次为 V4 系列带来多模态理解能力，并显著提升了 agent 能力，使模型在视觉-语言任务中更有用。使用 DeepSeek 模型的开发者和企业现在可以通过 API 使用这一能同时处理文本和视觉输入的实验性模型。 模型权重已在 Hugging Face 上发布，API 使用模型 ID 'deepseek-v4-flash-vision-exp' 即可访问。该模型被标注为实验性；ApexBench 是 DeepSeek 报告中所用的 agent 基准，采用 Pass@1 指标，但该基准的任务数量和创建机构尚未完全公开。

telegram · zaihuapd · 8月31日 11:41

**背景**: DeepSeek 是一家以开源权重大模型（如 V3 和 V4）著称的中国 AI 实验室。V4-Flash 是其中注重速度的纯文本版本，此次实验性发布在其基础上加入视觉模块并进行持续训练，以解锁多模态理解能力。ApexBench 评估的是交互式多模态 agent 在学术海报编辑、分布式 HPC 分析等实际任务上的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp">deepseek-ai/ DeepSeek - V 4 - Flash - Vision - Exp · Hugging Face</a></li>
<li><a href="https://api-docs.deepseek.com/updates/">DeepSeek API Docs</a></li>
<li><a href="https://www.datalearner.com/en/benchmarks/apexbench">ApexBench: Multimodal Agent Benchmark and Model Scores ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#multimodal`, `#AI model`, `#vision`, `#agent`

---