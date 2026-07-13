---
layout: default
title: "Horizon Summary: 2026-07-13 (EN)"
date: 2026-07-13
lang: en
---

> From 19 items, 6 important content pieces were selected

---

1. [Telegram's t.me Domain Suspended, Sparks Speculation](#item-1) ⭐️ 8.0/10
2. [LAPD Ends Flock Surveillance Contract Amid Privacy Concerns](#item-2) ⭐️ 8.0/10
3. [DOOMQL: A Doom-like game powered entirely by SQLite queries](#item-3) ⭐️ 8.0/10
4. [CoT Is a Scaling Trap; Latent Reasoning Is the Next Wave](#item-4) ⭐️ 8.0/10
5. [Reddit Debate: What Is Continual Learning?](#item-5) ⭐️ 8.0/10
6. [Open-source tool filters arXiv papers by research interests](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Telegram's t.me Domain Suspended, Sparks Speculation](https://www.whois.com/whois/t.me) ⭐️ 8.0/10

Telegram's t.me domain, used for short links, has been suspended, as confirmed by WHOIS lookup showing disabled status codes. This disruption affects millions of Telegram users globally and raises concerns about the platform's reliance on GoDaddy as registrar, which has a history of opaque domain actions. The domain's status codes include clientRenewProhibited and serverDeleteProhibited, which ICANN documentation indicates are typically used during legal disputes or when deletion is pending.

hackernews · Tiberium · Jul 13, 19:52 · [Discussion](https://news.ycombinator.com/item?id=48897878)

**Background**: Telegram is currently under legal and regulatory investigations in Russia, France, and India for various allegations. The t.me domain is a shortcut used by Telegram for sharing content.

**Discussion**: Community comments express surprise that Telegram uses GoDaddy, known for lack of transparency, and note that the suspension may relate to India's investigation into exam cheating. One user highlights the importance of using redirects instead of direct third-party domain links.

**Tags**: `#Telegram`, `#domain suspension`, `#ICANN`, `#GoDaddy`, `#regulatory investigation`

---

<a id="item-2"></a>
## [LAPD Ends Flock Surveillance Contract Amid Privacy Concerns](https://techcrunch.com/2026/07/13/lapd-lets-contract-with-surveillance-giant-flock-expire-citing-serious-concerns-over-civil-liberties-and-privacy/) ⭐️ 8.0/10

The Los Angeles Police Department has allowed its contract with Flock Safety to expire, citing serious concerns over civil liberties and privacy. However, the cameras remain operational and continue collecting data that Flock can sell to other agencies. This decision highlights the tension between law enforcement surveillance and civil liberties, and reveals a loophole where private surveillance infrastructure persists even after contract termination. It underscores the challenge of regulating data collection by private companies that supply government agencies. Flock Safety owns the cameras and poles, so even without an LAPD contract, the cameras continue to record data that can be sold to other entities like CHP, LASB, FBI, and Palantir. The LAPD could also access data informally, making the contract expiration largely symbolic.

hackernews · forks · Jul 13, 15:11 · [Discussion](https://news.ycombinator.com/item?id=48893947)

**Background**: Flock Safety is a surveillance company specializing in automated license plate recognition (ALPR) systems, which capture vehicle license plate data, photos, and location information. ALPR technology is used by law enforcement for tracking vehicles but has raised mass surveillance and privacy concerns. The LAPD's decision reflects broader debates about the balance between public safety and privacy rights.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.cnet.com/home/security/when-flock-comes-to-town-why-cities-are-axing-the-controversial-surveillance-technology/">When Flock Surveillance Comes to Your Town: Everything to Know ... - CNET</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the contract expiration's impact, noting Flock cameras remain active and data is accessible to other agencies. One user highlighted high recidivism rates despite surveillance, questioning its effectiveness. Another argued it should be illegal for government to buy data it couldn't legally collect itself.

**Tags**: `#surveillance`, `#privacy`, `#civil liberties`, `#Flock`, `#LAPD`

---

<a id="item-3"></a>
## [DOOMQL: A Doom-like game powered entirely by SQLite queries](https://simonwillison.net/2026/Jul/13/doomql/#atom-everything) ⭐️ 8.0/10

Peter Gostev released DOOMQL, a Doom-like game where SQLite handles all game logic including movement, collision, enemy AI, and rendering through SQL queries. The game runs as a Python terminal script and uses a recursive CTE to implement a full ray tracer in SQLite. This project demonstrates an extremely novel use of SQLite as a complete game engine, pushing the boundaries of what a database can do. It inspires software engineers to think creatively about using databases beyond traditional roles and showcases the power of SQL for complex computations. The game is implemented as a Python terminal script and can be run with `uv run host/doomql.py`. It creates a SQLite database that can be explored with Datasette, and Simon Willison used Datasette Apps to build a live-refreshing web interface with a minimap. The rendering is done via a huge SQL query that implements ray tracing using a recursive CTE.

rss · Simon Willison · Jul 13, 22:34

**Background**: SQLite is a lightweight, embedded SQL database engine widely used in applications for data storage. Recursive CTEs (Common Table Expressions) allow SQL queries to perform iterative computations, which is leveraged here for ray tracing. The uv tool is an extremely fast Python package manager written in Rust, used to run the project. Datasette is a tool for exploring and publishing SQLite databases, and Datasette Apps lets users build custom HTML/JavaScript apps that query the database.

<details><summary>References</summary>
<ul>
<li><a href="https://forum.openmw.org/viewtopic.php?t=7193">SQLite based approach to storing game world state - openmw.org</a></li>
<li><a href="https://github.com/astral-sh/uv">GitHub - astral-sh/uv: An extremely fast Python package and project manager, written in Rust. · GitHub</a></li>
<li><a href="https://medium.com/@dieggo.filipe/uv-the-new-python-package-manager-you-need-to-know-491a147af74c">UV: The New Python Package Manager You Need to Know! | by Diego Lima | Medium</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#game-development`, `#python`, `#novel-approach`, `#doom`

---

<a id="item-4"></a>
## [CoT Is a Scaling Trap; Latent Reasoning Is the Next Wave](https://www.reddit.com/r/MachineLearning/comments/1uviru5/chain_of_thought_is_a_scaling_trap_the_next_wave/) ⭐️ 8.0/10

A Reddit post argues that Chain-of-Thought (CoT) reasoning is a costly interface artifact rather than a scalable path, and proposes that the next wave of LLM reasoning will shift into latent space, with methods like Coconut, HRM, and RecursiveMAS. This discussion highlights a critical limitation of current LLM reasoning—autoregressive token generation is inefficient and unfaithful—and points toward emerging latent reasoning approaches that could drastically reduce cost and latency while improving reasoning depth, but also introduces new governance challenges. The post identifies faithfulness and system cost as two practical problems of CoT, then surveys latent reasoning methods: Coconut uses continuous latent steps, HRM separates planning from execution, and RecursiveMAS passes latent embeddings between agents. BDH (Dragon Hatchling) aims to combine latent iteration with principled state management, achieving 97.4% accuracy on Sudoku without CoT.

reddit · r/MachineLearning · /u/meowsterpieces · Jul 13, 17:50

**Background**: Chain-of-Thought (CoT) reasoning forces LLMs to generate intermediate textual steps, which is interpretable but expensive and can be unfaithful. Latent reasoning methods perform internal computations in a continuous vector space without generating tokens, reducing cost and allowing deeper recursion, but lose direct visibility of the reasoning process.

<details><summary>References</summary>
<ul>
<li><a href="https://ht0324.github.io/blog/2025/Coconut/">Continuous Latent Reasoning for LLMs ( COCONUT ) - Review</a></li>
<li><a href="https://github.com/sapientinc/HRM-Text">GitHub - sapientinc/HRM-Text: HRM-Text is a 1B text generation model based on the HRM architecture, strengthened by task completion and latent space reasoning. · GitHub</a></li>
<li><a href="https://recursivemas.github.io/">Recursive Multi-Agent Systems</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#LLM reasoning`, `#chain-of-thought`, `#latent reasoning`, `#AI research`

---

<a id="item-5"></a>
## [Reddit Debate: What Is Continual Learning?](https://www.reddit.com/r/MachineLearning/comments/1uvm2p4/whats_your_take_on_continual_learning_d/) ⭐️ 8.0/10

A Reddit discussion questions the definition and importance of continual learning, referencing Dario Amodei's prediction that it will be achieved by 2026 and Demis Hassabis's claim that it is the most important unsolved breakthrough for AGI. Continual learning is widely considered a key bottleneck on the path to AGI, yet its definition remains contested, causing confusion in research and industry. Clarifying what continual learning truly requires could accelerate progress toward more general AI. The discussion highlights that continual learning is often conflated with catastrophic forgetting, online learning, lifelong learning, or meta-learning, and questions whether the bottleneck is architectural, data-related, or fundamental to evaluation and benchmarking.

reddit · r/MachineLearning · /u/watercolorer2024 · Jul 13, 19:47

**Background**: Continual learning aims to enable AI models to learn sequentially without forgetting previous knowledge, addressing the stability-plasticity dilemma. Catastrophic forgetting, where neural networks rapidly lose old information when trained on new data, is a major challenge. Meta-learning, or 'learning to learn,' is a related but distinct concept focused on optimizing the learning process itself.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Catastrophic_forgetting">Catastrophic forgetting</a></li>
<li><a href="https://en.wikipedia.org/wiki/Meta-learning_(computer_science)">Meta-learning (computer science) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#continual learning`, `#AGI`, `#catastrophic forgetting`, `#AI research`, `#machine learning`

---

<a id="item-6"></a>
## [Open-source tool filters arXiv papers by research interests](https://www.reddit.com/r/MachineLearning/comments/1uvcdf7/hundreds_of_papers_hit_arxiv_every_day_and_maybe/) ⭐️ 8.0/10

A developer created Research Radar, an open-source tool that automatically fetches arXiv papers, scores them against a user's custom research interests, and summarizes the most relevant ones in a daily digest. This tool addresses the common pain point of information overload for researchers, saving 30-60 minutes daily by surfacing only the papers that matter, and its domain-agnostic design makes it useful across fields like ML, physics, and biology. Research Radar uses a two-pass scoring system: a cheap model for abstract skimming and a strong model for full-text deep reading, with costs benchmarked in the repo. It is model-agnostic, supporting Claude, Codex, or local models via Ollama/vLLM.

reddit · r/MachineLearning · /u/usedtobreath · Jul 13, 13:59

**Background**: arXiv is a preprint repository where thousands of papers are posted daily, making it challenging for researchers to stay current with relevant work. Many use RSS feeds or newsletters, but these often highlight popular rather than personalized content. Research Radar automates the filtering and summarization process by scoring papers against a user's stated interests.

**Tags**: `#arXiv`, `#research tool`, `#NLP`, `#open source`, `#machine learning`

---