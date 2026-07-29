---
layout: default
title: "Horizon Summary: 2026-07-29 (EN)"
date: 2026-07-29
lang: en
---

> From 43 items, 9 important content pieces were selected

---

1. [Open-source engine runs Gemma 4 26B in 2GB RAM on M-series Mac](#item-1) ⭐️ 9.0/10
2. [Self-Replicating AI Worm Attacks Microsoft Word via Copilot](#item-2) ⭐️ 9.0/10
3. [Moonshot AI raises $3.5B at $35B valuation on Kimi K3 breakthrough](#item-3) ⭐️ 9.0/10
4. [Mitchell Hashimoto Launches Superlogical on Open Source libghostty](#item-4) ⭐️ 8.0/10
5. [Handbook.md Study Finds Long Policies Fail to Govern AI Agents](#item-5) ⭐️ 8.0/10
6. [AI's Perfect Moment for Cryptanalysis: Matthew Green](#item-6) ⭐️ 8.0/10
7. [Discovering cryptographic weaknesses with Claude](#item-7) ⭐️ 8.0/10
8. [Russia charges Telegram founder Durov with aiding terrorism, issues international warrant](#item-8) ⭐️ 8.0/10
9. [Hugging Face widely used for deepfake nude images, report finds](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Open-source engine runs Gemma 4 26B in 2GB RAM on M-series Mac](https://github.com/drumih/turbo-fieldfare) ⭐️ 9.0/10

TurboFieldfare, an open-source inference engine written in Swift and Metal, streams routed experts from SSD to run the 4-bit quantized Gemma 4 26B-A4B-IT model in approximately 2GB of RAM on any M-series Mac. This breakthrough enables running a 26B-parameter Mixture-of-Experts model on low-memory Macs (8GB or 16GB) that previously could not fit the model, democratizing on-device AI capabilities without expensive hardware upgrades. The engine achieves 5–6 tok/s on an 8GB M2 MacBook Air and 31–35 tok/s on an M5 MacBook Pro, using a small expert cache and bounded parallel pread to overlap SSD reads with GPU computation. It also includes an experimental OpenAI-compatible local server with streaming and tool calls.

hackernews · gitpusher42 · Jul 29, 15:05 · [Discussion](https://news.ycombinator.com/item?id=49098510)

**Background**: Mixture-of-Experts (MoE) models like Gemma 4 use a sparse architecture where only a subset of 'experts' are activated per token, reducing computation. The model's 4-bit quantized weights occupy about 14GB, but conventional inference requires loading all weights into RAM. TurboFieldfare keeps only the shared layers and KV cache (which stores prior attention keys/values) in RAM, while streaming the needed experts from SSD on demand.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2202.09368">[2202.09368] Mixture-of-Experts with Expert Choice Routing Intro to Routing: Mixture-of-Experts and Expert Choice [2510.04694] Multilingual Routing in Mixture-of-Experts Mixture-of-Experts with Expert Choice Routing - NeurIPS Mixture-of-Experts with Expert Choice Routing - Google Research Top-K Routing: Expert Selection in Mixture of Experts Models Parameter-Efficient Routed Fine-Tuning: Mixture-of-Experts ...</a></li>
<li><a href="https://huggingface.co/blog/not-lain/kv-caching">KV Caching Explained: Optimizing Transformer Inference Efficiency</a></li>
<li><a href="https://www.emergentmind.com/topics/4-bit-model-quantization">4-Bit Model Quantization</a></li>

</ul>
</details>

**Discussion**: Community members were impressed by the engineering feat, with some noting parallels to mmap-based approaches in llama.cpp. A user shared a compilation tweak for older macOS versions, and another asked about running on non-Mac platforms like Jetson. Overall sentiment was positive, praising the practical on-device AI advancement.

**Tags**: `#inference engine`, `#on-device AI`, `#Gemma 4`, `#model compression`, `#Swift/Metal`

---

<a id="item-2"></a>
## [Self-Replicating AI Worm Attacks Microsoft Word via Copilot](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 9.0/10

Security researcher Håkon Måløy discovered a prompt injection variant where hidden instructions in Word documents cause Microsoft Copilot to propagate the attack to new documents, forming a self-replicating worm. The technique was responsibly disclosed to Microsoft over 144 days ago, but no full mitigation exists yet. This marks the first demonstration of a self-replicating worm leveraging AI-powered document assistants, posing a significant security threat to enterprise environments that widely deploy Copilot in Office. It highlights the fundamental vulnerability of LLMs to confuse instructions with data, potentially leading to large-scale data exfiltration and malware propagation. The attack exploits Copilot's inability to distinguish between user prompts and content within documents; hidden instructions (e.g., white-on-white text) are interpreted as commands, causing Copilot to modify documents and copy the instructions into new files, enabling worm-like propagation. The attack class remains unmitigated because current AI architectures inherently mix instructions with data.

rss · Simon Willison · Jul 29, 18:43

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs cause LLMs to behave unintendedly, often by tricking the model into ignoring its original instructions. Traditional prompt injection attacks require user interaction, but this new variant adds self-replication, turning it into a worm. Previous research on AI worms by IBM and the University of Toronto demonstrated similar capabilities in generative AI systems, but this is the first to target Microsoft Word's Copilot integration specifically.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://www.ibm.com/think/insights/malicious-ai-worm-targeting-generative-ai">Researchers develop malicious AI ‘worm’ targeting generative AI systems | IBM</a></li>
<li><a href="https://www.utoronto.ca/news/u-t-researchers-demonstrate-ai-worm-could-target-any-online-device">U of T researchers demonstrate AI worm could target any online device | University of Toronto</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed deep concern that this class of attacks is fundamentally unfixable as long as AI cannot separate instructions from data. Some users reported uninstalling Copilot and disabling AI features locally. Others noted that similar obfuscation techniques like white text remain effective, demonstrating the difficulty of mitigation.

**Tags**: `#prompt injection`, `#security`, `#AI`, `#Microsoft Word`, `#worm`

---

<a id="item-3"></a>
## [Moonshot AI raises $3.5B at $35B valuation on Kimi K3 breakthrough](https://www.bloomberg.com/news/articles/2026-07-29/china-s-moonshot-ai-passes-funding-goal-to-hit-35-billion-value) ⭐️ 9.0/10

Moonshot AI completed a $3.5 billion funding round at a $35 billion post-money valuation, far exceeding its $1-2 billion target, driven by its breakthrough Kimi K3 model that rivals frontier AI systems from OpenAI and Anthropic. The massive funding and valuation signal that Chinese AI companies can produce world-class models that disrupt global markets, as the release of Kimi K3 triggered a tech stock selloff reminiscent of the 'DeepSeek moment' earlier in 2025. Kimi K3 has 2.8 trillion parameters and uses a hybrid linear attention mechanism called Kimi Delta Attention (KDA), with a 1M-token context window. Moonshot AI has already initiated a new funding round at a $50 billion pre-money valuation and plans an IPO in Hong Kong as early as this year.

telegram · zaihuapd · Jul 29, 10:12

**Background**: Moonshot AI is a Chinese AI startup that developed the Kimi chatbot and large language models. Its first version in 2023 was notable for supporting 128,000 tokens. The open-weights Kimi K2 was released in July 2025, and Kimi K3, the flagship model, was publicly released on July 16, 2026 with open-source weights promised. The term 'DeepSeek moment' was coined in early 2025 after DeepSeek's R1 model caused stock market turmoil, and Kimi K3's similar market impact revived that term.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and What the Open Weights Mean for the Community</a></li>

</ul>
</details>

**Tags**: `#AI`, `#funding`, `#Moonshot AI`, `#Kimi K3`, `#LLM`

---

<a id="item-4"></a>
## [Mitchell Hashimoto Launches Superlogical on Open Source libghostty](https://www.superlogical.com/) ⭐️ 8.0/10

Mitchell Hashimoto announced Superlogical, a new company that will build commercial terminal applications on top of the open source libghostty library, which he previously donated to a non-profit organization. This move demonstrates a sustainable open source business model where a company builds proprietary products on top of a community-owned foundation, ensuring the library remains free for all. It could inspire other developers to follow a similar path of donating core infrastructure to non-profits while commercializing higher-level applications. Superlogical will use libghostty exactly as any other consumer, under the MIT license, and plans to upstream shared terminal work for the benefit of the entire ecosystem. The library originated from Ghostty, a fast, GPU-accelerated terminal emulator also created by Hashimoto.

hackernews · yan · Jul 29, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49098965)

**Background**: Ghostty is a fast, feature-rich, cross-platform terminal emulator that uses platform-native UI and GPU acceleration. libghostty is the core library from Ghostty, handling VT sequence parsing, cursor management, and text reflow. Mitchell Hashimoto, known for creating HashiCorp and tools like Terraform, donated Ghostty to a non-profit before starting Superlogical.

<details><summary>References</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty-org/ghostty: 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.</a></li>

</ul>
</details>

**Discussion**: Community members praised the model of transferring ownership to a non-profit and building a company on that open source dependency, calling it a clean approach. Some compared the architecture to historical component technologies like OLE/COM, while others expressed frustration with the vague title, preferring more informative headlines.

**Tags**: `#open-source`, `#terminal`, `#business-model`, `#ghostty`, `#mitchell-hashimoto`

---

<a id="item-5"></a>
## [Handbook.md Study Finds Long Policies Fail to Govern AI Agents](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

A new arXiv study titled 'handbook.md' demonstrates that long policy documents do not reliably govern AI agents, exposing fundamental limitations in current long-context models and quantization techniques. This finding challenges the common assumption that AI agents can effectively follow lengthy policy instructions, with significant implications for deploying agents in regulated environments such as finance, healthcare, and legal compliance. The study highlights that extreme quantization of model KV caches and poorly designed inference samplers exacerbate the problem, and that even models with 1M token context windows fail in practice.

hackernews · spIrr · Jul 29, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49096969)

**Background**: Large language models (LLMs) have a limited context window that determines how many tokens they can process at once. To reduce memory and computational costs, models often use quantization, which lowers the precision of weights and activations. Long policy documents exceed effective context capacity, causing agents to 'forget' or misapply instructions. Techniques like RAG and memory buffering are proposed to work around these limits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/ai/what-is-quantization/">What is quantization in machine learning?</a></li>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>

</ul>
</details>

**Discussion**: The community discussion (275 points, 177 comments) largely agrees with the study's conclusions, with users noting that long context models overstate their capabilities. One user attributes failures to extreme quantization and poor samplers, advocating for local inference. Another draws a parallel to human limitations in following long policies.

**Tags**: `#AI agents`, `#long context`, `#policy compliance`, `#model limitations`, `#arXiv`

---

<a id="item-6"></a>
## [AI's Perfect Moment for Cryptanalysis: Matthew Green](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

Matthew Green notes that we are in the historic transition from traditional cryptography to post-quantum algorithms, and argues that this is the ideal time for AI to advance cryptanalysis. He references HAWK and other standards being considered, and the possibility that AI could either undermine or strengthen confidence in new hard problems. If AI can successfully break or validate post-quantum candidates, it will directly impact the security of future global encryption standards. This commentary is crucial for researchers and policymakers deciding which algorithms to adopt. Green specifically mentions HAWK, a lattice-based signature scheme in the NIST PQC standardization process, and references Impagliazzo's 'Minicrypt' world. He suggests that AI-driven cryptanalysis could produce a more robust literature, assuming it does not break all hard problems.

rss · Simon Willison · Jul 29, 18:18

**Background**: Post-quantum cryptography (PQC) aims to create encryption that resists attacks from quantum computers, which could break current RSA and ECC algorithms. NIST is leading standardization, with HAWK among the candidates. Impagliazzo's Five Worlds classify possible computational complexity scenarios; Minicrypt is a world where one-way functions exist but public-key cryptography is impossible. The transition to PQC is a massive global effort, making rigorous cryptanalysis urgent.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nist.gov/pqc">Post-quantum cryptography | NIST</a></li>
<li><a href="https://hawk-sign.info/">Hawk</a></li>
<li><a href="https://blog.computationalcomplexity.org/2004/06/impagliazzos-five-worlds.html">Computational Complexity: Impagliazzo 's Five Worlds</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#post-quantum`, `#AI`, `#cryptanalysis`, `#security`

---

<a id="item-7"></a>
## [Discovering cryptographic weaknesses with Claude](https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/#atom-everything) ⭐️ 8.0/10

Anthropic researchers used their Claude Mythos model to identify mathematical flaws in the HAWK post-quantum signature scheme and a reduced-round version of AES, with the work costing around $100,000 in API fees over 60 hours. This demonstrates that large language models can assist in high-level cryptographic research, potentially accelerating vulnerability discovery and reducing reliance on human intuition alone. It also introduces a new benchmark, CryptanalysisBench, for evaluating LLMs in cryptanalysis. The discovered weaknesses have no practical impact on current computer systems, but the researchers shared the exact prompts used, which included human guidance to push the model toward more ambitious findings. A related paper, 'CryptanalysisBench: Can LLMs do Cryptanalysis?', describes the evaluation framework created in collaboration with ETH Zurich, Tel Aviv University, and the University of Haifa.

rss · Simon Willison · Jul 28, 22:45

**Background**: Cryptographic hash functions are one-way mathematical operations used in digital signatures and password storage, with properties like preimage resistance and collision resistance. HAWK is a lattice-based digital signature scheme submitted to the NIST Post-Quantum Cryptography standardization process, designed to resist attacks from both classical and quantum computers. AES (Advanced Encryption Standard) is a symmetric block cipher with key sizes of 128, 192, or 256 bits, where the number of rounds varies (10 for AES-128); attacking reduced-round versions is a common research technique to understand cipher security margins.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">Advanced Encryption Standard - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hash_(cryptography)">Hash (cryptography)</a></li>
<li><a href="https://hawk-sign.info/">Hawk</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#AI`, `#Claude`, `#security`, `#research`

---

<a id="item-8"></a>
## [Russia charges Telegram founder Durov with aiding terrorism, issues international warrant](https://www.interfax.ru/russia/1106228) ⭐️ 8.0/10

Russia's Federal Security Service (FSB) has filed criminal charges against Telegram founder Pavel Durov under Article 205.1, Part 1.1 of the Criminal Code for aiding terrorist activities, and placed him on an international wanted list. This marks a significant escalation in Russia's legal pressure on a major tech platform, raising concerns about free speech and platform liability. It could set a precedent for how governments target tech leaders for content moderation decisions. The FSB alleges Telegram's management refused to delete channels and bots used by Ukrainian intelligence and terrorist groups to coordinate attacks, resulting in casualties and billions of rubles in damages. Durov is charged under a specific anti-terrorism provision.

telegram · zaihuapd · Jul 29, 05:56

**Background**: Telegram is an encrypted messaging app founded by Pavel Durov, who left Russia in 2014 after disputes over user data. The platform has faced tensions with Russian authorities over encryption and content moderation. Article 205.1 deals with aiding terrorist activities, carrying severe penalties.

**Tags**: `#Telegram`, `#Pavel Durov`, `#Russia`, `#terrorism`, `#legal`

---

<a id="item-9"></a>
## [Hugging Face widely used for deepfake nude images, report finds](https://www.theverge.com/ai-artificial-intelligence/971723/hugging-face-nudify-deepfake-undress-women-children) ⭐️ 8.0/10

AI Forensics, a European nonprofit, released a report on July 28 revealing that seven of the top nine image-editing models on Hugging Face can easily generate non-consensual deepfake nude images, including of children. The researchers set up a honeypot that received over 1,000 requests in seven days, 73% of which were sexually explicit and nearly 7% targeted minors. This exposes critical security gaps in open-source AI platforms regarding content safety and model misuse, raising urgent ethical and legal concerns. The findings highlight platform responsibility and could impact the safety and privacy of women and children. The report states that Hugging Face has almost no platform-level safeguards, contradicting its own policy against non-consensual content and child nudity. AI Forensics recommends implementing prompt filtering and output scanning mechanisms to block harmful image generation.

telegram · zaihuapd · Jul 29, 08:20

**Background**: Hugging Face is a popular open-source platform for hosting and sharing machine learning models. Deepfake technology uses AI to create realistic but fake images or videos. A honeypot is a cybersecurity tool that lures attackers to monitor their behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://juejin.cn/post/7642531705475776546">网 络 安 全 蜜 罐 管理系统（ HoneyPot ...</a></li>
<li><a href="https://yeasy.gitbook.io/agentic_ai_guide/di-si-bu-fen-wei-lai-zhan-wang/11_future/11.1_security">11.1 安全边界：提示词注入与防御策略 | 智能体AI 权威指南 | Agentic AI Guide</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#deepfake`, `#Hugging Face`, `#content moderation`, `#platform safety`

---