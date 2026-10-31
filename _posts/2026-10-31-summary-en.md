---
layout: default
title: "Horizon Summary: 2026-10-31 (EN)"
date: 2026-10-31
lang: en
---

> From 34 items, 9 important content pieces were selected

---

1. [Tampered Claude Code extension slipped onto Cursor Marketplace, injected attacker SSH key](#item-1) ⭐️ 8.0/10
2. [Northflank breach fuels fears of a wave of attacks on multi-tenant SaaS](#item-2) ⭐️ 8.0/10
3. [NES Emulator Runs Inside ~1GB of Qwen Model Weights](#item-3) ⭐️ 8.0/10
4. [Tangled launches federated, self-hostable code forge on AT Protocol](#item-4) ⭐️ 8.0/10
5. [Researcher Documents Five Full Cross-Tenant Compromises in Azure](#item-5) ⭐️ 8.0/10
6. [AI Isn't Replacing SREs, It's Deskilling Them](#item-6) ⭐️ 8.0/10
7. [NES 6502 emulator baked into Qwen3.5-4B weights](#item-7) ⭐️ 8.0/10
8. [DeepSeek reportedly raises RMB 105.5B in second round at RMB 615.5B+ valuation](#item-8) ⭐️ 8.0/10
9. [Apple Intelligence to Begin Testing in China on November 4 With Alibaba's Qwen](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Tampered Claude Code extension slipped onto Cursor Marketplace, injected attacker SSH key](https://phorion.io/blog/offical-claude-code-vsx-compromise/) ⭐️ 8.0/10

A malicious actor with access to Cursor's marketplace published a tampered copy of the Claude Code VS Code extension that silently appended an attacker-controlled public key labeled "svc-telemetry" to users' ~/.ssh/authorized_keys. Anthropic's Felix Rieseberg confirmed the extension was a third-party marketplace copy, not a compromise of Anthropic's systems, and Cursor said the maliciously modified build was live from roughly 2:27 a.m. PT to 1:35 p.m. PT on Thursday. This is a textbook extension-marketplace supply-chain attack against a widely used AI coding tool, and it shows that installing a trusted brand's plugin from a secondary registry can hand an attacker persistent remote access to a developer machine. Anyone who installed the Claude Code extension through Cursor's marketplace or Open VSX rather than the official Microsoft registry should check their SSH configuration. The payload was minimal: the tampered build simply added an SSH public key to authorized_keys, which would grant the attacker passwordless login to the affected machine. Users can check on macOS with `grep -qs svc-telemetry ~/.ssh/authorized_keys && echo "svc-telemetry key found" || echo "No key found; machine not impacted"`, and commenters noted the exact scope of which registries were affected is still somewhat unclear, though the official Microsoft marketplace build is believed clean.

hackernews · _chall · Oct 30, 07:09 · [Discussion](https://news.ycombinator.com/item?id=50300683)

**Background**: VS Code extensions are typically distributed through Microsoft's VS Code Marketplace, but IDEs such as Cursor and VSCodium cannot use that registry directly, so they rely on Open VSX and their own marketplaces instead. Because an extension runs with the full privileges of the editor process, a malicious extension can read and write files such as ~/.ssh/authorized_keys, which lists the public keys allowed to log into an account over SSH. Supply-chain attacks through extension registries — typosquatting, hijacked publisher accounts, tampered builds — have become a recurring threat to developers over the past few years.

<details><summary>References</summary>
<ul>
<li><a href="https://danielraffel.me/2026/01/05/i-built-a-vs-code-cursor-extension-to-open-agents-in-the-editor-area/">I built a VS Code / Cursor extension to open Agents in the Editor Area</a></li>
<li><a href="https://labs.cloudsecurityalliance.org/research/csa-research-note-vscode-extension-supply-chain-breach-20260/">VSCode Marketplace Poisoning: How 18 Minutes Breached GitHub</a></li>

</ul>
</details>

**Discussion**: The thread is largely a clarification exercise: an Anthropic engineer stressed that neither Anthropic's systems nor employee laptops were compromised, and commenters pushed back on early reporting by pointing to the original Phorion write-up and Cursor's own blog for the precise ~11-hour exposure window. Others supplied concrete detection commands and debated whether the official Microsoft marketplace build was also affected, with the consensus being that the Open VSX/Cursor channel was the vector.

**Tags**: `#security`, `#supply-chain-attack`, `#vs-code-extensions`, `#ai-coding-tools`, `#cursor-marketplace`

---

<a id="item-2"></a>
## [Northflank breach fuels fears of a wave of attacks on multi-tenant SaaS](https://status.northflank.com/) ⭐️ 8.0/10

Northflank, a UK-based Kubernetes-based PaaS provider, disclosed a security breach via its status page, prompting a large Hacker News discussion (354 points, 272 comments). Commenters noted that this is at least the sixth substantial attack on multi-tenant as-a-service vendors since September, following incidents at PingCAP/TiDB, Fireworks AI, Zeabur, OpenCode Console and Railway. The string of incidents is being framed as a systemic risk of the multi-tenant SaaS model rather than a run of bad luck, since a single vulnerability or misconfiguration can expose every tenant's data at once. Commenters argue it could push enterprise buyers back toward hyperscalers, where ease of use cannot compensate for security. The linked source is only a status page, so technical specifics such as the attack vector, affected scope and customer data exposure remain unclear; one commenter observed that the provider apparently does not grant access to customer code or binaries. The thread also surfaced workarounds like encrypting environment variables and hard-coding the decryption key inside the deployed binary, though this only helps if the attacker cannot reach the running application.

hackernews · js4ever · Oct 30, 15:10 · [Discussion](https://news.ycombinator.com/item?id=50305025)

**Background**: Northflank is a UK-based platform-as-a-service (PaaS) offering that combines a developer-friendly workflow with Kubernetes under the hood, including Git-based deploys, managed databases, preview environments and GPU support. Multi-tenancy — where many customers share the same infrastructure — is what makes such platforms cheap and easy to operate, but OWASP notes that a single vulnerability or misconfiguration can leak data across tenant boundaries. Hyperscalers such as AWS, Azure and Google Cloud are the large-scale alternative, offering deeper security investment at the cost of more operational complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://northflank.com/blog/what-is-paas-hosting">What is PaaS hosting? Benefits and how it works | Blog — Northflank</a></li>
<li><a href="https://europeanstack.com/software/northflank">Northflank Review 2026 | EuropeanStack</a></li>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html">Multi Tenant Security - OWASP Cheat Sheet Series</a></li>

</ul>
</details>

**Discussion**: The thread is broadly alarmed: one top commenter catalogues six lightning-fast attacks on multi-tenant vendors since September and calls it “a full infosec emergency unfolding.” Others share defensive tricks such as encrypting env vars with the key baked into the binary, predict enterprise buyers converging back to hyperscalers, and worry about a future where technical security is no longer achievable and zero trust plus behavioral friction becomes the norm; a few simply ask what Northflank is.

**Tags**: `#security`, `#saas`, `#infrastructure`, `#cloud`, `#incident-response`

---

<a id="item-3"></a>
## [NES Emulator Runs Inside ~1GB of Qwen Model Weights](https://github.com/dbreunig/nesformer) ⭐️ 8.0/10

A developer has released nesformer, a working Nintendo Entertainment System emulator built inside roughly 1GB of Qwen model weights rather than as a conventional deterministic program. The project shows that LLM weights can encode and execute a nontrivial stateful program, fueling discussion about putting VMs, interpreters, and tools directly inside models instead of relying only on external tool calls. The emulator reportedly runs 150–290× slower than real NES hardware, and discussion notes that it models not just the CPU but also RAM using a gated DeltaNet-style architecture; the author says the working weights and code were produced from just two prompts.

hackernews · dbreunig · Oct 30, 16:40 · [Discussion](https://news.ycombinator.com/item?id=50306442)

**Background**: The NES is an 8-bit console whose games depend on precise CPU, graphics, and memory behavior, so emulators are normally deterministic programs that reproduce those circuits. Qwen is Alibaba Cloud's family of open-weight language models, and neural-network weights are the learned parameters that normally drive predictions rather than exact program execution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://playground.tensorflow.org/">A Neural Network Playground</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were impressed by the hack and intrigued by the idea of compiling a small VM, Python interpreter, or Unix tools into model weights and running them via matmul operations. At the same time, many emphasized the huge efficiency gap: deterministic programs are thousands of times cheaper, and the 150–290× slowdown shows how impractical LLM-based emulation is today. Commenters also noted surprise that the project simulates RAM, not just the CPU.

**Tags**: `#LLMs`, `#emulation`, `#Qwen`, `#neural-network-weights`, `#Hacker News`

---

<a id="item-4"></a>
## [Tangled launches federated, self-hostable code forge on AT Protocol](https://tangled.org/blog/forge/) ⭐️ 8.0/10

Tangled has launched a federated code forge built on the AT Protocol, shipping finalized lexicons, an overhauled architecture and UI, support for organizations, and easier self-hosting of the whole stack or individual parts. The team says private repositories will roll out over the following couple of weeks. It offers developers a Git hosting option where repositories and identity are portable rather than locked to a single provider, and finalized lexicons open the door for other forges to interoperate with Tangled instead of competing as isolated silos. That makes it a concrete test of whether AT Protocol's data model can extend beyond social networking into developer tooling. Tangled logs users in with their Bluesky account and carries over their social graph, and its architecture is built around lexicon-defined records, so questions about whether issue, pull-request and comment records live under repository scope or user scope directly affect interoperability. The company behind it is a Finnish startup that has raised €3.8M, and the project is still early-stage, with private repos not yet generally available.

hackernews · zlliang · Oct 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=50305573)

**Background**: The AT Protocol (ATproto) is an open protocol for decentralized publishing that underpins Bluesky and the wider "ATmosphere" of interoperable apps; unlike ActivityPub-based networks, it emphasizes portable identity and data, and lets users move between services. Its schema system, called lexicons, defines record types and RPC methods in JSON so that independent applications can agree on data formats and interoperate. By defining code-forge lexicons, Tangled lets repository, issue and release data live in the same federated data model that social apps use, which is why self-hosting and cross-forge compatibility are central to the announcement.

<details><summary>References</summary>
<ul>
<li><a href="https://atproto.com/guides/lexicon">Lexicons - AT Protocol</a></li>
<li><a href="https://nordictech.news/p/tangled-eur-3-8m-federated-github-alternative">Tangled Raises EUR 3.8M to Build a Federated GitHub Rival</a></li>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Sentiment was largely positive, with one user planning to migrate a side project off self-hosted Gitea to Tangled while keeping GitHub for discoverability and namespace squatting, and asking for a git-bug bridge to sync issues. Another commenter pressed on whether the finalized lexicons move issue, PR and comment records to repository scope rather than user scope, since their own forge (juju.bi) wants to act as a Tangled "knot server". Others offered UI critique, calling the homepage and timeline cluttered and suggesting the profile activity chart switch to GitHub-style contribution squares.

**Tags**: `#federated-software`, `#code-forge`, `#at-protocol`, `#git`, `#self-hosting`

---

<a id="item-5"></a>
## [Researcher Documents Five Full Cross-Tenant Compromises in Azure](https://www.binarysecurity.no/posts/2026/10/one-root-case) ⭐️ 8.0/10

A security researcher at Binary Security published a detailed writeup documenting five distinct cross-tenant compromise vulnerabilities in Microsoft Azure, including path traversal and insecure direct object reference (IDOR) flaws that allowed access to other customers' resources. The post, titled around a single "root case," traces the five issues back to shared underlying access-control weaknesses rather than treating them as isolated bugs. Tenant isolation is the fundamental trust boundary of a public cloud, so a cross-tenant flaw does not merely expose one victim but potentially every customer holding a paid account on the platform. Because Azure underpins identity, storage and application hosting for a huge share of enterprises, these findings have direct implications for anyone running multi-tenant workloads or relying on Entra ID for authentication and authorization. The flaws stem from insufficient access-control checks on user-supplied object identifiers, and the writeup's mitigation advice to "add randomness to resource names" drew community criticism as resembling security by obscurity rather than a real authorization fix. Commenters also flagged a separate, related problem: the callback at the end of the login.microsoftonline.com adminconsent flow is forgeable when an attacker knows another customer's tenant ID, and Microsoft's documentation warning not to use the tenant ID for authentication is only useful if an alternative authentication path actually exists.

hackernews · swq115 · Oct 30, 10:06 · [Discussion](https://news.ycombinator.com/item?id=50301854)

**Background**: Public clouds are multi-tenant: many customers share the same infrastructure while logically isolated by identifiers such as tenant IDs, subscription IDs and resource names. A cross-tenant vulnerability is one that lets an attacker in one tenant escape that isolation and read or modify another tenant's data, which is why cloud providers treat isolation engineering as a top-tier security investment. The two bug classes named here are classic: IDOR occurs when an application trusts an object identifier supplied in a URL or parameter without checking that the caller owns it, while path traversal abuses sequences like "../" to reach files or endpoints outside the intended directory.

<details><summary>References</summary>
<ul>
<li><a href="https://owasp.org/projects/cloud-tenant-isolation">OWASP Cloud Tenant Isolation</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/IDOR">Insecure Direct Object Reference (IDOR) - Security | MDN</a></li>
<li><a href="https://www.systemshardening.com/articles/cross-cutting/multi-tenancy-security-patterns/">Multi-Tenancy Security Patterns: Isolation, Data Separation ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely praised the researcher's work while expressing broader unease about Azure's isolation record, with one arguing Azure appears far ahead of competitors in the volume of cross-tenant leaks and questioning why enterprises still migrate there. Others raised a concrete related concern about the forgeable adminconsent callback using a foreign tenant ID, and one noted that the path traversal and IDOR issues likely date back to the inception of the affected capabilities.

**Tags**: `#cloud-security`, `#azure`, `#vulnerability-research`, `#multi-tenancy`, `#access-control`

---

<a id="item-6"></a>
## [AI Isn't Replacing SREs, It's Deskilling Them](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) ⭐️ 8.0/10

An opinion piece published in the SigNoz newsletter argues that AI agents in site reliability engineering will primarily deskill engineers rather than replace them, drawing a parallel to aviation, where the FAA mandates manual flying hours even when autopilot is fully capable. The essay proposes that SRE teams could similarly designate certain incidents — even ones the AI could handle — as human-practice opportunities, and it sparked a large Hacker News debate with roughly 498 points and 376 comments. The debate touches a core fear across operations and DevOps: that leaning on autonomous AI agents for incident triage and remediation will erode the deep systems understanding that makes SREs valuable when automation fails. It matters to any organization adopting AI SRE tooling, because how teams structure human practice and oversight now will determine whether they keep the expertise to debug novel outages later. The article's central proposal is a deliberate "manual flying time" analogue: reserving some incidents for humans even when AI could resolve them faster, mirroring FAA-style rules that keep pilots proficient. The caveat is that this creates deliberate inefficiency in production systems, and the piece is an opinion essay rather than empirical research, so the deskilling claim rests on analogy and anecdote rather than measurement.

hackernews · dorianniemiec · Oct 30, 15:52 · [Discussion](https://news.ycombinator.com/item?id=50305693)

**Background**: Site reliability engineering is a discipline, pioneered at Google, that applies software engineering to infrastructure and operations, with heavy emphasis on automation and infrastructure-as-code to keep large services available and performant. AI SRE agents are a newer layer: systems that use contextual reasoning over alerts, telemetry, code changes and incident history to perform alert triage, root cause analysis, and guided remediation without step-by-step human instruction. Deskilling is a long-studied phenomenon in automation research, where humans who delegate tasks to machines gradually lose the manual competence needed to intervene when the machine fails.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Site_reliability_engineering">Site reliability engineering</a></li>
<li><a href="https://www.augmentcode.com/guides/ai-sre-ai-powered-site-reliability-engineering">AI SRE: The 2026 Guide to AI-Powered Site Reliability Engineering</a></li>
<li><a href="https://rootly.com/blog/building-trust-with-ai-agents-in-site-reliability-engineering">Building trust with AI agents in site reliability engineering</a></li>

</ul>
</details>

**Discussion**: Commenters broadly validated the concern while disagreeing on its implications. Several praised the aviation analogy as the right industry to learn from on keeping humans from making mistakes as complexity grows; one startup engineer countered that Claude now beats them at AWS CLI debugging by roughly 10x, while another insisted there is no real "understanding" in AI-generated applications, full stop. A prominent counterpoint argued that "Terraform deskilled us too" and nobody demands hand-configured infrastructure, so teams should push AI toward automatic detection and remediation to reach five nines.

**Tags**: `#AI/ML`, `#SRE`, `#DevOps`, `#automation`, `#skill-atrophy`

---

<a id="item-7"></a>
## [NES 6502 emulator baked into Qwen3.5-4B weights](https://simonwillison.net/2026/Oct/30/nesformer/) ⭐️ 8.0/10

Drew Breunig released nesformer, a project that encodes a working NES 6502 CPU emulator into the weights of Qwen3.5-4B, allowing NES ROMs such as Super Mario Bros to run slowly inside the model. It is a concrete, if impractical, test of how much computation can be embedded in LLM parameters rather than delegated to external tools, extending the qwenputer experiment from a RISC-V CPU to NES emulation. The emulator is very slow and does not reach standard NES clock speed; Breunig says it was built with Claude Opus 5.5 prompts, and the model reportedly used Christopher Pow's long-standing nestest conformance suite for NES CPU validation.

rss · Simon Willison · Oct 30, 21:59

**Background**: The NES uses a 6502-derived CPU, and emulators normally reproduce its instruction behavior in software. qwenputer showed that a CPU can be "compiled" into a model's weights instead of being run as an external program; nesformer applies that idea to the NES's CPU. Qwen3.5-4B is a roughly 4B-parameter model from Alibaba's Qwen family, making the demonstration notable because it fits in a relatively small parameter budget.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MOS_Technology_6502">MOS Technology 6502 - Wikipedia</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-4B">Image-Text-to-Text model with 5B parameters. Download, explore files...</a></li>
<li><a href="https://github.com/divagr18/qwenputer">GitHub - divagr18/ qwenputer : A computer, compiled into the weights...</a></li>

</ul>
</details>

**Discussion**: The visible Hacker News discussion centers on Breunig sharing the exact Claude Opus 5.5 prompts he used, including the instruction to read the qwenputer article and explore emulating the NES chip and RAM. The thread is technically substantive, though the excerpt does not capture a clear consensus beyond interest in the experiment.

**Tags**: `#LLM`, `#emulation`, `#retro-computing`, `#prompt-engineering`, `#hacker-news`

---

<a id="item-8"></a>
## [DeepSeek reportedly raises RMB 105.5B in second round at RMB 615.5B+ valuation](https://www.theinformation.com/articles/behind-deepseeks-16-billion-funding-chinese-tech-titans-state-players) ⭐️ 8.0/10

According to a report from The Information, DeepSeek closed a second funding round of roughly RMB 105.5 billion at a valuation above RMB 615.5 billion, with close to 30 investors participating. Tencent put in RMB 10 billion, CATL and its chairman Zeng Yuqun together contributed RMB 10 billion, and the investor list also includes CXMT, SMIC, Meituan, vivo and Xiaohongshu. The round would be one of the largest ever for a Chinese AI startup and shows that the country's biggest internet platforms, chipmakers and battery suppliers are all converging on a single frontier lab. The jump in state-backed capital from about 2% in the first round to roughly 27% here signals that Beijing now treats frontier LLM capacity as strategic infrastructure rather than a purely private venture bet. The figures come from a paywalled The Information report and have not been confirmed by DeepSeek or any investor, so both the raise size and the valuation should be treated as unverified. The first round, completed in June, was about RMB 51 billion, meaning the second round is roughly double the size, and the unusually broad investor mix spans hyperscalers, DRAM and foundry players, and consumer-app companies.

telegram · zaihuapd · Oct 30, 12:37

**Background**: DeepSeek is a Hangzhou-based AI lab spun out of the quant trading firm High-Flyer, best known for releasing open-weight models such as V3 and R1 that matched far more expensive Western systems at a fraction of the training cost. CXMT (ChangXin Memory Technologies) is China's largest DRAM maker and a core piece of the country's effort to reduce reliance on Samsung, SK Hynix and Micron, while SMIC is the mainland's leading chip foundry. Both sit inside a broader wave of state-guided capital for AI and semiconductors, including the RMB 344 billion third phase of the National Integrated Circuit Industry Investment Fund and a dedicated national AI industry investment fund. The presence of these names on DeepSeek's cap table suggests the deal is as much about securing domestic compute and memory supply as about financial returns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bybit.com/zh-MY/learn/stocks/deepseek-company-overview-valuation-ipo">什么是 DeepSeek ？ 公 司 概况、 估 值 与 IPO 前 景 跟单 | Bybit Learn</a></li>
<li><a href="https://zh.wikipedia.org/zh-sg/长鑫存储">长 鑫 存 储 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.sohu.com/a/851045638_121798711">600亿大手笔！国家人工智能产业投资基金成立，推动AI与半导体融合发展...</a></li>

</ul>
</details>

**Tags**: `#AI funding`, `#DeepSeek`, `#China tech`, `#LLM industry`, `#state investment`

---

<a id="item-9"></a>
## [Apple Intelligence to Begin Testing in China on November 4 With Alibaba's Qwen](https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/) ⭐️ 8.0/10

Apple announced that the first batch of Apple Intelligence features — including Live Translation, the Photos Clean Up tool, and Writing Tools — will enter beta testing in China on November 4 via the latest iOS developer beta, before a full release to Chinese users with iOS 27.3 in December. Apple is also partnering with Alibaba so that its Qwen (Tongyi Qianwen) model powers Siri, Writing Tools, and Visual Intelligence for eligible users. China is Apple's second-largest market, and Apple Intelligence had been unavailable there since its 2024 launch, putting the iPhone at a disadvantage against aggressively AI-equipped domestic rivals such as Huawei and Xiaomi. Bringing a local partner's model into Siri and system-level features is a template for how foreign AI products may enter the Chinese market, and a significant win for Alibaba's Qwen ecosystem. The initial rollout covers only the first wave of features and excludes the next-generation AI Siri, while support for other Apple platforms (iPad, Mac, Vision Pro) will follow only after the necessary regulatory approvals. Access is limited to users who bought an Apple Intelligence–capable iPhone in China, or whose device region and Apple Account country/region are both set to China.

telegram · zaihuapd · Oct 30, 21:44

**Background**: Apple Intelligence is Apple's umbrella brand for on-device and cloud-assisted AI features across its operating systems, such as Writing Tools, notification summaries, and Visual Intelligence, which lets users press the camera-control buttons to identify objects, translate text, or look up information about what's on screen. Because Chinese regulations require generative AI services to be approved and usually backed by a licensed domestic provider, Apple could not simply extend its own models — or its overseas ChatGPT integration — to China. Qwen (Tongyi Qianwen) is Alibaba Cloud's family of large language and multimodal models, widely used both as open-weight releases and as an enterprise API, making it a natural local partner for Siri and writing assistance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.alibabacloud.com/en/solutions/generative-ai/qwen?_p_lc=1">Qwen - Alibaba Cloud</a></li>
<li><a href="https://support.apple.com/guide/iphone/learn-visual-intelligence-iph12eb1545e/ios">Learn about what’s around you with Visual Intelligence on ...</a></li>

</ul>
</details>

**Tags**: `#Apple Intelligence`, `#China`, `#Alibaba Qwen`, `#iOS`, `#AI localization`

---