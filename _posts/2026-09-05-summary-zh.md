---
layout: default
title: "Horizon Summary: 2026-09-05 (ZH)"
date: 2026-09-05
lang: zh
---

> 从 28 条内容中筛选出 2 条重要资讯。

---

1. [语言模型可声明自身注意力以减少长上下文开销](#item-1) ⭐️ 8.0/10
2. [Anthropic 计划最高 2 万亿美元估值 IPO，外部信托掌握董事会多数任命权](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [语言模型可声明自身注意力以减少长上下文开销](https://www.reddit.com/r/MachineLearning/comments/1w7sgf3/language_models_can_control_their_own_attention_r/) ⭐️ 8.0/10

研究者提出了“声明式注意力”（Declarative Attention, DA）协议：语言模型在思维链中输出 <global>、<focus>、<local> 等标记，声明接下来需要关注的上下文区域。在 Gemma-4-31B 与 Qwen-3.6-27B 上的零样本测试中，DA 在 15 项长上下文任务上把解码时需读取的 token 数分别降低 52.0% 和 31.1%，而精度仅下降 1.27 和 2.75 个百分点。 长上下文推理的瓶颈在于每一步生成都要读取完整的键值缓存（KV cache），在百万 token 级对话中尤为突出。DA 为稀疏注意力开辟了一条新的内生机理路径：模型无需借助额外的打分网络，即可自行选择注意力区域，有望显著降低长上下文服务的成本。 DA 是零样本方法，可直接用于现有模型，无需微调或额外的检索模型；推理引擎将模型的声明当作工具调用解析，并据此生成注意力掩码。作者指出，模型声明的模式未必最优，若将 DA 纳入训练过程，有望进一步改善精度与效率之间的权衡。

reddit · r/MachineLearning · /u/eigenlaplace · 9月5日 06:07

**背景**: Transformer 依靠注意力机制来决定每个历史 token 对当前输出的权重；在自回归解码时，每个新 token 都要读取之前所有 token 的键值，这一 KV 缓存会随上下文长度不断增大。以往的稀疏注意力方法通常用轻量级代理分数预先筛选相关 token，但每步仍需要扫描整个序列。DA 的思路不同：它让语言模型在生成思维链时自己声明需要的是完整上下文、某个特定区域还是仅最近的输出，推理引擎随后可以跳过被声明为无关的 KV 缓存部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.02737v1">Language Models Can Control Their Own Attention - arXiv.org</a></li>
<li><a href="https://arxiv.deeppaper.ai/papers/2609.02737v1">Language Models Can Control Their Own Attention | Arxiv - DeepPaper</a></li>
<li><a href="https://r4j4n.github.io/blogs/posts/kv/">Transformers Optimization: Part 1 - KV Cache | Rajan Ghimire</a></li>

</ul>
</details>

**标签**: `#attention`, `#efficiency`, `#language models`, `#KV cache`, `#inference`

---

<a id="item-2"></a>
## [Anthropic 计划最高 2 万亿美元估值 IPO，外部信托掌握董事会多数任命权](https://www.ft.com/content/9536c7b9-c600-48ec-8fe2-453b0ca187e9) ⭐️ 8.0/10

据报道，Anthropic 正筹备首次公开募股（IPO），估值最高或达 2 万亿美元。在其治理架构下，长期利益信托（LTBT）已任命 7 名董事中的 4 名，并且公司须在发布新 AI 模型等重大行动前通知该信托。 此事意义重大，因为它可能成为规模最大的 AI 公司上市之一，也是 AI 行业的标志性事件。LTBT 掌握特殊治理权力，表明 Anthropic 在走向公开市场时试图将长期公共利益与股东压力分离开来。 LTBT 不持有 Anthropic 任何股权，却已选出 7 名董事中的 4 名，并可罢免其所任命的董事。除须提前获知新 AI 模型发布外，信托还会定期与管理层沟通，以监督公司的长期利益。

telegram · zaihuapd · 9月5日 01:26

**背景**: Anthropic 是一家公益公司（PBC），这种法律结构要求其在追求股东利益的同时兼顾公共利益。它还设立了长期利益信托（LTBT），受托人不持有公司股份，但拥有包括任免董事会多数成员在内的实质性治理权力，而且该信托的权限会随着公司发展逐步扩大。近期，前美联储主席本·伯南克加入 LTBT，进一步凸显了该机构在监督 AI 风险与公共利益方面的角色。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wallstreetcn.com/articles/3776607">前美联储主席伯南克加入Anthropic 治 理 机构，参与监督AI...</a></li>
<li><a href="https://penchan.co/market/ai/anthropic/why-public-benefit-corporation/">Anthropic 為 什 麼 是 公 益 公司？ PBC... | 小企鵝 Penchan</a></li>
<li><a href="https://www.tmtpost.com/8059401.html">伯南克加入Anthropic 长 期 利 益 信 托 ：美联储独立性逻辑能否延伸到AI...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#corporate governance`

---