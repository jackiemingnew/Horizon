---
layout: default
title: "Horizon Summary: 2026-09-05 (EN)"
date: 2026-09-05
lang: en
---

> From 28 items, 2 important content pieces were selected

---

1. [Language Models Declare Their Own Attention to Reduce Long-Context Cost](#item-1) ⭐️ 8.0/10
2. [Anthropic plans up to $2T IPO as external trust controls board picks](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Language Models Declare Their Own Attention to Reduce Long-Context Cost](https://www.reddit.com/r/MachineLearning/comments/1w7sgf3/language_models_can_control_their_own_attention_r/) ⭐️ 8.0/10

Researchers propose Declarative Attention (DA), a protocol in which language models emit tokens such as <global>, <focus>, and <local> inside their chain-of-thought to announce where they will attend. In zero-shot tests on Gemma-4-31B and Qwen-3.6-27B across 15 long-context tasks, DA reduces the number of attended tokens during decoding by 52.0% and 31.1% respectively, with accuracy drops of only 1.27 and 2.75 percentage points. Long-context inference is bottlenecked by reading the entire key-value cache at every generation step, especially for tasks over million-token conversations. DA offers a new intrinsic avenue for sparse attention that lets the model choose its own attention regions without an extra scoring network, potentially making long-context serving much cheaper. DA is zero-shot and works on off-the-shelf models, meaning no fine-tuning or auxiliary retrieval model is required; the inference engine parses the model's declarations like tool calls and derives the attention mask accordingly. The authors note that the declared modes are not necessarily optimal and that incorporating DA into training could further improve the accuracy-efficiency trade-off.

reddit · r/MachineLearning · /u/eigenlaplace · Sep 5, 06:07

**Background**: Transformers use attention to determine how much weight each past token gets; during autoregressive decoding, each generated token must read keys and values from all previous tokens, and this KV cache becomes bigger with context length. Existing sparse-attention work often pre-filters tokens using lightweight proxy scores, but that still scans the entire sequence each step. DA takes a different approach: it asks the model itself, while producing its chain-of-thought, to declare whether it needs the full context, a specific region, or only the recent output. The inference engine can then skip the declared-irrelevant parts of the KV cache.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.02737v1">Language Models Can Control Their Own Attention - arXiv.org</a></li>
<li><a href="https://arxiv.deeppaper.ai/papers/2609.02737v1">Language Models Can Control Their Own Attention | Arxiv - DeepPaper</a></li>
<li><a href="https://r4j4n.github.io/blogs/posts/kv/">Transformers Optimization: Part 1 - KV Cache | Rajan Ghimire</a></li>

</ul>
</details>

**Tags**: `#attention`, `#efficiency`, `#language models`, `#KV cache`, `#inference`

---

<a id="item-2"></a>
## [Anthropic plans up to $2T IPO as external trust controls board picks](https://www.ft.com/content/9536c7b9-c600-48ec-8fe2-453b0ca187e9) ⭐️ 8.0/10

Anthropic is reportedly preparing an initial public offering that could value it as high as $2 trillion. Under its governance structure, the Long-Term Benefit Trust (LTBT) has appointed 4 of the company's 7 directors and must be notified of major actions such as releasing new AI models. This matters because it could be one of the largest AI company listings ever and a defining event for the AI industry. The LTBT's unusual governance power shows Anthropic trying to separate long-term public benefit from shareholder pressure as it moves toward public markets. The LTBT holds no equity in Anthropic, yet it selected 4 of the 7 board members and can remove the directors it appointed. Besides being notified about new AI model releases, the trust regularly communicates with company management to oversee long-term interests.

telegram · zaihuapd · Sep 5, 01:26

**Background**: Anthropic is a public benefit corporation (PBC), a legal structure that requires balancing public benefit with shareholder interests. The company created the Long-Term Benefit Trust (LTBT), whose members are independent trustees holding no stock but possessing real governance power, including appointing or removing a majority of the board; the trust's authority is designed to grow over time as Anthropic scales. Recently, former Federal Reserve chair Ben Bernanke joined the LTBT, underscoring its role in overseeing AI risks and public interest.

<details><summary>References</summary>
<ul>
<li><a href="https://wallstreetcn.com/articles/3776607">前美联储主席伯南克加入Anthropic 治 理 机构，参与监督AI...</a></li>
<li><a href="https://penchan.co/market/ai/anthropic/why-public-benefit-corporation/">Anthropic 為 什 麼 是 公 益 公司？ PBC... | 小企鵝 Penchan</a></li>
<li><a href="https://www.tmtpost.com/8059401.html">伯南克加入Anthropic 长 期 利 益 信 托 ：美联储独立性逻辑能否延伸到AI...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#corporate governance`

---