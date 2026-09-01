---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 44 items, 11 important content pieces were selected

---

1. [Anthropic launches Claude Fable 5.1 and Mythos 5.1 with better writing, cheaper cache reads](#item-1) ⭐️ 9.0/10
2. [Google Play Blocks AnkiDroid Link to Open Collective Donations](#item-2) ⭐️ 8.0/10
3. [Jujutsu creator Martin von Zweigbergk joins ERSC](#item-3) ⭐️ 8.0/10
4. [Small Transformer Trained in 1.5 Hours Beats Many LLMs on ARC Benchmark](#item-4) ⭐️ 8.0/10
5. [Apple reveals forensic evidence in OpenAI trade-secret lawsuit](#item-5) ⭐️ 8.0/10
6. [Python 3.15.0 Release Candidate 2 Announced, Final Phase Before October Release](#item-6) ⭐️ 8.0/10
7. [Wrapture: New Python Library Unifies Tracing and Testing via Monkeypatching](#item-7) ⭐️ 8.0/10
8. [Korea's Trillion-Dollar Sovereign AI Push: Nvidia Gains, Hynix Loses](#item-8) ⭐️ 8.0/10
9. [2026 Latent Reasoning Landscape Maps BDH-CQ, HRM/TRM, Coconut](#item-9) ⭐️ 8.0/10
10. [EvoUndo: Verifying Recoverability of LLM Agent Self-Evolution](#item-10) ⭐️ 8.0/10
11. [Virtualizor Update Infrastructure BGP-Hijacked; Root Backdoor Installed via Malicious Updates](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic launches Claude Fable 5.1 and Mythos 5.1 with better writing, cheaper cache reads](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

Anthropic has released Claude Fable 5.1 and Claude Mythos 5.1, the latest additions to its Claude model family. The new models bring improved writing quality, lower cache read pricing, and progress in scientific reasoning capabilities. This release sharpens Anthropic's competitive edge in the LLM market by reducing inference costs through a 75% cut in cache read pricing, which may pressure other providers. It also signals continued focus on long-running agentic tasks and scientific domains, potentially broadening adoption in enterprise and research settings. The price cut comes specifically from cache read pricing falling from $1/M to $0.25/M, making Fable 5.1's cache reads half the cost of Opus's $0.5/M. The release also includes three breaking changes that appear to patch inadvertent chain-of-thought disclosure, and the accompanying system card details safety evaluations.

hackernews · denysvitali · Sep 1, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49525378)

**Background**: Claude Mythos is Anthropic's most powerful series of large language models; Claude Fable is a 'Mythos-class' model released publicly with added safeguards, while Mythos itself remains restricted-access. According to industry estimates, Mythos has roughly 8 trillion parameters and Fable 5 around 5 trillion. A system card is a structured document that discloses an AI system's architecture, safeguards, and safety evaluations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos</a></li>
<li><a href="https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1">What's new in Claude Fable 5.1 - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: Community reactions are largely positive. An Anthropic insider praised Fable 5.1's writing style as more natural and responsive to instructions, and highlighted anticipated gains in science. Another user noted that without Terminal-Bench-Science results, improvements in other benchmarks appear limited, while others discussed the pricing dynamics and the three breaking changes as fixes for chain-of-thought leaks.

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#Model Release`

---

<a id="item-2"></a>
## [Google Play Blocks AnkiDroid Link to Open Collective Donations](https://github.com/ankidroid/Anki-Android/issues/21656) ⭐️ 8.0/10

AnkiDroid, a popular open-source flashcard app, reported that Google Play is no longer allowing it to link to its Open Collective donation page. The policy enforcement, documented in a GitHub issue, has sparked debate among developers and FOSS advocates. This decision threatens a key funding channel for a widely-used open-source project, illustrating how app store policies can exert control over independent software sustainability. It also highlights growing concerns about platform monopolies and the financial fragility of FOSS projects. Google Play's policy requires payments to go through its billing system, with a stated exception for tax-exempt donations. AnkiDroid's donations via Open Collective are not tax-deductible because the project is under Open Source Collective, a 501(c)(6) entity, not a 501(c)(3) charity, which may be why Google disallowed the external link.

hackernews · hexa555 · Sep 1, 10:11 · [Discussion](https://news.ycombinator.com/item?id=49520022)

**Background**: AnkiDroid is an open-source Android flashcard app based on the spaced-repetition system Anki, with millions of downloads on the Google Play Store. Open Collective is a crowdfunding and financial management platform that many open-source projects use to collect and manage donations. Google Play has historically enforced strict payment policies, and in 2019 it temporarily removed the WireGuard VPN app for linking to external payment options — a case often cited as an example of Google's control over app distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open_Collective">Open Collective - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Android_app_stores">List of Android app stores</a></li>
<li><a href="https://github.com/ankidroid/Anki-Android">GitHub - ankidroid/Anki-Android: AnkiDroid: Anki flashcards on Android. Your secret trick to achieve superhuman information retention. · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters largely sympathize with AnkiDroid and criticize Google's enforcement, recalling similar past incidents such as WireGuard's removal in 2019. Some clarified the tax-exempt donation nuance: Open Source Collective is a 501(c)(6), so donations aren't tax-deductible, which may explain Google's action. Others expressed gratitude to the app and some said they would switch to Linux phones to avoid Google's control.

**Tags**: `#Android`, `#Open Source`, `#Google Play`, `#Donations`, `#App Store Policy`

---

<a id="item-3"></a>
## [Jujutsu creator Martin von Zweigbergk joins ERSC](https://ersc.io/blog/martin-joins-ersc) ⭐️ 8.0/10

Martin von Zweigbergk, the creator of the Jujutsu version control system, has joined ERSC (East River Source Control). The company also announced that its storage product will enter private beta later this month. This signals a major move in the version control space, as Jujutsu is seen as a promising next-generation git-compatible tool. ERSC is positioning itself as a competitor to GitHub, so having such a key developer on board could shape the future of code hosting and developer workflows. Von Zweigbergk will continue to be a core maintainer of jj as an open source project under the Apache 2.0 license. ERSC Storage enters private beta later this month, but the company's broader differentiation from GitHub remains under discussion.

hackernews · steveklabnik · Sep 1, 17:46 · [Discussion](https://news.ycombinator.com/item?id=49525297)

**Background**: Jujutsu (jj) is a Rust-based version control system that works with git repositories, offering features like undo, automatic rebasing, and a simpler command set. ERSC (East River Source Control) is a company aiming to build a code hosting platform that competes with GitHub.

<details><summary>References</summary>
<ul>
<li><a href="https://ersc.io/blog/martin-joins-ersc">East River Source Control Names Jujutsu Creator Martin von... // ERSC</a></li>
<li><a href="https://github.com/jj-vcs/jj">jj-vcs/jj - Jujutsu—a version control system</a></li>

</ul>
</details>

**Discussion**: Commenters are optimistic about jj's UX and its undo capabilities, but some question ERSC's value proposition relative to GitHub. One commenter argued that since jj is git-compatible, ERSC needs to demonstrate how it addresses GitHub's shortcomings rather than merely offering a new steering wheel.

**Tags**: `#jujutsu`, `#version-control`, `#ersc`, `#developer-tools`, `#announcement`

---

<a id="item-4"></a>
## [Small Transformer Trained in 1.5 Hours Beats Many LLMs on ARC Benchmark](https://mvakde.github.io/blog/44-on-arc-1/) ⭐️ 8.0/10

A blog post by M. Vakde describes training a small autoregressive transformer from scratch in just 1.5 hours that achieves competitive results on the ARC benchmark, outperforming many larger LLMs. The author emphasizes this is not an LLM and shows complex reasoning tasks can be tackled without massive scaling. This challenges conventional scaling assumptions in AI, showing that a tiny, specially trained model can outperform huge LLMs on a key reasoning benchmark. It could reinvigorate interest in small models, efficient training methods, and novel architectures rather than simply scaling up compute. The model is a small autoregressive transformer trained from scratch (not an LLM) and reportedly reached top-5 performance on Kaggle. The author argues that 'training on eval puzzles' is not 'training on test labels' because ARC is a metalearning benchmark where learning from evaluation puzzles is allowed.

hackernews · porridgeraisin · Sep 1, 09:52 · [Discussion](https://news.ycombinator.com/item?id=49519939)

**Background**: The ARC (Abstraction and Reasoning Corpus) benchmark, introduced by François Chollet, consists of grid-based visual puzzles designed to measure general intelligence rather than simple pattern recognition. Traditionally, good performance on ARC required massive LLMs or complex architectures with huge training costs. This result suggests that with the right architecture and training strategy, a small transformer can achieve competitive results, potentially democratizing research on this important benchmark.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Abstraction_and_Reasoning_Corpus">Abstraction and Reasoning Corpus</a></li>
<li><a href="https://deepgram.com/learn/arc-llm-benchmark-guide">ARC Benchmark Guide for Evaluating LLMs | Deepgram</a></li>
<li><a href="https://arcprize.org/">ARC Prize</a></li>

</ul>
</details>

**Discussion**: In the Hacker News discussion, the author (evilmathkid) clarified that the model is NOT an LLM but a small AR transformer, sparking debate about sample efficiency and whether training on eval puzzles constitutes cheating. Some commenters praised the result (e.g., 'Sounds like a good day to be you, top 5 on Kaggle'), while others asked for simpler explanations and discussed the validity of the approach. Overall sentiment was curious and mostly supportive, with some critical questions about methodology.

**Tags**: `#AI`, `#machine-learning`, `#transformers`, `#ARC-benchmark`, `#LLMs`

---

<a id="item-5"></a>
## [Apple reveals forensic evidence in OpenAI trade-secret lawsuit](https://9to5mac.com/2026/08/31/apple-openai-forensic-macbook-evidence/) ⭐️ 8.0/10

Apple has presented forensic evidence in its lawsuit against OpenAI, alleging that former employee Mr. Liu downloaded confidential Apple circuit schematics and used them in his work at OpenAI. The evidence reportedly includes iCloud-synced files from a MacBook and a Mac mini. The case could set a precedent on whether AI models that train on trade secrets create 'irreversible and continually propagating uses' of that secret. It also raises important privacy questions about cloud-synced data on company-owned devices. Apple discovered Liu's use of the schematic because he ran it on a Mac mini that synced via iCloud to the MacBook he took from Apple; Apple now seeks access to that Mac mini. Liu allegedly sent instructions to destroy evidence upon learning of Apple's investigation, and he used LTspice to run simulations while stating his AI 'agent' learned to operate the tool.

hackernews · colinprince · Sep 1, 20:19 · [Discussion](https://news.ycombinator.com/item?id=49527573)

**Background**: Trade secret law protects confidential business information from unauthorized use or disclosure. In the AI era, feeding trade secrets into AI models raises novel legal questions about whether the models' learned knowledge constitutes misappropriation. Additionally, iCloud synchronization can blur the line between personal and corporate data, as files on one device may automatically appear on another.

**Discussion**: Commenters are intrigued by Apple's argument that AI learning from trade secrets may cause irreversible propagation, calling it a high-impact legal test. Others voice privacy concerns about employers accessing personal information synced to company devices. One commenter jokingly hopes for an 'AI-laundered' Linux driver for MacBooks.

**Tags**: `#Apple`, `#OpenAI`, `#trade-secrets`, `#privacy`, `#litigation`

---

<a id="item-6"></a>
## [Python 3.15.0 Release Candidate 2 Announced, Final Phase Before October Release](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 8.0/10

Python 3.15.0 candidate 2 has been announced by release manager Hugo van Kemenade, marking the final release candidate phase before the stable release in October. From this point, only bug fixes are permitted between the candidate and the final release. This announcement signals that Python 3.15 is nearly ready for production, prompting third-party maintainers to test their projects and publish compatible wheels. It helps ensure the broader ecosystem is prepared for the new version on day one of its release. The release candidate is not yet available in GitHub Actions; maintainers can use the allow-prereleases and check-latest flags to automatically test against the latest RC and eventually the stable release. Wheels built against 3.15.0 release candidates will remain compatible with future 3.15 versions.

rss · Simon Willison · Sep 1, 14:59

**Background**: A release candidate (RC) is a version that is feature-complete and only receives bug fixes before the final release. Python binary wheels are prebuilt distribution packages that install without compilation, and the Python Packaging User Guide notes they are preferred by pip and uv. The RC phase is a critical window for the Python ecosystem to validate compatibility and prepare wheels, as demonstrated by Simon Willison's earlier experience of finding a bug only after a release had shipped.

<details><summary>References</summary>
<ul>
<li><a href="https://packaging.python.org/specifications/binary-distribution-format/">Binary distribution format - Python Packaging User Guide</a></li>
<li><a href="https://realpython.com/python-wheels/">What Are Python Wheels and Why Should You Care? – Real Python</a></li>
<li><a href="https://teamhub.com/blog/understanding-the-significance-of-release-candidate-in-software-development/">What is Release Candidate in Software Development ?</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Release Candidate`, `#Software Development`, `#Ecosystem`

---

<a id="item-7"></a>
## [Wrapture: New Python Library Unifies Tracing and Testing via Monkeypatching](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 8.0/10

Graham Dumpleton released Wrapture, a Python library extending wrapt-style monkeypatching to combine tracing and testing. It provides configuration-based OpenTelemetry tracing and acts as an alternative to unittest.mock for overrides. This unifies two common developer workflows—observability and testing—through a single consistent API. It offers a novel, more transparent alternative to unittest.mock for instrumentation, and its agent-driven development shows a notable approach by an experienced maintainer. Wrapture is young—only a few weeks old—and every line of code and documentation was written by an AI assistant under Graham's direction. It supports an entirely configuration-based TOML mechanism for adding tracing, plus a binding API for stubbing functions in tests.

rss · Simon Willison · Aug 31, 23:59

**Background**: Monkeypatching refers to dynamically modifying or extending code at runtime. wrapt is a Python module by Graham Dumpleton (also known for mod_wsgi and New Relic's Python agent) that provides a transparent object proxy for building decorators, wrappers, and monkeypatching tools. Wrapture builds on those ideas, applying them to both tracing (via OpenTelemetry) and testing (as a unittest.mock alternative).

<details><summary>References</summary>
<ul>
<li><a href="https://pypi.org/project/wrapt/">wrapt · PyPI</a></li>
<li><a href="https://github.com/GrahamDumpleton/wrapt">GitHub - GrahamDumpleton/wrapt: A Python module for decorators, wrappers and monkey patching. · GitHub</a></li>
<li><a href="https://stackoverflow.com/questions/5626193/what-is-monkey-patching">python - What is monkey patching? - Stack Overflow</a></li>

</ul>
</details>

**Tags**: `#Python`, `#testing`, `#tracing`, `#monkeypatching`, `#wrapt`

---

<a id="item-8"></a>
## [Korea's Trillion-Dollar Sovereign AI Push: Nvidia Gains, Hynix Loses](https://newsletter.semianalysis.com/p/koreas-trillion-dollar-sovereign) ⭐️ 8.0/10

Korea is investing trillions of dollars in sovereign AI, running a national AI tournament to select its own foundation models. SemiAnalysis argues this reshapes the competitive landscape, benefiting Nvidia while hurting Hynix and putting pressure on Samsung. Sovereign AI is a global trend as nations seek control over their AI infrastructure, data, and models. Korea's approach shows how government-led AI investments can shift the balance among semiconductor giants, with open-source models playing a pivotal role. Korea's Ministry of Science and ICT has selected LG AI Research, SK Telecom, Upstage, Naver Cloud, and NC AI to build domestic foundation models. The competition also involves citizen scoring, with winners set to power a free national AI service.

rss · Semianalysis · Sep 1, 20:14

**Background**: Sovereign AI refers to a nation's ability to control its entire AI stack—compute, data, models, and talent—rather than relying on foreign providers. Korea's push is part of a broader global movement where governments fund domestic AI champions to reduce dependence on US and Chinese technology. The tournament-style selection is unusual, opening the process to citizen participation and emphasizing open-source models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>
<li><a href="https://koreatechtoday.com/korea-picks-five-national-champions-to-lead-sovereign-ai-push/">Korea Picks Five National Champions to Lead Sovereign AI Push</a></li>
<li><a href="https://www.techtimes.com/articles/323429/20260806/korea-opens-citizen-lottery-pick-national-ai-champion-starting-friday.htm">Korea Opens Citizen Lottery To Pick National AI Champion ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Semiconductors`, `#Sovereign AI`, `#Nvidia`, `#Korea`

---

<a id="item-9"></a>
## [2026 Latent Reasoning Landscape Maps BDH-CQ, HRM/TRM, Coconut](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/) ⭐️ 8.0/10

A Reddit analysis categorizes latent reasoning methods into at least five families, including Coconut, Soft Thinking, Abstract-CoT, recurrent-depth models, HRM/TRM, and BDH-CQ. The post argues that future progress may depend on architectures that reason in continuous hidden states rather than explicit chain-of-thought. This synthesis highlights a potential shift away from readable chain-of-thought, which underpins much of current interpretability and evaluation work. The trade-off between efficiency and traceability could shape future LLM architectures and safety practices. The post distinguishes latent reasoning families by how tasks are acquired (context, memory, or gradient optimization) and where intermediate computation occurs (language tokens, abstract tokens, or continuous latent states). It specifically highlights BDH-CQ, built on the Dragon hatchling architecture, which reports a point beyond the published cost–accuracy Pareto frontier on ARC-AGI-1 and shows scaling laws up to 600B parameters.

reddit · r/MachineLearning · /u/Typical-Scene-5794 · Sep 1, 15:14

**Background**: Latent reasoning is an alternative to chain-of-thought (CoT) prompting, where models repeatedly transform their continuous hidden state and decode only the final answer instead of verbalizing intermediate steps. Key papers include Coconut (arXiv 2412.06769), which feeds the last hidden state back as the next input embedding, and HRM/TRM (arXiv 2510.04871), which use tiny recursive networks for reasoning. BDH-CQ (arXiv 2608.09888) combines in-context learning with recurrent latent reasoning, allowing inference-time demonstrations to update model memory.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2608.09888">BDH-CQ: In-Context Learning with Recurrent Latent Reasoning | alphaXiv</a></li>
<li><a href="https://arxiv.org/abs/2412.06769">[2412.06769] Training Large Language Models to Reason in a Continuous Latent Space</a></li>
<li><a href="https://arxiv.org/pdf/2510.04871">Less is More: Recursive Reasoning with Tiny Networks</a></li>

</ul>
</details>

**Tags**: `#latent reasoning`, `#chain-of-thought`, `#LLM architectures`, `#AGI research`, `#continual learning`

---

<a id="item-10"></a>
## [EvoUndo: Verifying Recoverability of LLM Agent Self-Evolution](https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/) ⭐️ 8.0/10

EvoUndo is a new framework for representing, synthesizing, diagnosing, and independently verifying the recoverability of LLM agent self-modifications. In tests across 600 unseen tasks, it identified 197 capability-improving mutations that failed recoverability, and an extended recovery calculus recovered 191 of them, versus 0 with standard repair strategies. This addresses a critical open problem in AI safety: how to let LLM agents improve themselves without risking irreversible harmful changes. By co-designing verification, state grounding, and recovery-language expressivity, EvoUndo provides a path toward safer autonomous agents. The framework uses a typed effect system to define recovery languages and a grounding-by-expressivity intervention to separate two bottlenecks. On the gpt-oss-120b backbone, exact-address diagnostics reduced recovery to 133/143 in the richer language, whereas a Qwen3.8-27B replication preserved the main effects but not this negative interaction, indicating model dependence.

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · Sep 1, 19:17

**Background**: LLM agents increasingly modify their own prompts, tools, middleware, resources, and execution harnesses at runtime to improve capability. However, a successful mutation may leave persistent effects that cannot be safely reversed in states different from the one in which it was created. Recoverability is the property that a modification can be reversed without side effects. EvoUndo formalizes this concept and provides a framework for verifying it, co-designing verification, state grounding, and recovery-language expressivity.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28363">[2608.28363] EvoUndo: Recoverability-Constrained Self ...</a></li>
<li><a href="https://arxiv.org/pdf/2608.28363v1">EvoUndo: Recoverability-Constrained Self-Evolution for LLM ...</a></li>
<li><a href="https://huggingface.co/papers/2608.28363">Paper page - EvoUndo : Recoverability -Constrained Self-Evolution for...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#self-evolution`, `#recoverability`, `#AI safety`, `#machine learning`

---

<a id="item-11"></a>
## [Virtualizor Update Infrastructure BGP-Hijacked; Root Backdoor Installed via Malicious Updates](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 8.0/10

Between August 28 and 30, 2026, attackers hijacked BGP routes for Virtualizor's update infrastructure and delivered malicious update packages signed with valid TLS certificates. A limited number of systems that updated within that window were compromised with a root backdoor; the vendor says this was a distribution-chain compromise, not a software vulnerability. This is a serious supply-chain attack because BGP hijacking let attackers sign malicious updates with legitimate TLS certificates, making the payload look authentic. It also highlights how routing infrastructure, not just code bugs, can be exploited to backdoor server management platforms used by many hosting providers. Independent forensics showed the malicious update wrote a root SSH key, installed a Java payload, and created a persistent service. AlbaHost found compromise indicators on 5 of 34 hypervisors, and Softaculous stated there is currently no evidence that other products were affected.

telegram · zaihuapd · Sep 1, 06:05

**Background**: BGP (Border Gateway Protocol) is the routing protocol that directs traffic between autonomous systems on the internet; BGP hijacking occurs when an attacker corrupts routing tables and advertises fake routes so traffic destined for a legitimate IP prefix is diverted to attacker-controlled infrastructure. Virtualizor is a web-based VPS control panel developed by Softaculous, and its update servers are trusted endpoints that hosting providers use to apply patches. When those routes are hijacked, an update channel can be poisoned while still presenting valid TLS certificates, making malicious versions almost indistinguishable from official ones.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/virtualizor-compromise/">BGP Hijack Diverts Softaculous Traffic to Deliver Malicious Virtualizor ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/BGP_hijacking">BGP hijacking</a></li>
<li><a href="https://en.wikipedia.org/wiki/Softaculous">Softaculous</a></li>

</ul>
</details>

**Tags**: `#BGP hijacking`, `#supply chain attack`, `#rootkit`, `#Virtualizor`, `#security`

---