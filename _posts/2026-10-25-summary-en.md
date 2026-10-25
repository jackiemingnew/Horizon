---
layout: default
title: "Horizon Summary: 2026-10-25 (EN)"
date: 2026-10-25
lang: en
---

> From 29 items, 3 important content pieces were selected

---

1. [Oregon Police Quote $2.5M, 21 Years of Work, for One Officer's Records](#item-1) ⭐️ 8.0/10
2. [Cerebras Details How It Serves Trillion-Parameter Models](#item-2) ⭐️ 8.0/10
3. [Brotli CVE-2026-111497 (CVSS 9.2) Spreads to Python HTTP Stacks](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Oregon Police Quote $2.5M, 21 Years of Work, for One Officer's Records](https://theintercept.com/2026/10/01/oregon-police-misconduct-public-records-cost-fee/) ⭐️ 8.0/10

The Eugene Police Department in Oregon told a local news outlet that fulfilling its public records request about a single police officer would require at least 44,816 hours of staff time and cost approximately $2,484,599.04, according to a report by The Intercept. That is roughly 21 years of full-time work for one employee, quoted in response to a request concerning just one officer. Quoting a prohibitive price is a way for agencies to refuse records without ever formally denying the request, effectively pricing journalists and ordinary citizens out of public oversight. If such fees become routine, the practical right to inspect government records — a cornerstone of press freedom and police accountability — erodes even where the law on paper guarantees access. The quoted figure of 44,816 staff hours works out to about 21 years of continuous full-time labor, and the dollar estimate was itemized to the cent at $2,484,599.04 — a level of precision that makes the quote look calculated rather than a rough estimate. The request concerned records about one officer, making the scale of the estimate especially striking compared with the narrow scope of what was sought.

hackernews · tdeck · Oct 25, 18:04 · [Discussion](https://news.ycombinator.com/item?id=50234232)

**Background**: Public records laws — the federal Freedom of Information Act (FOIA) and its state-level equivalents, such as Oregon's public records law — give the public and press a right to request government documents. These laws typically allow agencies to charge for the staff time and copying costs needed to search for and redact records, which creates a loophole: an agency can comply on paper while setting a price no requester can pay. Journalists often request fee waivers on public-interest grounds, and some jurisdictions cap fees or impose statutory response deadlines, but enforcement varies widely.

**Discussion**: Commenters saw the case as part of a broader pattern: one described a school district that has spent months dribbling out records in monthly installments with no end in sight, while others contrasted the US system with the UK's 30-day statutory response window and warned that German officials, notably Jens Spahn, are pushing reforms that would legalize exactly this kind of prohibitive fee. Several also noted precedent for absurd quotes, citing a 2015 Department of Defense estimate of 15 million hours and $660 million — over 1,700 years of work — for a single FOIA request.

**Tags**: `#public-records`, `#FOIA`, `#government-transparency`, `#press-freedom`, `#policy`

---

<a id="item-2"></a>
## [Cerebras Details How It Serves Trillion-Parameter Models](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras) ⭐️ 8.0/10

Cerebras published a technical blog post explaining how it deploys trillion-parameter frontier AI models on its wafer-scale hardware, describing how model layers are streamed across the chip's processing cores. The post drew heavy discussion on Hacker News (348 upvotes, 127 comments) about whether the approach is practically accessible. Serving trillion-parameter models at very high token throughput is one of the hardest problems in AI infrastructure, and Cerebras' wafer-scale approach is a genuine alternative to multi-GPU clusters. If it works at scale, it could reshape the economics of inference and give enterprises a faster option than GPU-based clouds. Cerebras' CS-3 system is built on the Wafer Scale Engine 3, a 5nm chip with 4 trillion transistors and 900,000 AI-optimized cores, and the newer CS-4 combines three WSE-3 Turbo processors. A key caveat raised by commenters is that achieving these speeds requires enormous hardware, so availability is limited and the served models often lag the frontier by months.

hackernews · gmays · Oct 25, 01:33 · [Discussion](https://news.ycombinator.com/item?id=50227356)

**Background**: Cerebras builds AI chips that are radically different from Nvidia GPUs: instead of slicing a silicon wafer into many separate chips, it keeps the whole wafer intact as one giant processor, which gives massive on-chip memory bandwidth and avoids the networking bottlenecks of multi-GPU clusters. Trillion-parameter models are so large they normally must be split across many GPUs, making inference slow and expensive. The Wafer Scale Engine 3 is the third generation of this design and powers Cerebras' inference cloud service.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/chip">Cerebras WSE-3 Turbo | Wafer-Scale AI Chip</a></li>
<li><a href="https://developer.nvidia.com/blog/demystifying-ai-inference-deployments-for-trillion-parameter-large-language-models/">Demystifying AI Inference Deployments for Trillion Parameter ...</a></li>

</ul>
</details>

**Discussion**: Commenters were split: some praised the technology but argued Cerebras lacks the capital and manufacturing capacity to meet demand, so it relies on cheap plans to give users a taste while serving older models. Others defended the strategy, expecting near-frontier models at a fraction of the cost and several times the speed within months, while some noted that the accessible models (such as GPT-OSS 120B) are fast but not accurate enough for their needs, and one professional described the company as having remarkable technology but an inadequate team.

**Tags**: `#AI`, `#hardware`, `#inference`, `#Cerebras`, `#large language models`

---

<a id="item-3"></a>
## [Brotli CVE-2026-111497 (CVSS 9.2) Spreads to Python HTTP Stacks](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 8.0/10

The Brotli decoder vulnerability CVE-2026-111497, initially disclosed under the name Node2Shell and later called HTTP2Shell, affects Brotli versions 1.0.3 through 1.2.0 and carries a CVSS 4.0 score of 9.2. Patched releases are Brotli 1.2.1 and brotlicffi 1.2.1.0 for Python, plus Node.js 22.23.4, 24.22.1 and 26.12.1. Brotli is a core HTTP compression format negotiated by browsers and servers, so the vulnerable decoder sits in the request path of widely deployed Node.js and Python web stacks. An unauthenticated attacker who can send a crafted compressed stream can trigger memory corruption, making this an urgent patch for anyone running these runtimes or the libraries that embed them. Exploitation can cause memory corruption, leakage of sensitive data, process crashes, or potentially arbitrary code execution, and the flaw was reportedly discovered in February of this year. The vulnerability lives in the decoder rather than the encoder, meaning servers and clients that merely decompress attacker-supplied Brotli content are exposed even if they never compress anything themselves.

telegram · zaihuapd · Oct 25, 02:42

**Background**: Brotli is an open-source lossless compression algorithm Google released in 2015 with a focus on HTTP compression, offering better ratios than gzip by combining LZ77-style back-references, Huffman coding and a built-in static dictionary. Because it is a standard content-encoding in HTTP, browsers and servers transparently decode Brotli streams, and libraries such as brotlicffi provide CFFI bindings so Python programs can call the reference C implementation directly. CVSS is the industry-standard framework maintained by FIRST that scores vulnerability severity from 0 to 10, with version 4.0 refining how attack complexity and exploitable conditions are described.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/Brotli">Brotli - 维基百科，自由的百科全书</a></li>
<li><a href="https://pypi.org/project/brotlicffi/">Python CFFI bindings to the Brotli library</a></li>
<li><a href="https://www.first.org/cvss/v4-0/cvss-v40-specification.pdf">CVSS v4.0 Specification - 2024-06-18 - FIRST</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#brotli`, `#nodejs`, `#python`

---