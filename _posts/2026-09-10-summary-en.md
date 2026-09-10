---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 35 items, 3 important content pieces were selected

---

1. [Shopify migrates its mobile app from React Native back to native Swift and Kotlin](#item-1) ⭐️ 8.0/10
2. [Researchers question whether OpenAI can be trusted with unpublished math](#item-2) ⭐️ 8.0/10
3. [Microsoft Declares Rust a Tier-1 Language for Internal Development](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Shopify migrates its mobile app from React Native back to native Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify announced it is migrating its flagship mobile app off React Native and back to fully native iOS and Android codebases written in Swift and Kotlin. The engineering blog post prompted a large Hacker News discussion (roughly 670 points and 447 comments) about cross-platform frameworks, migration cost, and whether LLM-assisted rewrites make such moves cheaper. Shopify is one of the highest-profile companies to abandon React Native, and its decision adds momentum to a broader industry swing back toward native mobile development. Because it is a large e-commerce app with global scale, the move signals to other teams that cross-platform savings may not outweigh the cost of a lowest-common-denominator UX and long-term maintenance. The discussion highlights that the app has a large, mature surface area, and community members note that modern LLMs (such as codex-style coding agents with tools like Maestro for UI testing) can automate much of the mechanical porting work, though polish and platform-specific optimization still require human effort. Commenters also caution that claims of LLMs making migrations trivially cheap are overstated, since engineers had completed similar RN-to-native rewrites before 2026 without LLM assistance.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is an open-source UI framework from Meta that lets developers build apps for iOS, Android and other platforms using JavaScript and React, sharing one codebase across platforms. Swift is Apple's native language for iOS, and Kotlin is Google's first-class language for Android; writing in them separately gives full access to platform APIs and performance but requires two separate codebases and teams. For nearly two decades, teams have debated whether cross-platform frameworks truly reduce engineering headcount or simply trade staffing savings for a weaker per-platform experience.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native - Wikipedia</a></li>
<li><a href="https://reactnative.dev/">React Native · Learn once, write anywhere</a></li>
<li><a href="https://arxiv.org/abs/2410.08806">[2410.08806] Don't Transform the Code, Code the Transforms: Towards Precise Code Rewriting using LLMs</a></li>

</ul>
</details>

**Discussion**: Sentiment is broadly supportive of moving off React Native, but commenters disagree about the reasons: one engineer says they achieved a 90% automated port overnight using a coding agent and Maestro, while another argues the 'LLM made migration affordable' narrative is wrong, having done a similar rewrite by hand before LLM tooling matured. A long-time observer notes teams repeatedly assume cross-platform frameworks cut headcount, only to discover they inherit a lowest-common-denominator app without the promised savings, and several people argue that now that code is increasingly generated, React Native's main advantage — letting web developers ship mobile apps — is eroding.

**Tags**: `#React Native`, `#Mobile Development`, `#Swift`, `#Kotlin`, `#Cross-Platform`

---

<a id="item-2"></a>
## [Researchers question whether OpenAI can be trusted with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

A post on the mathstodon.xyz Mastodon instance sparked a widely-read Hacker News debate (about 577 points and 579 comments) over whether mathematicians can safely share unpublished work with OpenAI, given concerns about attribution and confidentiality. Commenters argue over whether OpenAI's models can leak ideas sighted in user chats into later pretraining or whether superhuman results come purely from large-scale reinforcement learning on verifiable math. The episode crystallizes a broader trust problem for AI-for-science: if frontier labs can absorb unpublished ideas from researchers who use their models, traditional norms of attribution and priority in mathematics and other fields could break down. It also feeds into existing worries, such as the Leiden Declaration on AI and Mathematics, that reliance on AI proofs and proprietary models will skew research agendas and disadvantage those without access. The key technical crux is whether a model's parameters can memorize and generalize from ideas seen in user chats during pretraining, versus whether results emerge from reinforcement learning on verifiable math problems with massive compute; one commenter notes the data is many orders of magnitude larger than the model. A recurring, more skeptical point is that generating roughly 300 billion output tokens from a model still in training, shortly after learning a major proof may have been in its training data, looks like 'parallel construction'.

hackernews · pred_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: Pretraining is the stage where a language model learns statistical patterns from enormous text corpora, and reinforcement learning (RL) is a later stage that rewards a model for solving problems correctly, for example verifiable math problems with known answers. Because frontier labs keep model weights and training mixtures secret, outsiders cannot easily tell whether a specific result came from general reasoning or from memorized user input. Traditional mathematics relies on public attribution and priority, so any ambiguity about where an idea originated is unusually sensitive in that community.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Leiden_Declaration_on_Artificial_Intelligence_and_Mathematics">Leiden Declaration on Artificial Intelligence and Mathematics</a></li>
<li><a href="https://www.nature.com/articles/s41567-025-03042-0">Mathematical discovery in the age of artificial intelligence</a></li>
<li><a href="https://mastodonservers.net/server/1470-mathstodon">Mathstodon Mastodon Server Instance</a></li>

</ul>
</details>

**Discussion**: Sentiment is largely skeptical of OpenAI. One highly-rated analogy compares OpenAI to a human collaborator: if a human had taken shared ideas and published without attribution, it would be considered deeply unethical, which is why many feel the same standard should apply here. Others argue both explanations can be true at once, and one commenter dismisses the concern as moot because the work is still 'brute force in a verifiable domain'.

**Tags**: `#OpenAI`, `#research-ethics`, `#AI-for-math`, `#trust`, `#Hacker-News`

---

<a id="item-3"></a>
## [Microsoft Declares Rust a Tier-1 Language for Internal Development](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

In a guest post published by the Rust Foundation, Microsoft formally designated Rust as a 'tier-1 language' for internal development, placing it alongside C++, C#, and TypeScript as one of its best-supported languages. This engineering status means Rust now receives first-class tooling, build, and support investment within Microsoft. The designation is a major mainstream validation for Rust, signaling that a platform vendor with deep C/C++ roots considers the language ready for large-scale enterprise systems work and reducing institutional resistance to adopting it for greenfield projects. It also means every major OS vendor with a stake in C and C++ tooling has now diversified its systems-programming options. Community discussion points to Microsoft's stated ambition to convert roughly 1 billion lines of C/C++ to Rust by 2030 through automated tooling, and to the notable technical detail that Rust's LLVM backend has reportedly been replaced by MSVC's backend. Note that much of this is strategic positioning and reported rumour rather than a shipped technical release, so concrete toolchain timelines remain unclear.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**Background**: Rust is a general-purpose systems programming language created at Mozilla and first stabilized in 2015; it enforces memory safety at compile time via its 'borrow checker' rather than a garbage collector. This matters because memory-safety bugs have historically accounted for a large share of security vulnerabilities in C and C++ codebases, including Microsoft's own. A 'tier-1 language' at Microsoft is one that the company officially supports for internal engineering, meaning it gets dedicated build tooling, documentation, and ecosystem investment comparable to its flagship languages.

<details><summary>References</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier - 1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language)</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-msvc?view=msvc-170">What's new for MSVC Build Tools | Microsoft Learn</a></li>

</ul>
</details>

**Discussion**: The Hacker News thread (576 points, 313 comments) was broadly positive, with commenters framing the move as proof that Rust is no longer a 'fledgling' language but a mature competitor to C++ and C#, and highlighting the reported MSVC backend integration as the real headline. Others added concrete context such as Microsoft's 1-billion-line migration goal and DARPA-funded work on automated C-to-Rust translation, while some noted that newer 'better C/C++' alternatives like Zig and Odin still have rougher edges, and debated whether this is strategic validation rather than a technical breakthrough.

**Tags**: `#rust`, `#microsoft`, `#systems-programming`, `#memory-safety`, `#programming-languages`

---