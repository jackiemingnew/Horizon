---
layout: default
title: "Horizon Summary: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
---

> From 30 items, 13 important content pieces were selected

---

1. [Bun's Rust Rewrite Progress and Delay](#item-1) ⭐️ 9.0/10
2. [Moonshot AI Open-Sources Kimi K3: 2.8T Parameter Model](#item-2) ⭐️ 9.0/10
3. [Critical RCE Vulnerability Found in Fastjson2 Library](#item-3) ⭐️ 9.0/10
4. [vLLM v0.26.0 Released with Inkling Family and Performance Boosts](#item-4) ⭐️ 8.0/10
5. [Judge Rejects Google's DMCA Bid to Block Search Scraping](#item-5) ⭐️ 8.0/10
6. [Forum Project Switches from React to HTMX for Interactivity](#item-6) ⭐️ 8.0/10
7. [Paged Out #9: A Hacker-Curious Technical Zine](#item-7) ⭐️ 8.0/10
8. [Opinionated Guide Ranks AI Tools, Shifts to Agentic Systems](#item-8) ⭐️ 8.0/10
9. [Frontier LLMs Show Consistent Left-Leaning Bias in Sole Benchmark](#item-9) ⭐️ 8.0/10
10. [CXMT surges 471% on STAR Market debut, record IPO](#item-10) ⭐️ 8.0/10
11. [Google Teases Gemini 4: Most Ambitious Pre-training, Launch by Year End](#item-11) ⭐️ 8.0/10
12. [China Rebuts US Sanctions Threat Over AI Model Distillation](#item-12) ⭐️ 8.0/10
13. [China starts mass production of domestic DUV lithography machines](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bun's Rust Rewrite Progress and Delay](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 9.0/10

Bun's Rust rewrite has shipped in Claude Code over a month ago, but the public release of Bun v1.4 is delayed because the project lead Jarred Sumner promised a certain number of newly passing Node.js tests that have not been achieved yet. This rewrite from Zig to Rust is a major technical transition for a widely-used JavaScript runtime, impacting performance and safety. The delay highlights the challenges of meeting compatibility goals during a large-scale rewrite. The Rust rewrite was a mechanical port using LLMs, and the release is delayed until the promised Node.js test passing numbers are met, with PRs up but not yet merged. Jarred expects the release most likely next Tuesday.

hackernews · tomlockwood · Jul 27, 11:12 · [Discussion](https://news.ycombinator.com/item?id=49067854)

**Background**: Bun is a fast all-in-one JavaScript runtime designed as a drop-in replacement for Node.js, originally written in Zig. The rewrite to Rust aims to improve memory safety and leverage Rust's ecosystem. The transition involves using the same test suite to ensure compatibility.

<details><summary>References</summary>
<ul>
<li><a href="https://bun.com/blog/bun-in-rust">Rewriting Bun in Rust | Bun Blog</a></li>
<li><a href="https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/">Rewriting Bun in Rust</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/ bun : Incredibly fast JavaScript runtime , bundler...</a></li>

</ul>
</details>

**Discussion**: Jarred confirmed the rewrite is going well and has been used in Claude Code. Commenters discuss the trade-offs of using LLMs for the port and note that a separate project (Buz) claims to fix the original Zig codebase with faster builds.

**Tags**: `#bun`, `#rust`, `#javascript-runtime`, `#software-engineering`, `#rewrite`

---

<a id="item-2"></a>
## [Moonshot AI Open-Sources Kimi K3: 2.8T Parameter Model](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 9.0/10

Moonshot AI has open-sourced Kimi K3, a 2.8 trillion parameter Mixture-of-Experts model, on Hugging Face, making it the first open-source model at the 3-trillion scale. It introduces novel architectures including Kimi Delta Attention and Attention Residuals, supports a 1 million token context window, and achieves competitive performance with frontier models. Kimi K3's open release marks a significant milestone in AI transparency, proving that extremely large models (3T scale) can be made publicly accessible. This democratizes access to top-tier model capabilities, potentially accelerating research and application development in long-context reasoning, agentic tasks, and multimodal understanding. Kimi K3 uses a Stable LatentMoE framework with 896 experts, activating 16 per token, achieving approximately 2.5x training efficiency improvement over Kimi K2. It supports native text, image, and video understanding, and can be deployed with inference frameworks like Transformers, vLLM, and SGLang, with MXFP4 quantization available.

telegram · zaihuapd · Jul 27, 15:15

**Background**: Large language models (LLMs) are typically measured by parameter count; models with over 1 trillion parameters are rare due to immense computational costs. Mixture-of-Experts (MoE) architectures allow models to activate only a subset of parameters per token, making scaling more efficient. Moonshot AI previously released Kimi K2, and Kimi K3 builds upon it with novel attention mechanisms (Kimi Delta Attention and Attention Residuals) that improve memory management and contextual understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://jianyuh.github.io/attention/2025/12/13/KDA.html">Linear Attention : Kimi Delta Attention | Jianyu Huang’s Blog</a></li>
<li><a href="https://github.com/MoonshotAI/Attention-Residuals">GitHub - MoonshotAI/Attention-Residuals · GitHub</a></li>
<li><a href="https://www.emergentmind.com/topics/kimi-delta-attention">Kimi Delta Attention : Delta ‐Rule Linear Mechanism</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#large language model`, `#Moonshot AI`, `#Mixture of Experts`

---

<a id="item-3"></a>
## [Critical RCE Vulnerability Found in Fastjson2 Library](https://mp.weixin.qq.com/s/LJaul1jNjK9pXRAkoUiMEA) ⭐️ 9.0/10

A critical remote code execution (RCE) vulnerability has been disclosed in Fastjson2, affecting all versions up to 2.0.62, with no official patch yet available. This vulnerability allows attackers to bypass AutoType checks and execute arbitrary code via malicious JSON data, posing a severe security risk to applications using Fastjson2. The vulnerability was disclosed by Chaitin Technology on July 27, 2024, and the project maintainers have confirmed the issue. However, the pull request #7695 was closed without merging, and no official fix exists in any released version.

telegram · zaihuapd · Jul 27, 10:31

**Background**: Fastjson2 is a high-performance Java JSON library developed by Alibaba. AutoType is a feature that allows automatic type deserialization based on JSON content, which, if not properly restricted, can be exploited for Remote Code Execution attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://alibaba.github.io/fastjson2/autotype_cn.html">FASTJSON 2 Autotype机制介绍 | fastjson2</a></li>
<li><a href="https://github.com/alibaba/fastjson2">GitHub - alibaba/fastjson2: 🚄 FASTJSON2 is a Java JSON library with excellent performance.</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#RCE`, `#Fastjson2`, `#Java`

---

<a id="item-4"></a>
## [vLLM v0.26.0 Released with Inkling Family and Performance Boosts](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 was released with 411 commits from 212 contributors, introducing the full Inkling model family support, DeepSeek-V4 performance optimizations, and a new fp32 lm_head option for generation models. This release significantly enhances vLLM's capabilities for large-scale LLM inference, particularly with the new Inkling family and DeepSeek-V4 optimizations, which could improve throughput and accuracy for production deployments. The Inkling model family support includes piecewise CUDA graphs, Hopper FA4 relative attention, MTP=1 speculative decoding, LoRA, and NVFP4 quantization. DeepSeek-V4 improvements include a specialized routing kernel achieving 2.94% end-to-end TPOT gain and fused_topk_bias with 1.5-2x kernel speedup.

github · khluu · Jul 27, 01:06

**Background**: vLLM is an open-source high-throughput LLM inference engine. The Inkling model family is a new multimodal model released by Thinking Machines Lab. Piecewise CUDA graphs split the model computation into pieces to handle variable token lengths during prefill, improving efficiency over standard CUDA graphs.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/thinkingmachines/Inkling">thinkingmachines/ Inkling · Hugging Face</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#AI/ML`, `#release`, `#performance optimization`

---

<a id="item-5"></a>
## [Judge Rejects Google's DMCA Bid to Block Search Scraping](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

A U.S. judge ruled that Google Search Engine Results Pages (SERPs) are not copyrightable compilations, rejecting Google's attempt to use the Digital Millennium Copyright Act (DMCA) to block scraping by third parties like SerpAPI. This ruling sets a significant precedent for web scraping legality, potentially limiting large platforms' ability to use copyright law to shut down data extraction services, which are vital for market research, SEO, and fraud detection. The court found that Google's SERPs lack the minimal creativity required for copyright protection, as they are essentially automated compilations of facts. Notably, the ruling does not address other legal grounds Google might raise, such as contract terms or trespass.

hackernews · cdrnsf · Jul 27, 18:15 · [Discussion](https://news.ycombinator.com/item?id=49073513)

**Background**: The DMCA is a U.S. law that criminalizes circumvention of technological measures protecting copyrighted works. Web scraping involves automated extraction of data from websites, often used for price comparison, content monitoring, and research. Google had deprecated its own search API, leading to reliance on third-party scrapers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DMCA">DMCA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Web_scraping">Web scraping</a></li>

</ul>
</details>

**Discussion**: Comments largely support the ruling, with users noting Google's hypocrisy in scraping others while objecting to being scraped. Some lament the lack of a legitimate Google search API, while others highlight the importance of scraping for identifying scams like fake ESTA sites.

**Tags**: `#scraping`, `#DMCA`, `#copyright`, `#search engines`, `#legal`

---

<a id="item-6"></a>
## [Forum Project Switches from React to HTMX for Interactivity](https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/) ⭐️ 8.0/10

The Misago forum software project announced it is removing React.js from its codebase and adopting HTMX for UI interactivity, shifting from a client-side JavaScript framework to a server-driven hypermedia approach. This migration reflects a growing industry trend toward simpler, hypermedia-driven web architectures, especially for content-focused applications. It demonstrates that HTMX can reduce client-side complexity while maintaining dynamic interactions, potentially influencing other projects to reconsider heavy JavaScript frameworks. HTMX allows partial page updates by extending HTML with custom attributes for AJAX calls, eliminating the need for custom JavaScript. However, community members noted that sending large HTML fragments can become slow for highly interactive components like complex filter forms.

hackernews · Ralfp · Jul 27, 09:58 · [Discussion](https://news.ycombinator.com/item?id=49067301)

**Background**: HTMX is an open-source JavaScript library created by Carson Gross that enables dynamic web interactions using HTML attributes, following a hypermedia-driven approach. It contrasts with component-based frameworks like React that rely on a virtual DOM and client-side state management. The Misago project is a real-world case study of migrating from a heavy client-side framework to server-driven interactivity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">Htmx</a></li>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>

</ul>
</details>

**Discussion**: Community feedback was mixed: james2doyle reported performance issues with HTMX for complex filterable listings due to large HTML payloads, while snorremd and prologic praised its suitability for forums and general web apps, especially when combined with server-sent events and utility CSS frameworks like Tailwind.

**Tags**: `#HTMX`, `#React`, `#Web Development`, `#Server-Side Rendering`, `#JavaScript Frameworks`

---

<a id="item-7"></a>
## [Paged Out #9: A Hacker-Curious Technical Zine](https://pagedout.institute/download/PagedOut_009.pdf) ⭐️ 8.0/10

Paged Out #9 has been released as a free PDF, featuring deeply technical articles on topics like subpixel rendering and computable tilings. This zine continues the tradition of hacker zines like 2600 and Phrack, offering high-quality, deep technical content that fosters curiosity and community engagement among engineers and hackers. Notable articles include 'Baby Steps in C', 'The Subpixel Zoo' cited on page 30, and an uncredited rediscovery of Wang's work on computable tilings, which relates the halting problem to the domino problem.

hackernews · laurensr · Jul 27, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49070138)

**Background**: Subpixel rendering uses individual red, green, and blue subpixels to increase effective resolution, commonly used for text on LCD screens. Computable tilings, studied by Wang in the 1960s, show that the domino problem (whether a set of tiles can tile the plane) is equivalent to the halting problem, linking tiling patterns to computation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Subpixel_rendering">Subpixel rendering</a></li>
<li><a href="https://dl.ifip.org/db/conf/ifipTCS/ifipTCS2008/LafitteW08.pdf">Computability of Tilings .</a></li>

</ul>
</details>

**Discussion**: The community reacted very positively, praising the zine as 'modern 2600' and 'beautifully designed'. One user found 'Baby Steps in C' hilarious, while another noted that the computable tilings piece was an uncredited rediscovery of Wang's work, adding a critique about attribution.

**Tags**: `#technical zine`, `#hacker culture`, `#programming`, `#low-level computing`, `#magazine`

---

<a id="item-8"></a>
## [Opinionated Guide Ranks AI Tools, Shifts to Agentic Systems](https://simonwillison.net/2026/Jul/27/an-opinionated-guide-to-which-ai-to-use-to-do-stuff/#atom-everything) ⭐️ 8.0/10

Ethan Mollick's updated guide on AI tool selection now emphasizes agentic systems over chat, and removes Gemini due to its lack of a direct competitor in the Codex/ChatGPT Work/Cowork category. This guide provides practical, up-to-date advice for professionals choosing AI tools, reflecting the industry's rapid shift toward autonomous, multi-step agentic systems that can perform hours of human work in one go. Key modes include ChatGPT Work and Codex for OpenAI, and Claude Cowork and Code for Anthropic; naming is confusing and capabilities differ between mobile and desktop apps.

rss · Simon Willison · Jul 27, 21:55

**Background**: Agentic AI systems pursue goals autonomously over multiple steps without per-step human approval, contrasting with single-turn chat models. This guide reflects a growing trend where AI can access computers and execute complex workflows, moving beyond simple Q&A.

<details><summary>References</summary>
<ul>
<li><a href="https://remolda.com/en/glossary/agentic-ai">Agentic AI — definition | Remolda</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://support.google.com/gemini/answer/17094507?hl=en-CA&co=GENIE.Platform=Android">Use Gemini Spark to manage your tasks & workflows in Gemini Apps...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLMs`, `#agentic systems`, `#model comparison`, `#opinionated guide`

---

<a id="item-9"></a>
## [Frontier LLMs Show Consistent Left-Leaning Bias in Sole Benchmark](https://www.reddit.com/r/MachineLearning/comments/1v8fnzw/evaluated_6_frontier_llms_gpt54_claude_sonnet_46/) ⭐️ 8.0/10

In a solo evaluation project, six frontier large language models—GPT-5.4, Claude Sonnet 4.6, Claude Opus 4.7, Gemini Pro, Gemini Flash, and Grok 4.3—were tested across eight bias and fairness benchmarks comprising approximately 20,600 examples, revealing that all models exhibit left-leaning political bias, with Grok's behavior contradicting its right-leaning self-report. This benchmark provides independent, empirical evidence of systematic political bias in frontier LLMs, which is crucial for AI fairness research and model deployment decisions, especially as these models are increasingly used in content moderation and policy applications. Notably, on the Political Compass benchmark, Grok self-reported as right-leaning but behaved left-leaning in actual content classification and policy question answering; refusal rates on BBQ race-related questions ranged from 20.3% for GPT-5.4 to about 5% for Claude Sonnet 4.6 and Gemini Pro.

reddit · r/MachineLearning · /u/marggggggggg · Jul 27, 22:37

**Background**: Bias benchmarks like WinoBias (gender bias in coreference resolution), BBQ (Bias Benchmark for QA), and SeeGULL (stereotype dataset with geo-cultural coverage) are designed to detect harmful biases in language models. The Political Compass is a two-axis political ideology test measuring economic left-right and social authoritarian-libertarian dimensions. Understanding model biases is essential for responsible AI deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/winobias">WinoBias : Gender Bias in Coreference Benchmark</a></li>
<li><a href="https://github.com/google-research-datasets/seegull">GitHub - google-research- datasets / seegull : SeeGULL is...</a></li>
<li><a href="https://en.wikipedia.org/wiki/The_Political_Compass">The Political Compass - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#bias`, `#fairness`, `#benchmarking`, `#AI ethics`

---

<a id="item-10"></a>
## [CXMT surges 471% on STAR Market debut, record IPO](https://www.stcn.com/article/detail/4042119.html) ⭐️ 8.0/10

Changxin Memory Technologies (CXMT), a leading Chinese memory chip maker, surged 471.59% on its first trading day on the STAR Market, opening at 49.5 yuan per share, far above its IPO price of 8.66 yuan. This record-breaking IPO highlights China's push for semiconductor self-sufficiency, especially in memory chips, and could boost investor confidence in domestic chipmakers. It also provides significant capital for CXMT to expand production and compete with global giants like Samsung and SK Hynix. CXMT raised about 57.9 billion yuan initially, potentially up to 66.6 billion yuan if the overallotment option (greenshoe) is fully exercised, surpassing SMIC's 53.2 billion yuan record from 2020. The company forecasts net profit attributable to parent of 50-57 billion yuan for the first half of 2026, turning from losses.

telegram · zaihuapd · Jul 27, 01:29

**Background**: The Science and Technology Innovation Board (STAR Market) is a NASDAQ-style board on the Shanghai Stock Exchange, designed to support high-tech and innovative companies with less stringent listing requirements. An overallotment option (greenshoe) allows underwriters to sell additional shares if demand is strong, stabilizing the stock price after listing. CXMT is China's leading DRAM manufacturer, critical for reducing reliance on foreign memory chips.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hstong.com/sns/status/long/16263179804177497">捷利交易宝 | 【港股打新学堂】第10期： 超 额 配 售 选 择 权 与发 售 量调整 权</a></li>
<li><a href="https://cj.sina.com.cn/articles/view/7879922977/1d5ae152101901akqi?froms=ggmp&vt=4">cj.sina.com.cn/articles/view/7879922977/1d5ae152101901akqi?froms...</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#IPO`, `#存储芯片`, `#科创板`, `#国产替代`

---

<a id="item-11"></a>
## [Google Teases Gemini 4: Most Ambitious Pre-training, Launch by Year End](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 8.0/10

Google CEO Sundar Pichai announced during the Q2 2026 earnings call that the next-generation large model, Gemini 4, is already in training, calling it their most ambitious pre-training project to date, with an expected release by November or December 2026. Gemini 4 represents Google's continued push to lead in the AI frontier, and its release could set new benchmarks for large language models, impacting the broader AI ecosystem and competitive dynamics with rivals like OpenAI. The model is still in pre-training, with Pichai stating that Google will prioritize computing resources for cutting-edge AGI research. Additionally, the Gemini 3.x Flash series will maintain almost monthly iteration cycles focusing on capabilities like intelligent coding.

telegram · zaihuapd · Jul 27, 04:06

**Background**: Gemini is Google's family of large language models, competing with models like GPT-4 from OpenAI. Pre-training involves training a model on vast amounts of data to learn language patterns, followed by fine-tuning for specific tasks. Google has been iterating on Gemini, with previous versions like Gemini 1.5 and 2.0, and now Gemini 4 is touted as the most ambitious yet.

**Tags**: `#Google`, `#Gemini`, `#AI`, `#LLM`, `#pre-training`

---

<a id="item-12"></a>
## [China Rebuts US Sanctions Threat Over AI Model Distillation](https://www.mofcom.gov.cn/syxwfb/art/2026/art_7f1622463a7c48ef9fad600ce0ef702f.html) ⭐️ 8.0/10

On July 27, the Chinese Ministry of Commerce rebutted US plans to investigate and sanction Chinese AI firms for model distillation and intellectual property theft, stating that distillation is a widely used industry technique and that US firms also distill Chinese models. This response highlights the growing geopolitical tension over AI technology and could escalate trade conflicts, potentially disrupting global AI collaboration and open-source model sharing. The Ministry noted that nearly 200 US startups have urged their government not to restrict access to Chinese open-source models, and China warned it will take necessary measures to protect its firms' legitimate rights if its interests are substantively damaged.

telegram · zaihuapd · Jul 27, 11:01

**Background**: Model distillation is a technique where a smaller model is trained to mimic a larger, more powerful model, often used to reduce computational costs. It is a common practice in AI development, with many companies and researchers using open-source models for distillation. The US has raised concerns that Chinese firms are using distillation to steal intellectual property from US AI models, while China argues the practice is standard and reciprocal.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.volcengine.com/articles/7478160196578377737">大模型" 蒸 馏 "是什么？ - 文章 - 开发者社区 - 火山引擎</a></li>

</ul>
</details>

**Tags**: `#AI`, `#geopolitics`, `#model distillation`, `#trade war`

---

<a id="item-13"></a>
## [China starts mass production of domestic DUV lithography machines](https://www.theinformation.com/articles/china-starts-mass-producing-homegrown-duv-chipmaking-tools-advance-local-chip-industry) ⭐️ 8.0/10

China has begun mass-producing its own immersion deep ultraviolet (DUV) lithography machines, aiming to produce about 5 units this year and 20 units by 2027, for domestic chipmakers like SMIC and Hua Hong. This marks a significant step in China's efforts to reduce reliance on foreign chipmaking equipment, challenging ASML's dominance, especially if export restrictions tighten. The domestic DUV machines still lag behind ASML in performance and reliability; chipmakers will need months of testing. Key components from Japan faced supply delays this year.

telegram · zaihuapd · Jul 27, 14:10

**Background**: DUV lithography machines are essential for patterning circuits on silicon wafers in semiconductor manufacturing. Immersion lithography uses a liquid layer (typically water) between the lens and wafer to enhance resolution, enabling smaller features below 45nm. ASML currently dominates the advanced lithography market with both DUV and EUV machines.

<details><summary>References</summary>
<ul>
<li><a href="https://min.news/en/digital/0f6b59b4f9f4346928c71bc30fa0125e.html">DUV lithography machine has changed! What are the roads for China...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Immersion_lithography">Immersion lithography</a></li>
<li><a href="https://lifeboat.com/blog/2025/10/netherlands-tightens-export-restrictions-on-microchip-machines-mainly-targeting-asml">Netherlands tightens export restrictions on microchip machines , mainly...</a></li>

</ul>
</details>

**Tags**: `#chip manufacturing`, `#DUV lithography`, `#China semiconductor`, `#ASML`, `#geopolitics`

---