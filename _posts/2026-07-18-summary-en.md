---
layout: default
title: "Horizon Summary: 2026-07-18 (EN)"
date: 2026-07-18
lang: en
---

> From 38 items, 13 important content pieces were selected

---

1. [GPT-5.6 Solves 30-Year Convex Optimization Conjecture](#item-1) ⭐️ 9.0/10
2. [LG monitors silently install software via Windows Update](#item-2) ⭐️ 9.0/10
3. [Kimi K3 Reaches Frontier AI Parity, Ignites Distillation Debate](#item-3) ⭐️ 9.0/10
4. [TSMC A14 Process Surpasses Expectations: Yield and Performance Near 90%](#item-4) ⭐️ 9.0/10
5. [Regressive JPEGs Use Network Delay for Playback](#item-5) ⭐️ 8.0/10
6. [Stack Overflow Decline Graph Sparks Debate on AI vs Policy](#item-6) ⭐️ 8.0/10
7. [Goodbye, Bikesheds: Reversible Decisions and MD5crypt](#item-7) ⭐️ 8.0/10
8. [Did blatant AI slop win DeepMind Kaggle prize?](#item-8) ⭐️ 8.0/10
9. [Doubao Phone Drops GUI Automation for MCP-Based AI Integration](#item-9) ⭐️ 8.0/10
10. [Meta Negotiates $10B AI Computing Lease to Anthropic](#item-10) ⭐️ 8.0/10
11. [SpaceX in talks with Pentagon for billions in AI computing power](#item-11) ⭐️ 8.0/10
12. [Trump admin considers FINRA-like agency to vet top AI models](#item-12) ⭐️ 8.0/10
13. [San Francisco Orders Apple and Google to Remove AI 'Nudify' Apps](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-5.6 Solves 30-Year Convex Optimization Conjecture](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 9.0/10

GPT-5.6, using a Sol variant, reportedly solved a long-standing open problem in convex optimization by proving a conjecture about oracle complexity through a single prompt. This demonstrates that large language models can make genuine contributions to advanced mathematics, potentially accelerating discovery and shifting research priorities away from 'low-hanging fruit' problems. The solved conjecture relates to the oracle complexity of convex optimization over Lipschitz functions on a spherical domain, with the proof verified by domain experts on Reddit. The model used was GPT-5.6 Sol, not the most capable Ultra variant.

hackernews · mbustamanter · Jul 18, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48957779)

**Background**: Convex optimization is a branch of mathematical optimization where the objective function and constraints are convex. Oracle complexity measures the number of queries to an oracle (e.g., gradient evaluation) required to achieve a desired accuracy. This 30-year gap refers to the discrepancy between upper and lower bounds on oracle complexity for certain classes of convex problems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted the contribution is real but niche, and questioned whether such AI achievements will make researchers obsolete—some argued it will push researchers to focus on truly novel approaches. One comment clarified the successful model was Sol Pro, not Ultra, and discussed the multi-agent architecture behind it.

**Tags**: `#AI`, `#mathematics`, `#convex optimization`, `#GPT-5.6`, `#breakthrough`

---

<a id="item-2"></a>
## [LG monitors silently install software via Windows Update](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 9.0/10

Connecting some LG monitors to a Windows PC triggers automatic installation of McAfee subscription-promoting software through Windows Update without user consent. This represents a serious security and privacy breach, as the software runs with full system privileges, starts at boot, and is installed without any user interaction, affecting a large number of Windows users who own LG monitors. The issue occurs even if the monitor was connected previously, and the software is installed every time the system boots. Workarounds include disabling automatic download of device-related applications in Group Policy or Device Installation Settings.

hackernews · baranul · Jul 18, 10:21 · [Discussion](https://news.ycombinator.com/item?id=48956688)

**Background**: Windows Update can automatically install drivers and associated software for detected hardware. Monitors are recognized as devices, and manufacturers can supply driver packages that include additional software. This mechanism is similar to the autorun vulnerability that allowed malware to spread via USB drives.

<details><summary>References</summary>
<ul>
<li><a href="https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent">LG monitors silently install software through Windows Update ...</a></li>

</ul>
</details>

**Discussion**: Community members are outraged, highlighting that the software is effectively malware and runs with no sandboxing. Several users provided workarounds via Group Policy or Device Installation Settings. There is debate whether the blame lies with LG or Microsoft for allowing such automatic installations.

**Tags**: `#security`, `#windows`, `#privacy`, `#supply chain`, `#lg`

---

<a id="item-3"></a>
## [Kimi K3 Reaches Frontier AI Parity, Ignites Distillation Debate](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 9.0/10

Chinese startup Moonshot AI released Kimi K3, a 2.8 trillion parameter model that achieves performance parity with leading frontier models from OpenAI and Anthropic, as reported on July 17, 2026. This development challenges the lead of US frontier labs and raises concerns about knowledge distillation methods, potentially reshaping global AI competition and prompting geopolitical debate over open-weight model access. Kimi K3 features a 1M-token context window and is priced at $3/$15 per million input/output tokens, directly competing with GPT-5.6 Sol and Claude Opus 4.8 in both performance and cost.

hackernews · sbochins · Jul 18, 17:32 · [Discussion](https://news.ycombinator.com/item?id=48960218)

**Background**: Knowledge distillation is a technique where a smaller 'student' model is trained to mimic a larger 'teacher' model, enabling cost-efficient deployment. Frontier models like GPT-5 and Claude are closed-source, but Kimi K3's open-weight access has sparked debate over whether its parity was achieved through distillation of these closed models.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html">China's Moonshot AI unveils Kimi K3 that rivals OpenAI, Anthropic - CNBC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters express mixed views: some argue distillation is inevitable and not an 'attack', while others highlight usage limit issues and question the true cost-effectiveness of K3. Concerns about government regulation and geopolitical risks are also prominent, with comparisons to early Napster days.

**Tags**: `#AI`, `#distillation`, `#frontier models`, `#open-source`, `#geopolitics`

---

<a id="item-4"></a>
## [TSMC A14 Process Surpasses Expectations: Yield and Performance Near 90%](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-confirms-significant-yield-and-performance-improvements-in-a14-update-strong-interest-from-ai-hpc-and-smartphone-customers) ⭐️ 9.0/10

TSMC announced that its A14 (1.4nm-class) process has made rapid progress in the past three months, with device performance and 256 Mb SRAM yield both approaching 90%, up from 85% and above 80% respectively in April. This milestone indicates that A14 is on track for mass production in the second half of 2028, potentially enabling next-generation AI, HPC, and smartphone chips with significantly better performance and power efficiency than current N2 nodes. Compared to N2, A14 is expected to deliver 10-15% higher performance at same power, 25-30% lower power at same frequency, and 23% higher logic transistor density, partly due to its second-generation GAA nanosheet transistors.

telegram · zaihuapd · Jul 18, 05:00

**Background**: A14 is TSMC's 1.4nm-class node, succeeding N2 (2nm-class). It uses gate-all-around (GAA) nanosheet transistors, which offer better electrostatic control than FinFETs, enabling further scaling. TSMC's N2 process uses first-generation GAA, while A14 leverages a second-generation version, building on N2's learning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.patsnap.com/resources/blog/articles/gaa-transistors-at-2nm-nanosheet-architecture-explained/">GAA transistors at 2nm: nanosheet architecture explained | PatSnap</a></li>
<li><a href="https://semiengineering.com/new-transistor-structures-at-3nm-2nm/">New Transistor Structures At 3nm/2nm</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#TSMC`, `#A14`, `#chip manufacturing`, `#AI`

---

<a id="item-5"></a>
## [Regressive JPEGs Use Network Delay for Playback](https://maurycyz.com/projects/bad_jpeg/) ⭐️ 8.0/10

The project creates progressive JPEG images that display an animated sequence of low-fidelity frames during loading, using network delay as the sole timing mechanism. This clever hack repurposes progressive JPEG decoding for creative applications like steganography, progress bars, or trolling, while highlighting overlooked features of image encoding. Each animation frame is encoded as a separate scan of a progressive JPEG; the browser decodes scans sequentially as data arrives, producing the animation. Playback speed is uncontrollable and varies with network conditions.

hackernews · vitaut · Jul 18, 03:14 · [Discussion](https://news.ycombinator.com/item?id=48954851)

**Background**: Progressive JPEGs load images in multiple scans, showing a blurry low-resolution version first, then sharpening with each subsequent scan. Unlike baseline JPEGs that load top-to-bottom, progressive JPEGs allow the entire image to be perceived early. The regressive JPEG project exploits this behavior to create an animation by encoding each frame as a scan.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ionos.com/digitalguide/websites/web-design/progressive-jpeg/">Progressive JPEGs | An introduction to image compression - IONOS</a></li>
<li><a href="https://elementor.com/blog/progressive-jpegs/">Progressive JPEGs: What They Are & How They Boost Web Performance</a></li>

</ul>
</details>

**Discussion**: Commenters praised the creative absurdity and suggested uses like steganography to bypass content filters. Retr0id noted similar work with interlaced PNG (adam7). Some proposed server-side timed chunk sending for controllable playback.

**Tags**: `#jpeg`, `#image-encoding`, `#hacker-culture`, `#novelty`, `#compression`

---

<a id="item-6"></a>
## [Stack Overflow Decline Graph Sparks Debate on AI vs Policy](https://data.stackexchange.com/stackoverflow/query/1953768#graph) ⭐️ 8.0/10

A Stack Exchange Data Explorer graph shows a clear decline in Stack Overflow activity over time, with community comments debating whether the cause is AI tools like ChatGPT or the platform's own exclusionary policies. This matters because Stack Overflow has been a cornerstone for developers, and its decline affects how programmers seek help and share knowledge, potentially shifting the ecosystem toward AI-driven answers or more inclusive platforms. The graph shows activity peaking around 2014, before the widespread availability of modern AI tools. Some commenters note that the decline accelerated after Stack Overflow was acquired by Prosus in 2021.

hackernews · secretslol · Jul 18, 11:12 · [Discussion](https://news.ycombinator.com/item?id=48956949)

**Background**: Stack Overflow is a Q&A platform for programmers, where users ask and answer technical questions. It has long been criticized for its strict moderation and high barriers for new users, which may have discouraged participation. Recent advancements in AI, such as ChatGPT, provide direct answers, reducing the need for traditional forums.

**Discussion**: Commenters are divided: some blame AI for taking over answer sources, while others argue that Stack Overflow's own gatekeeping and lack of community drove users away. Several point out that the decline began long before AI became mainstream, citing the 2014 peak and the 2021 acquisition as key events.

**Tags**: `#stackoverflow`, `#ai-impact`, `#community`, `#decline`, `#data-analysis`

---

<a id="item-7"></a>
## [Goodbye, Bikesheds: Reversible Decisions and MD5crypt](https://queue.acm.org/detail.cfm?id=3818307) ⭐️ 8.0/10

The article reflects on the phenomenon of bikeshedding in software development, introduces the concept of reversible decisions to mitigate it, and pays homage to PHK's MD5crypt algorithm and other contributions. It offers practical wisdom for improving decision-making efficiency in technical teams, and highlights the lasting impact of early open-source contributions on foundational security infrastructure like password hashing. The article discusses that reversible decisions (those that can be easily undone) should be made quickly without extensive debate, while irreversible decisions warrant more careful consideration. It also traces the history of MD5crypt, a password hashing scheme introduced in FreeBSD in 1994.

hackernews · Ygg2 · Jul 18, 17:27 · [Discussion](https://news.ycombinator.com/item?id=48960155)

**Background**: Bikeshedding, derived from Parkinson's law of triviality, refers to the tendency to spend excessive time on minor, easy-to-understand issues while neglecting more important but complex ones. MD5crypt is a password hashing algorithm that uses MD5 with a salt and multiple iterations to store passwords securely. It was one of the early attempts to strengthen password storage against brute-force attacks, predating bcrypt and scrypt.

<details><summary>References</summary>
<ul>
<li><a href="https://www.urbandictionary.com/define.php?term=bikeshedding">Urban Dictionary: bikeshedding</a></li>
<li><a href="https://en.wikipedia.org/wiki/MD5">MD5 - Wikipedia</a></li>
<li><a href="https://www.onlinehashcrack.com/guides/cryptography-algorithms/md5crypt-a-comprehensive-analysis-of-its-use-in-cryptography.php">md5crypt: A Comprehensive Analysis of Its Use in Cryptography</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted the utility of reversible decisions, with one noting that throwing money at bikeshed problems can solve them. Another praised PHK's MD5crypt creation. A user expressed initial frustration with the article but later appreciated its depth after rereading. Some joked about replacing physical bikesheds with JIRA ticket painting.

**Tags**: `#software engineering`, `#bikeshedding`, `#decision-making`, `#open source`, `#password hashing`

---

<a id="item-8"></a>
## [Did blatant AI slop win DeepMind Kaggle prize?](https://www.reddit.com/r/MachineLearning/comments/1uzyf66/did_blatant_ai_slop_just_win_a_25k_usd_deepmind/) ⭐️ 8.0/10

A Reddit user claims that the grand prize winner of a DeepMind-sponsored Kaggle competition on cognitive AI benchmarks contained nonsensical content and unfounded claims, providing evidence of flawed methodology and code. This raises serious questions about the integrity of high-profile AI competitions and peer review processes, potentially undermining trust in benchmark development and prize allocation in the AI community. The winning submission was reportedly ten times the requested format size, with analysis revealing nonsensical number generation and unjustified claims. Organizers defended the review as subjective.

reddit · r/MachineLearning · /u/TheWerkmeister · Jul 18, 15:10

**Background**: Kaggle is a platform for data science competitions where sponsors like DeepMind offer prizes. This particular competition, 'Measuring Progress Toward AGI - Cognitive Abilities', challenged participants to design new cognitive-science-based AI benchmarks. Winners are selected through a review process that may sometimes lack rigor.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kaggle">Kaggle - Wikipedia</a></li>
<li><a href="https://ai.plainenglish.io/why-todays-ai-benchmarks-are-broken-and-what-deepmind-s-200k-hackathon-is-doing-about-it-44407812a1d4">Why Today’s AI Benchmarks Are Broken — and What...</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#Kaggle`, `#DeepMind`, `#competition controversy`, `#peer review`

---

<a id="item-9"></a>
## [Doubao Phone Drops GUI Automation for MCP-Based AI Integration](https://www.latepost.com/news/dj_detail?id=3648) ⭐️ 8.0/10

Doubao phone announced it will abandon GUI-based automation (screen reading and click simulation) for major apps like WeChat and Taobao, and instead require these super apps to provide Model Context Protocol (MCP) services to enable AI agent integration. The company has also increased its supply from 30,000 units to hundreds of thousands. This strategic shift moves away from fragile, platform-dependent automation to an open protocol standard, aligning with moves by Apple and Google to adopt similar frameworks for AI agent integration. It pressures super apps to open up their data and controls, potentially reshaping the mobile AI ecosystem. The Doubao phone assistant software received generative AI service备案 (filing) on July 15, 2025, and its first technical preview was released in December 2025, but it was previously disabled due to bans from WeChat and Taobao. The company is now ramping up production from an initial 30,000 units to 'hundreds of thousands'.

telegram · zaihuapd · Jul 18, 00:29

**Background**: GUI automation allows AI agents to interact with apps by reading screen content and simulating taps, similar to how a human would use the phone. However, it is fragile and can be blocked by app developers. The Model Context Protocol (MCP), introduced by Anthropic in November 2024, is an open standard that enables AI systems to connect directly to external tools and data sources in a structured way, making integration more reliable and secure.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#MCP`, `#mobile operating systems`, `#AI integration`, `#ecosystem strategy`

---

<a id="item-10"></a>
## [Meta Negotiates $10B AI Computing Lease to Anthropic](https://www.nytimes.com/2026/07/17/technology/meta-anthropic-ai-computing-power.html) ⭐️ 8.0/10

Meta is negotiating a deal to lease AI computing power to Anthropic for a potential $10 billion over two years, with monthly payments and early exit options for both parties. This deal highlights the extreme scarcity of AI computing resources and Meta's strategy to monetize its massive infrastructure investments, potentially reshaping how AI compute is allocated among major players. The proposal was made by Anthropic in June 2026, and negotiations are still early and may not conclude. Meta plans to spend up to $145 billion this year, much of it on AI and data centers.

telegram · zaihuapd · Jul 18, 01:14

**Background**: AI computing power, especially for training large language models, is in high demand and short supply. Companies like Meta and Google are building massive data centers, while AI startups like Anthropic need vast compute resources but lack their own infrastructure. Renting spare capacity from tech giants is becoming a common arrangement.

**Tags**: `#AI`, `#Meta`, `#Anthropic`, `#cloud computing`, `#infrastructure`

---

<a id="item-11"></a>
## [SpaceX in talks with Pentagon for billions in AI computing power](https://www.wsj.com/tech/ai/spacex-in-talks-to-provide-computing-power-for-pentagons-ai-push-15e752e4) ⭐️ 8.0/10

SpaceX is negotiating with the U.S. Department of Defense to provide data center computing power for running artificial intelligence models, with a potential deal worth tens of billions of dollars. If finalized, this would mark a major expansion of SpaceX's role beyond launch services into cloud computing for national security, potentially reshaping the defense AI landscape and challenging incumbents like Amazon and Microsoft. The talks are ongoing and could still fall through; SpaceX has recently signed similar computing deals with Anthropic and Google, and plans to significantly expand its cloud business.

telegram · zaihuapd · Jul 18, 01:44

**Background**: The Pentagon is urgently acquiring cloud computing capabilities to support AI applications in national security and daily operations. It has recently approved SpaceX, Amazon, Google, Microsoft, and Oracle to use their AI models and technologies in classified environments. SpaceX, known for its Starlink satellite network, is leveraging its infrastructure to enter the cloud computing market.

<details><summary>References</summary>
<ul>
<li><a href="https://t.me/jinxw/795412">禁闻网 – Telegram</a></li>
<li><a href="https://www.nbd.com.cn/articles/2026-02-27/4271111.html">Anthropic拒向 五 角 大 楼 妥协；谷歌Nano Banana...</a></li>

</ul>
</details>

**Tags**: `#AI算力`, `#SpaceX`, `#国防`, `#云计算`, `#五角大楼`

---

<a id="item-12"></a>
## [Trump admin considers FINRA-like agency to vet top AI models](https://www.bloomberg.com/news/articles/2026-07-17/us-considers-creating-finra-like-watchdog-to-vet-top-ai-models) ⭐️ 8.0/10

The Trump administration is considering creating an independent regulatory agency, modeled after FINRA, to review the safety of top AI models. The proposal, led by Treasury Secretary Scott Bessent, is under review by White House Chief of Staff Susie Wiles and aims to address concerns from Wall Street and Silicon Valley. This move could establish a formal, industry-participated framework for AI safety regulation, giving both financial and tech sectors more influence over security standards. It may also respond to AI companies' recent disputes with the government over model releases. The proposed agency would report to the SEC, similar to FINRA. The plan aligns with a suggestion from Google DeepMind CEO Demis Hassabis regarding an industry-funded independent watchdog. However, President Trump has not yet reviewed the plan, and details may change.

telegram · zaihuapd · Jul 18, 05:45

**Background**: The Financial Industry Regulatory Authority (FINRA) is a private self-regulatory organization that oversees brokerage firms and exchange markets in the US, operating under SEC oversight. Similarly, the proposed AI watchdog would be an independent body funded by the industry, aiming to self-regulate AI safety. This model is intended to combine industry expertise with government oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FINRA">FINRA</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#government policy`, `#Trump administration`, `#AI safety`

---

<a id="item-13"></a>
## [San Francisco Orders Apple and Google to Remove AI 'Nudify' Apps](https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/) ⭐️ 8.0/10

San Francisco City Attorney David Chiu ordered Apple and Google to remove dozens of 'nudify' apps from their app stores, threatening legal action and civil penalties if they fail to comply. This action sets a precedent for holding major tech platforms accountable for hosting non-consensual deepfake apps, highlighting the growing legal and ethical challenges of AI-generated synthetic media. The letter claims Apple and Google knowingly profited from these apps, which use AI to digitally remove clothing from photos without consent, and that the companies face potential civil penalties. Apple has removed three apps and terminated related developer accounts, while Google suspended five Play Store apps.

telegram · zaihuapd · Jul 18, 08:45

**Background**: Deepfake technology uses machine learning to create realistic but fake images and videos, often without consent. 'Nudify' apps are a specific type of deepfake pornography that digitally alter photos to make subjects appear naked, raising serious privacy and consent issues. The Tech Transparency Project had previously warned about the prevalence of such apps in both Apple and Google app stores.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deepfake">Deepfake - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nudify_apps">Nudify apps</a></li>
<li><a href="https://www.techtransparencyproject.org/articles/nudify-apps-widely-available-in-apple-and-google-app-stores">TTP - Nudify Apps Widely Available in Apple and Google App Stores</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#deepfakes`, `#app store regulation`, `#privacy`, `#platform accountability`

---