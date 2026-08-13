---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 32 items, 11 important content pieces were selected

---

1. [Spaghettifying DRAM: New Exploit Uses DRAM Scrambling to Unlock Hidden CPU Memory](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Pro 0813 Released with Open Weights and API Access](#item-2) ⭐️ 9.0/10
3. [DeepSeek-V4-Pro Launches with Agent Upgrades and Time-Based API Pricing](#item-3) ⭐️ 9.0/10
4. [Gemini 3.7 Flash](#item-4) ⭐️ 8.0/10
5. [Cerebras and OpenAI Launch GPT-5.6 Sol Ultrafast, Claiming 7x Speedup](#item-5) ⭐️ 8.0/10
6. [Choose Boring Technology: A Timeless Case for Innovation Tokens](#item-6) ⭐️ 8.0/10
7. [DeepSeek Releases Open-Source Agent Harness Developer Preview](#item-7) ⭐️ 8.0/10
8. [Worldproof tool shows pixel metrics often can’t rank world models](#item-8) ⭐️ 8.0/10
9. [DeepMind launches sign language-to-text AI SL2T, debuting on Pixel 11](#item-9) ⭐️ 8.0/10
10. [DeepSeek Releases Open-Source Harness and V4-Pro-0813 Weights](#item-10) ⭐️ 8.0/10
11. [OpenAI Previews Ultrafast Mode, Speeds Up GPT-5.6 Sol by 14x](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Spaghettifying DRAM: New Exploit Uses DRAM Scrambling to Unlock Hidden CPU Memory](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

Security researcher Christopher Domas published 'Skitter Creek Bath Salts', a tool that exploits AMD DRAM scrambling to create address aliases reaching normally protected memory such as SMRAM, PSP private memory, and the C6 idle-state. The project introduces a novel DRAM attack technique called 'Spaghettifying DRAM'. This research shows that DRAM scrambling — a feature intended to protect memory from physical probing — can be reverse-engineered to bypass CPU security fences, potentially exposing trusted memory regions on AMD systems. It raises serious concerns for platforms built on AMD hardware, including gaming consoles like Xbox and PlayStation, and lowers the barrier after an attacker already achieves kernel-level code execution. The README identifies AMD16h (the Jaguar architecture, circa 2013) as an affected family and notes that Zen 3 uses a different base address for memory controller registers, leaving support on newer CPUs unclear. The technique uses the z3 SMT solver to derive the DRAM scrambling transform, turning it into a 'rosetta stone' for generating aliases that bypass the fences and locks built into the coherent memory view.

hackernews · matt_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**Background**: DRAM scrambling is a modern memory-controller feature that permutes or hashes address bits before they reach the physical DRAM, making it harder for attackers who probe physical wires to correlate addresses with data. This project, by well-known hardware hacker Christopher Domas, shows the scrambling transform can be fully solved and abused as an aliasing primitive. The name references spaghettification in astrophysics, where a strong gravitational field stretches objects into long thin shapes — here the scrambled address space is bent and folded relative to the normal coherent view of memory.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking _everything_ on the CPU with DRAM scrambling · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spaghettification">Spaghettification - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement for Christopher Domas's upcoming Black Hat talk, with several praising his past reverse-engineering presentations. Some noted that while the attack requires ring-0 access, it could then expose everything on consoles like Xbox and PlayStation; others questioned which CPU generations are affected, observing that confirmed AMD16h/Jaguar is an older architecture and Zen 3 would need a different address calculation.

**Tags**: `#security`, `#DRAM`, `#exploit`, `#hardware`, `#research`

---

<a id="item-2"></a>
## [DeepSeek V4 Pro 0813 Released with Open Weights and API Access](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 9.0/10

DeepSeek V4 Pro 0813 is now available via API on OpenRouter, with open weights published on Hugging Face (1.7T parameters, 893 GB). Simon Willison observed that the model generates strikingly different images across its low, medium, and high reasoning levels. This release continues the trend of open-weight frontier-scale models, making cutting-edge capabilities available for self-hosting and research. The observed qualitative differences between reasoning levels also show that reasoning effort can materially change model behavior beyond mere benchmark scores. The open weights are 893 GB with 1.7 trillion parameters, released on Hugging Face under deepseek-ai/DeepSeek-V4-Pro-0813. Benchmark results were circulated via unofficial channels: a Reddit post that moderators deleted as low-effort and an ASCII-art table on Hacker News.

rss · Simon Willison · Aug 12, 23:59

**Background**: DeepSeek is a Chinese AI lab known for releasing large Mixture-of-Experts (MoE) language models, such as the earlier DeepSeek-V4-Pro with 1.6T total parameters and a 1M-token context window. Open-weight models like these let anyone download and run the trained parameters on their own hardware, unlike closed APIs, and OpenRouter provides a single API gateway to many such models.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro">DeepSeek V4 Pro - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**Discussion**: Simon Willison's post highlights that benchmark information was not officially announced but leaked through a WeChat group, deleted from Reddit, and reposted as an ASCII table on Hacker News. This suggests the community is actively discussing and verifying performance data through informal channels.

**Tags**: `#DeepSeek`, `#LLM`, `#open-weights`, `#Hugging Face`, `#AI release`

---

<a id="item-3"></a>
## [DeepSeek-V4-Pro Launches with Agent Upgrades and Time-Based API Pricing](https://api-docs.deepseek.com/zh-cn/updates) ⭐️ 9.0/10

DeepSeek-V4-Pro has been officially released across the app, web, and API, keeping the same API call format under the model name deepseek-v4-pro. The release adds improved agent capabilities, native Responses API support with Codex compatibility, and new low/high/max thinking modes for V4-Pro and V4-Flash. This update positions DeepSeek as a more direct competitor to frontier AI APIs by adopting the emerging Responses API standard and strengthening agentic workflows. Developers can now build Codex-compatible agents with DeepSeek, while the new peak/off-peak pricing could make off-peak usage significantly cheaper and influence how AI APIs are priced. The new peak/off-peak API pricing takes effect at 00:00 on August 17, 2026, with off-peak rates set at half the peak-hour price. V4-Pro and V4-Flash thinking modes now support three settings—low, high, and max—alongside the native Responses API format.

telegram · zaihuapd · Aug 13, 11:12

**Background**: The Responses API is an API primitive introduced by OpenAI that evolved from Chat Completions, adding persistent reasoning, hosted tools, and agentic capabilities for developers. AI agents are semi- or fully autonomous systems that perceive, reason, and act to accomplish tasks, often coordinating with other agents or humans. Peak/off-peak pricing, similar to electricity tariffs, charges lower rates during non-peak hours to balance load and reduce costs.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/blog/responses-api">Why we built the Responses API | OpenAI Developers</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI`, `#LLM`, `#API`, `#Pricing`

---

<a id="item-4"></a>
## [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

Google introduces Gemini 3.7 Flash, a new efficient AI model with strong vision-to-HTML performance and introductory pricing, sparking extensive community discussion.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**Tags**: `#Gemini`, `#Google`, `#AI models`, `#LLM`, `#Machine learning`

---

<a id="item-5"></a>
## [Cerebras and OpenAI Launch GPT-5.6 Sol Ultrafast, Claiming 7x Speedup](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

Cerebras and OpenAI have announced GPT-5.6 Sol Ultrafast, a new API service tier powered by Cerebras hardware that runs the model up to 14x faster and delivers up to 750 output tokens per second. On frontier benchmarks it achieved a claimed 7x speedup over standard Sol with comparable accuracy, including answering all 2,500 HLE questions in 11 hours 11 minutes. This milestone shows that specialized wafer-scale hardware can dramatically accelerate state-of-the-art LLM inference, potentially reshaping cost and latency tradeoffs for enterprise AI applications. The collaboration signals deeper integration between OpenAI's models and Cerebras custom silicon, which could intensify competition among inference providers. Ultrafast mode is being previewed with no published pricing, and some performance comparisons rely on internal data rather than independent reruns of the Artificial Analysis suite. Cerebras reports a 5.6x end-to-end speedup on GDP-Val with no quality degradation, and it runs 11x faster than Claude Fable 5 and 5x faster than Opus 4.8 on Fast mode.

hackernews · pr337h4m · Aug 13, 18:10 · [Discussion](https://news.ycombinator.com/item?id=49289844)

**Background**: Cerebras builds wafer-scale processors such as the WSE-3, a 5nm chip with 4 trillion transistors and 900,000 AI-optimized cores, which can feed an entire LLM from a single chip without the memory bottlenecks of multi-GPU systems. Frontier benchmarks like Humanity's Last Exam (HLE) and GDP-Val are designed to test models on demanding reasoning and economically valuable work tasks. Faster inference can change how models are used, allowing more tokens to be generated per second or enabling techniques like iterative refinement within practical time limits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are cautiously excited but skeptical: several note that neither Cerebras nor OpenAI explicitly state that Ultrafast matches standard Sol's quality exactly, and the lack of pricing suggests it may be expensive. Others argue that speed itself improves reasoning by enabling iteration and revision, and they compare the reported throughput favorably against competing models like Claude Fable 5 and Opus 4.8.

**Tags**: `#LLM inference`, `#Cerebras`, `#OpenAI`, `#GPT-5.6`, `#performance acceleration`

---

<a id="item-6"></a>
## [Choose Boring Technology: A Timeless Case for Innovation Tokens](https://mcfunley.com/choose-boring-technology) ⭐️ 8.0/10

Dan McKinley's 2015 essay 'Choose Boring Technology' has resurfaced on Hacker News, reigniting discussion of its 'innovation tokens' framework. The essay argues that companies should default to boring, well-understood technology and ration novel choices as a finite budget. The 'innovation tokens' concept gives engineering leaders a concrete way to weigh novelty against risk, making it a durable decision-making heuristic. It remains relevant even amid new trends like AI agents, as it helps teams channel innovation into product value while keeping infrastructure dependable. The essay posits that each company starts with roughly three innovation tokens, and spending one on a new database, framework, or paradigm leaves fewer for other experiments. The core idea is to push innovation into areas that differentiate the product, not into foundational infrastructure.

hackernews · tosh · Aug 13, 17:48 · [Discussion](https://news.ycombinator.com/item?id=49289512)

**Background**: The 'boring technology' philosophy in software engineering encourages using mature, predictable tools over trendy alternatives, since mature tools reduce unexpected failures and maintenance burden. The innovation tokens metaphor, popularized by this essay, operationalizes this philosophy by setting a clear budget for non-standard choices. This framework has been widely cited in engineering leadership discussions as a tool for making and communicating tradeoffs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lessannoyingbusiness.com/post/innovation-tokens">Innovation Tokens - When to break from the status quo</a></li>
<li><a href="https://mattrickard.com/innovation-tokens">Innovation Tokens - Matt Rickard</a></li>
<li><a href="https://concepts.dsebastien.net/concept/innovation-tokens/">Innovation Tokens - Concepts</a></li>

</ul>
</details>

**Discussion**: The Hacker News comments largely praise the essay's practicality, with one user calling it a core engineer mindset and another highlighting innovation tokens as critical for explaining tradeoffs. However, some push back: a commenter calls the token concept 'arbitrary' and 'unserious', arguing that engineers should evaluate requirements, risks, and gains on their merits. A third commenter suggests that in the age of agents, teams should spend all their innovation tokens on the agent layer and keep everything else boring.

**Tags**: `#software engineering`, `#technology strategy`, `#innovation tokens`, `#engineering culture`

---

<a id="item-7"></a>
## [DeepSeek Releases Open-Source Agent Harness Developer Preview](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek has released DeepSeek Harness (dsh), an open-source developer preview of an agent harness, with source code available on GitHub under the MIT license. The framework features traceable append-only session logs and a hot-reloadable plugin system built on Cordis. As an open-source agent harness from a major AI lab, it gives developers full inspectability into agent runs and a modular plugin architecture, in contrast to proprietary US models that encrypt or obfuscate traces. This could accelerate community-driven agent tooling and lower the barrier to building production-ready agents. Everything is treated as a plugin, and the harness supports resume, fork, search, and replay over the same event stream. The preview is early and MIT-licensed, so rough edges and breaking changes are expected; the system leverages Cordis v4 for hot-loading and unloading plugins with side-effect rollback.

hackernews · bjin · Aug 13, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49285244)

**Background**: An agent harness is the software infrastructure that wraps a large language model so it can act as an agent—managing tools, memory, state persistence, and execution environments. DeepSeek Harness was announced as a developer preview on DeepSeek's website and GitHub, with documentation describing its 'everything is a plugin' design and trajectory view. The plugin system is powered by Cordis, which enables hot-reloading and dynamic enable/disable of components without restarting the process.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>

</ul>
</details>

**Discussion**: The discussion is largely positive. Commenters highlight traceable append-only logs as a 'killer feature' compared with encrypted or obfuscated traces from US models; one paper author explains that the system adds hot-reload and dynamic enable/disable to the plugin system, including UI components. Another commenter notes DeepSeek Harness resembles Pi Coding Agent, and one cautious take describes the underlying paper as useful but not revolutionary.

**Tags**: `#deepseek`, `#agent-harness`, `#open-source`, `#tracing`, `#plugins`

---

<a id="item-8"></a>
## [Worldproof tool shows pixel metrics often can’t rank world models](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/) ⭐️ 8.0/10

The author released Worldproof, an open-source diagnostic tool for world models, and found that pixel metrics like SSIM and PSNR often cannot rank models on real robot rollout videos. A copy-last-frame baseline scored 0.983 SSIM and 53.9 dB PSNR on SO-101 recordings, with error flat across horizons, so all models tie. This matters because it exposes a hidden failure mode in world-model evaluation: standard fidelity metrics can have zero discriminative power on real robot data, making benchmark rankings meaningless. It pushes the community to measure the “usable window” of horizons on their own data rather than inheriting defaults from other papers. The analysis uses 64 rollouts per configuration, interquartile-mean aggregation with stratified bootstrap confidence intervals following Agarwal et al. 2021, and dynamic-region masked metrics. The usable horizon on DROID footage was roughly steps 8–24; both short and long horizons collapse into ties, and LPIPS behaved inconsistently without a clear explanation.

reddit · r/MachineLearning · /u/georgia_bucea · Aug 13, 19:58

**Background**: World models are neural networks that predict future video frames given an initial context and a sequence of actions, commonly used in model-based reinforcement learning and robotics. Pixel metrics such as PSNR and SSIM compare images pixel-wise or on luminance/contrast/structure, but they can be insensitive when backgrounds are static or motion is small. The post was shared on r/MachineLearning and includes open-source code; the SO-101 is an open-source robotic arm from Hugging Face's LeRobot project, and DROID is a large real-world manipulation dataset.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/TheRobotStudio/SO-ARM100">GitHub - TheRobotStudio/SO- ARM 100: Standard Open Arm 100</a></li>
<li><a href="https://ieeexplore.ieee.org/document/5596999/">Image Quality Metrics: PSNR vs. SSIM | IEEE Conference Publication | IEEE Xplore</a></li>

</ul>
</details>

**Tags**: `#world models`, `#model evaluation`, `#robotics`, `#machine learning`, `#open source`

---

<a id="item-9"></a>
## [DeepMind launches sign language-to-text AI SL2T, debuting on Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

DeepMind unveiled SL2T, a multilingual sign language-to-text model, and it is now available on Pixel 11 in Gboard and Live Transcribe. It initially supports American Sign Language to English, with more languages and devices planned. This is a significant milestone for accessibility, bringing sign language AI out of research labs and into everyday consumer devices. It could help deaf and hard-of-hearing users communicate more easily, and it sets a precedent for other tech companies to integrate similar models. The model was trained on over 100,000 hours of data across more than 50 sign languages, and it achieves a zero-shot BLEURT score of 70 on the FLEURS-ASL benchmark. To protect privacy, it only processes hand and body pose keypoints rather than raw video footage.

telegram · zaihuapd · Aug 13, 08:55

**Background**: Sign language recognition is a challenging computer vision problem because sign language relies on fast, complex hand gestures and body movements. FLEURS-ASL is a recent benchmark that extends the FLORES/FLEURS multilingual datasets to American Sign Language, and BLEURT is a learned metric that measures how closely generated text matches human judgments of fluency and meaning. By using pose keypoints instead of full video, DeepMind reduces privacy risks while maintaining translation quality.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2408.13585v1">FLEURS-ASL: Including American Sign Language in Massively ...</a></li>
<li><a href="https://github.com/google-research/bleurt">GitHub - google-research/bleurt: BLEURT is a metric for ...</a></li>
<li><a href="https://aclanthology.org/2025.naacl-long.314.pdf">FLEURS-ASL: Including American Sign Language in Massively ...</a></li>

</ul>
</details>

**Tags**: `#sign language`, `#accessibility`, `#DeepMind`, `#AI model`, `#translation`

---

<a id="item-10"></a>
## [DeepSeek Releases Open-Source Harness and V4-Pro-0813 Weights](https://mp.weixin.qq.com/s/mANdGRI4fO_sEbC1ECEoZQ) ⭐️ 8.0/10

DeepSeek announced the open-source release of DeepSeek Harness under the MIT license and made the DeepSeek-V4-Pro-0813 weights available on Hugging Face. The harness is now in developer preview and includes its full source code. This release offers a model-agnostic, plugin-based alternative to the agent infrastructure behind Claude Code and Codex, potentially lowering barriers for AI agent development. It also signals DeepSeek's continued push to open-source core tools and models, which could accelerate adoption across the AI/ML community. DeepSeek Harness uses an 'everything is a plugin' architecture powered by Cordis, and offers four operating modes: Standard, PTC, Minimal, and Creation. Its PTC (Programmatic Tool Calling) mode lets the model generate a single program to orchestrate multiple tool calls, reducing round trips. The Hugging Face page for V4-Pro-0813 temporarily returned 404 before being restored.

telegram · zaihuapd · Aug 13, 12:39

**Background**: An agent harness is a framework that lets large language model agents interact with tools, manage sessions, sandboxes, storage, and scheduling. DeepSeek Harness is designed to be model-agnostic, so developers can swap or recompose each capability as a plugin. Cordis is a meta-framework for spatiotemporal composability that powers this plugin architecture. DeepSeek-V4-Pro-0813 is the newly released model weight set from DeepSeek, distributed via Hugging Face.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness/tree/master">GitHub - deepseek-ai/deepseek-harness · GitHub</a></li>
<li><a href="https://venturebeat.com/technology/deepseek-harness-launches-as-open-source-rival-to-claude-code-alongside-v4-pro-on-api-with-higher-prices">DeepSeek Harness launches as open source rival to Claude Code ...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI`, `#Open Source`, `#Model Release`, `#Harness`

---

<a id="item-11"></a>
## [OpenAI Previews Ultrafast Mode, Speeds Up GPT-5.6 Sol by 14x](https://openai.com/index/previewing-ultrafast/) ⭐️ 8.0/10

OpenAI has previewed Ultrafast, a new API service tier that runs GPT-5.6 Sol up to 14 times faster than standard processing, delivering up to 750 output tokens per second. The service is powered by Cerebras and is initially available only to select customers. This dramatically reduces inference latency for OpenAI's most capable model, making it practical for time-sensitive applications such as fault response, financial research, customer service, and e-commerce. It also highlights the growing role of specialized inference hardware like Cerebras in the AI ecosystem. The Ultrafast preview is limited to a select group of customers, with OpenAI saying access will expand as compute capacity grows. Despite the speedup, OpenAI and Cerebras state that there is no compromise in output quality.

telegram · zaihuapd · Aug 13, 17:04

**Background**: Cerebras Systems develops semiconductors, supercomputers, and software for deep-learning applications, including AI inference. It claims its hardware can deliver inference up to 15 times faster than NVIDIA GPUs, with examples such as running DeepSeek R1 at 1,500+ tokens per second. Ultrafast leverages Cerebras' Wafer Scale Engine to accelerate OpenAI's GPT-5.6 Sol, marking a partnership between a leading AI lab and a specialized inference hardware vendor.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT‑5.6 Sol at up to ... - OpenAI</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://www.ithinkdiff.com/openai-ultrafast-api-tier-gpt-5-6-sol-750-tokens-per-second/">OpenAI Previews Ultrafast Mode: GPT-5.6 Sol at 14x Speed</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#performance`, `#Cerebras`, `#ultrafast`

---