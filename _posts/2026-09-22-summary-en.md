---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22
lang: en
---

> From 39 items, 9 important content pieces were selected

---

1. [OpenAI launches GPT-6 Sol and Luna with lower pricing](#item-1) ⭐️ 10.0/10
2. [Anthropic Releases Claude Opus 5.5 With Cheaper Pricing](#item-2) ⭐️ 9.0/10
3. [Pentagon: AI Overreliance Contributed to Deadly Strike on Iran School](#item-3) ⭐️ 9.0/10
4. [Claude Opus 5.5, GPT-6 Sol and Luna Launch a New Price War](#item-4) ⭐️ 9.0/10
5. [vLLM v0.30.0 ships Fast Start weight cache and DeepSeek-V4 support](#item-5) ⭐️ 8.0/10
6. [Artificial Analysis benchmarks Claude Opus 5.5 at max reasoning effort](#item-6) ⭐️ 8.0/10
7. [Alibaba Unveils Zhenwu V900 AI Chip, Claiming 3x Compute of M890](#item-7) ⭐️ 8.0/10
8. [Cloudflare's Python Workers Reach General Availability](#item-8) ⭐️ 8.0/10
9. [DeepSeek and Tsinghua Release DSec Sandbox Platform Technical Report](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI launches GPT-6 Sol and Luna with lower pricing](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 10.0/10

OpenAI announced GPT-6 Sol and Luna, two new models in the GPT-6 family that are available in the API as gpt-6-sol and gpt-6-luna. Sol is positioned as the cost-efficient high-end tier below the flagship GPT-6 Astra, while Luna is the fast, low-cost tier — and early commenters note that Luna costs roughly half as much as GPT-5.6 Luna. Pricing and usage limits are now the deciding factors for many developers choosing between OpenAI and Anthropic, so a cheaper mid-tier model directly affects tooling costs and how far subscription plans stretch. The release also shows OpenAI filling out a three-tier GPT-6 lineup (Astra, Sol, Luna) rather than shipping a single flagship, which reshapes how teams route everyday work versus hard tasks. Sol is described as sitting above the fast Luna tier and below the flagship GPT-6 Astra, offering more intelligence and better results than similarly priced competitor models, with higher usage limits and lower cost for difficult work tasks. Because the models use OpenAI-compatible chat completions endpoints, developers can build against GPT-6 Astra and switch by changing the model ID, though API rate limits still cap requests and tokens over a given time window.

hackernews · OfficialTurkey · Sep 22, 18:00 · [Discussion](https://news.ycombinator.com/item?id=49805509)

**Background**: OpenAI has been shipping the GPT-6 generation in tiers: GPT-6 Astra launched earlier in September 2026 and was billed as the company's most powerful model yet, with Sol and Luna now covering the mid-range and fast/cheap ends of the lineup. In practice, a "tier" means the same API shape and endpoint but different trade-offs in intelligence, latency and price per token, so developers can route simple requests to a cheap model and reserve the expensive one for hard problems. Usage limits in subscription plans (such as ChatGPT Plus or the 20x coding plans) are downstream of these per-token costs, which is why price cuts generate so much discussion.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT‑6 Sol and Luna - OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-sol">GPT - 6 Sol - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/">OpenAI launches GPT-6 Sol and Luna, boasting lower cost and ...</a></li>

</ul>
</details>

**Discussion**: Commenters focused heavily on price and usage limits: simonw called Luna being half the price of GPT-5.6 Luna "a really big deal" and posted side-by-side SVG "pelican" renderings for Sol, Luna and Astra, while jeffnash argued Codex beats Claude Code largely because of opaque reset windows and the odd 20x/5x plan math, plus effectively unmetered ChatGPT usage on the 20x plan. Others were more sentimental — m_fayer said GPT-5.6 Sol was a rare model they "clicked" with and worries a technically better successor won't feel as natural — while leokennis noted that for an average person ChatGPT Plus already feels near-limitless and "just works".

**Tags**: `#OpenAI`, `#GPT-6`, `#LLM`, `#AI models`, `#pricing`

---

<a id="item-2"></a>
## [Anthropic Releases Claude Opus 5.5 With Cheaper Pricing](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic announced Claude Opus 5.5, a new frontier model that ships with across-the-board price cuts compared with Claude Opus 5 — cache reads drop from $0.50 to $0.20, input tokens from $5 to $4, output tokens from $25 to $20, and cache writes from $6.25 to $5 per million tokens. The release also emphasizes a more natural communication style, which Anthropic says early testers found clearer and easier to follow over long sessions. Opus 5 was reportedly the highest-spend model on OpenRouter, so cutting prices on the flagship tier directly lowers costs for heavy API users and increases competitive pressure on other frontier labs. The release also signals that Anthropic is pushing capability and adoption at the same time, even as it publicly calls for pacing frontier development. The pricing table is the most concrete part of the announcement: cache reads fall to $0.20 and output to $20 per million tokens, which matters most for agentic or long-context workloads where cached input dominates cost. Anthropic's messaging also stresses readability and putting important information up front, framing clearer communication as both a usability and a safety benefit.

hackernews · km144 · Sep 22, 16:29 · [Discussion](https://news.ycombinator.com/item?id=49803892)

**Background**: A frontier model is a large-scale machine learning model that is currently among the most capable in existence, typically showing strong multi-step reasoning, coding, and tool-use abilities. LLM API pricing is quoted in US dollars per million tokens, split into input (prompt) and output (completion) tokens, and prompt caching lets repeated context be stored and re-read at a much lower price than fresh input. Anthropic's Claude Opus line is its top-tier, most expensive model family, so pricing changes there are closely watched by developers building on the API.

<details><summary>References</summary>
<ul>
<li><a href="https://distillation.technology/learn/what-is-a-frontier-model">What Is a Frontier Model ? | Distillation Technologies</a></li>
<li><a href="https://onpremisia.com/llm-api-pricing">LLM API Pricing by Provider (2026) — Compare per - token costs</a></li>
<li><a href="https://siliconanalysts.com/data/llm-pricing">LLM API Pricing — $/ Million Tokens by Model (2026)</a></li>

</ul>
</details>

**Discussion**: Hacker News reaction was sharply divided: one top comment mocked the release for opening with a reminder of Anthropic's recent call to "pace the frontier" while the rest of the post uses specific numbers to show it is doing the opposite, and others welcomed the long-awaited price drop by comparing token costs line by line. Several users said they would rather stay on cheaper alternatives such as DeepSeek v4.1 for heavy agentic work, while others shared practical tests of the new model's behavior.

**Tags**: `#AI/ML`, `#LLM`, `#Anthropic`, `#model release`, `#pricing`

---

<a id="item-3"></a>
## [Pentagon: AI Overreliance Contributed to Deadly Strike on Iran School](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 9.0/10

A Pentagon report concluded that overreliance on AI-assisted targeting contributed to a U.S. missile strike on a school in Minab, Iran, finding that the United States "failed in its obligation to do everything feasible to verify" that the school was a military objective and that the failure "went beyond mere negligence." The report states the U.S. "directed the strikes at the building of the school while being aware of a substantial risk of striking a civilian object and acting recklessly as regards the possibility that this would happen." This is one of the first documented cases in which military AI tooling has been officially linked to mass civilian casualties, turning abstract debates about lethal autonomous weapons and AI ethics into a concrete accountability crisis. It is likely to intensify scrutiny of the Pentagon's AI procurement pipeline, its contractors such as Palantir, and the legal question of who — if anyone — can be held responsible when an algorithm shapes a lethal decision. According to officials cited in the reporting, the Minab site was cataloged as an Islamic Revolutionary Guard Corps facility because of outdated data, then fed into Maven alongside other candidates and returned as a recommendation; some users reportedly expected Maven to flag stale records or contradictions in the assembled intelligence, even though the system was not designed to do that. Project Maven is officially framed as human-in-the-loop decision support rather than an autonomous weapons system, which leaves open exactly where machine output ended and human judgment should have begun.

hackernews · devonnull · Sep 22, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49806430)

**Background**: Project Maven, officially the Algorithmic Warfare Cross Functional Team, is a U.S. Department of Defense initiative launched in 2017 to accelerate machine learning and data integration in intelligence, surveillance, target acquisition, and reconnaissance workflows; it now operates under the National Geospatial-Intelligence Agency and integrates drone, satellite, and other sensor data to flag potential targets for human analysts. Google withdrew from the program in 2018 after internal protests, and follow-on integrators have included Palantir, Anduril, Amazon Web Services, and Anthropic, which withdrew in 2026. The Pentagon has credited Maven with supporting 2024 targeting for airstrikes in Iraq, Syria, and Yemen. The incident also feeds into the long-running international debate over lethal autonomous weapons systems, which are designed to search for and engage targets based on programmed constraints with little or no human intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Maven">Project Maven</a></li>
<li><a href="https://www.cnas.org/events/project-maven">Project Maven: Artificial Intelligence in Warfare | CNAS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapon">Lethal autonomous weapon</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters largely pushed back on framing "AI" as the root cause, with one reading of the report's details arguing that AI "doesn't really seem like the culprit," and another blaming officials who embrace AI without understanding its blind spots. Several stressed that accountability must stay with humans: as one put it, "An AI can't be tried in a court," so a responsible person is needed for every lethal action. Others criticized the blame-shifting between the Pentagon and Palantir, asking how decisions leading to innocent deaths came to be treated like a botched B2B SaaS rollout.

**Tags**: `#AI ethics`, `#military AI`, `#accountability`, `#Project Maven`, `#lethal autonomous weapons`

---

<a id="item-4"></a>
## [Claude Opus 5.5, GPT-6 Sol and Luna Launch a New Price War](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

Anthropic released Claude Opus 5.5 and, roughly an hour later, OpenAI released GPT-6 Sol and GPT-6 Luna, both of which Simon Willison reviewed in a first-impressions post. GPT-6 Luna is priced at $0.10 per million input tokens and $0.50 per million output tokens — half the price of GPT-5.6 Luna — while GPT-6 Sol saw a similar reduction versus GPT-5.6 Sol, and Claude Opus 5.5 also received a price cut to $4/$20 per million tokens. This simultaneous frontier release and steep price cut signals a broad escalation of the price war in the LLM market, meaning developers can now build applications on top-tier models at a fraction of last year's cost. It also puts direct pressure on competing labs, since Grok 4.7 had positioned itself as the cheap option at $2/$6 but is now matched on input price by GPT-6 Sol. A key caveat is that GPT-5.6 models have a scheduled 25% price increase coming in November, so GPT-6 is half the price of the promotional GPT-5.6 rates rather than the eventual ones. At $0.10/$0.50, GPT-6 Luna is among the cheapest models OpenAI has ever released, beaten only by the far weaker GPT-4.1 Nano ($0.10/$0.40) and GPT-5 Nano ($0.05/$0.40), and since GPT-5.6 Terra costs the same as GPT-6 Sol, Willison argues any remaining reason to use Terra has evaporated.

rss · Simon Willison · Sep 22, 23:46

**Background**: Simon Willison is a widely followed developer and writer whose blog posts are a common reference point for evaluating new LLM releases, and he is known for using a quirky qualitative test — generating an SVG of a pelican riding a bicycle — to compare models side by side. Token pricing quoted here is per million tokens, split into input, cached input and output rates, which is the standard way API costs are compared across providers. The two launches landed in an unusually dense week of model releases that also included xAI's Grok 4.7 and Xiaomi's MiMo v2.6 Flash/Pro, an omnimodal series the company open-sourced as part of its reinforcement-learning research.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Jun/6/six-months-in-llms/">The last six months in LLMs, illustrated by pelicans on bicycles - Simon Willison's Weblog</a></li>
<li><a href="https://github.com/simonw/pelican-bicycle">LLM benchmark: Generate an SVG of a pelican riding a bicycle - GitHub</a></li>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo-V2.6 | Xiaomi</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Anthropic`, `#OpenAI`, `#AI pricing`, `#model releases`

---

<a id="item-5"></a>
## [vLLM v0.30.0 ships Fast Start weight cache and DeepSeek-V4 support](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM released v0.30.0, a large update containing 762 commits from 315 contributors (104 of them new). The release introduces a "Fast Start" persistent per-GPU weight-cache daemon, support for many new models such as DeepSeek-V4.1-Flash, DeepSeek-V4-Flash-Vision-Exp, GLM-5.3-Flash, K2-Horizon and Cohere Compass, plus a DeepSeek-V4 CPU backend, Gumbel-max watermarking, the HiSparse host-tier KV cache and a broad set of Model Runner V2 performance improvements. vLLM is one of the most widely used open-source LLM inference and serving frameworks, so these changes propagate quickly into production stacks, RL training loops and self-hosted deployments. In particular, Fast Start directly attacks engine cold-start latency and the new CPU backend plus expanded model coverage widen the range of hardware and model architectures teams can serve. Fast Start keeps post-quantized, tensor-parallel-sharded weights resident in GPU memory so that a restarting engine can map them over CUDA IPC via `--load-format ipc_cache` instead of re-reading them from disk, and it now also covers FP4 checkpoints and multi-node TP. On the performance side, freezing garbage collection during CUDA graph capture reduced capture time from 12s to 2s and engine initialization from 28.9s to 8.2s on H200, while the DeepSeek-V4 CPU backend relies on AVX512/AMX kernels for sparse MLA, indexer, mHC and compressor operations.

github · khluu · Sep 22, 05:20

**Background**: vLLM is an open-source engine for serving large language models that popularized PagedAttention-style KV cache management, and it is commonly used with quantization formats such as FP8, MXFP8 and NVFP4 to shrink memory use — MXFP8, for example, applies a shared power-of-two scale per block of 32 elements. Modern serving also leans on multiply-accumulate optimized attention kernels like FlashMLA for DeepSeek-style architectures, tensor parallelism (TP) to split a model across GPUs, and CUDA graphs to eliminate per-step launch overhead. The release also references DeepSeek's Engram conditional-memory lookups, which can be prefetched from host DRAM while other layers compute, and features such as HiSparse that spill KV cache pages to pinned host memory when GPU memory is under pressure.

<details><summary>References</summary>
<ul>
<li><a href="https://nvidia.github.io/cudnn-frontend/mxfp8-attention-scaling/">How Scales Are Applied in MXFP8 Attention - nvidia.github.io</a></li>
<li><a href="https://www.deepep.org/en/flashmla">FlashMLA</a></li>
<li><a href="https://generativeai.pub/deepseeks-engram-the-lookup-table-that-eats-transformer-layers-90b5f6a99a90">DeepSeek’s Engram : The Lookup Table That Eats... | Generative AI</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#llm-inference`, `#model-serving`, `#release`, `#ai-infrastructure`

---

<a id="item-6"></a>
## [Artificial Analysis benchmarks Claude Opus 5.5 at max reasoning effort](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 8.0/10

Artificial Analysis published an evaluation page for Claude Opus 5.5 at its "max" reasoning setting, with separate pages also available for the "xhigh" and default "medium" settings. The coverage quickly drew Hacker News discussion (roughly 216 points and 62 comments) focused on its intelligence, cost and benchmark reliability compared with open-weight models. The evaluation feeds an ongoing debate about whether closed frontier models still justify their price premium when open-weight alternatives land close on many benchmarks at a fraction of the cost. It also highlights how reasoning-effort settings, not just the model itself, now determine real-world quality and per-task spending. Commenter simonw noted that at the max setting the model twice exhausted its 128,000-token budget while still reasoning on a simple "SVG of a pelican riding a bicycle" prompt, while hglaser cited roughly half the cost per task versus Opus 5 when comparing matched high-effort runs. The reliance on a single independent third-party evaluation page, rather than an official release announcement, means the numbers should be read as one lab's snapshot.

hackernews · theanonymousone · Sep 22, 16:51 · [Discussion](https://news.ycombinator.com/item?id=49804316)

**Background**: Artificial Analysis is an independent benchmarking firm that publishes continuously updated evaluations of language, image, video and speech models and ranks them on an aggregate Intelligence Index. The "max" reasoning setting refers to a control that lets a model spend a much larger budget of internal reasoning tokens before answering, which typically raises quality on hard tasks but also raises latency and cost. Open-weight models are systems whose trained parameters are publicly downloadable, so anyone can self-host and fine-tune them, in contrast to closed API-only models.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://www.everydev.ai/tools/artificial-analysis">Artificial Analysis - AI Model Benchmarking Platform | EveryDev.ai</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open - Weights Model ? | AI21</a></li>

</ul>
</details>

**Discussion**: Sentiment was mixed to skeptical: cmiles8 argued frontier models are only slightly better than open-weight alternatives while costing around 100x more, and breckenedge worried that providers' benchmark scores regress weeks after launch once users have switched. Others were more positive, with hglaser praising the roughly halved cost per task versus Opus 5, while linuxrebe1 said he had reverted to Opus 4.8 because Opus 5 lost track of tasks and went off on tangents.

**Tags**: `#AI`, `#LLM`, `#Claude`, `#benchmarks`, `#pricing`

---

<a id="item-7"></a>
## [Alibaba Unveils Zhenwu V900 AI Chip, Claiming 3x Compute of M890](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 8.0/10

At the 2026 Yunqi Conference, Alibaba's chip unit T-Head unveiled the Zhenwu V900, which it calls China's most powerful domestic AI chip, claiming three times the compute of the previous-generation Zhenwu M890 and the ability to scale a single cluster to 500,000 cards. Alibaba CEO Eddie Wu also said the self-developed M890 supernode already supports inference for 2-trillion-parameter models and will be deployed at scale on Alibaba Cloud this quarter, while Qwen plans to train new 5T–10T-parameter models and Alibaba Cloud targets over 20GW of global datacenter capacity by 2032. The announcement positions Alibaba as a full-stack AI player spanning chips, cloud and models, directly challenging Nvidia's dominance and Huawei's Ascend roadmap in the race for large-scale domestic AI compute. If the 500,000-card cluster and trillion-parameter roadmap materialize, it would reshape how Chinese AI labs train and serve frontier models despite export restrictions on advanced GPUs. The new chip is the foundation for a planned 500,000-card wide-area supernode cluster rated at 1GW of compute with a 6-microsecond communication latency target, built on NPO optical modules, HPN 8.0 networking and the CPFS storage system, aimed at training ten-trillion-parameter MoE models. The predecessor M890 is a training-and-inference unified chip used in the Panjiu AL128 node server, whose 128-card supernode claims hundred-nanosecond-level communication latency and was already adapted to run Qwen3.8, a 2.4-trillion-parameter flagship model.

telegram · zaihuapd · Sep 22, 03:30

**Background**: Supernode (SuperPod) is a cluster architecture, first popularized by Nvidia, that tightly couples many compute nodes via high-speed interconnect so they behave as one logical system with large bandwidth, low latency and unified memory addressing; running trillion-parameter models requires spreading weights across dozens or hundreds of such high-speed cards. Alibaba's T-Head (PingTouGe) is the company's in-house semiconductor arm, and the Yunqi Conference is Alibaba Cloud's annual flagship event where it typically announces chip, cloud and model roadmaps. The 2026 event comes amid intensifying competition with Huawei, which has also announced Ascend supernode clusters scaling beyond 500,000 cards.

<details><summary>References</summary>
<ul>
<li><a href="https://www.chooseai.net/news/7318/">阿里云计划建 50 万卡广域超节点集群：1GW 算力、6 微秒通信延迟-Choo...</a></li>
<li><a href="https://www.ithome.com/0/952/644.htm">阿里云发布“真武 M890”AI 芯片及 128 卡超节点服务器，可支持海量 Agent 并发推理 - IT之家</a></li>
<li><a href="https://www.qbitai.com/2026/07/457694.html">阿里云：真武芯片超节点已成功适配Qwen3.8，上线百炼提供推理服务</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#Alibaba`, `#semiconductors`, `#cloud computing`, `#LLM infrastructure`

---

<a id="item-8"></a>
## [Cloudflare's Python Workers Reach General Availability](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

Cloudflare announced that Python Workers are now generally available (GA), making Python a first-class language on its developer platform alongside JavaScript. The runtime natively supports popular Python web frameworks such as FastAPI, Django, and Flask, and can run PostgreSQL databases and AI orchestration libraries like LangChain while integrating directly with Cloudflare services including Workers AI, R2, and D1. This removes a major barrier for the large Python developer community, which previously had to rewrite logic in JavaScript/TypeScript or run Python on heavier container-based serverless platforms. It strengthens Cloudflare's position in edge computing and serverless against AWS Lambda and Vercel by letting teams deploy existing Python frameworks and AI stacks to the edge with minimal changes. Developers install packages and deploy Python Workers using pywrangler, the dedicated CLI for Python Workers, and example projects are published in Cloudflare's python-workers-examples repository. D1 provides serverless SQLite-style databases at the edge, R2 offers S3-compatible object storage with zero egress fees, and Workers AI supplies managed inference — all of which can now be called directly from Python code.

telegram · zaihuapd · Sep 22, 04:00

**Background**: Cloudflare Workers is a serverless platform that runs application code on Cloudflare's global edge network rather than in a single region, traditionally using JavaScript and WebAssembly. Python support arrived about two years ago as an open beta, built on Pyodide, a WebAssembly build of CPython that lets Python run inside the Workers runtime. Reaching GA means the feature is considered production-ready and stable enough for general use, with official support rather than experimental status. Frameworks like FastAPI, Django, and Flask are standard Python web toolkits, while LangChain is a widely used library for building applications on top of large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/python-workers-ga/">Python Workers are now generally available | Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/workers/languages/python/">Write Cloudflare Workers in Python · Cloudflare Workers docs</a></li>
<li><a href="https://developers.cloudflare.com/r2/">Overview · Cloudflare R 2 docs</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#Serverless`, `#Python`, `#Edge Computing`, `#Workers AI`

---

<a id="item-9"></a>
## [DeepSeek and Tsinghua Release DSec Sandbox Platform Technical Report](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI and Tsinghua University jointly released a technical report on DeepSeek Elastic Compute (DSec), a sandbox infrastructure platform that serves roughly 3 million sandbox instances per day to support large-scale agent training and evaluation. The platform exposes four backends through a unified SDK — FnCall, containers, Firecracker microVMs, and full VMs — and decouples stateful rollout execution from preemptible GPU training by integrating deeply with reinforcement learning frameworks. As AI labs shift from static model training toward agentic systems that need to execute code and interact with real environments, sandbox throughput becomes a hard scaling bottleneck; DSec shows a production-grade design that sustains hundreds of thousands of concurrent sandboxes. The report gives the wider AI infrastructure community a rare, concrete look at how a frontier lab builds and operates the execution layer behind agent reinforcement learning. A single production unit runs about 160 nodes and peaks at over 380,000 concurrent sandboxes with creation rates above 5,000 per second, while one node can densely host 3,200 containers or 800 microVMs. By loading EROFS images on demand over the 3FS distributed file system instead of doing full Docker pulls, DSec reports 1.7x faster task completion and 57% less disk write, with memory sharing and reclamation cutting peak memory usage by roughly 40%.

telegram · zaihuapd · Sep 22, 04:45

**Background**: Agent training requires models to actually run code, browse, or operate software in isolated environments, so each training sample needs a disposable execution sandbox. Firecracker is a lightweight virtual machine monitor that runs microVMs combining hardware-level isolation with container-like startup speed, while EROFS is a read-only Linux filesystem designed for immutable images and container/application sandbox images. 3FS is DeepSeek's own open-sourced distributed file system built for the high-throughput, low-latency demands of AI training and inference.

<details><summary>References</summary>
<ul>
<li><a href="https://erofs.docs.kernel.org/en/latest/">Overview — EROFS filesystem project</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker - microvm / firecracker : Secure and fast microVMs...</a></li>
<li><a href="https://winbuzzer.com/2025/04/20/deepseeks-open-source-3fs-distributed-file-system-promises-efficiency-and-better-scaling-for-ai-workloads-xcxwbn/">DeepSeek's Open Source 3 FS Distributed File System Promises...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#agent training`, `#sandbox`, `#reinforcement learning`, `#distributed systems`

---