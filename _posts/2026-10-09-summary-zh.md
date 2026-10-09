---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09
lang: zh
---

> 从 37 条内容中筛选出 3 条重要资讯。

---

1. [中国科学家研制成功核光钟](#item-1) ⭐️ 9.0/10
2. [OpenAI API 为 GPT-6.1 Sol 新增 Ultrafast 模式](#item-2) ⭐️ 8.0/10
3. [SpaceX 拟收购全美低频段频谱，为 Starlink Mobile 铺路](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [中国科学家研制成功核光钟](https://www.nature.com/articles/s41586-026-11122-1) ⭐️ 9.0/10

清华大学研究团队利用自主研制的 148 纳米连续波真空紫外激光和掺钍-229 氟化钙晶体，在国际上率先研制出核光钟并实现稳定运行，相关成果发表于《自然》。该时钟以钍-229 原子核的能级跃迁作为计时基准。 核光钟的精度有望比目前最好的原子钟提高约一个数量级，因此一台可稳定运行的核光钟未来可能支撑国际单位制“秒”的重新定义，并提升卫星导航、深空探测的计时精度以及基础物理检验能力。这也标志着精密测量从电子跃迁向原子核跃迁扩展，而中国在这一方向上率先拿出了成果。 该时钟以钍-229m 同质异能态极低能量的跃迁（约 8.36 电子伏特，对应真空紫外波段的 148.38 纳米）作为参考频率，而这一波段恰恰是窄线宽连续波激光最难实现的区域。此前 2026 年已有多项工作演示了 148 纳米连续波光源，包括镉蒸气中的四波混频和四硼酸锶中的二次谐波产生，正是这些进展使共振激发钍原子核成为可能。

telegram · zaihuapd · 10月8日 05:19

**背景**: 传统原子钟依靠原子核外电子在不同能级间跃迁产生的振荡来计时，而核光钟使用的是原子核内部的跃迁；由于原子核对外界杂散电磁场和碰撞远不敏感，这类时钟理论上更稳定、更精确。钍-229 之所以特别适合，是因为它最低的激发态（同质异能态钍-229m）仅比基态高约 8.36 电子伏特，低到可以用真空紫外激光直接驱动，这是其他已知核同质异能态都做不到的。把钍-229 掺入氟化钙等晶体中可以同时探测大量原子核，正是这种固态方案让稳定运行成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nuclear_optical_clock">Nuclear optical clock</a></li>
<li><a href="https://www.nature.com/articles/s41586-026-11084-4">A thorium-229 optical nuclear clock with feedback loop | Nature</a></li>
<li><a href="https://www.nature.com/articles/s41586-026-10107-4">Continuous-wave narrow-linewidth vacuum ultraviolet laser ...</a></li>

</ul>
</details>

**标签**: `#nuclear-clock`, `#thorium-229`, `#precision-measurement`, `#metrology`, `#physics-research`

---

<a id="item-2"></a>
## [OpenAI API 为 GPT-6.1 Sol 新增 Ultrafast 模式](https://developers.openai.com/api/docs/changelog) ⭐️ 8.0/10

OpenAI 在 Responses API（v1/responses）中为 GPT-6.1 Sol 新增了名为 Ultrafast 的服务层级，生成速度相对 Standard 最高提升约 8 倍。该层级面向所有 API 用户开放，价格为 Standard 的 6 倍，短上下文下约为每百万 token 输入 12 美元、缓存输入 0.60 美元、输出 60 美元。 这为对延迟敏感的生产负载——实时智能体、交互式编程助手和多步工作流——提供了一条无需更换模型即可换取速度的途径。它也把“速度溢价”正式写进 OpenAI 的定价体系，让开发者熟悉的成本与延迟权衡直接体现在 API 计费中。 所引用的价格针对短上下文场景，提示或输出更长时成本会更高；8 倍是相对 Standard 的最高速度描述，并非有保证的吞吐量。该更新目前仅以变更日志形式出现，尚未公布独立的第三方基准测试，也缺少速率限制与可用性方面的细节说明。

telegram · zaihuapd · 10月9日 00:00

**背景**: GPT-6.1 Sol 是 OpenAI GPT-6.1 模型家族的一员，与 Astra 一同于 2026 年 9 月 29 日发布，定位是在能力与成本之间取得平衡，适用于写代码、理解文档和执行多步业务流程等日常工作。Responses API 于 2025 年 3 月推出，是 OpenAI 用于构建智能体应用的接口，支持有状态交互以及文件搜索、网络搜索和计算机操作等内置工具。服务层级让开发者可以在同一模型上选择不同的性价比档位，而不必为了调整速度去更换模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT-6.1 Sol | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6.1_Sol">GPT-6.1 Sol</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#API`, `#GPT-6.1 Sol`, `#Ultrafast mode`, `#Pricing`

---

<a id="item-3"></a>
## [SpaceX 拟收购全美低频段频谱，为 Starlink Mobile 铺路](https://x.com/SpaceX/status/2108291133025698301) ⭐️ 8.0/10

SpaceX 宣布与 Grain Management 达成协议，拟收购一套覆盖全美的低频段频谱许可证组合，即 800 MHz 频段中最多 14 兆赫兹的成对频谱，用于其 Starlink Mobile 服务。公司表示，把这批频谱与 Gen2 星座结合起来，将让美国民众无论身处何地都能获得高速移动宽带。 低频段频谱穿透建筑物能力强、传播距离远，恰好补上了长期以来阻碍卫星直连手机服务与地面运营商竞争的最后一个关键技术缺口。如果交易完成，Starlink 将从卫星宽带提供商转变为与 AT&T、Verizon 和 T-Mobile 正面竞争的全国性移动运营商，这三家传统运营商的股价在消息公布后大幅下跌。 该频谱组合为 800 MHz 频段中最多 14 兆赫兹的成对频谱，SpaceX 称其填补了"最后几项关键技术缺口之一"，并使 Starlink Mobile 能够在室内正常使用。交易仍需获得包括 FCC 在内的监管机构批准，双方未披露交易金额。

telegram · zaihuapd · 10月9日 01:04

**背景**: 低频段频谱一般指 1 GHz 以下的频率，其信号传播距离远、穿透墙体能力强，因此被视为移动通信中最宝贵的资源之一——T-Mobile 正是凭借 600 MHz 频谱建立起覆盖优势。卫星直连手机服务过去主要依赖与卫星之间的视线链路，因此在室内、隧道和高楼密集的城市中往往难以使用，这也是 Starlink 需要地面频谱的根本原因。Gen2 是 SpaceX 的第二代 Starlink 星座，FCC 已额外批准 7,500 颗 Gen2 卫星，使其获准总数达到约 15,000 颗，这些卫星面向更高容量和来自太空的移动覆盖而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/10/08/spacex-spectrum-license-att-verizon-tmobile.html">SpaceX spectrum license hammers shares of AT&T ... - CNBC</a></li>
<li><a href="https://www.satellitetoday.com/connectivity/2026/10/08/spacex-moves-to-acquire-nationwide-low-band-spectrum-for-starlink-mobile/">SpaceX Moves to Acquire Nationwide Low-Band Spectrum for ...</a></li>
<li><a href="https://finance.yahoo.com/technology/articles/spacex-agrees-acquire-nationwide-800-212204943.html?fr=sycsrp_catchall">SpaceX Agrees to Acquire Nationwide 800 MHz Low-Band Spectrum ...</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#spectrum`, `#telecom`, `#satellite-internet`

---