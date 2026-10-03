---
layout: default
title: "Horizon Summary: 2026-10-03 (EN)"
date: 2026-10-03
lang: en
---

> From 31 items, 4 important content pieces were selected

---

1. [AI beats top human Stratego player with 34x fewer training games](#item-1) ⭐️ 8.0/10
2. [Greg Kroah-Hartman Dissects Anthropic's Mythos Kernel Bug Claims](#item-2) ⭐️ 8.0/10
3. [Google Research's Cogentic Coordinates Multi-Agent LLMs to Discover New Math Proofs](#item-3) ⭐️ 8.0/10
4. [Claude Code adds a TypeScript-based mods system](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI beats top human Stratego player with 34x fewer training games](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 8.0/10

A new AI system has defeated the best human Stratego player in history, solving a long-standing hidden-information game challenge that had resisted strong AI play. The result is published in Nature (s41586-026-11036-y) with an accompanying arXiv preprint (2511.07312), and the system reportedly learned using roughly 34 times fewer games than DeepMind's DeepNash. Imperfect-information games are a hard frontier for AI because the optimal move depends on facts the player cannot observe, so classic look-ahead search breaks down. Demonstrating a much stronger Stratego agent at a fraction of the training cost suggests these methods could transfer to real-world domains such as negotiation, security, and other strategic settings where information is hidden. Stratego is played on a 10x10 board with 40 pieces per side, and there are more than 10^33 possible starting configurations; both players can see where enemy pieces are but not what they are until combat reveals them. Because a move's value depends on hidden information, the agent cannot rely on the usual 'if I do this, they will do that' search, and the key reported advance is the dramatically greater sample efficiency rather than raw strength alone.

hackernews · PaulHoule · Oct 2, 14:11 · [Discussion](https://news.ycombinator.com/item?id=49933740)

**Background**: Stratego is a chess-like two-player strategy board wargame in which each army's 40 pieces represent officer and soldier ranks via a numbering scheme, plus bombs and a flag. It is a classic imperfect-information benchmark, alongside poker, where techniques that work in perfect-information games like chess and Go — such as Monte Carlo tree search combined with self-play — tend to fall apart. DeepMind's 2022 DeepNash was the previous high-water mark for machine play in Stratego, and it required an enormous number of self-play games to reach top-human level.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stratego">Stratego - Wikipedia</a></li>
<li><a href="https://deepmind.google/blog/mastering-stratego-the-classic-game-of-imperfect-information/">Mastering Stratego , the classic game of imperfect information</a></li>
<li><a href="https://www.zmescience.com/science/ai-beats-humans-stratego/">This AI Finally Beat the Best Humans at One of the Last Board Games ...</a></li>

</ul>
</details>

**Discussion**: Commenters were largely enthusiastic, with many sharing childhood Stratego memories — including one who dominated everyone locally and another who discovered a friend had subtly marked pieces to cheat. The most substantive point came from a commenter who argued the sample-efficiency gain (about 34x fewer games than DeepNash) is the critical piece, since in hidden-information games the best move depends on things you cannot know, making look-ahead search impossible; others joked about having planned to build the first winning bot themselves.

**Tags**: `#AI`, `#game-playing`, `#imperfect-information`, `#reinforcement-learning`, `#research`

---

<a id="item-2"></a>
## [Greg Kroah-Hartman Dissects Anthropic's Mythos Kernel Bug Claims](https://www.youtube.com/watch?v=NnV_cWeoo5Q) ⭐️ 8.0/10

In a Kernel Recipes 2026 talk titled "Security in the LLM Age," Linux kernel stable maintainer Greg Kroah-Hartman walked through Anthropic's claim that its Mythos model had discovered 79 Linux kernel vulnerabilities and showed that the list collapses to roughly one hour of real kernel development work. His slide breakdown classified the 79 items as 24 with no detail beyond "something crashed," 14 that were not bugs at all, 3 with fabricated data, 15 already fixed in the latest release (11 by other developers, 4 by Anthropic) and only 20 that actually required fixes. The talk is a rare, evidence-based rebuttal from one of the most credible figures in kernel development to the wave of AI-driven vulnerability disclosure, and it directly challenges the framing that frontier models are so dangerous they must be restricted while simultaneously being marketed as security breakthroughs. It matters for kernel maintainers, security engineers and anyone evaluating LLM-based vulnerability scanning, because low-quality or already-fixed reports waste scarce maintainer time and can distort public perception of software risk. Of the 20 findings that did require fixes, Kroah-Hartman noted that 7 depended on the assumption of a malicious filesystem image and 2 required an attacker who can already inject data, meaning many were not remotely exploitable in realistic threat models. He also pointed out that the approach amounted to pattern matching over decades of existing kernel developer patches, applied elsewhere to check whether the same fix had been universally propagated, and that Anthropic did not credit the original developers who fixed those CVEs.

hackernews · usernomdeguerre · Oct 2, 02:51 · [Discussion](https://news.ycombinator.com/item?id=49929391)

**Background**: Greg Kroah-Hartman is the maintainer of the Linux kernel's stable and longterm release branches and one of the most prolific kernel contributors, giving his assessment unusual weight. Kernel Recipes is a well-known annual Linux kernel developers' conference, and a CVE is the standard public identifier for a disclosed security vulnerability. Anthropic's Mythos is a frontier model the company has described as too dangerous for open release, and it promoted the 79-vulnerability kernel finding as evidence of its security capabilities, which is what Kroah-Hartman's talk examines.

<details><summary>References</summary>
<ul>
<li><a href="https://imiel.dev/blog/anthropic-mythos-disclosure-ledger-2026-teardown">1,611 Bugs Found, 27 Fixed: Anthropic 's Fire Hose... | Imiel Visser</a></li>
<li><a href="https://webdinavia.com/blog/anthropic-mythos-model">Anthropic 's Mythos Model Deemed Too Dangerous for Public</a></li>
<li><a href="https://vuldb.com/article/llm-generated-cve-descriptions-undermine-security-data-quality-and-trust">LLM Generated CVE Descriptions Undermine Security Data Quality...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters broadly welcomed Kroah-Hartman's candor, with several quoting the slide breakdown and summarizing the whole episode as "one hour of kernel development." A recurring criticism was that Anthropic relied on pattern matching over prior kernel developer patches without citing the people who originally fixed those CVEs, and commenters found the dissonance stark between safety-marketing claims that the model is too dangerous to release and this modest real-world security output.

**Tags**: `#LLM security`, `#kernel development`, `#AI safety`, `#vulnerability disclosure`, `#open source`

---

<a id="item-3"></a>
## [Google Research's Cogentic Coordinates Multi-Agent LLMs to Discover New Math Proofs](https://arxiv.org/abs/2609.40324v1) ⭐️ 8.0/10

Google Research has introduced Cogentic, a multi-agent proof-discovery system built on Gemini that runs a "prove–verify" loop: several independent provers explore different directions while a dedicated component performs adversarial verification, and confirmed results are written into a persistent verification ledger. According to the report, the system produced new results on five open problems in online learning, auction theory, and mechanism design, all independently verified by domain experts and written up in an accompanying paper. If confirmed, this marks a step beyond LLMs solving textbook or competition problems toward contributing genuinely new results on open research questions in theoretical computer science, and it suggests multi-agent orchestration plus adversarial verification could become a standard architecture for trustworthy AI-assisted research. It would matter most to researchers in theoretical CS, machine learning theory, and the growing field of AI-for-mathematics, where the bottleneck is no longer generating candidate arguments but reliably checking them. A key design detail is the feedback loop: lemmas that survive verification are promoted into a persistent ledger, while failed attempts and the verifier's critiques feed into later briefings so progress carries across rounds. The system reportedly works from the problem statement alone with no expert hints, and it also targets inference efficiency; however, this news comes from a brief Telegram post with no accompanying discussion, and the arXiv identifier (2609.40324) looks unusual, so the findings should be treated as unverified until the paper itself is examined.

telegram · zaihuapd · Oct 2, 12:04

**Background**: Automated theorem proving has traditionally relied on interactive proof assistants such as Coq and Lean, in which every step is machine-checked. Recent LLM work has combined language models with such checkers, but most successes have been on known problems or formalization of existing proofs rather than on open questions. Cogentic sits in a newer line of multi-agent designs: instead of asking one model for an answer, it runs several agents in parallel, adds an explicitly adversarial verifier whose job is to falsify claims, and keeps a ledger of what has and has not been established. The open problems mentioned — online learning, auction theory and mechanism design — are areas of theoretical computer science where new theorems are normally the product of months of human effort.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.40324">Cogentic: Multi - Agent Orchestration for Automated Proof Discovery</a></li>
<li><a href="https://agihunt.info/en/e/1a0f9cea5c8b68af181e13c5f80">Google 's Cogentic Multi - Agent System Tackles… · AGI Hunt</a></li>
<li><a href="https://academy.dair.ai/papers/cogentic-multi-agent-orchestration-for-automated-proof-discovery-2609.40324?ref=symbolika.ai">Cogentic: Multi-Agent Orchestration for Automated Proof Discovery</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#AI for mathematics`, `#theorem proving`, `#Google Research`, `#Gemini`

---

<a id="item-4"></a>
## [Claude Code adds a TypeScript-based mods system](https://claude.com/blog/claude-code-mods) ⭐️ 8.0/10

Anthropic launched Claude Code mods, a feature that lets developers rewrite prompts, add new interface elements, or replace built-in functionality with a small amount of TypeScript code. Mods are distributed alongside plugins and are now supported in both the CLI and the desktop app, with some built-in features already converted into mods and more migrations planned. This is a notable extensibility milestone for one of the most widely used AI coding tools, turning previously hard-coded built-in features into user-replaceable plugins and giving teams a way to shape the agent's behavior to their own workflows. It also signals that the "everything is a plugin" architecture is becoming a competitive norm among agent harnesses, as illustrated by DeepSeek Harness's similar design. Mods run with the same permissions as Claude Code itself and are not sandboxed, so Anthropic explicitly warns users to only install them from trusted sources; users can also have Claude write mods on their own. Because mods can replace built-in features, installing one from an untrusted plugin effectively grants it the same trust level as the tool itself.

telegram · zaihuapd · Oct 2, 12:32

**Background**: Claude Code is Anthropic's agentic command-line coding tool, which reads and edits files, runs commands, and completes coding tasks on a developer's machine. An extensibility layer like mods lets third parties and users change the agent's default behavior without waiting for Anthropic to ship features. DeepSeek Harness, an open-source agent harness from DeepSeek, is built on a comparable "everything is a plugin" architecture, which is why its team drew the parallel between the two designs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://www.deepseek.com/en/harness/">DeepSeek Harness | Explore the limits of intelligence</a></li>
<li><a href="https://deepseekharness.dev/">DeepSeek Harness - AI Agent Framework Installation & Usage Guide</a></li>

</ul>
</details>

**Discussion**: After the release, DeepSeek Harness team lead Cui Tianyi quoted an Anthropic staffer's post on X to offer congratulations and explain how the feature resembles DeepSeek Harness's "everything is a plugin" design. The community reaction was broadly positive, with commenters joking that good designs think alike.

**Tags**: `#AI coding tools`, `#Claude Code`, `#Anthropic`, `#extensibility`, `#developer tools`

---