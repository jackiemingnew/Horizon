---
layout: default
title: "Horizon Summary: 2026-10-01 (EN)"
date: 2026-10-01
lang: en
---

> From 34 items, 7 important content pieces were selected

---

1. [DeepSeek Open-Sources Foundational Components for Huawei Ascend](#item-1) ⭐️ 9.0/10
2. [Google Announces Gemini 4 Argon, a Frontier Model Still in Early Preview](#item-2) ⭐️ 8.0/10
3. [Team publicly reverses its "no MCP" stance, sparking debate](#item-3) ⭐️ 8.0/10
4. [32-Researchers Survey Covers Tokenization Across Modern NLP](#item-4) ⭐️ 8.0/10
5. [Cloudflare to Become a Public Certificate Authority](#item-5) ⭐️ 8.0/10
6. [Kimi K3 Lands in OpenAI Codex Enterprise Billing via Baseten](#item-6) ⭐️ 8.0/10
7. [Reddit to Kill RSS Feeds and Public API Access Over AI Scraping](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek Open-Sources Foundational Components for Huawei Ascend](https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww) ⭐️ 9.0/10

On September 30, 2026, DeepSeek open-sourced a suite of foundational software components targeting Huawei's Ascend compute platform, covering the TileLang high-level language compiler toolchain, high-performance compute libraries, and distributed communication libraries, explicitly positioned as counterparts to its earlier NVIDIA/GPU-oriented stack. The release includes DeepGEMM Ascend, DeepEP Ascend, TileKernels, FlashMLA, and DeepSelect, and DeepSeek says it is working with Huawei on a 128-card supernode solution for Ascend 950. This is a substantial software-stack play aimed directly at NVIDIA's CUDA moat: by porting the same toolchain, compute kernels, and communication primitives it uses on GPUs to Ascend, DeepSeek lowers the cost for developers and model builders to move workloads onto Chinese domestic hardware. It also strengthens the wider domestic AI ecosystem, since mature, high-performance open libraries are often the real barrier to adopting a non-NVIDIA accelerator, not raw chip throughput. DeepSeek claims the components reach performance close to the hardware ceiling in multiple benchmarks, and DeepGEMM Ascend is reported to be fully API-compatible with DeepGEMM, supporting BF16, FP8 and FP4 GEMM, MQA logits, and MegaMoE so users can keep the same APIs and development workflow as on other platforms. One caveat: the source material is a short aggregated snippet without technical depth or community discussion, so the performance claims and the exact release scope have not been independently verified.

telegram · zaihuapd · Sep 30, 03:09

**Background**: Ascend is Huawei's AI accelerator line, and its software stack (CANN) has historically been far less mature than NVIDIA's CUDA, which is why most Chinese AI training and inference still runs on NVIDIA GPUs. TileLang, one component in this release, is an open-source high-performance AI kernel DSL led by Peking University researchers and released in January 2025; it uses a "tile" blocking abstraction so developers can express computations in near-mathematical form while the compiler handles loop optimization and memory scheduling. DeepEP is a communication library focused on expert parallelism (the all-to-all dispatch/combine kernels used by Mixture-of-Experts models), and DeepGEMM is a high-performance GEMM kernel library — both were originally created for NVIDIA GPUs. Ascend 950 is Huawei's next-generation chip, and "supernode" refers to tightly interconnected multi-card clusters, in this case a 128-card configuration.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepGEMM-Ascend">GitHub - deepseek-ai/DeepGEMM-Ascend: DeepGEMM-Ascend: clean ...</a></li>
<li><a href="https://zglg.work/ai/news/zh/2026-09-30-deepseek-open-sources-ascend-infrastructure-tilelang-deepgemm-and-deepep">DeepSeek开源昇腾基础组件：TileLang、DeepGEMM与DeepEP同批落地 | zg...</a></li>
<li><a href="https://baike.baidu.com/item/TileLang/67440655">TileLang - 百度百科</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#Huawei Ascend`, `#open source`, `#AI infrastructure`, `#compilers`

---

<a id="item-2"></a>
## [Google Announces Gemini 4 Argon, a Frontier Model Still in Early Preview](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) ⭐️ 8.0/10

Google announced Gemini 4 Argon, which it describes as its new frontier model built for real-world coding, enterprise knowledge work, and cyber defense, sitting at the top of the Gemini family above the Gemini 3.8 line that shipped through September 2026. Crucially, the model is not yet generally available: Google says it will continue gathering feedback from early testers and iterating on guardrails before making Argon available to developers, enterprises, and consumers. The release is another data point in a year of rapid leapfrogging among frontier labs, undermining the once-influential 'winner-takes-all' theory that the first lab to gain a lead in AI would never cede ground. For enterprises and developers, it reinforces that capability leadership is now distributed across hyperscalers, neoclouds, and startups, so workflows should be designed to keep model providers swappable. Google names three explicit target domains — software engineering, enterprise knowledge work such as legal tasks, and cyber defense — and the announcement notes that Argon agents are working on migrating C/C++ codebases to Rust across Google. Because Argon is still an early preview, no generally available pricing or public benchmark results are settled yet, and the guardrail iteration implies access terms may change before launch.

hackernews · bradleyg223 · Sep 30, 20:04 · [Discussion](https://news.ycombinator.com/item?id=49913571)

**Background**: Frontier models are the most advanced general-purpose AI systems available at a given moment, typically defined by massive scale and the ability to handle complex, multi-step reasoning and agentic workflows. Google's Gemini family is its flagship line of such models, with each numbered generation succeeding the last; an 'early preview' release is a common industry practice of showing a model to select testers and partners before opening it to the general public. Google's framing of Argon around coding, enterprise knowledge work, and cyber defense reflects where labs currently see the highest-value, near-term commercial demand for frontier capability.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon - The Keyword</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/google-gemini-4-argon-ai.html">Google rolls out Gemini 4 Argon, its most advanced model - CNBC</a></li>
<li><a href="https://www.datacamp.com/blog/gemini-4-argon">Gemini 4 Argon: Benchmarks, Pricing, and Access | DataCamp</a></li>

</ul>
</details>

**Discussion**: Hacker News discussion (roughly 921 points and 631 comments) was intense and largely substantive. One widely cited anecdote describes Gemini 3.8 Flash autonomously attaching GDB to a GPU driver and writing an LD_PRELOAD shim to get ROCm working with llama.cpp, which commenters took as evidence of a real capability leap, while another top thread argues that Dario Amodei's 'concentrating' winner-takes-all thesis has been disproven by the distributed competitive landscape. Others mocked Google for again shipping a model that is not yet released ('can't release a model' allegations), and the most practical advice was to keep both model and provider replaceable so intelligence becomes a commodity.

**Tags**: `#AI`, `#LLM`, `#Google Gemini`, `#model-release`, `#AI-competition`

---

<a id="item-3"></a>
## [Team publicly reverses its "no MCP" stance, sparking debate](https://earendil.com/posts/you-said-no-mcp/) ⭐️ 8.0/10

A team behind a widely-read post titled "You said no MCP" publicly reversed its previously firm rejection of the Model Context Protocol (MCP) and explained why it now endorses the standard for connecting agents to tools and data. The reversal drew a 610-point, 340-comment Hacker News thread that turned into a broad referendum on MCP versus CLI-based agent tooling. A prominent, public reversal matters because MCP spent much of this year being declared dead by influential voices who crowned command-line tooling the winner, often glossing over MCP's advantages in security, observability, deployment and operations. If more teams follow suit, MCP's role as the default integration layer for AI agents — rather than ad-hoc CLI wrappers — could be reinforced across the developer tooling ecosystem. The post and commenters concede MCP is not performance-optimal, robust or uniform in its current form, but argue that ubiquity and end-user compatibility win anyway — comparisons were drawn to USB-C, NVMe and HDMI, which are successful despite their flaws. One commenter also cited Armin Ronacher's observation that strong opinions are often defended with arguments that have long since become outdated.

hackernews · yarapavan · Sep 30, 09:55 · [Discussion](https://news.ycombinator.com/item?id=49906637)

**Background**: The Model Context Protocol is an open standard and open-source framework introduced by Anthropic in November 2024 to standardize how AI systems such as large language models connect to external tools, data sources and workflows — frequently described as "a USB-C port for AI." It was subsequently adopted by major AI providers including OpenAI and Google DeepMind. The main alternative is CLI-based agent tooling, in which an AI agent runs in the terminal with direct access to the filesystem, shell and developer tools, editing files, running tests and committing changes autonomously.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://github.com/bradAGI/awesome-cli-coding-agents">Awesome CLI Coding Agents - GitHub</a></li>

</ul>
</details>

**Discussion**: Sentiment on Hacker News was mixed but leaned positive toward the reversal: gk1 praised the team for changing a strongly-held belief publicly and cited Armin Ronacher on outdated arguments, while CharlieDigital argued the call was obvious as early as March and criticized influencers who declared MCP dead. alin23 reported using MCP well beyond coding, embedding it in macOS apps like rcmd, Clop and Lunar so they can be configured in natural language even with local models, and _fw summed up the pragmatic view that MCP may be suboptimal but "something is better than nothing" because it is widely compatible and will improve over time.

**Tags**: `#MCP`, `#AI agents`, `#developer tooling`, `#LLM integration`, `#Hacker News discussion`

---

<a id="item-4"></a>
## [32-Researchers Survey Covers Tokenization Across Modern NLP](https://www.reddit.com/r/MachineLearning/comments/1wuccjf/tokenization_a_survey_for_modern_nlp_r/) ⭐️ 8.0/10

Over roughly eight months, 32 tokenizer researchers collaborated on what they describe as the most comprehensive survey of tokenization in modern NLP, covering algorithms, evaluations, multilinguality, encodings and theory, and is now shared publicly via alphaXiv. The survey also examines candidate replacements for tokenizers, such as latent tokenization and visual tokenization, as well as adjacent topics including constrained generation, token healing and tokenizer security concerns. Tokenization is widely described as understudied even though it affects essentially every NLP task, so a single collaborative reference consolidating algorithms, evaluation practices, multilingual behavior and security risks could become a standard entry point for both practitioners and newcomers. It also signals that the field is seriously debating whether discrete subword tokenizers should be replaced altogether by latent or visual representations. The survey is a synthesis rather than a new model or benchmark contribution, so its value lies in organizing and comparing existing methods rather than reporting new experimental results. Beyond core tokenizer algorithms, it devotes space to closely related problems such as constrained generation, token healing — the inference-time fix for token-boundary artifacts at the prompt edge — and security issues associated with tokenization.

reddit · r/MachineLearning · /u/mcmcmcmcmcmcmcmcmc_ · Sep 30, 18:13

**Background**: Tokenization is the preprocessing step that splits raw text into the subword units, or tokens, that a language model actually reads and predicts, using algorithms such as BPE, WordPiece and Unigram language models. Because a model never sees characters directly, token boundaries influence everything from vocabulary size and multilingual fairness to prompt behavior and output formatting. Token healing addresses a known artifact where a prompt ends mid-token, causing the model's first generated token to be split unnaturally, while constrained generation forces the decoder to emit output that conforms to a grammar, regex or schema. More recent research explores latent tokens — learnable vectors that are not interpretable as natural-language words — as an alternative to fixed discrete vocabularies.

<details><summary>References</summary>
<ul>
<li><a href="https://guidance.readthedocs.io/en/latest/example_notebooks/tutorials/token_healing.html">Token healing — Guidance latest documentation</a></li>
<li><a href="https://insertchat.com/glossary/constrained-generation">Constrained Generation in nlp - InsertChat</a></li>
<li><a href="https://arxiv.org/pdf/2505.12629">Enhancing Latent Computation in Transformers with Latent Tokens</a></li>

</ul>
</details>

**Tags**: `#NLP`, `#tokenization`, `#survey`, `#language modeling`, `#machine learning`

---

<a id="item-5"></a>
## [Cloudflare to Become a Public Certificate Authority](https://blog.cloudflare.com/cloudflare-certificate-authority/) ⭐️ 8.0/10

Cloudflare announced plans to become a public certificate authority, having applied to the Chrome, Apple, Microsoft and Mozilla root programs and signed an agreement with GlobalSign to acquire a broadly trusted root certificate. No certificates are being issued yet, but Cloudflare says it will prioritize ACME-based automated issuance and renewal and intends to issue production Merkle Tree Certificates (MTCs) in Q1 2027 for the post-quantum era. Cloudflare already terminates TLS for a large share of the web, so owning a trusted root lets it issue certificates directly instead of relying on third-party CAs, potentially simplifying PKI for its customers and pressuring incumbents on price and automation. Its ACME-first and post-quantum roadmap could also accelerate industry-wide adoption of Merkle Tree Certificates and shorter-lived certificate models. Merkle Tree Certificates are a proposed X.509 format being standardized in the IETF (draft-ietf-plants-merkle-tree-certs) that integrates public logging in the style of Certificate Transparency, keeping certificate and logging overhead low even with large post-quantum signature algorithms. Because the plan still depends on root program approvals and a GlobalSign root acquisition, the timeline is subject to change and no issuance is available to users today.

telegram · zaihuapd · Sep 30, 06:26

**Background**: A certificate authority is a trusted entity that digitally signs TLS certificates, which browsers and operating systems accept only if they chain back to a root certificate already trusted in their root stores. Getting into programs like Chrome's Root Store or Mozilla's CA program is a lengthy audit-and-review process, so buying an existing trusted root from GlobalSign is a shortcut to being widely recognized. ACME (RFC 8555), the protocol created for Let's Encrypt, automates certificate issuance and renewal, and post-quantum cryptography refers to algorithms designed to resist attacks from future quantum computers — but their large keys and signatures create new efficiency problems for TLS certificates.

<details><summary>References</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/">draft-ietf-plants-merkle-tree-certs-06 - Merkle Tree Certificates</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment">Automatic Certificate Management Environment - Wikipedia</a></li>
<li><a href="https://www.encryptionconsulting.com/education-center/merkle-tree-certificates/">Merkle Tree Certificates (MTC) Explained</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#Certificate Authority`, `#PKI`, `#ACME`, `#Post-Quantum`

---

<a id="item-6"></a>
## [Kimi K3 Lands in OpenAI Codex Enterprise Billing via Baseten](https://36kr.com/newsflashes/4005691489112198) ⭐️ 8.0/10

US AI infrastructure company Baseten announced that enterprise customers can now run Kimi K3 inside OpenAI's Codex coding tool, with inference costs billed directly against their existing OpenAI enterprise procurement commitments rather than requiring a separate vendor onboarding process. This makes Kimi K3 the first Chinese open-weight model to enter OpenAI's enterprise paid settlement system. Enterprise AI procurement is increasingly consolidated around a few large committed-spend contracts, so letting a Chinese open-weight model be paid for through an existing OpenAI commitment sharply lowers adoption friction for enterprises that already have budget locked up with OpenAI. It also signals a new layer of interoperability between Chinese LLMs and US enterprise procurement systems, with implications for Moonshot AI, Baseten, OpenAI and corporate model buyers alike. Kimi K3 is a 2.8-trillion-parameter mixture-of-experts open-weight model released on July 16, 2026, and its custom license requires inference providers earning over US$20 million annually to share up to 30% of revenue — a provision that matters because Baseten is itself an inference provider. Notably, the routing and billing go through Baseten rather than through a direct OpenAI–Moonshot AI commercial agreement.

telegram · zaihuapd · Sep 30, 11:23

**Background**: Kimi is the large language model series from Chinese company Moonshot AI; K3, its flagship, is described as the largest open-weight model ever released and is competitive with frontier models from OpenAI and Anthropic. OpenAI Codex is OpenAI's coding agent, launched in April 2025 as the Codex CLI and now also available through ChatGPT's web app, a desktop app, and IDE integrations. Baseten is an AI inference platform that offers usage-based cloud pricing for deploying, serving and training models. Many large enterprises buy AI through "committed spend" agreements, prepaying a minimum amount that all eligible usage is drawn against — which is exactly the mechanism Baseten is piggybacking on here.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K3">Kimi K3</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Baseten">Baseten</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Kimi K3`, `#OpenAI Codex`, `#Enterprise AI`

---

<a id="item-7"></a>
## [Reddit to Kill RSS Feeds and Public API Access Over AI Scraping](https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/) ⭐️ 8.0/10

Reddit announced it will discontinue RSS feed support on November 13, and will shut down public API access by March 2027, citing large-scale scraping and automated abuse, particularly by AI bots. The company is steering moderators toward Discord Relay and has told third-party app and bot developers they must complete registration by January 12, 2027 or lose API access. RSS and the public API are foundational plumbing for third-party Reddit clients, moderation bots, archiving projects and academic research, so their removal will break a wide range of tools that were never built by Reddit itself. It also extends a broader industry trend of platforms locking down data access in response to AI training crawlers, further shrinking the open, machine-readable web. RSS is a lightweight, openly specified XML format that any reader can poll without authentication, so removing it eliminates a scraping-free, low-bandwidth way to follow subreddits. The key deadline is January 12, 2027 for API registration, with the full public API shutdown following in March 2027, while Discord Relay — a proprietary, chat-based workaround — replaces the open feed standard for moderation workflows.

telegram · zaihuapd · Oct 1, 00:27

**Background**: RSS (Really Simple Syndication) lets a site publish its updates as a standard XML file that feed readers check periodically and download into a user interface, which is why it has long been the backbone of news aggregation and self-hosted bots. Reddit's public API played a similar role for developers, powering mobile clients, moderation tools and data-research pipelines; Reddit already triggered widespread protests in 2023 when it introduced API pricing that killed several third-party apps. Discord Relay-style tools instead push content into Discord servers and channels, giving users a controlled, authenticated distribution channel rather than an open feed that anyone — including AI crawlers — can read.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/RSS">RSS - 维基百科，自由的百科全书 - zh.wikipedia.org</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2017735765103236977">RSS 原理介绍：从零理解信息订阅的本质 - 知乎</a></li>
<li><a href="https://getrelaybot.com/">Relay · Discord support without the panel</a></li>

</ul>
</details>

**Tags**: `#Reddit`, `#Public API`, `#RSS`, `#AI Scraping`, `#Platform Policy`

---