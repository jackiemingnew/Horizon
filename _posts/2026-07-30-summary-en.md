---
layout: default
title: "Horizon Summary: 2026-07-30 (EN)"
date: 2026-07-30
lang: en
---

> From 38 items, 18 important content pieces were selected

---

1. [OpenAI cuts GPT-5.6 Luna price by 80%](#item-1) ⭐️ 9.0/10
2. [Kimi K3: Open-Weight Model Reaches Frontier via Novel Techniques](#item-2) ⭐️ 9.0/10
3. [AI Finds Major Weakness in NIST Post-Quantum Candidate HAWK](#item-3) ⭐️ 9.0/10
4. [Cheap TV Streaming Sticks Pose Serious Security Risks](#item-4) ⭐️ 8.0/10
5. [GitHub Launches Stacked Pull Requests in Public Preview](#item-5) ⭐️ 8.0/10
6. [Gemini Robotics 2 integrates whole body intelligence for robots](#item-6) ⭐️ 8.0/10
7. [UEFA Boycotts FIFA Competitions Over Governance Concerns](#item-7) ⭐️ 8.0/10
8. [Muon Mystery Solved, Old Calculations Overturned](#item-8) ⭐️ 8.0/10
9. [Google to Expand Age Checks on Android Worldwide by Year End](#item-9) ⭐️ 8.0/10
10. [Economic Analysis of Refactoring with AI](#item-10) ⭐️ 8.0/10
11. [GCC Steering Committee Announces AI Contribution Policy](#item-11) ⭐️ 8.0/10
12. [Schneier: AI Writing Tasks Atrophy Critical Thinking](#item-12) ⭐️ 8.0/10
13. [Professor Loses PhD Candidates Over Conference Review Process](#item-13) ⭐️ 8.0/10
14. [MLVC: Solving Cross-Platform Compatibility for Learned Video Codecs](#item-14) ⭐️ 8.0/10
15. [ByteDance Restructures To B: Feishu Merged with Doubao and Volcano Engine](#item-15) ⭐️ 8.0/10
16. [US Senators Warn Apple Against Buying Chinese Memory Chips](#item-16) ⭐️ 8.0/10
17. [Google DeepMind Disbands Nobel-Winning AlphaFold Team](#item-17) ⭐️ 8.0/10
18. [EU Launches AI Super Factory Tender, Aims for €30B Investment](#item-18) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI cuts GPT-5.6 Luna price by 80%](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) ⭐️ 9.0/10

OpenAI announced an 80% price reduction for GPT-5.6 Luna, its fastest and most affordable model, making it five times cheaper than before. This dramatic price cut advances the price-performance frontier, enabling enterprises to run five times more inference for the same cost and potentially accelerating AI adoption at scale. The cost reduction was achieved through kernel optimizations that reduced serving cost by 20% and efficiency experiments that improved token-generation efficiency by over 15%.

hackernews · tedsanders · Jul 30, 17:15 · [Discussion](https://news.ycombinator.com/item?id=49112867)

**Background**: GPT-5.6 is a family of models released by OpenAI in July 2026, featuring three tiers: Sol (flagship), Terra (mid-range), and Luna (fastest and most affordable). The price cut comes amid a broader trend of falling AI model prices, with competitors like Kimi K3 and GLM 5.2 also reducing costs.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/">Advancing the price - performance frontier with GPT-5.6 | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise and excitement at the 80% cut, with some comparing it to the dial-up to broadband transition. Others noted that many tasks don't require the most capable model, and this price drop makes Luna even more attractive for high-volume inference. There was speculation about OpenAI's internal cost savings and whether this signals a new phase of price competition.

**Tags**: `#AI`, `#OpenAI`, `#GPT-5.6`, `#pricing`, `#machine learning`

---

<a id="item-2"></a>
## [Kimi K3: Open-Weight Model Reaches Frontier via Novel Techniques](https://www.reddit.com/r/MachineLearning/comments/1vaysjf/how_kimi_k3_engineered_its_way_to_the_frontier_r/) ⭐️ 9.0/10

Moonshot's Kimi K3 open-weight model ranks fourth among 580 models on Artificial Analysis, achieved through three key innovations: Kimi Delta Attention, quantile balancing for mixture-of-experts, and AgentENV for scalable reinforcement learning. This demonstrates that open-weight models can compete with proprietary frontier models like Claude Opus 5 and GPT-5.6 Sol, and the released code and detailed report advance the entire field of efficient attention and expert load balancing. Kimi Delta Attention replaces the KV cache in 69 of 93 layers with a 128x128 matrix per head, reducing memory for a 1M-token context from 104.6 GiB to 27.2 GiB. Quantile Balancing eliminates hyperparameters by computing bias directly from router score margins, enabling 896 experts per layer.

reddit · r/MachineLearning · /u/noninertialframe96 · Jul 30, 16:37

**Background**: Kimi K3 is a Mixture-of-Experts (MoE) language model with 2.8 trillion parameters, using only about 30B activated per forward pass. Standard multi-head attention uses a key-value (KV) cache that grows linearly with sequence length, which becomes prohibitive for long contexts. Delta attention is a linear attention variant that compresses the KV cache into a fixed-size matrix. In Mixture-of-Experts models, maintaining balanced expert utilization is challenging; previous methods like auxiliary loss or bias nudging require tuning, but quantile balancing reformulates the problem as a linear program. AgentENV is an open-source reinforcement learning runtime based on Firecracker microVMs, providing fast checkpoint and resume for agentic tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://openathena.ai/blog/quantile-balancing/">Mixture of Experts Quantile Balancing: Validated at 32B-A5B (1e22 FLOPs) Scale | Open Athena</a></li>
<li><a href="https://www.marktechpost.com/2026/07/27/kimi-ai-and-kvcache-ai-open-sources-agentenv/">Kimi AI and kvcache-ai Open Sources ' AgentENV ... - MarkTechPost</a></li>

</ul>
</details>

**Tags**: `#efficient attention`, `#mixture of experts`, `#reinforcement learning`, `#language models`, `#open-weight model`

---

<a id="item-3"></a>
## [AI Finds Major Weakness in NIST Post-Quantum Candidate HAWK](https://startupfortune.com/claude-mythos-broke-hawk-and-the-nist-post-quantum-timeline-may-not-survive-it/) ⭐️ 9.0/10

Anthropic's Claude Mythos Preview model discovered a severe cryptographic weakness in NIST post-quantum candidate HAWK within 60 hours, reducing its key strength from 2^64 to 2^38 bits. This demonstrates AI's growing capability to accelerate cryptanalysis, potentially impacting the timeline for post-quantum cryptography standardization and federal migration deadlines set by the White House. The attack cost approximately $100,000 in API fees and does not break HAWK in polynomial time, meaning larger parameter sets remain secure. The study also included an improved attack on 7-round AES-128, but full AES-128 remains unaffected.

telegram · zaihuapd · Jul 30, 05:47

**Background**: HAWK is a lattice-based digital signature scheme selected as a candidate in NIST's post-quantum cryptography standardization process. NIST is running a competition to select quantum-resistant algorithms to replace current standards like RSA and ECC, which are vulnerable to future quantum computers. The security of HAWK relies on the Lattice Isomorphism problem. AI's ability to find flaws quickly raises questions about the evaluation process for post-quantum candidates.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/321876/20260728/ai-cracks-post-quantum-cipher-60-hours-after-two-years-human-review-failed.htm">AI Cracks Post-Quantum Cipher in 60 Hours After Two Years of Human Review Failed</a></li>
<li><a href="https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization">NIST Post-Quantum Cryptography Standardization</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#post-quantum`, `#AI`, `#Anthropic`, `#NIST`

---

<a id="item-4"></a>
## [Cheap TV Streaming Sticks Pose Serious Security Risks](https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/) ⭐️ 8.0/10

An article on KrebsOnSecurity warns that inexpensive streaming sticks often come pre-infected with malware, used for residential proxy and ad fraud, and that major retailers continue to sell these devices despite repeated FBI warnings. These devices are widely used, creating a massive botnet threat that could be activated to attack critical infrastructure, potentially affecting millions of homes. The article highlights the lack of retailer accountability and the ease with which attackers can exploit insecure IoT devices. Some streaming sticks ship with a non-disableable ad overlay and are designed to perform ad fraud and residential proxy services. They often run outdated Android versions with no security patches, making them vulnerable to no-click exploits.

hackernews · speckx · Jul 30, 17:04 · [Discussion](https://news.ycombinator.com/item?id=49112744)

**Background**: A botnet is a network of compromised devices controlled remotely by an attacker, often used for DDoS attacks, data theft, or ad fraud. IoT devices like streaming sticks are particularly vulnerable because they often lack security updates and are not regularly monitored. The FBI and security industry have repeatedly warned about the risks of cheap, unverified streaming devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Botnet">Botnet</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/data-and-ai/iot-security-risks/">Top 10 IoT Security Risks and How to Mitigate Them</a></li>

</ul>
</details>

**Discussion**: Comments expose deeper concerns: one user notes the potential for a massive, unblockable botnet spanning U.S. and Russian homes; another criticizes retailers for escaping responsibility. A user shares a personal experience with a projector displaying persistent ads, while others debate whether incompetence or malice is the greater threat. One comment suggests using a computer for full control.

**Tags**: `#security`, `#IoT`, `#streaming devices`, `#botnet`, `#privacy`

---

<a id="item-5"></a>
## [GitHub Launches Stacked Pull Requests in Public Preview](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/) ⭐️ 8.0/10

GitHub has rolled out stacked pull requests in public preview, allowing developers to create a chain of dependent PRs that can be reviewed and merged sequentially. This feature enables developers to break large changes into smaller, incremental PRs, improving code review efficiency and reducing merge conflicts in complex workflows. The stacked PRs feature is available via a GitHub CLI extension (`gh stack`) and through the GitHub UI, with support for automatic dependency tracking across the stack.

hackernews · tomzorz · Jul 30, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49112232)

**Background**: Traditionally, developers working on large features had to either create a single massive PR or manage multiple dependent branches manually. Stacked pull requests formalize this workflow by allowing PRs to be built on top of each other, each containing a logical chunk of work, which can be reviewed and merged independently once the base PR is merged.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/en/pull-requests/how-tos/stacked-pull-requests">Stacked pull requests - GitHub Docs</a></li>
<li><a href="https://docs.github.com/en/pull-requests/tutorials/roll-out-stacked-prs">Roll out stacked pull requests to your organization - GitHub Docs</a></li>
<li><a href="https://docs.github.com/en/pull-requests/get-started/about-stacked-prs">About stacked pull requests - GitHub Docs</a></li>

</ul>
</details>

**Discussion**: The community is excited about the feature, with developers like steveklabnik calling it "one of the biggest changes to hit GitHub in years." However, concerns were raised about bugs — for instance, matharmin reported that merging an entire stack is often broken, and using squash+merge requires re-approval for each PR, undermining the workflow benefits.

**Tags**: `#GitHub`, `#pull requests`, `#stacked PRs`, `#development workflow`, `#version control`

---

<a id="item-6"></a>
## [Gemini Robotics 2 integrates whole body intelligence for robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) ⭐️ 8.0/10

Google DeepMind has announced Gemini Robotics 2, a new AI model that provides robots with whole body intelligence by combining deep spatial reasoning and long-horizon planning to handle complex, unfamiliar tasks. This represents a notable advancement in robotics AI, moving beyond simple task execution to more adaptive and autonomous behavior, which could accelerate the deployment of robots in homes, workplaces, and industrial settings. The model is based on the Gemini 2.0 language model and includes a variant called Gemini Robotics ER 2 for embodied reasoning, with access currently restricted to trusted testers such as Agile Robots, Boston Dynamics, and Apptronik.

hackernews · ai2027 · Jul 30, 15:15 · [Discussion](https://news.ycombinator.com/item?id=49111237)

**Background**: Gemini Robotics 2 builds on earlier vision-language-action models that allow robots to understand and interact with their environment. Whole body intelligence refers to the ability to coordinate the entire body—not just arms or grippers—to perform tasks that require spatial awareness and multi-step planning, such as navigating cluttered spaces or manipulating objects intelligently.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_Robotics">Gemini Robotics</a></li>
<li><a href="https://deepmind.google/models/gemini-robotics/">Gemini Robotics 2</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/">Introducing Gemini Robotics ER 2</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: a DeepMind researcher praises the lab's breadth of work, while others express skepticism about current robotics hardware limitations, such as poor actuators and slow motion. Some commenters draw parallels to the early days of large language models, suggesting that rapid progress could follow.

**Tags**: `#robotics`, `#AI`, `#Google DeepMind`, `#whole body intelligence`, `#Gemini`

---

<a id="item-7"></a>
## [UEFA Boycotts FIFA Competitions Over Governance Concerns](https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/) ⭐️ 8.0/10

UEFA and its 55 national associations have announced they will not participate in FIFA competitions, citing corruption and governance issues. This boycott could trigger a major restructuring of global football governance, potentially leading to a split in international football similar to a religious schism. The announcement came in a statement on UEFA's official website, and follows longstanding concerns over FIFA's leadership under Gianni Infantino and proposed expansion of World Cup to 48 or even 64 teams.

hackernews · dickfickling · Jul 30, 18:40 · [Discussion](https://news.ycombinator.com/item?id=49113929)

**Background**: UEFA is the governing body for European football, while FIFA governs world football. Tensions have escalated due to FIFA's commercial push and alleged corruption. UEFA has threatened to create its own alternative tournament.

**Discussion**: Commenters largely support UEFA's move, calling for Infantino's removal and criticizing FIFA's corruption. Some suggest UEFA should host its own World Cup, as the FIFA tournament has become overly commercialized. The discussion compares the situation to a fork in open-source software.

**Tags**: `#sports`, `#governance`, `#FIFA`, `#UEFA`, `#football`

---

<a id="item-8"></a>
## [Muon Mystery Solved, Old Calculations Overturned](https://www.quantamagazine.org/physicists-solve-a-muon-mystery-now-old-results-dont-add-up-20260729/) ⭐️ 8.0/10

Physicists have resolved the long-standing muon g-2 anomaly by using advanced lattice QCD calculations, showing that the previous discrepancy between experiment and theory was due to incomplete theoretical modeling. The updated Standard Model prediction now agrees with the experimental measurement. This resolution reaffirms the Standard Model of particle physics and eliminates a major hint of new physics that drove decades of research. It also underscores the critical role of precise theoretical calculations in interpreting experimental data. The Fermilab Muon g-2 experiment released its final results on June 3, 2025, after six years of data collection. The new lattice QCD calculations reduced the discrepancy from over 4 sigma to about 0.5 sigma, effectively solving the anomaly.

hackernews · ibobev · Jul 30, 15:22 · [Discussion](https://news.ycombinator.com/item?id=49111305)

**Background**: The muon's magnetic moment is slightly larger than predicted by the Dirac equation; this small difference, the anomalous magnetic moment, is sensitive to virtual particles. Measurements at Brookhaven and Fermilab showed a persistent deviation from the Standard Model prediction, suggesting possible new physics. However, improved lattice QCD calculations of the hadronic vacuum polarization contribution have now aligned theory with experiment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Muon_g−2_Experiment">Muon g−2 Experiment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Muon_g-2">Muon g-2 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anomalous_magnetic_moment">Anomalous magnetic moment</a></li>

</ul>
</details>

**Discussion**: The community reacted with a mix of humor and reflection; one commenter joked about avoiding a decade-long research dead end, while another drew parallels to the Copernican revolution. A lighthearted comment about 'worst Feynman diagrams ever' indicated playful banter.

**Tags**: `#physics`, `#muon`, `#particle physics`, `#anomaly`, `#quantum mechanics`

---

<a id="item-9"></a>
## [Google to Expand Age Checks on Android Worldwide by Year End](https://android-developers.googleblog.com/2026/07/google-play-age-signals-api-safer-experiences.html) ⭐️ 8.0/10

Google announced it will expand age verification checks on Android devices worldwide by the end of 2026, using a new Age Signals API in Google Play to provide safer experiences for minors. This move could reshape how age-restricted content is accessed on Android, but raises significant privacy and user experience concerns, especially around mandatory account creation and data handling. The Age Signals API allows apps to request age information from users, but does not mandate a single method; it supports both on-device age estimation and third-party privacy-preserving credentials. However, critics note that apps not integrating the API (like Telegram) could still expose minors to inappropriate content.

hackernews · dmantis · Jul 30, 10:13 · [Discussion](https://news.ycombinator.com/item?id=49107950)

**Background**: Age verification online is a growing regulatory requirement in many regions, but balancing privacy and effectiveness is challenging. On-device age estimation techniques analyze facial features entirely on the user's device without transmitting images, while zero-knowledge proof systems allow verification without revealing exact birth dates. Google's approach aims to provide a scalable solution but faces criticism for potential privacy intrusions and usability friction.

<details><summary>References</summary>
<ul>
<li><a href="https://www.incode.com/use-cases/on-device-age-estimation">On device age estimation</a></li>
<li><a href="http://newamerica.org/oti/briefs/exploring-privacy-preserving-age-verification/">Exploring Privacy-Preserving Age Verification: A Close Look at Zero-Knowledge Proofs</a></li>
<li><a href="https://didit.me/blog/privacy-preserving-age-verification/">Privacy-Preserving Age Verification: Verify Age Without Data</a></li>

</ul>
</details>

**Discussion**: Comments show a polarized debate: some users are fundamentally opposed to age verification, arguing it leads to mandatory accounts and reinforces monopolies. Others criticize Google's implementation as too complex, suggesting simpler 'parent mode' checkboxes. A few see potential in regulatory solutions but worry about data abuse by companies.

**Tags**: `#privacy`, `#android`, `#age verification`, `#google play`, `#policy`

---

<a id="item-10"></a>
## [Economic Analysis of Refactoring with AI](https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html) ⭐️ 8.0/10

Martin Fowler's article quantifies the economic benefits of refactoring code, including when assisted by AI, and discusses how AI can be aligned with software engineering best practices. This analysis provides concrete data to support refactoring decisions, helping teams justify time spent on improving code quality, especially in the context of AI-generated code. The article includes quantitative measurements showing that refactoring reduces token consumption for AI models and improves reasoning, and it emphasizes that AI should follow the same best practices as human developers.

hackernews · javaeeeee · Jul 30, 15:10 · [Discussion](https://news.ycombinator.com/item?id=49111176)

**Background**: Technical debt refers to the extra cost incurred when choosing a quick solution over a more robust one, leading to higher maintenance costs over time. Refactoring is the practice of restructuring code to reduce technical debt without changing its external behavior. Martin Fowler is a renowned author in software engineering, particularly known for his work on refactoring.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technical_debt">Technical debt - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters note that best practices long ignored by companies are being rediscovered for AI, such as keeping documentation in code. There is appreciation for the article's concrete, quantitative approach, and discussion about the limitations of AI in understanding project context for refactoring.

**Tags**: `#refactoring`, `#AI`, `#software engineering`, `#economics`, `#best practices`

---

<a id="item-11"></a>
## [GCC Steering Committee Announces AI Contribution Policy](https://lwn.net/Articles/1086041/) ⭐️ 8.0/10

The GCC steering committee has announced a new policy requiring transparency and human oversight for all AI-generated contributions to the compiler. This policy sets a precedent for major open-source projects navigating AI contributions, aiming to preserve code quality and community trust while accommodating new tools. AI-generated patches must be clearly labeled and reviewed by a human who takes full responsibility; the community emphasizes guidance over punishment for non-compliance.

hackernews · arto · Jul 30, 11:45 · [Discussion](https://news.ycombinator.com/item?id=49108685)

**Background**: GCC (GNU Compiler Collection) is a foundational open-source compiler suite widely used in Linux and other systems. As AI coding assistants like GitHub Copilot become common, open-source projects face challenges from low-quality, automated contributions. This policy seeks to balance innovation with code integrity.

**Discussion**: Community comments reflect cautious support, with appreciation for the guiding approach and concerns about enforcement. A notable quote highlights the socioeconomic dimension of AI access. Overall sentiment is mixed but engaged.

**Tags**: `#GCC`, `#open-source`, `#AI policy`, `#compiler`, `#community guidelines`

---

<a id="item-12"></a>
## [Schneier: AI Writing Tasks Atrophy Critical Thinking](https://simonwillison.net/2026/Jul/30/bruce-schneier/#atom-everything) ⭐️ 8.0/10

Bruce Schneier argues that using AI for writing tasks, such as policy memos, can atrophy critical thinking skills, comparing assignments to mental gym workouts. This perspective is significant because it challenges the growing trend of integrating AI into education and work, highlighting potential cognitive costs. It affects educators, employers, and anyone relying on AI for intellectual tasks. Schneier's blog post from July 2026 presents a simple decision framework for when to use AI. He distinguishes between 'gym tasks' (for mental exercise) and 'work tasks' (for output).

rss · Simon Willison · Jul 30, 18:25

**Background**: Bruce Schneier is a renowned security technologist and author, known for his insights on technology and society. The debate over AI in education has intensified with the rise of generative AI tools like ChatGPT, which can produce human-quality writing. Critics argue that over-reliance on AI may undermine students' ability to think critically and write independently.

**Tags**: `#AI`, `#critical thinking`, `#education`, `#writing`, `#cognitive skills`

---

<a id="item-13"></a>
## [Professor Loses PhD Candidates Over Conference Review Process](https://www.reddit.com/r/MachineLearning/comments/1vawwb8/i_have_lost_three_and_a_half_potential_phd/) ⭐️ 8.0/10

An early-career assistant professor reports losing three and a half potential PhD students because the frustrating conference review process demotivated them, despite papers receiving positive reviews but still being rejected. This highlights a systemic flaw in top-tier ML conferences that discourages talented early-career researchers from pursuing academia, potentially harming the field's future. The professor notes that papers without obvious flaws receive increasingly random reviews after multiple resubmissions, and even unanimous weak accepts can still lead to rejection.

reddit · r/MachineLearning · /u/AffectionateLife5693 · Jul 30, 15:30

**Background**: In machine learning, the 'big three' conferences (NeurIPS, ICML, ICLR) are highly competitive and influential. The peer review process, while intended to ensure quality, has been criticized for high randomness and demotivating authors, especially early-career researchers. This post reflects widespread frustration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning">International Conference on Machine Learning - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#ML conferences`, `#peer review`, `#academic pipeline`, `#PhD recruitment`, `#systemic issues`

---

<a id="item-14"></a>
## [MLVC: Solving Cross-Platform Compatibility for Learned Video Codecs](https://www.reddit.com/r/MachineLearning/comments/1vb3xwd/mlvc_multiplatform_learned_video_codec_for/) ⭐️ 8.0/10

Researchers introduce MLVC, a learned video codec that achieves consistent entropy decoding across heterogeneous NPUs by transmitting scale parameters through the hyperprior, avoiding the need for bit-exact neural network execution. This addresses a critical barrier to real-world deployment of learned video codecs—cross-platform incompatibility due to numerical differences in entropy decoding on different NPUs, which has kept traditional codecs like H.264 dominant for over a decade. MLVC runs at approximately 100 FPS for 360p/540p video on consumer NPUs. The approach avoids reliance on fully specified fixed-point arithmetic, which current hardware and toolchains do not reliably support.

reddit · r/MachineLearning · /u/tanelai · Jul 30, 19:40

**Background**: Learned video codecs use neural networks to compress video, promising better compression efficiency than hand-engineered codecs like H.264 and AV1. However, they require specialized hardware like NPUs for efficient inference. A major challenge is that entropy decoding in neural codecs is sensitive to numerical differences; even small rounding variations across different NPU platforms can cause decoding failures. Traditional approaches attempt bit-exactness via integer quantization, but this is not guaranteed due to hardware differences.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2508.01852v2">Context Guided Transformer Entropy Modeling for Video Compression</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10139143">Entropy Modeling in Video Compression Based on Machine Learning | IEEE Conference Publication | IEEE Xplore</a></li>

</ul>
</details>

**Discussion**: The author, who is one of the paper's authors, posted the news and is available to answer questions. No other comments are provided in the content.

**Tags**: `#learned video codec`, `#cross-platform compatibility`, `#entropy model`, `#neural compression`, `#NPU`

---

<a id="item-15"></a>
## [ByteDance Restructures To B: Feishu Merged with Doubao and Volcano Engine](https://news.qq.com/rain/a/20260730A03CAP00) ⭐️ 8.0/10

ByteDance has reorganized its AI business by merging the Feishu product team with the Doubao team to form a new 'Doubao Product Team' led by Zhao Qi, with Feishu head Xie Xin reporting to him. Additionally, Feishu's marketing, sales, and customer service teams have been integrated with Volcano Engine under a new 'Creativity Service Platform' led by Tan Dai. This marks the largest restructuring of ByteDance's To B business since its founding, signaling a strategic push to tightly integrate its enterprise productivity suite (Feishu) with its leading AI chatbot (Doubao) and cloud platform (Volcano Engine). The move could accelerate AI-powered enterprise solutions and intensify competition with other Chinese tech giants in the enterprise software market. After the reorganization, Feishu's existing products and services will remain unchanged, and the team will deepen cooperation with Doubao on productivity scenarios. The Doubao enterprise edition, co-developed by both teams, is already in internal testing with select Feishu customers.

telegram · zaihuapd · Jul 30, 02:55

**Background**: Feishu (known as Lark internationally) is ByteDance's enterprise collaboration platform offering chat, documents, meetings, and workflow automation. Doubao, launched in August 2023, is China's most popular AI chatbot with approximately 60 million monthly active users as of November 2024. Volcano Engine, launched in 2020, is ByteDance's cloud service platform. This restructuring combines these three pillars to create a more integrated AI-powered enterprise offering.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lark_(software)">Lark (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Doubao">Doubao - Wikipedia</a></li>
<li><a href="https://baike.baidu.com/en/item/Volcano+Engine/1423148">Volcano Engine - ByteDance's cloud service platform</a></li>

</ul>
</details>

**Tags**: `#ByteDance`, `#Feishu`, `#AI`, `#enterprise software`, `#restructuring`

---

<a id="item-16"></a>
## [US Senators Warn Apple Against Buying Chinese Memory Chips](https://www.bloomberg.com/news/articles/2026-07-29/senators-warn-apple-not-to-buy-memory-chips-from-chinese-firms) ⭐️ 8.0/10

Bipartisan US senators sent a letter to Apple CEO Tim Cook urging the company to stop purchasing memory chips from Chinese firms CXMT and YMTC, citing their inclusion on a Pentagon blacklist for military ties. This could disrupt Apple's supply chain amid a global memory shortage and rising prices, impacting products like Mac, iPad, and Vision Pro, while escalating US-China technology tensions. Apple was reportedly in procurement negotiations with CXMT and YMTC and raised prices on Mac, iPad, home devices, and Vision Pro in June 2026; senators demanded a commitment by August 21, 2026, and information on certification and tech data sharing.

telegram · zaihuapd · Jul 30, 06:12

**Background**: CXMT (ChangXin Memory Technologies) is China's top DRAM chipmaker, and YMTC (Yangtze Memory Technologies) is a leading NAND flash manufacturer. Both have been placed on US export control lists due to alleged military ties, raising national security concerns. The memory chip market is currently experiencing tight supply and price increases, making Apple's sourcing options more limited.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.ymtc.com/en/">YMTC - YMTC</a></li>
<li><a href="https://www.ft.com/stream/1fd5ea0b-60b5-4b51-aad6-3067ba04d49e">Yangtze Memory Technologies | Financial Times</a></li>

</ul>
</details>

**Tags**: `#geopolitics`, `#semiconductor`, `#supply chain`, `#Apple`, `#memory chips`

---

<a id="item-17"></a>
## [Google DeepMind Disbands Nobel-Winning AlphaFold Team](https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33?syn-25a6b1a6=1) ⭐️ 8.0/10

Google DeepMind has disbanded the AlphaFold team, with key members John Jumper, Jonas Adler, and Alexander Pritzel leaving for Anthropic, while remaining staff are reassigned to projects like Gemini, enzyme design, and Isomorphic Labs. This signals a strategic shift in AI research priorities and intensifies talent competition, as DeepMind redirects resources toward broader AI applications while Anthropic gains top talent in computational biology. Nearly a quarter of the original AlphaFold paper authors have left DeepMind entirely, and the remaining authors have been reassigned internally, with some moving to Isomorphic Labs for drug discovery.

telegram · zaihuapd · Jul 30, 07:45

**Background**: AlphaFold is a deep learning system developed by DeepMind that predicts protein structures with high accuracy, winning the 2024 Nobel Prize in Chemistry. DeepMind is a subsidiary of Alphabet, and Isomorphic Labs is an Alphabet spin-off focusing on AI-driven drug discovery.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Isomorphic_Labs">Isomorphic Labs</a></li>
<li><a href="https://www.isomorphiclabs.com/">Reimagining Drug Discovery Process with AI - Isomorphic Labs</a></li>

</ul>
</details>

**Tags**: `#DeepMind`, `#AlphaFold`, `#Anthropic`, `#AI research`, `#talent migration`

---

<a id="item-18"></a>
## [EU Launches AI Super Factory Tender, Aims for €30B Investment](https://www.wsj.com/world/europe/eu-opens-call-for-creation-of-local-ai-gigafactories-c286213d) ⭐️ 8.0/10

The European Commission launched a tender on Thursday to build up to seven AI super factories, aiming to mobilize approximately €30 billion in investment, with €10 billion from EU and member state funds. Bids are due by November 12, and winning projects are expected to be announced by July 2027 and operational within 18 months of signing. This initiative represents a major strategic move by the EU to strengthen its AI infrastructure and compete with the US and other global leaders in AI technology. The significant investment could accelerate European AI research and development, fostering innovation and reducing dependence on foreign AI capabilities. The tender supports two phases: site selection and expansion for up to seven facilities. The EU expects the total investment to be leveraged from public and private sources, with €10 billion directly from EU and member states.

telegram · zaihuapd · Jul 30, 11:50

**Background**: AI super factories are large-scale computing facilities specifically designed to train advanced artificial intelligence models, requiring massive amounts of computational power and energy. The EU has been seeking to boost its technological sovereignty and reduce reliance on non-European cloud and AI services, especially amid geopolitical tensions and the rapid AI advancements by companies like OpenAI and Google.

**Tags**: `#AI`, `#EU`, `#investment`, `#infrastructure`, `#geopolitics`

---