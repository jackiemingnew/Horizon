---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03
lang: en
---

> From 42 items, 6 important content pieces were selected

---

1. [Astra reads and writes neural network weights, lifting Qwen math accuracy fivefold](#item-1) ⭐️ 9.0/10
2. [YC startup Subvocal unveils RF smart glasses that turn silent mouthing into text](#item-2) ⭐️ 8.0/10
3. [Ubuntu LTS kernels still unpatched for critical Linux 0day RCE after nearly three weeks](#item-3) ⭐️ 8.0/10
4. [WIRED Finds 400+ AI Apps Hiding Sexual Deepfake Tools](#item-4) ⭐️ 8.0/10
5. [Swedish supermarket chain ICA hit by cyberattack that set freezers to 50°C](#item-5) ⭐️ 8.0/10
6. [Anthropic IPO Filing Shows $33.2B Revenue and a $104B Net Loss](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Astra reads and writes neural network weights, lifting Qwen math accuracy fivefold](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 9.0/10

A new blog post on weight-space programming reports that a frontier model called Astra (referred to in coverage as GPT-6 Astra, from MIT CSAIL) can natively read and edit another network's weights without any optimizer or training run. In its eighth experiment, Astra hand-edited Qwen3.5-0.8B, modifying 131,072 weight entries — roughly 0.016% of the model's ~800M parameters — and raised MATH-500 accuracy from 7.9% to 48.1%. If reproducible, this is a paradigm-shift-level result: model behavior would become something you can inspect and patch directly in weight space rather than only through retraining, fine-tuning or prompt engineering. It also touches on recursive self-improvement, since a model that can reliably edit other models' weights could in principle improve AI systems without a conventional training loop. Astra traced Qwen's tendency to loop (85 of its first 96 practice answers ran to the 32,768-token limit) to a single direction written by the MLPs of layers 15 and 19, and subtracted that direction from 64 output columns in each layer; it computed the replacement values in Python before submitting the edited tensors for testing, and the fix also improved instruction following. The caveats are that this is a tiny 0.8B model on a single benchmark, and skeptics such as Sean Goedecke argue LLMs are not actually superhuman at reading and writing weights.

hackernews · dbreunig · Nov 2, 18:21 · [Discussion](https://news.ycombinator.com/item?id=50341174)

**Background**: Neural network weights are normally produced by an optimizer such as Adam or Muon, by a network trained to write other networks, or by compilers that turn formal programs into weights. The authors define "weight-space programming" as something different: a general-purpose LLM reading and writing a network's weights directly, not through an optimizer. Qwen is Alibaba Cloud's family of open-weight large language models, and Qwen3.5-0.8B is one of its smallest members, which makes it a convenient testbed for weight-level experiments.

<details><summary>References</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight -Space Programming: LLMs can natively read & write...</a></li>
<li><a href="https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/">LLMs are not superhuman at reading and writing neural network ...</a></li>
<li><a href="https://kingy.ai/blog/weight-space-programming-ai-agent-model-weights/">Weight-Space Programming: GPT-6 Astra Edits Qwen - kingy.ai</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread (2,059 points, 669 comments) is unusually substantive: vessenes said they were "shook" and would previously have guessed LLMs understand their own weights no better than humans understand neurons, while xg15 argued the result is not entirely out of the blue given LLMs' recurring ability to rapidly grasp sprawling complex systems. vanyle pushed back hardest, arguing this is not an emergent capability but likely the product of deliberately training Astra on neural weight data as an attempt at recursive self-improvement.

**Tags**: `#AI/ML`, `#interpretability`, `#weight-space editing`, `#LLM`, `#recursive self-improvement`

---

<a id="item-2"></a>
## [YC startup Subvocal unveils RF smart glasses that turn silent mouthing into text](https://news.ycombinator.com/item?id=50340088) ⭐️ 8.0/10

The Subvocal Company, a YC F26 startup founded by Georgia Tech students Aarush and Arnav, showed off smart glasses that use radio-frequency sensing to decode silently mouthed — or even fully internal, lips-closed — speech into text at speaking speed. The team says the system exceeds 200 words per minute, has raised about $1.3 million, and is now taking preorders. Silent speech input would let people dictate to AI tools and computers in libraries, offices, and public spaces where voice input like Wispr Flow is socially awkward, and it could be transformative for users with speech or motor impairments. If it works reliably across users, it also points toward always-available, hands-free AI input that does not require a microphone or camera. The glasses emit low-power radio waves, similar to Bluetooth, that pass through the face and are modulated by the tongue, lips, and soft palate; foundation models trained on that data decode the perturbations into text. The founders abandoned an earlier EMG-electrode approach (built in 36 hours at TreeHacks) because of sweat, electrical interference, placement variability, and comfort, and they note the hardest remaining problem is cross-user generalization, since everyone's facial anatomy produces different RF signatures.

hackernews · aarushyadav · Nov 2, 17:16

**Background**: Silent speech recognition (SSR) is a long-studied alternative to acoustic speech recognition that captures speech without any audible sound, using modalities such as muscle electrical signals (EMG), radar, depth sensing, or earphone-based acoustic sensing. MIT Media Lab's AlterEgo project popularized the idea of subvocal input via facial electrodes, while prior RF work like RFTattoo required RFID tags attached to the face. Subvocal's claim is that embedding antennas in ordinary-looking glasses frames makes the sensing invisible and practical for daily use.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eesel.ai/blog/subvocal">Subvocal glasses: silent speech to text, price and what's ...</a></li>
<li><a href="https://www.indiatoday.in/technology/news/story/subvocal-founded-by-arnav-and-aarush-makes-ai-glasses-that-turn-silent-words-into-text-3029418-2026-10-31">Subvocal, founded by Arnav and Aarush, makes AI glasses that ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Subvocal_recognition">Subvocal recognition - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News reaction was enthusiastic — many called it sci-fi-level and a big win for accessibility and hands-free computing — but commenters pressed on practicalities: one preorderer with a high nose bridge asked the team to keep adjustable metal nose pads, another wanted a clip-on module for existing prescription frames given limited frame sizes. Others asked how Subvocal compares to open-source silent-input projects like LipFlow, HushKey, Chaplin, and LipNet, and raised privacy worries about whether inference runs on-device or offline, citing fears of always-on sensing being used for profiling and ad targeting.

**Tags**: `#silent speech recognition`, `#smart glasses`, `#human-computer interaction`, `#accessibility`, `#privacy`, `#RF sensing`

---

<a id="item-3"></a>
## [Ubuntu LTS kernels still unpatched for critical Linux 0day RCE after nearly three weeks](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) ⭐️ 8.0/10

Ubuntu has left a critical Linux kernel 0day remote code execution flaw, tracked as CVE-2026-98432, unpatched in its LTS kernels for almost three weeks, and has published no mitigation guidance in the meantime. With no official fix or workaround from Canonical, community members have circulated their own temporary defenses and are questioning why the patch is taking so long. A remotely exploitable kernel flaw with no vendor patch leaves every affected Ubuntu LTS server and desktop exposed, and LTS releases are widely used in production and cloud infrastructure where kernel-level compromise means full host takeover. The silence also damages trust in Ubuntu's security response process, with at least one commenter saying they will stop choosing Ubuntu for new servers. The kernel is exploitable before the CVE fix lands, so one commenter proposed a raw-table PREROUTING rule using iptables' u32 match (`iptables -t raw -I PREROUTING -p tcp -m u32 ! --u32 "0>>24&0x0F=5" -j DROP`) to drop offending packets pre-emptively. By contrast, RHEL has published a mitigation that it admits "reduces exposure to this vulnerability but cannot fully prevent it," without explaining the caveat — a claim other commenters say they have not seen corroborated anywhere.

hackernews · majorchord · Nov 2, 18:39 · [Discussion](https://news.ycombinator.com/item?id=50341462)

**Background**: A zero-day vulnerability is a security hole that is known (or already exploited) before the vendor has shipped a fix, leaving defenders with only workarounds. Remote code execution (RCE) is the class of flaw that lets an attacker run arbitrary commands over a network without any user interaction, and in a kernel vulnerability that means full control of the machine. Ubuntu LTS (Long Term Support) releases are maintained for many years and are the default choice for servers, so a slow kernel patch there has an outsized blast radius compared with short-lived distributions. Kernel patches are normally routine, which is why the community is pressing Canonical for a concrete explanation of the delay rather than just a new kernel build.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/remote-code-execution/">What is Remote Code Execution (RCE)? | CrowdStrike</a></li>
<li><a href="https://en.wikipedia.org/wiki/Arbitrary_code_execution">Arbitrary code execution - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are broadly critical: one notes that nobody is publicly highlighting the iptables/nftables u32 PREROUTING drop rule that can block exploitation, while others demand a real explanation for the delay, point out that RHEL at least published a (vague) mitigation, and warn that consumer routers running Linux never receive kernel security updates at all. Several argue LLMs are handing script kiddies nation-state-grade tooling, making unpatched known bugs more dangerous, and at least one long-time user says the episode has shaken their faith in Ubuntu.

**Tags**: `#linux-kernel`, `#security-vulnerability`, `#ubuntu`, `#0day`, `#mitigation`

---

<a id="item-4"></a>
## [WIRED Finds 400+ AI Apps Hiding Sexual Deepfake Tools](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 8.0/10

WIRED published a November 2 investigation revealing a network of more than 400 linked AI apps and websites that present themselves as ordinary utilities — pet photo generators, language-learning tools, AI fitness coaches — but load a hidden sexual deepfake interface under certain conditions. After being shown the evidence, Apple removed 19 apps, Google had already taken down most of the 27 apps that were on Google Play as of September (together downloaded over 350,000 times), and Meta blocked 209 related apps from running ads. The case shows that app-store review and ad-review pipelines can be systematically circumvented at scale, meaning non-consensual sexual imagery tools can reach mainstream audiences — including minors, since many of the apps were rated suitable for all ages. It also puts pressure on Apple, Google and Meta to coordinate on policing the same operator network rather than acting only when journalists surface it. The apps reportedly passed review with benign functionality and later swapped in remote web content served from a server, a technique that lets operators change what users see without shipping a new native binary through review. Researchers linked the network through shared code, hosting details, Chinese-language source code and domain names, and traced it to Chinese-speaking developers and a Hong Kong-registered company — an attribution the outlets describe as investigative judgment; the operators did not respond to requests for comment.

telegram · zaihuapd · Nov 2, 12:45

**Background**: So-called "nudify" services use generative image models to remove clothing or synthesize explicit imagery from a single uploaded photo, and are frequently used to produce non-consensual intimate images. Because Apple's App Store and Google Play prohibit such content, operators disguise the apps as mundane AI tools and rely on remote web views to serve the prohibited features only after install. Investigators commonly unmask these networks by correlating shared code signatures, hosting infrastructure, domain registrations and ad-tracking identifiers across apps that otherwise look unrelated.

<details><summary>References</summary>
<ul>
<li><a href="https://www.openai-hub.com/news/2645/">苹果下架19款伪装App：深度伪造如何靠审核后换壳绕过App Store治理 - ...</a></li>
<li><a href="https://www.shuzhipunk.com/articles/CqvTLA0p2tX">400余款伪装AI应用暗藏深度伪造违规功能，科技巨头审核机制遭系统性绕...</a></li>
<li><a href="https://nudify.im/ai-clothes-remover/">AI Clothes Remover - Remove Clothing from Any Photo | Nudify .im</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#deepfakes`, `#app store moderation`, `#privacy`, `#content moderation`

---

<a id="item-5"></a>
## [Swedish supermarket chain ICA hit by cyberattack that set freezers to 50°C](https://x.com/InsiderGeo/status/2117164877701595165) ⭐️ 8.0/10

Swedish supermarket chain ICA said several of its stores were hit overnight by a cyberattack that remotely set refrigerators and freezers to 50°C, affecting locations including Sjöbo and Tomelilla. The stores suspended operations in the morning and were expected to reopen around 9 a.m. local time, with ICA apologizing to customers. This is a concrete cyber-physical attack in which a purely digital intrusion produced immediate physical and financial damage — spoiled food, closed stores and lost revenue — rather than data theft. It fits a pattern of similar refrigeration-system attacks on retailers in France, Ireland, Belgium and the US in recent weeks, and should push retail OT/IoT operators to treat cooling and building-control systems as security-critical assets. ICA has not disclosed how attackers reached the refrigeration controls, and no technical details on the intrusion vector, affected store count or total spoilage losses were given. Security researchers have repeatedly warned that internet-exposed refrigeration and building-automation controllers can be abused through legitimate setpoint functions, meaning attackers need no destructive malware to cause damage.

telegram · zaihuapd · Nov 2, 13:52

**Background**: Modern supermarkets run refrigeration and HVAC equipment on networked control systems — part of the operational technology (OT) and Internet of Things (IoT) world — often managed remotely by staff or contractors for monitoring and energy efficiency. When such controllers are reachable from the internet or protected only by weak credentials, attackers can change temperature setpoints much as an authorized technician would, so the system behaves as if a legitimate command were issued. Because spoilage and food-safety risks are immediate, retailers typically pull chilled and frozen products from sale after any such incident, as happened at SuperValu stores in Ireland and at Intermarché and Coopérative U stores in France.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/">Cold Chain, Open Control: Exposed Refrigeration Systems Reveal...</a></li>
<li><a href="https://www.euronews.com/2026/11/02/cyberattack-hits-belgian-supermarket-fridges-and-freezers">Cyberattacks hit supermarket fridges and freezers in... | Euronews</a></li>
<li><a href="https://www.rte.ie/news/world/2026/1102/1597622-cyber-attacks-appliances/">Explainer: Is my fridge vulnerable to a cyber attack ?</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#IoT/OT security`, `#cyber-physical attack`, `#critical infrastructure`, `#retail`

---

<a id="item-6"></a>
## [Anthropic IPO Filing Shows $33.2B Revenue and a $104B Net Loss](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) ⭐️ 8.0/10

Anthropic updated its IPO prospectus on Monday, disclosing $33.24 billion in revenue for the first three quarters of 2026 through September 30, a roughly 1,200% year-over-year increase, with the third quarter alone bringing in about $17 billion. The same filing showed a net loss of $104 billion for the period, far wider than the $25.1 billion loss reported a year earlier. The disclosure offers a rare, audited-level look at the economics of a leading AI lab just before it lists publicly, showing revenue scaling at an extraordinary pace while losses scale even faster. Its roughly $895.4 billion in compute and infrastructure commitments also signals how much future spending the company has locked in, which matters to investors, cloud providers, and chip suppliers across the AI supply chain. Anthropic says the first-half net loss was driven largely by fair-value changes on convertible notes and derivative liabilities, so it does not fully reflect actual operating cash consumption. The roughly $895.4 billion in cumulative purchase and lease commitments is almost entirely dedicated to compute and infrastructure.

telegram · zaihuapd · Nov 2, 15:12

**Background**: Anthropic is the AI company behind the Claude family of models, and an IPO prospectus is the registration document a company files before selling shares to the public, disclosing revenue, losses, and major obligations. Under accounting rules, convertible notes and derivative liabilities must be marked to fair value each period, and when a company's valuation soars those marks can create large non-cash losses that sit alongside real operating results. Compute commitments are multi-year contracts to buy GPU capacity and cloud infrastructure, essentially a bet that future model training and serving demand will justify the spend.

**Tags**: `#Anthropic`, `#AI industry`, `#IPO`, `#financials`, `#compute infrastructure`

---