---
layout: default
title: "Horizon Summary: 2026-10-13 (EN)"
date: 2026-10-13
lang: en
---

> From 38 items, 6 important content pieces were selected

---

1. [Cyberattack Forces Defrosting in European Supermarket Fridges](#item-1) ⭐️ 8.0/10
2. [WiFi 7 Router Repurposed into a 320 Msps SDR Receiver](#item-2) ⭐️ 8.0/10
3. [Codex CLI silently installs a persistent, self-updating daemon by default](#item-3) ⭐️ 8.0/10
4. [Show HN: PS2 Games Statically Recompiled to WebAssembly](#item-4) ⭐️ 8.0/10
5. [Python 3.15 lands with explicit lazy imports under PEP 810](#item-5) ⭐️ 8.0/10
6. [learnc tunes named constants in unmodified C code to fit data](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cyberattack Forces Defrosting in European Supermarket Fridges](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

A cyberattack disabled refrigeration controllers at supermarket chains across Europe, including French retailer Intermarché, where roughly 150 stores were targeted around October 12, causing freezers to run automatic defrost cycles. The incident also disrupted in-store pricing systems and deliveries, according to reporting from Reuters, the BBC and Le Monde. It is a rare, publicly visible case of an attack on operational technology rather than IT, showing that internet-connected legacy refrigeration controllers in retail can be weaponized with immediate physical consequences such as food spoilage and supply disruption. It also suggests attackers may be reusing the same class of refrigeration exploits across multiple regions, including an August 2026 incident involving freezers at U.S. military facilities. Suspected entry points include end-of-support Danfoss controllers such as the SM800 (end of support 2021) and SC355 (end of support 2016), which Claroty's Team82 previously examined in research titled 'Freeze the Controller, Defrost the Food.' Notably, these devices are often internet-connected for legitimate reasons — remote defrost scheduling, diagnostics and fleet-wide efficiency benchmarking — so simply 'not connecting them' is rarely an option for operators.

hackernews · Zeekaas · Oct 12, 12:16 · [Discussion](https://news.ycombinator.com/item?id=50055304)

**Background**: Commercial refrigeration is managed by electronic case controllers that decide when compressors run and when the system performs a defrost cycle, briefly warming the evaporator coils to melt accumulated ice. In recent years vendors have pushed these controllers online so that service engineers can fix issues remotely and retailers can compare energy performance across hundreds of stores. Because many such controllers were designed 15–20 years ago, before OT security was a concern, they often ship with weak authentication, no firmware update path, and long past end-of-support dates — the classic 'legacy IoT' problem in brownfield industrial environments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.danfoss.com/en/products/dcs/electronic-controls/">Electronic controls - Danfoss</a></li>
<li><a href="https://iotdigitaltwinplm.com/brownfield-iot-legacy-machine-connectivity-playbook-2026/">Brownfield IoT : Legacy Machine Connectivity... - IoT Digital Twin PLM</a></li>
<li><a href="https://www.linkedin.com/advice/3/dealing-legacy-iot-devices-your-network-you-uekff">Secure Legacy IoT : Mitigate Network Risks</a></li>

</ul>
</details>

**Discussion**: Commenters on Hacker News largely agreed the root cause is economics rather than ignorance: controllers such as the Danfoss SM800 and SC355 have known CVEs but stores operate on razor-thin margins and shift-work IT staff with no budget for security reviews or hardware refresh cycles. Several pushed back on the reflexive 'why connect a freezer to the internet?' reaction, noting that subscription-locked lab and industrial equipment forces connectivity, and others speculated whether the attack is linked to the August 2026 U.S. military commissary freezer incident or a copycat.

**Tags**: `#cybersecurity`, `#iot`, `#industrial-control-systems`, `#supply-chain`, `#legacy-systems`

---

<a id="item-2"></a>
## [WiFi 7 Router Repurposed into a 320 Msps SDR Receiver](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 8.0/10

A GitHub project called w1700k-sdr (github.com/h0m3us3r/w1700k-sdr) shows how to repurpose the chipset inside a WiFi 7 router into a software-defined radio receiver that samples at 320 Msps in the 5 GHz band. The same developer had previously built eSpDR, an SDR built on an ESP32 Wi-Fi microcontroller. It suggests that cheap, mass-produced consumer networking hardware can serve as a high-sample-rate SDR front end, which is far cheaper than dedicated SDR equipment capable of comparable rates. If the technique generalizes to other Wi-Fi cards, ordinary laptops and routers could become budget instruments for RF experimentation, spectrum monitoring and research. Because the 320 Msps figure is roughly double the width of the band of interest, it corresponds to a wide instantaneous capture bandwidth, but the project is a receiver only — no transmit capability is claimed. A commenter notes the same chipset is used in the Banana Pi R4, suggesting the approach may work on that board as well.

hackernews · djfergus · Oct 12, 12:41 · [Discussion](https://news.ycombinator.com/item?id=50055593)

**Background**: A software-defined radio (SDR) is a radio system in which functions traditionally implemented in analog hardware — mixers, filters, amplifiers, modulators and demodulators — are instead performed in software on a general-purpose computer or embedded system, typically after an RF front end and analog-to-digital converter. This lets one device receive many different radio protocols simply by changing the software. WiFi 7, also known as IEEE 802.11be, is the seventh generation of Wi-Fi, built for extremely high throughput, and its chipsets contain fast analog front ends and digitizers operating in the 5 GHz and 6 GHz bands — the very components an SDR needs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software-defined radio</a></li>
<li><a href="https://www.tp-link.com/in/wifi7/">What is WiFi 7 ? What does WiFi 7 offer? | TP-Link WiFi 7 Router</a></li>

</ul>
</details>

**Discussion**: Commenters were enthusiastic, calling it possibly the cheapest way to get a 320 Msps receiver at 5 GHz and pointing to the developer's earlier ESP32-based eSpDR project as evidence that more Wi-Fi cards could be turned into SDRs. Others noted the Banana Pi R4 likely shares the same chipset, asked whether software-defined radios are why phone makers restrict third-party access to FM radios, and mused about combining such a receiver with attenuators, filters and mixers to build a cheap substitute for a service monitor.

**Tags**: `#SDR`, `#WiFi 7`, `#hardware hacking`, `#RF`, `#embedded systems`

---

<a id="item-3"></a>
## [Codex CLI silently installs a persistent, self-updating daemon by default](https://github.com/openai/codex/issues/48195) ⭐️ 8.0/10

A GitHub issue (openai/codex#48195) reports that OpenAI's Codex CLI ships a persistent background daemon that is enabled by default and updates itself automatically, and that there is no documented way for users to disable it. The report quickly drew a 480-point Hacker News thread with 244 comments, in which developers described concrete fallout such as multi-gigabyte stale version caches and auto-updates corrupting repository permissions. This matters to anyone running an AI coding agent in their terminal, because a hidden always-on process that silently pulls and swaps binaries expands the attack surface and the software supply chain footprint of a tool developers use on their own machines and inside corporate repositories. It also signals a broader shift in developer tooling toward heavyweight, self-managing background services, which raises questions about consent, transparency and enterprise policy compliance. Users report the daemon consumed roughly 12 GB of disk space in accumulated old versions, and that auto-updating would randomly make .git read-only and block their work in progress. A community workaround exists but is undocumented: setting `daemon_auto_start = false` under `[features]` in `~/.codex/config.toml`, and for the PID/lock files written to `~/.codex`, deleting them and replacing them with symlinks to `/dev/null` marked immutable with `chattr +i`.

hackernews · whimblepop · Oct 12, 18:29 · [Discussion](https://news.ycombinator.com/item?id=50060694)

**Background**: Codex CLI is OpenAI's lightweight coding agent that runs locally in the terminal; it was released on April 16, 2025 alongside the o3 and o4-mini reasoning models, and it is distinct from the older 2021 Codex language model that powered GitHub Copilot. A background daemon is a long-running process that keeps running after the main application exits, typically to handle updates, sessions or remote tasks; when combined with automatic self-updating, it means code can be fetched and executed without an explicit user action, which is why such behaviour is usually discussed in the context of software supply chain security.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Codex_CLI">Codex CLI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model)</a></li>
<li><a href="https://grokipedia.com/page/supply_chain_security">Supply chain security</a></li>

</ul>
</details>

**Discussion**: Sentiment is overwhelmingly negative but constructive: users call the daemon bloated and buggy, with one describing Codex as worse than Claude Code on every metric, while another notes Claude Code uses the same operational model of versioned binaries and background tasks. Others share practical mitigations (the feature flag, symlinking lock files to /dev/null with `chattr +i`), and several report switching to deliberately minimal harnesses such as hax that rely mostly on plain bash instead of an over-engineered agent.

**Tags**: `#ai-coding-agents`, `#codex-cli`, `#developer-tools`, `#privacy`, `#software-supply-chain`

---

<a id="item-4"></a>
## [Show HN: PS2 Games Statically Recompiled to WebAssembly](https://github.com/snuri00/ps2-web-recomp) ⭐️ 8.0/10

A developer published a Show HN project called ps2-web-recomp (github.com/snuri00/ps2-web-recomp) that statically recompiles PlayStation 2 games into WebAssembly so they can run directly inside a web browser. The post drew strong engagement, reaching 277 points and 145 comments on Hacker News. It shows static recompilation — a rapidly maturing technique — being pointed at a complex console like the PS2 and delivered through WebAssembly, which could make game preservation and browser-based play far more accessible. The discussion also surfaced parallel efforts, hinting that a small ecosystem of recompilation-to-WASM tooling is starting to form. Commenters pointed to a parallel project, cretz/vitaslop, which instead of individual games "builds" an ARM-to-WASM transpiler in WASM for the PS Vita and includes WebGPU shader and audio transcoding. Other suggestions included compiling the recompiler itself to WebAssembly so conversions could be done entirely from a browser, while one commenter raised the caveat that decompilation/recompilation projects lack the trust and vetting of the established emulator scene.

hackernews · deadxwarrior · Oct 12, 06:46 · [Discussion](https://news.ycombinator.com/item?id=50052251)

**Background**: Static recompilation is a form of binary translation in which machine code for one instruction set architecture is translated ahead of time into code for another target, rather than being interpreted instruction-by-instruction at runtime as an emulator does; well-known examples include N64Recomp for Nintendo 64 binaries. WebAssembly (Wasm) is a portable, W3C-standardized binary format that runs at near-native speed in browsers and other hosts, making it a natural target for such translated code. Together they let a console binary be converted once and then executed anywhere a Wasm runtime exists, such as a web page.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Static_recompilation">Static recompilation</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://github.com/N64Recomp/N64Recomp">GitHub - N64Recomp/N64Recomp: Tool to statically recompile ...</a></li>

</ul>
</details>

**Discussion**: The overall sentiment is enthusiastic admiration for the engineering, tempered by a notable trust-and-safety concern that decomp/recomp projects lack the vetting of the emulator scene and could hide malware. Discussion added value through a directly comparable PS Vita ARM-to-WASM project, a proposal to run the recompiler itself in the browser, and a lighthearted jab about Gran Turismo's loading screens.

**Tags**: `#WebAssembly`, `#Static Recompilation`, `#Game Emulation`, `#Reverse Engineering`, `#Show HN`

---

<a id="item-5"></a>
## [Python 3.15 lands with explicit lazy imports under PEP 810](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 has been released, and Simon Willison highlights two headline additions: PEP 810 explicit lazy imports, written as `lazy import json` or `lazy from pathlib import Path`, and PEP 798 unpacking in comprehensions such as `[*L for L in lists]`. He also notes that with Python 3.10 now past support he can drop it from his projects and finally start using features introduced back in Python 3.11. Lazy imports attack a long-standing pain point: Python imports modules eagerly at the top of a file, so installing a plugin with heavy dependencies can add multiple seconds to the startup of every command. Benchmarks cited for the feature show app startup dropping from about 104 ms with normal imports to roughly 36 ms with everything lazy, a nearly 3x speedup, and because Python underpins so much tooling and infrastructure, a new major version affects essentially the entire ecosystem. PEP 810 is the second attempt at lazy imports in CPython: PEP 690 proposed global, implicit lazy imports in 2022 and was withdrawn in 2023 over concerns about complexity and unpredictability, so the explicit, opt-in design is what finally got it approved, and the module is only imported the first time one of its symbols is actually used. PEP 798 extends the unpacking syntax that came from PEP 448 and shipped in Python 3.5, and Willison had previously had to tell LLM plugin authors to hand-roll lazy imports to avoid heavy dependencies such as `sentence_transformers` slowing the `llm` command.

rss · Simon Willison · Oct 12, 18:15

**Background**: Python ships a new feature release every October and supports each version for about five years, split into a bug-fix phase and a security-only phase, which is why 3.10 reaching end of life pushed Willison to drop it. A PEP, or Python Enhancement Proposal, is the document format used to propose and debate language changes; PEP 810 defines the syntax and semantics of explicit lazy imports, in contrast with Python's normal eager imports that load a module the moment the import statement runs. Lazy imports defer that loading until the imported name is first used, trading a small amount of indirection for faster startup and lower memory use in programs that import far more modules than any single run actually needs.

<details><summary>References</summary>
<ul>
<li><a href="https://peps.python.org/pep-0810/">PEP 810 – Explicit lazy imports | peps . python .org</a></li>
<li><a href="https://socket.dev/blog/pep-810-proposes-explicit-lazy-imports-for-python-3-15">PEP 810 Proposes Explicit Lazy Imports for Python 3.15 - Soc...</a></li>
<li><a href="https://realpython.com/python315-lazy-imports/">Python 3.15 Preview: Lazy Imports – Real Python</a></li>

</ul>
</details>

**Tags**: `#python`, `#python-3.15`, `#pep-810`, `#lazy-imports`, `#programming-languages`

---

<a id="item-6"></a>
## [learnc tunes named constants in unmodified C code to fit data](https://www.reddit.com/r/MachineLearning/comments/1x4dlbm/learnc_fit_the_constants_in_existing_c_code_to/) ⭐️ 8.0/10

A new MIT-licensed tool called learnc automatically fits named constants inside unmodified C source files against a score function written by the user, then writes the same file back with updated values. On held-out data it delivered a 9.1% BD-rate improvement at equal SSIM for stb_image_write.h's 128-entry JPEG quantization tables (versus 2.7% for mozjpeg's tables), and raised Google's WebRTC VAD F1 from 0.810 to 0.859 on the LibriParty eval set. This offers a generic, code-agnostic optimization loop: any C codebase with tunable constants and a measurable objective can be improved without rewriting the algorithm or introducing new dependencies. It is particularly valuable for systems and signal-processing engineers who rely on hand-tuned heuristics, and the result on JPEG quantization tables suggests it can rediscover or beat design choices made by mature, expert-tuned projects like mozjpeg. The JPEG experiment tuned 128 quantization-table constants on 12 Kodak images and tested on the other 12, with the gain checked independently in libjpeg using scikit-image; the VAD experiment tuned every constant in vad_core.c on LibriParty dev and reported results on the eval split. The authors note limits: there is no JPEG gain below 1 bpp, and the approach is best suited to tens or hundreds of constants rather than large weight sets.

reddit · r/MachineLearning · /u/keep_up_sharma · Oct 12, 20:51

**Background**: BD-rate is a standard compression metric that expresses the average bitrate savings at equal quality, so 9.1% means the tuned tables need 9.1% fewer bits for the same SSIM. Quantization tables are the fixed integer tables inside JPEG encoders that determine how aggressively each frequency coefficient is discarded, and they are traditionally hand-tuned by experts. WebRTC VAD is a lightweight, low-latency voice activity detector used in real-time communication to classify audio frames as speech or silence, and its behavior is governed by hardcoded thresholds and constants; LibriParty is a speech dataset with background noise and music used to benchmark such detectors.

<details><summary>References</summary>
<ul>
<li><a href="https://deepwiki.com/wiseman/py-webrtcvad/5.3-webrtc-vad-algorithm">WebRTC VAD Algorithm | wiseman/py-webrtcvad | DeepWiki</a></li>
<li><a href="https://huggingface.co/speechbrain/vad-crdnn-libriparty">speechbrain/vad-crdnn- libriparty · Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2601.10373">Towards Efficient Low- rate Image Compression with...</a></li>

</ul>
</details>

**Tags**: `#optimization`, `#C`, `#tooling`, `#JPEG`, `#WebRTC-VAD`

---