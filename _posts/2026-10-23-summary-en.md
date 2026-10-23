---
layout: default
title: "Horizon Summary: 2026-10-23 (EN)"
date: 2026-10-23
lang: en
---

> From 44 items, 12 important content pieces were selected

---

1. [Switch 2 jailbroken with AI-agent KVM and Bluetooth switch rig](#item-1) ⭐️ 9.0/10
2. [Quad9 to Exit France After Contempt Fine Over DNS Blocking](#item-2) ⭐️ 8.0/10
3. [NVIDIA OpenShell: a Sandboxed Runtime for Fleets of AI Agents](#item-3) ⭐️ 8.0/10
4. [GNU Taler Prepares to Launch Operations in Germany](#item-4) ⭐️ 8.0/10
5. [eMudhra Exits Global SSL/TLS Certificate Business After Weak Keys Cracked](#item-5) ⭐️ 8.0/10
6. [New triangulator cuts 3.7M map polygons in 489 ms, beating Earcut](#item-6) ⭐️ 8.0/10
7. [WorldTUI: a 360M model fine-tuned to simulate a terminal UI](#item-7) ⭐️ 8.0/10
8. [Anthropic Donates Agent Skills Standard to Linux Foundation's AAIF](#item-8) ⭐️ 8.0/10
9. [Australian court orders Apple to open iPhone to third-party app stores](#item-9) ⭐️ 8.0/10
10. [Study: Smart TVs Keep Reporting Viewing Data After ACR Is Turned Off](#item-10) ⭐️ 8.0/10
11. [333 Backdoored Tor Exit Relays Taken Offline After Ebury Infection](#item-11) ⭐️ 8.0/10
12. [Banned Nvidia B300 Servers Surface in Chinese State-Linked Network, Filings Redacted](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Switch 2 jailbroken with AI-agent KVM and Bluetooth switch rig](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/) ⭐️ 9.0/10

A detailed public write-up documents a jailbreak of the Nintendo Switch 2 and an unusual AI-agent-driven test harness: JetKVM units send controller input over USB and capture HDMI video, while a Bluetooth smart switch physically presses the power button to recover crashed consoles. A jailbreak for a current-generation console could enable homebrew, modding, game dumping and emulation/recompilation, putting pressure on Nintendo's hardware and legal controls; the KVM-plus-agent pattern also gives security researchers a reusable way to automate closed devices that offer no debug interface. JetKVM is an open-source remote KVM device that provides USB HID input and HDMI capture, and the write-up uses a SwitchBot Bot-style Bluetooth switch to press the power button because a crashed Switch 2 needs a physical press to restart. The setup is notable for closing the loop—agent sees the screen, sends inputs, and resets hardware—but coverage notes this is not yet a commonplace piracy method and Nintendo can still patch the underlying exploit.

hackernews · ledoge · Oct 22, 08:01 · [Discussion](https://news.ycombinator.com/item?id=50192536)

**Background**: The Nintendo Switch 2 is Nintendo's current-generation console and successor to the Switch. Jailbreaking means bypassing its security to run unsigned code, which can enable homebrew but also piracy. JetKVM is an open-source KVM (keyboard, video, mouse) over IP device that lets a remote user control a computer at the hardware level, including USB input and HDMI capture. LLM-based agents can use such interfaces to observe a screen and take actions, making them useful for automated hardware testing and security research.

<details><summary>References</summary>
<ul>
<li><a href="https://jetkvm.com/">JetKVM - Control any computer remotely</a></li>
<li><a href="https://github.com/jetkvm/kvm">GitHub - jetkvm / kvm : Control any computer remotely · GitHub</a></li>
<li><a href="https://kotaku.com/nintendo-switch-2-jailbreak-hack-exploit-piracy-homebrew-emulation-modding-2000748784">The Switch 2 Has Been Jailbroken For The First Time</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed and focused on the implications: if the filesystem is decrypted read/write, Switch 2 game dumps and recomps/decomps could soon bring console exclusives to arbitrary hardware. They also enjoyed the 'Switch SwitchBot Bot' power-button rig and criticized LLM guardrails that block legitimate security research, while some noted the expert human did the real exploit work and the tooling mainly enabled automation.

**Tags**: `#security`, `#jailbreak`, `#hardware-hacking`, `#reverse-engineering`, `#llm-agents`

---

<a id="item-2"></a>
## [Quad9 to Exit France After Contempt Fine Over DNS Blocking](https://quad9.net/news/blog/au-revoir-france/) ⭐️ 8.0/10

Quad9, the Swiss non-profit public DNS resolver, announced it is withdrawing its service from France after a French court held it in contempt and fined it for failing to block infringing domains to Sony Music Entertainment's satisfaction. Quad9's CTO John Todd said the organization will likely apply geoIP filters to cut off French users after November 24, even though it has argued that geoIP filtering is technically inadequate for selectively denying resolution of specific names. The case exposes the legal untenability of DNS-level content blocking: a resolver can be fined for non-compliance even though the rightsholder itself defeated the geo-blocking measure with a VPN, a standard consumer tool. It also follows Cisco's earlier exit from the French market and sets a precedent that could push other public resolvers to abandon jurisdictions rather than implement court-ordered filtering, affecting internet users' access to a free, privacy-focused DNS service. The blocking order originated with Sony Music Entertainment GmbH, which used a VPN from Germany to reach content that Quad9 had geo-blocked, and the court then agreed with Sony that Quad9 was non-compliant. Quad9 notes the inherent conflict in its position — it must now geo-block all French users even while arguing geo-blocking is an ineffective mechanism for name-specific blocking — and its withdrawal is set to take effect around November 24.

hackernews · farrokhi · Oct 22, 14:32 · [Discussion](https://news.ycombinator.com/item?id=50195959)

**Background**: DNS is often described as the internet's phone book: it translates human-readable domain names into IP addresses so browsers can reach servers. Public recursive resolvers such as Quad9, Google Public DNS and Cloudflare's 1.1.1.1 answer these lookups for anyone who configures them, and they can also refuse to resolve known malware or court-ordered domains. Rights holders in France, notably Canal+, have won web-blocking injunctions against DNS operators including Google, Cloudflare and Cisco, and Cisco subsequently left the French market. Geo-blocking, which restricts access based on the IP address's presumed location, is widely known to be bypassable with VPNs and proxies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quad9">Quad9 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Geo-blocking">Geo-blocking</a></li>
<li><a href="https://quad9.net/">Quad9 | A public and free DNS service for a better security ...</a></li>

</ul>
</details>

**Discussion**: Commenters were overwhelmingly critical of the ruling, with several invoking the analogy of punishing a phone book company for listing a criminal's number, and one calling it absurd that a plaintiff can circumvent a protection with a VPN and then have the defendant fined for non-compliance. Quad9's CTO joined the thread to clarify that the company understands the apparent contradiction of geo-blocking French users while arguing geo-blocking is insufficient, and others drew parallels to Cisco's exit and to Canal+'s campaigns against Google, Cloudflare and Cisco. Some suggested DNS resolvers should retaliate by refusing to resolve domains belonging to the companies that sue them.

**Tags**: `#DNS`, `#internet censorship`, `#geo-blocking`, `#privacy`, `#policy/legal`

---

<a id="item-3"></a>
## [NVIDIA OpenShell: a Sandboxed Runtime for Fleets of AI Agents](https://github.com/NVIDIA/OpenShell) ⭐️ 8.0/10

NVIDIA released OpenShell, an open-source, secure-by-design runtime that executes autonomous AI agents inside kernel-level sandboxes governed by declarative policy, with capability controls over filesystem access, network egress and credentials. Announced at GTC San Jose 2026, it also governs where agent inference is routed, positioning it as infrastructure-level rather than prompt-level security. Agents are only useful when they can read files, install packages, call APIs and use credentials, but those same permissions make them a data-exfiltration vector, so a vendor-backed, policy-driven sandbox could become a standard building block for teams deploying agents at scale. NVIDIA entering this space signals that agent runtime security is becoming a platform layer rather than something每个团队自己拼凑. The controls are enforced at the kernel/sandbox level with declarative policies rather than relying on prompt-level guardrails, which matters because prompt injection defenses alone routinely fail against tool-using agents. The open question raised by commenters is that domain-based network allowlisting still leaves exfiltration paths open when a trusted destination is itself compromised or when data is smuggled through permitted API calls.

hackernews · niemandhier · Oct 22, 17:44 · [Discussion](https://news.ycombinator.com/item?id=50198675)

**Background**: Autonomous agents are LLM-driven programs that loop through planning, tool calls and observation, so they need real permissions on a machine: reading a codebase, running package installs, hitting external APIs and holding API keys. Sandboxing and capability control are the standard mitigations — restricting what an agent can touch and where its traffic can go — but balancing capability against containment is an unsolved trade-off, and prompt injection plus credential abuse remain the leading attack paths for agentic systems in 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/ai/openshell/">NVIDIA OpenShell | Open, Secure Runtime for AI Agents</a></li>
<li><a href="https://perspectives.nvidia.com/nvidia-openshell/">OpenShell</a></li>
<li><a href="https://cryptobriefing.com/nvidia-openshell-ai-agent-security/">Nvidia launches OpenShell , an open-source runtime for securing...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters broadly welcomed the tooling but pushed back on the marketing: 'smallnix' called the claim of maximal access plus maximal safety an oxymoron, arguing you can only strike a balance. One user shared that iron proxy already covers domain-based network restrictions and credential swapping, yet still cannot stop codebase exfiltration of the kind seen in the Hugging Face incident, while others said containerizing agents is already table stakes and OpenShell looks like a good way to manage those containers.

**Tags**: `#ai-agents`, `#sandboxing`, `#security`, `#nvidia`, `#agent-runtime`

---

<a id="item-4"></a>
## [GNU Taler Prepares to Launch Operations in Germany](https://www.taler.net/en/news/2026-13.html) ⭐️ 8.0/10

GNU Taler, the open-source privacy-preserving electronic payment system, has announced that it is getting ready to operate in Germany, moving from a research project toward a real-world deployment with German partners. The announcement states that Taler will be operated by a German entity, with GLS Bank among the participating institutions. If it succeeds, Taler would offer Europeans a privacy-preserving, non-blockchain alternative for digital payments that does not depend on US payment giants, a long-standing goal for EU digital sovereignty. Its launch also puts it in direct competition with Wero, the bank-backed European payment scheme being rolled out by major banks. Taler e-money is issued with a validity period, so wallets must periodically exchange expiring digital cash online before the coins lapse, which makes prolonged offline use impractical; Taler is explicitly designed as an online payment system, with offline support only explored as a research design document. The system relies on blind signatures so merchants learn who paid while the bank or issuer cannot link payments to individuals, and like any regulated e-money service it remains subject to KYC requirements.

hackernews · dewey · Oct 22, 16:14 · [Discussion](https://news.ycombinator.com/item?id=50197404)

**Background**: GNU Taler is a free-software electronic payment system that, unlike Bitcoin and most cryptocurrencies, does not use a blockchain; instead it uses cryptographic blind signatures issued by a bank or exchange to create digital cash. Its core privacy claim is asymmetric: the payer is anonymous to the issuer and the state, but the merchant is identified so that transactions remain auditable and tax-compliant. Wero is a separate European payment initiative backed by major banks and acquirers to replace national schemes like Giropay and iDEAL with a single bank-app-based transfer system across Europe.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.taler.net/design-documents/030-offline-payments.html">23.31. DD 30: Offline payments — GNU Taler</a></li>
<li><a href="https://wero-wallet.eu/about">Wero - All about Wero : Europe's mobile payment solution</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were broadly sympathetic to Taler's mission, with one GLS Bank customer praising it as a needed European alternative to US payment providers, but several raised sharp concerns: that expiring e-money requiring periodic online connection is worse than Bitcoin for offline use, that EU regulators will choke off meaningful privacy through KYC just as they did with crypto, and that competing against bank-backed Wero will be very hard.

**Tags**: `#GNU Taler`, `#digital payments`, `#privacy`, `#open source`, `#EU regulation`

---

<a id="item-5"></a>
## [eMudhra Exits Global SSL/TLS Certificate Business After Weak Keys Cracked](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business) ⭐️ 8.0/10

Indian certificate authority eMudhra announced that its board has decided to withdraw from its global SSL/TLS certificate business, roughly five days after a researcher disclosed that eight of its intermediate CA private keys had been cracked. The company framed the move as a business decision and argued that the social-media scrutiny was 'out of proportion to SSL/TLS's place in our business'. A publicly trusted certificate authority abandoning the global market is a rare and consequential event: website operators using eMudhra certificates must migrate to another CA, and browser root-store programs must decide whether to distrust or remove the company's roots. It also reinforces how severely a weak-key misissuance incident can damage trust in a CA, echoing past removals such as WoSign and Entrust. eMudhra insists that 'there were no end entity certificates issued out of the affected CA's' and that its global SSL/TLS infrastructure runs separately from its other operations, but it has not published a clear root-cause explanation. The cracked keys were reportedly so weak that one could be trivially factored — a detail that has become the focal point of ridicule and doubt online.

hackernews · bo0tzz · Oct 22, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50195110)

**Background**: A certificate authority issues digital certificates that vouch for a website's identity, and each certificate is signed with the CA's private key. Browsers and operating systems only accept certificates chained to roots in their trust stores, which are governed by root programs run by Mozilla, Google, Apple and Microsoft. An intermediate CA sits between a root and the leaf certificates websites use, so if an intermediate's signing key leaks, an attacker can mint certificates that vulnerable clients accept as genuine — which is why root-store maintainers demand detailed incident reports and can ultimately distrust a CA.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html">eMudhra to Exit Global SSL/TLS Business After 8 Intermediate CA...</a></li>
<li><a href="https://www.coindesk.com/tech/2026/10/21/a-company-that-vouches-for-websites-had-secret-keys-so-weak-that-8-of-them-were-cracked">Internet panics after 8 eMudhra private keys get cracked</a></li>
<li><a href="https://cybersecuritynews.com/emudhra-security-compromise/">eMudhra Certificate Authority Compromise Triggers Emergency...</a></li>

</ul>
</details>

**Discussion**: Commenters on the 900+ point Hacker News thread were highly critical: they mocked the triviality of the compromised keys with a fake PEM block reading 'BEGIN RSA PRIVATE KEY / 4', and faulted eMudhra for apologizing without ever explaining whether the failure was a human or process mistake. Others linked to the 'absolutely brutal question battery' the Chrome team filed publicly on Mozilla Bugzilla, and questioned the claim that no end-entity certificates were issued, given that anyone could have issued certificates from the affected CAs.

**Tags**: `#pki`, `#tls`, `#security`, `#certificate-authority`, `#incident-response`

---

<a id="item-6"></a>
## [New triangulator cuts 3.7M map polygons in 489 ms, beating Earcut](https://globus.software/blog/2026/10/16/cutting-map-polygons/) ⭐️ 8.0/10

A blog post by Evgen presents a polygon triangulation library — referred to in the discussion as Earstrip — that triangulates 3.7 million real-world map polygons in 489 ms, faster than the established baselines it was benchmarked against, including Mapbox's Earcut. The post publishes its datasets and comparisons so others can reproduce the numbers, and it drew immediate attention from the authors of Earcut and Delaunay32. Triangulation sits on the hot path of every vector map renderer, since polygons must be broken into triangles before the GPU can draw them, so cutting this cost changes how much geometry a browser can display per frame and how quickly tiles load. Because the two most relevant library authors showed up to compare notes, the result is likely to feed back into mainstream web mapping stacks rather than stay a one-off experiment. The benchmark runs over a large corpus of real map polygons and is compared against both an Earcut-style ear-clipping baseline and a Delaunay-based one, with the implementation built to WebAssembly for near-native speed. Open questions raised in the discussion include the size of the WASM binary versus Earcut's 4.1 kB min+gz footprint, and whether the many very small sliver triangles visible in the output cause rendering artifacts.

hackernews · molind · Oct 22, 09:31 · [Discussion](https://news.ycombinator.com/item?id=50193170)

**Background**: Polygon triangulation is the computational-geometry problem of partitioning a polygonal area into non-overlapping triangles, which is a prerequisite for filling shapes on a GPU, since graphics APIs only rasterize triangles. Mapbox's Earcut became the de facto standard for web maps by using ear clipping — repeatedly snipping off triangles from the polygon boundary — because it is small and fast enough for tiled map data. WebAssembly lets libraries written in C++, Rust or similar run in the browser at close to native speed, which is why it is increasingly used for compute-heavy geometry work.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mapbox/earcut">GitHub - mapbox/ earcut : The fastest and smallest JavaScript polygon ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polygon_triangulation">Polygon triangulation - Wikipedia</a></li>
<li><a href="https://dev.to/tianyaschool/combining-webassembly-with-webgl-high-performance-graphics-processing-322">Combining WebAssembly with WebGL High- Performance Graphics...</a></li>

</ul>
</details>

**Discussion**: The tone was strongly positive, with the Earcut author calling the library "really cool" while cautioning that he deliberately rejected some optimizations to keep Earcut's bundle small (4.1 kB min+gz) and asking how large the WASM build is. The Delaunay32 author asked how the approach compares with a divide-and-conquer constrained Delaunay triangulator, another commenter questioned whether the many tiny triangles hurt rendering, and a further thread asked why ear clipping beat Seidel's O(n log* n) trapezoidal method in practice — likely a triangle-quality and sliver-handling tradeoff.

**Tags**: `#triangulation`, `#computational-geometry`, `#performance-optimization`, `#webassembly`, `#maps-rendering`

---

<a id="item-7"></a>
## [WorldTUI: a 360M model fine-tuned to simulate a terminal UI](https://simedw.com/2026/10/21/world-model-terminal/) ⭐️ 8.0/10

Developer simedw published WorldTUI, a project in which a 360M-parameter model built on Qwen2.5-Coder-0.5B was fine-tuned to generate a fake terminal interface from user input in near-realtime. Rather than running real shell commands, the model predicts the next screen of terminal output, so the entire UI is produced generatively. The project is a compact, runnable demonstration of the idea that a user interface can be a learned world model rather than a hand-coded program, which commenters linked to research on "Neural Computers" where the OS exists only as a predict-next-frame loop. It also shows that a sub-billion-parameter fine-tune can produce convincing interactive behavior, lowering the cost of experimenting with generative interfaces. A small base model was chosen deliberately so generation could approach realtime speed, and Qwen2.5-Coder was picked because a coding model has already seen heavy CLI usage in its training data. The author published benchmarks comparing the fine-tune against the base model, and commenters were struck by how much fine-tuning improved memory behavior, not just surface formatting.

hackernews · alphax314 · Oct 22, 02:18 · [Discussion](https://news.ycombinator.com/item?id=50190363)

**Background**: A world model is a machine learning system that learns an internal representation of an environment and predicts how that environment changes in response to actions, instead of being explicitly programmed. Recent work applies the same idea to screens: a Generative UI is produced dynamically by a model rather than laid out by developers. Neural Computers extend this to the extreme, replacing a real operating system with a recurring loop of (user input) → (predicted pixels). WorldTUI scales this down to text-mode terminals running on a small fine-tuned LLM.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>
<li><a href="https://grokipedia.com/page/Generative_UI">Generative UI</a></li>
<li><a href="https://www.emergentmind.com/topics/neural-computers-ncs">Neural Computers : Unified Computation & Memory</a></li>

</ul>
</details>

**Discussion**: The discussion was enthusiastic: commenter gavinray described it as a micro-implementation of "Neural Computer" research and noted that a perfect neural computer would be indistinguishable from a real one, while nico shared a related "lossy git" project that stores code by training a neural network and regenerates it on checkout. andai asked how the fine-tune compares with the base model and was surprised that fine-tuning improved memory so significantly, and ponyous recalled an early ChatGPT demo where the model was told to "pretend to be a terminal." The author, simedw, joined the thread and offered to answer questions.

**Tags**: `#LLM fine-tuning`, `#world models`, `#generative UI`, `#terminal emulation`, `#neural computers`

---

<a id="item-8"></a>
## [Anthropic Donates Agent Skills Standard to Linux Foundation's AAIF](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) ⭐️ 8.0/10

Anthropic announced that it is donating its Agent Skills standard to the Agentic AI Foundation (AAIF), the Linux Foundation-backed body it co-founded with Block and OpenAI. The move follows Anthropic's earlier donation of the Model Context Protocol (MCP) to the same foundation. Transferring Agent Skills to vendor-neutral governance is meant to make the format more credible and broadly adoptable across competing AI vendors, reducing concerns that a single company controls how agents package and share capabilities. It affects developers building agent tooling, skill marketplaces, and cross-platform agent workflows. Agent Skills is described as a lightweight, open format for extending AI agents with specialized knowledge and workflows, and the AAIF was formed in December 2025 with founding contributions from Anthropic, Block, and OpenAI. The announcement concerns governance rather than a new technical version, and no changes to the skills specification itself were disclosed in the excerpt.

rss · Simon Willison · Oct 22, 18:09

**Background**: Agent Skills lets developers package instructions, scripts, and domain knowledge so an AI agent can perform specialized tasks, similar to reusable plugins for agents. MCP is a separate open protocol for connecting LLM applications to external tools and data sources, and Anthropic previously donated it to the AAIF. The AAIF is a Linux Foundation initiative intended to provide neutral, open governance for agentic AI standards.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation">Linux Foundation Announces the Formation of the Agentic AI ...</a></li>
<li><a href="https://aaif.io/">Agentic AI Foundation (AAIF) - Open Standards for Agentic AI</a></li>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>

</ul>
</details>

**Tags**: `#agent-skills`, `#ai-agents`, `#open-standards`, `#ai-governance`, `#anthropic`

---

<a id="item-9"></a>
## [Australian court orders Apple to open iPhone to third-party app stores](https://9to5mac.com/2026/10/21/apple-must-open-iphone-to-alternative-app-stores-in-australia-after-epic-games-ruling/) ⭐️ 8.0/10

Australia's Federal Court has ruled that Apple must let Australian iPhone users install apps from third-party app stores and websites, and must allow alternative payment methods and external payment links, starting March 1, 2027. Fortnite will also return to the Australian App Store immediately, and Apple says it will appeal the decision and seek a stay of enforcement. This is a landmark antitrust outcome that could reshape iOS app distribution well beyond Australia, giving developers a path around Apple's App Store commission and potentially encouraging similar rulings or legislation in other jurisdictions. It puts Australia in the same regulatory camp as the EU, whose Digital Markets Act already forces Apple to permit sideloading and alternative marketplaces. The court found Apple holds substantial market power in iOS app distribution and payments, and that its restrictions substantially lessened competition in breach of Australian competition law. Apple's planned appeal and stay request mean the March 1, 2027 deadline could still slip, and the ruling's exact technical scope—such as notarization or security requirements Apple may impose on sideloaded apps—has yet to be defined.

telegram · zaihuapd · Oct 22, 06:54

**Background**: The case stems from Epic Games' long-running antitrust fight with Apple, which began in 2020 when Epic added a direct payment option to Fortnite and Apple removed the game from the App Store. Apple has historically required all iOS apps to be distributed through its own App Store and to use its in-app purchase system, which takes a commission typically between 15% and 30%. Regulators worldwide, most notably the EU through the Digital Markets Act, have since challenged this model as anticompetitive gatekeeping.

**Tags**: `#antitrust`, `#apple`, `#app-store`, `#epic-games`, `#regulation`

---

<a id="item-10"></a>
## [Study: Smart TVs Keep Reporting Viewing Data After ACR Is Turned Off](https://watchingthewatchers.github.io/watchingthewatchers/index.html) ⭐️ 8.0/10

A study of automatic content recognition (ACR) on smart TVs tested 12 televisions from 10 manufacturers across 5,943 controlled experiments and found that some models still sent content-related traffic after ACR was disabled in settings. Two platforms transmitted viewing information in unencrypted form: VIDAA OS sent data over plaintext MQTT including a non-resettable device ID and audio fingerprints, while Vizio's WatchFree+ exposed program names in unencrypted domain queries that users cannot turn off. The findings show that opt-out controls advertised in smart TV privacy settings do not reliably stop viewing data collection, undermining a core assumption of consumer consent in the connected-TV market. Because ACR-derived data can reveal what people watch, when, and for how long, the gap affects anyone who owns a smart TV and assumes flipping a settings toggle ends the tracking. The experiment covered 12 TVs from 10 vendors and 5,943 controlled trials, making it a relatively large, systematic measurement rather than an anecdotal report. The VIDAA data flow is especially notable because the device identifier cannot be reset and the payloads carry audio fingerprints, while Vizio's leakage happens at the DNS layer through program names embedded in plaintext lookups rather than in the ACR toggle's scope.

telegram · zaihuapd · Oct 22, 09:50

**Background**: Automatic content recognition (ACR) is a technology built into most smart TVs that samples what appears on screen or in the audio track — from broadcasts, streaming apps, or even HDMI inputs — and matches it against a content database to identify what is being watched. Audio fingerprinting is the common mechanism: it generates a condensed digital summary of an audio signal that can be matched against known recordings. MQTT is a lightweight publish/subscribe messaging protocol widely used in IoT devices, and unless it is wrapped in TLS it transmits payloads in plaintext. Research like this matters because ACR opt-out settings are presented to consumers as a meaningful privacy control.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2026/10/does-opting-out-of-smart-tv-tracking-work-research-finds-suspicious-traffic/">Does opting out of smart TV tracking work? Research... - Ars Technica</a></li>
<li><a href="https://mqtt.org/">MQTT - The Standard for IoT Messaging</a></li>
<li><a href="https://en.wikipedia.org/wiki/Acoustic_fingerprint">Acoustic fingerprint - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#smart TV`, `#ACR`, `#IoT security`, `#data tracking`

---

<a id="item-11"></a>
## [333 Backdoored Tor Exit Relays Taken Offline After Ebury Infection](https://kaba.cx/posts/20261020_Tor/) ⭐️ 8.0/10

A Tor operator scripted a scan of roughly 3,000 exit relays and found 333 of them — about 10% of all exits — infected with the Ebury backdoor, which redirected SSH connections on port 22 to 12 interception servers to harvest credentials. The relays were flagged BadExit on October 4 and had all gone offline by the next day. Because exit relays are the point where Tor traffic re-enters the public internet, a 10% compromise rate means a substantial share of Tor users' SSH logins could have been silently captured, and anyone relying on Tor for anonymity around SSH or mail traffic should assume credentials may be exposed. It also shows how a single long-lived SSH backdoor family can quietly colonize a distributed volunteer-run network. The attackers appear to have compromised the servers in August, and they blocked certain ports so the relays would preferentially carry unencrypted email traffic for collection; the initial intrusion vector is still undetermined, and hijacked SSH connections would typically surface to users as an unexpected host key change.

telegram · zaihuapd · Oct 22, 14:52

**Background**: Tor routes traffic through three volunteer relays, and only the last one — the exit relay — touches the open internet, so a malicious exit can observe or tamper with anything not end-to-end encrypted. The Tor directory authorities can assign a relay the BadExit flag, which tells clients to stop building circuits that exit through it, effectively demoting it to a non-exit. Ebury is a Linux backdoor linked to the long-running Windigo operation; it infects SSH servers, hooks libc calls to hide itself, and has spread to hundreds of thousands of servers over more than a decade.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html">Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH ...</a></li>
<li><a href="https://archive.torproject.org/websites/support.torproject.org/relay-operators/what-is-the-bad-exit-flag/">What is the BadExit flag ? | Tor Project | Support</a></li>
<li><a href="https://arstechnica.com/security/2024/05/ssh-backdoor-has-infected-400000-linux-servers-over-15-years-and-keeps-on-spreading/">Linux maintainers were infected for 2 years by SSH-dwelling backdoor ...</a></li>

</ul>
</details>

**Tags**: `#Tor`, `#security incident`, `#Ebury malware`, `#backdoor`, `#SSH credential theft`

---

<a id="item-12"></a>
## [Banned Nvidia B300 Servers Surface in Chinese State-Linked Network, Filings Redacted](https://theinference.org/article/china-s-state-money-bought-banned-nvidia-b300-servers-then-redacted-the-receipts) ⭐️ 8.0/10

A Chinese state-controlled semiconductor leasing group reportedly financed the purchase of 32 ASUS servers equipped with embargoed Nvidia B300 chips for AI company Honor View Technology, as part of a larger deal of more than 700 servers worth over RMB 3 billion planned for a China Mobile facility in Ningxia. After the filing drew scrutiny, the leasing group resubmitted documents with the hardware descriptions removed, prompting Nvidia to say it is investigating with its manufacturing partners and ASUS to state that it complies with export controls. The case is direct evidence that top-tier, export-controlled AI accelerators may be reaching Chinese state-linked infrastructure, which would undercut US export controls at the very moment Washington is trying to keep advanced compute out of China. It also puts compliance pressure on the whole chain — Nvidia, server makers like ASUS, and the leasing and financing intermediaries that actually place the orders — and could trigger tighter scrutiny of who is allowed to buy high-end hardware. The B300 sits in the strictest tier of US export controls and is effectively banned for sale to China, and the redaction occurred only after the filing attracted attention, suggesting awareness of the sensitivity rather than a routine paperwork change. Nvidia said it is investigating together with its manufacturing partners, while ASUS said it abides by export-control rules; neither company confirmed how the chips reached the deal, and the servers are described as part of a much larger 700-plus unit, RMB 3-billion-plus procurement.

telegram · zaihuapd · Oct 22, 15:22

**Background**: Nvidia's data-center accelerators are subject to US Export Administration Regulations, and Nvidia publishes Export Control Classification Numbers (ECCNs) that determine whether a given part can be shipped to a country like China; products in the highest performance tiers require licenses that are generally denied. China Mobile's Ningxia hub in Zhongwei is one of China's flagship western computing clusters, promoted as a green-power and natural-cooling site for large data centers, which makes it a natural destination for large AI server purchases. Because such hardware is usually bought through intermediaries, leasing firms and financing partners can obscure the end user, which is exactly the gap this story points to.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/about-nvidia/company-policies/export-regulations/">NVIDIA Networking Export Regulation Compliance | NVIDIA</a></li>
<li><a href="https://en.qstheory.cn/2026-08/19/c_1206436.htm">China leverages green power to fuel computing boom</a></li>
<li><a href="https://www.datacentermap.com/china/zhongwei/china-mobile-ningxia/">China Mobile Ningxia Data Center in Zhongwei | Fengyun Road</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#export-controls`, `#AI-hardware`, `#China`, `#semiconductors`

---