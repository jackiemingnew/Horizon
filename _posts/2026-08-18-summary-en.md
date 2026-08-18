---
layout: default
title: "Horizon Summary: 2026-08-18 (EN)"
date: 2026-08-18
lang: en
---

> From 30 items, 4 important content pieces were selected

---

1. [Mojo🔥 is now open source](#item-1) ⭐️ 9.0/10
2. [The Amazon Tax: How Ad-Driven Search Erodes Shopper Trust](#item-2) ⭐️ 8.0/10
3. [Linux 7.3 Improves Performance When Running Out of VRAM](#item-3) ⭐️ 8.0/10
4. [Qwen 3.8 27B Scores 52 on Artificial Analysis, Matching GPT-5.6 Luna](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mojo🔥 is now open source](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 9.0/10

Mojo programming language's compiler and toolchain are now open source under Apache 2, following the 1.0 release.

rss · Simon Willison · Aug 18, 21:39

**Tags**: `#Mojo`, `#open source`, `#programming languages`, `#compiler`, `#AI`

---

<a id="item-2"></a>
## [The Amazon Tax: How Ad-Driven Search Erodes Shopper Trust](https://seths.blog/2026/08/the-amazon-tax/) ⭐️ 8.0/10

Seth Godin's blog post argues that Amazon's search results now prioritize sponsored ads and Amazon's own interests over the best product for shoppers. The Hacker News discussion shows widespread user frustration with the degraded search quality and ad-saturated results. Amazon is the default product search engine for millions of consumers, so degraded search results affect purchasing decisions at massive scale. This erodes trust in the platform and raises broader questions about platform economics where marketplaces monetize search intent rather than serving users. Amazon's A9 algorithm historically ranked products based on relevance and sales performance, but Sponsored Products placements now occupy a large share of results. Commenters report that roughly three-quarters of search results are sponsored ads, and the A10 algorithm evolution further weights conversion rate and external traffic.

hackernews · herbertl · Aug 18, 13:22 · [Discussion](https://news.ycombinator.com/item?id=49345263)

**Background**: Amazon's search engine is not a neutral discovery tool; it is a retail revenue engine. The A9/A10 algorithm ranks products by a mix of keyword relevance, sales velocity, conversion rate, and advertising spend. This incentivizes sellers to pay for ads to break through, as one commenter notes, even when they have a quality product with few reviews. The result is a feedback loop where ads dominate results and organic visibility shrinks.

<details><summary>References</summary>
<ul>
<li><a href="https://salesduo.com/blog/amazon-a9-search-engine-guide/">Amazon A9 Algorithm: How Amazon’s Search Engine Works (2026)</a></li>
<li><a href="https://www.repricerexpress.com/amazons-algorithm-a9/">Understanding Amazon's A9 Algorithm: Boost Your Product Rankings</a></li>
<li><a href="https://feedvisor.com/university/a9-search-engine/">Amazon A9 Algorithm: How It Works & How to Rank (2026)</a></li>

</ul>
</details>

**Discussion**: HN commenters largely agree with the critique, sharing personal anecdotes of shifting purchases away from Amazon. Some express nostalgia for when search meant locating the exact item, while others add economic analysis about platforms monetizing signal-to-noise degradation. A seller perspective counters that ads are the only way for new quality products to break through.

**Tags**: `#Amazon`, `#e-commerce`, `#search`, `#platform-economics`, `#consumer-behavior`

---

<a id="item-3"></a>
## [Linux 7.3 Improves Performance When Running Out of VRAM](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 8.0/10

According to a report on pixelcluster.dev, Linux 7.3 introduces improvements that boost performance when VRAM is exhausted by better handling GPU memory overcommit. The change has generated significant community interest, with many users hoping it will eventually be upstreamed. This matters because GPU memory exhaustion currently causes severe performance drops or system freezes, especially on systems with limited VRAM. Better overcommit handling could improve gaming, AI inference, and desktop responsiveness, while also putting pressure on Nvidia to support paging in its proprietary driver. The kernel's overcommit handling is controlled by vm.overcommit_memory and related sysctls, with heuristic mode refusing obviously excessive allocations while still allowing overcommit. As community members note, virtual memory fragmentation remains a concern, and Nvidia's proprietary driver appears to support no GPU memory paging at all.

hackernews · flaburgan · Aug 18, 07:51 · [Discussion](https://news.ycombinator.com/item?id=49342719)

**Background**: Memory overcommit is a technique where the kernel allows processes to reserve more virtual memory than physically available, betting that most allocated memory will never be touched; Linux handles the shortfall with reclaim and the OOM killer. VRAM overcommit applies the same idea to graphics memory, but when GPU memory is exhausted the performance impact can be severe. The Linux kernel documentation describes several overcommit accounting modes, from heuristic handling to strict no-overcommit mode.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kernel.org/doc/Documentation/vm/overcommit-accounting">The Linux kernel supports the following overcommit handling modes</a></li>
<li><a href="https://www.baeldung.com/linux/memory-overcommitment-oom-killer">Linux Memory Overcommitment and the OOM Killer | Baeldung on Linux</a></li>
<li><a href="https://gitlab.com/MaxIV/kubernetes/mortalgpu/-/tree/main">Files · main · MaxIV / kubernetes / MortalGPU · GitLab</a></li>

</ul>
</details>

**Discussion**: Reactions are largely positive, with users praising the clear article and Linux's fast pace of kernel improvements compared to Windows updates. Nvidia users are frustrated that the proprietary driver supports no VRAM paging at all, and a debate has emerged over whether the kernel or the application should decide how sticky memory should be to VRAM. Commenters also wonder if the kernel should defragment virtual memory occasionally, and one notes how much low-level performance engineering owes to young trans people.

**Tags**: `#linux`, `#kernel`, `#vram`, `#memory-management`, `#performance`

---

<a id="item-4"></a>
## [Qwen 3.8 27B Scores 52 on Artificial Analysis, Matching GPT-5.6 Luna](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 8.0/10

Qwen 3.8 27B, a compact open-weight model, scored 52 on the Artificial Analysis Intelligence Index, matching GPT-5.6 Luna (max) and finishing just one point behind GLM-5.2 (753B) and DeepSeek V4 Pro 0813 (1.7T). Simon Willison highlighted the result on August 17, 2026. A 27B-parameter model matching much larger flagship models suggests parameter efficiency is advancing rapidly, potentially lowering cost and hardware requirements for high-performance AI deployment. It may also intensify competition by showing frontier-level ability can be packed into a much smaller package. The Artificial Analysis Intelligence Index v4.1.1 combines benchmarks such as GDPval-AA v2, Terminal-Bench v2.1, SciCode, GPQA Diamond, and Humanity's Last Exam. The comparison models are far larger: GLM-5.2 has 753B parameters and DeepSeek V4 Pro 0813 has 1.7T parameters, while Luna's size is undisclosed.

rss · Simon Willison · Aug 17, 23:58

**Background**: The Artificial Analysis Intelligence Index is an independent synthesized metric designed to measure LLM 'smartness,' expanding from Q&A datasets to agentic and long-context reasoning tasks. Qwen is Alibaba's open-weight LLM family, and Qwen 3.8 27B is one of its latest 27B-parameter releases, available via Hugging Face and Ollama.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://ollama.com/library/qwen3.8:27b">qwen 3 . 8 : 27 b</a></li>

</ul>
</details>

**Tags**: `#ai`, `#llms`, `#qwen`, `#benchmark`, `#efficiency`

---