---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 43 items, 13 important content pieces were selected

---

1. [Firefox Compiled to WebAssembly Runs Inside Browser](#item-1) ⭐️ 9.0/10
2. [Japan to Buy 27,500 Nvidia Rubin Chips for Robot Sovereign AI](#item-2) ⭐️ 9.0/10
3. [Moonshot Releases Kimi K3, Open-Weight Frontier AI](#item-3) ⭐️ 8.0/10
4. [LM Studio Bionic: AI Agent for Open Models](#item-4) ⭐️ 8.0/10
5. [Roc Compiler Rewrite: Rust to Zig](#item-5) ⭐️ 8.0/10
6. [Thinking Machines Lab Releases Inkling Open-Weights Model](#item-6) ⭐️ 8.0/10
7. [Linus Torvalds Declares Linux Is Not Anti-AI](#item-7) ⭐️ 8.0/10
8. [QLoRA 2e-4 default learning rate is wrong for small datasets](#item-8) ⭐️ 8.0/10
9. [ExTernD: Ternary Decomposition for Accurate LLM Quantization](#item-9) ⭐️ 8.0/10
10. [CNKI to Remove Papers Listing AI as Authors](#item-10) ⭐️ 8.0/10
11. [EU rules Google must open Android, search data to rivals](#item-11) ⭐️ 8.0/10
12. [1Password Integrates Claude for Password-Free AI Login](#item-12) ⭐️ 8.0/10
13. [Truth Social to Sell Fast Access to Trump Posts to Wall Street](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox Compiled to WebAssembly Runs Inside Browser](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter compiled Firefox's Gecko engine to WebAssembly, allowing the full browser to run inside another browser via a WebSocket-based Wisp protocol. This demonstrates the feasibility of running a complete browser engine within a sandboxed WebAssembly environment, opening up possibilities for browser isolation, portable browsing, and novel application architectures. The project leveraged Gecko's strong single-process support and required an estimated $25,000 in AI token usage, though a Claude Max subscription reduced actual costs. All network traffic is proxied through Puter's servers using the Wisp protocol, with end-to-end encryption for HTTPS connections.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (WASM) is a binary instruction format that allows code written in languages like C++ to run in web browsers at near-native speed. Gecko is Mozilla's browser engine used in Firefox. Single-process mode simplifies the compilation of a complex GUI application like a browser to WASM. The Wisp protocol provides a low-overhead way to proxy TCP and UDP connections over a single WebSocket, which is necessary because WebAssembly code cannot directly open network sockets.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gecko_(software)">Gecko (software) - Wikipedia</a></li>
<li><a href="https://wiki.mozilla.org/Gecko:Overview">Gecko:Overview - MozillaWiki</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low ...</a></li>

</ul>
</details>

**Discussion**: On Hacker News, commenters expressed amazement at the technical feat, though some noted that the project required significant server scaling to handle traffic. The use of AI-assisted programming was also discussed as a factor in making the project feasible.

**Tags**: `#WebAssembly`, `#Firefox`, `#browser`, `#compilation`, `#demo`

---

<a id="item-2"></a>
## [Japan to Buy 27,500 Nvidia Rubin Chips for Robot Sovereign AI](https://www.bloomberg.com/news/articles/2026-07-16/japan-to-buy-nvidia-rubin-chips-to-build-sovereign-ai-for-robots) ⭐️ 9.0/10

Japan announced plans to purchase 27,500 Nvidia Rubin chips through a new company, Noetra, to build a large data center and develop a domestic foundational AI model for robotics, backed by ¥387.3 billion ($2.4B) in government funding. This initiative represents a major sovereign AI push by Japan to reduce dependence on foreign technology and compete with the US and China in robotics, potentially reshaping the global AI and robotics landscape with a goal of capturing over 30% of the global robot market by 2040. Noetra, led by President Hiroshi Tabata, aims to release the first AI model by March next year and a robot-specific version within a few years. Partners include SoftBank, Toyota-backed Preferred Networks, and NEC.

telegram · zaihuapd · Jul 16, 10:59

**Background**: Sovereign AI refers to national efforts to develop independent AI capabilities and reduce critical dependence on foreign providers. Nvidia's Rubin architecture, named after astrophysicist Vera Rubin, is the next-generation GPU/CPU platform using 3nm process and HBM4 memory, scheduled for release in Q3 2026. Japan seeks to create a 'third option' beyond US and Chinese AI dominance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rubin_(microarchitecture)">Rubin (microarchitecture) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_AI">Sovereign AI</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#sovereign AI`, `#robotics`, `#Japan`, `#chips`

---

<a id="item-3"></a>
## [Moonshot Releases Kimi K3, Open-Weight Frontier AI](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

Moonshot AI released Kimi K3, an open-weight frontier model with 2.8 trillion parameters, a 1 million token context window, and competitive pricing at $3/$15 per million tokens. This release challenges the notion that only US labs can produce frontier AI, potentially driving down costs and accelerating commoditization of advanced AI capabilities. Kimi K3 features a 1 million token context window and pricing that matches Anthropic's Sonnet series, though it is extremely high for a Chinese open-weight model.

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: Open-weight models allow users to download and run the model on their own hardware, though they may not include full training data or code. A context window refers to the amount of text the model can process at once; 1 million tokens is enough to handle large documents or long conversations.

<details><summary>References</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.innovatrixinfotech.com/blog/context-windows-explained-1-million-tokens-architecture">1 Million Token Context Window: What It Means for Builders ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Kimi K3's pricing is high for a Chinese model but justified if truly competitive with frontier models like Sol/Fable. Some debated whether Chinese labs are commoditizing AI to sell hardware, while others pointed out the immense training cost.

**Tags**: `#AI`, `#model release`, `#pricing`, `#Chinese AI`, `#frontier intelligence`

---

<a id="item-4"></a>
## [LM Studio Bionic: AI Agent for Open Models](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 8.0/10

LM Studio has launched Bionic, a new AI agent platform that uses open-source large language models to handle coding, document creation, and complex work tasks, with options for local execution or cloud connectivity. This launch expands LM Studio from a chat interface to a full agentic harness, making powerful open models accessible for practical tasks while offering cost control and data security for enterprises. Bionic supports voice input with local transcription, automatic checkpointing in Work projects, and flexible model execution including local, LM Link, or the LM Studio Secure Cloud for larger models.

hackernews · minimaxir · Jul 16, 20:18 · [Discussion](https://news.ycombinator.com/item?id=48939662)

**Background**: LM Studio is a popular desktop application that allows users to discover, download, and run large language models locally. It has now evolved from a chat-focused tool into an agentic platform with Bionic, enabling autonomous task execution using open models.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic, a new AI agent app for ... - 9to5Mac</a></li>
<li><a href="https://lmstudio.ai/blog/introducing-lm-studio-bionic">Introducing LM Studio Bionic: the AI agent for open models</a></li>

</ul>
</details>

**Discussion**: Founder Yagil offered free credits for testing Bionic with specific models. User inventor7777 praised its performance with Qwen3.6 35B but noted rough edges. Others discussed potential competition with Apple and enterprise use cases, and some expressed concerns about the shift in business model.

**Tags**: `#LM Studio`, `#AI agent`, `#open models`, `#local LLM`, `#coding`

---

<a id="item-5"></a>
## [Roc Compiler Rewrite: Rust to Zig](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

Richard Feldman, creator of the Roc programming language, announced that the Roc compiler is being rewritten from Rust to Zig, citing Zig's low-level memory control and faster build times as key reasons. This rewrite highlights real-world trade-offs between memory safety and low-level control in systems programming, and it could influence other compiler projects considering switching from Rust to Zig for performance gains. The rewrite focuses on Roc's compiler, which currently emits machine code, and leverages Zig's features like `ReleaseSafe` mode that catches use-after-free errors at runtime. The post notes that build time improvements were a major factor.

hackernews · jorangreef · Jul 16, 11:39 · [Discussion](https://news.ycombinator.com/item?id=48933149)

**Background**: Roc is a fast, friendly, functional language being developed by Richard Feldman. Rust is known for memory safety without garbage collection, while Zig prioritizes low-level control and faster compilation by forgoing some safety guarantees. The Roc compiler was originally prototyped in OCaml and then implemented in Rust.

<details><summary>References</summary>
<ul>
<li><a href="https://www.roc-lang.org/">The Roc Programming Language</a></li>
<li><a href="https://github.com/roc-lang/roc">GitHub - roc-lang/roc: A fast, friendly, functional language. Docs | Roc roc/docs/mini-tutorial-new-compiler.md at main · roc-lang/roc The Complete Roc Guide: From Zero to Expert - kodikra The Rise of Roc: A Game-Changer in Functional Programming Understanding Roc: Functional and separate from the runtime</a></li>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**Discussion**: Community comments debated whether safety concerns are overstated for compiler development, with some questioning Zig's runtime checks and others praising incremental builds. Users expressed mixed feelings about trading Rust's safety for Zig's speed.

**Tags**: `#Rust`, `#Zig`, `#compiler`, `#Roc`, `#programming languages`

---

<a id="item-6"></a>
## [Thinking Machines Lab Releases Inkling Open-Weights Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Thinking Machines Lab released Inkling, a 975B parameter open-weights Mixture-of-Experts multimodal model under Apache 2.0 license, trained on 45 trillion tokens of text, images, audio, and video. This release adds a strong open-weights contender to the US ecosystem, competing with Chinese open models, and offers a competitive base for fine-tuning, promoting accessibility and customization in AI research. Inkling has 975B total parameters with 41B active per token, uses Mixture-of-Experts architecture, and is multimodal (text, images, audio, video). A smaller Inkling-Small (276B, 12B active) is still being tested.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that splits computation across multiple specialized sub-networks (experts), activating only a subset per input, enabling larger models with lower computational cost. Open-weights models allow anyone to download and fine-tune the model weights, fostering transparency and community-driven development. Inkling targets the gap between frontier closed models and smaller open models by providing a capable base for customization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**Tags**: `#open-weights`, `#mixture-of-experts`, `#multimodal`, `#AI model`, `#Thinking Machines Lab`

---

<a id="item-7"></a>
## [Linus Torvalds Declares Linux Is Not Anti-AI](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds, the creator and top maintainer of Linux, has publicly stated that Linux is not an anti-AI project and that AI is a clearly useful tool, urging dissenters to fork the project or leave. This authoritative statement from the most influential figure in the Linux kernel community could shift the balance in the ongoing debate about AI's role in open-source development, potentially encouraging wider adoption of AI tools in kernel development. Torvalds made the statement on the Linux Media Mailing List, emphasizing that while there are other questions about AI (like its economic implications), its usefulness is no longer in question. He expressed that anyone who doubts that hasn't actually used AI.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linus Torvalds is the creator and long-time maintainer of the Linux kernel, one of the most successful open-source projects. The kernel community has had debates about incorporating AI-generated code or AI tools, with some members expressing concerns about quality, licensing, and ethical issues. Torvalds' position as benevolent dictator gives his statements significant weight in guiding the project's direction.

**Tags**: `#linus-torvalds`, `#linux`, `#artificial-intelligence`, `#open-source`

---

<a id="item-8"></a>
## [QLoRA 2e-4 default learning rate is wrong for small datasets](https://www.reddit.com/r/MachineLearning/comments/1uy1z8b/the_qlora_2e4_default_is_wrong_under_10k_samples/) ⭐️ 8.0/10

A practitioner discovered that the widely adopted 2e-4 learning rate for QLoRA fine-tuning is suboptimal on datasets under 10k samples; lowering it to 1e-4 and increasing epochs significantly improved evaluation performance. Many tutorials and tools hardcode the 2e-4 default, leading practitioners to waste time blaming their data or model when the real issue is hyperparameter choice. This insight could save weeks of debugging for anyone fine-tuning on small custom datasets. The author reports that with 2e-4, the model overfits within one epoch on small data, while reducing to 1e-4 and training for 5 epochs produced the best evaluation results. They propose a rule: above 30k samples use 2e-4, below 10k start at 1e-4 or lower, and tune in between.

reddit · r/MachineLearning · /u/Pretty-Ad774 · Jul 16, 12:50

**Background**: QLoRA (Quantized Low-Rank Adaptation) is a technique that combines quantization and LoRA to fine-tune large language models efficiently on consumer GPUs. The learning rate is a critical hyperparameter; too high can cause overfitting on small datasets. The default 2e-4 originates from the Alpaca dataset (52k samples) and has been blindly copied into many tutorials and codebases.

<details><summary>References</summary>
<ul>
<li><a href="https://unsloth.ai/docs">Unsloth Docs | Unsloth Documentation</a></li>
<li><a href="https://github.com/artidoro/qlora">GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub</a></li>
<li><a href="https://lightning.ai/pages/community/lora-insights/">Finetuning LLMs with LoRA and QLoRA: Insights from Hundreds of Experiments - Lightning AI</a></li>

</ul>
</details>

**Tags**: `#QLoRA`, `#fine-tuning`, `#learning rate`, `#small datasets`, `#machine learning`

---

<a id="item-9"></a>
## [ExTernD: Ternary Decomposition for Accurate LLM Quantization](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

The paper proposes ExTernD, a post-training quantization method that decomposes a weight matrix into two ternary matrices and a diagonal scaling matrix, enabling arbitrarily high accuracy by increasing rank while only slightly increasing VRAM usage. This approach addresses a fundamental limitation of ternary quantization—accuracy loss—by expanding the rank without significantly increasing memory, potentially enabling highly efficient LLM inference with near-lossless accuracy. ExTernD uses two ternary matrices and an inner diagonal scaling matrix, where the inner rank can be arbitrarily large to match target accuracy; empirical results show only slightly more VRAM than standard quantization methods.

reddit · r/MachineLearning · /u/LMTLS5 · Jul 16, 13:31

**Background**: Post-training quantization (PTQ) reduces model size and speeds up inference by converting weights from floating-point to lower-bit formats, such as ternary (values in {-1,0,1}). However, standard ternary quantization often causes significant accuracy degradation in large language models (LLMs). ExTernD overcomes this by decomposing the weight matrix and allowing flexible rank expansion.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2211.10438">[2211.10438] SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2407.11534">[2407.11534] LRQ: Optimizing Post-Training Quantization for Large Language Models by Learning Low-Rank Weight-Scaling Matrices</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Quantization`, `#Post-training quantization`, `#Model efficiency`

---

<a id="item-10"></a>
## [CNKI to Remove Papers Listing AI as Authors](https://www.zaobao.com.sg/news/china/story20260716-9371836) ⭐️ 8.0/10

CNKI, China's largest academic platform, announced it will remove papers that list AI tools such as DeepSeek and Gemini as authors, stating that AI cannot be held accountable for research integrity. This policy clarifies that AI cannot be credited as an author in academic publications, addressing growing concerns about accountability and integrity in research. It sets a precedent for other academic platforms and publishers worldwide. CNKI emphasized that AI lacks civil subject qualification and cannot assume responsibility for the authenticity, academic review, or accountability of papers. Authors who use AI in research or writing must disclose it in the methods or acknowledgments section.

telegram · zaihuapd · Jul 16, 07:45

**Background**: CNKI (China National Knowledge Infrastructure) is a major Chinese academic database hosting journals, theses, and conference papers. DeepSeek is a Chinese AI model that gained attention for its capabilities. The rise of generative AI has led to submissions where AI is listed as a co-author, prompting debates on authorship and ethics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CNKI">CNKI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI authorship`, `#academic publishing`, `#CNKI`, `#policy`, `#DeepSeek`

---

<a id="item-11"></a>
## [EU rules Google must open Android, search data to rivals](https://www.theverge.com/policy/966438/eu-google-android-ai-interoperability-search-data-dma) ⭐️ 8.0/10

The European Commission has decided that Google must open certain Android system features and Google Search data to qualified competitors under the Digital Markets Act (DMA). Third-party AI assistants like ChatGPT and Claude will gain system-level access and data privileges equivalent to Google's own Gemini. This ruling could dramatically reshape competition in mobile ecosystems and AI assistants by forcing Google to share its tightly controlled platform with rivals. It sets a precedent for how gatekeeper platforms under the DMA must enable interoperability for emerging AI services. Google may still assess requests against privacy and security criteria, but any restrictions must comply with EU regulations. The decision applies only to Android and Google Search, not other Google services, and is based on the DMA's interoperability obligations for gatekeepers.

telegram · zaihuapd · Jul 16, 13:19

**Background**: The Digital Markets Act (DMA) is an EU law targeting large online platforms designated as 'gatekeepers,' requiring them to ensure fair and open digital markets. Google (Alphabet) was designated a gatekeeper in September 2023 for services including Android and Search. The DMA mandates that gatekeepers allow third parties to interoperate with their core platform services under certain conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_Markets_Act">Digital Markets Act - Wikipedia</a></li>
<li><a href="https://digital-markets-act.ec.europa.eu/index_en">Digital Markets Act (DMA) - European Union</a></li>

</ul>
</details>

**Tags**: `#欧盟`, `#数字市场法`, `#谷歌`, `#Android`, `#AI助手`

---

<a id="item-12"></a>
## [1Password Integrates Claude for Password-Free AI Login](https://9to5mac.com/2026/07/16/1password-now-lets-claude-sign-in-to-websites-without-seeing-your-passwords/) ⭐️ 8.0/10

1Password has launched an integration with Claude on Mac, allowing the AI agent to log into websites on behalf of users without ever accessing passwords or 2FA codes. Credentials are injected directly into web pages via a secure channel, and user approval is required per session via biometric authentication. This integration combines password management with AI automation while preserving strong privacy guarantees, as credentials never enter Claude's context or memory. It could streamline workflows for users who need to automate repeated logins, such as testing or data entry, without compromising security. The feature is currently available for Mac users of 1Password business, family, and personal plans, requiring both the 1Password and Claude desktop and browser extensions. If auto-fill submission fails, filled credentials are immediately erased, and permissions are limited to the current session.

telegram · zaihuapd · Jul 16, 15:54

**Background**: 1Password is a popular password manager that stores login credentials and other sensitive data in an encrypted vault. Claude is an AI assistant developed by Anthropic. The integration allows Claude to act as an agent to perform logins on behalf of the user, but with a secure channel that ensures the AI never sees the actual passwords or 2FA codes, addressing a common privacy concern with AI agents accessing sensitive data.

**Tags**: `#password management`, `#AI integration`, `#security`, `#Claude`, `#1Password`

---

<a id="item-13"></a>
## [Truth Social to Sell Fast Access to Trump Posts to Wall Street](https://www.cnn.com/2026/07/16/business/truth-social-data-wall-street) ⭐️ 8.0/10

Trump Media & Technology Group announced the launch of Truth API, a data service providing millisecond-latency access to real-time posts from the top 10 accounts on Truth Social, available to institutional investors starting August 1, 2026. This service could give high-frequency traders an information advantage, as Trump's posts have historically moved markets on issues like tariffs and Iran, raising ethical concerns about monetizing presidential communications for financial gain. The API targets institutional financial clients but pricing has not been disclosed; it offers access only to the top 10 accounts, and TMTG frames it as a high-margin recurring revenue stream from its proprietary data.

telegram · zaihuapd · Jul 17, 01:02

**Background**: Truth Social has become Trump's primary channel for policy announcements, with his posts on tariffs, Iran, and the Strait of Hormuz previously triggering sharp movements in stock and oil markets. High-frequency trading (HFT) uses algorithms to execute trades in milliseconds, often profiting from tiny price changes. The combination of real-time access to market-moving posts and HFT could amplify volatility and raise fairness concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/16/trump-truth-social-wall-street-traders-api.html">Truth Social launches service to give Wall Street traders an ...</a></li>
<li><a href="https://marketchameleon.com/articles/b/2026/7/16/trump-media-launches-truth-api-institutional-market-impact">Trump Media Unveils Truth API: Real-Time Access to ...</a></li>

</ul>
</details>

**Tags**: `#Truth Social`, `#API`, `#Wall Street`, `#high-frequency trading`, `#ethics`

---