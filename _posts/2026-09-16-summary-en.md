---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
lang: en
---

> From 33 items, 3 important content pieces were selected

---

1. [Hackers Breach Flock Safety Cameras, Exposing Hardcoded Credentials](#item-1) ⭐️ 8.0/10
2. [TMLR quizzes authors of 10 desk-rejected papers; most can't explain their own work](#item-2) ⭐️ 8.0/10
3. [Cloudflare adds setting to block AI training crawlers while keeping search indexing](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Hackers Breach Flock Safety Cameras, Exposing Hardcoded Credentials](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

Security researcher Micah Lee, in reporting published by Wired in collaboration with 404 Media, documented how hackers gained access to Flock Safety ALPR surveillance cameras by exploiting hardcoded credentials, plaintext-stored secrets, and a broken secure boot process. Distributed Denial of Secrets subsequently published partition images taken from the cameras, and Flock's Vulnerability Disclosure Policy was shown to explicitly exclude cases where researchers interact with the device or download its data. Flock Safety's ALPR cameras are deployed at scale by police departments and neighborhood associations across the United States, and the finding that they can be physically compromised undermines the trust these agencies place in the data they collect. Because federal services like the NCIC hotlist are routinely compared against Flock-collected plates, a camera-level breach raises direct privacy and civil-liberties concerns for anyone whose vehicle is scanned. The exposed secret was an API key rather than an admin password, but it can be used to request credentials that are themselves stored in plaintext and appear capable of authenticating to Flock's servers; it remains unclear exactly what an attacker could do after authenticating as a camera. Commenters also noted that Flock's VDP welcomes disclosures only as long as researchers never interact with the device or download its data, which critics say is designed to create an appearance of responsible security posture rather than to actually learn about vulnerabilities.

hackernews · driverdan · Sep 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=49726586)

**Background**: Flock Safety builds automated license plate recognition (ALPR) cameras that photograph passing vehicles and let law enforcement search the resulting plate data, and its systems are frequently linked to hotlists such as the FBI's National Crime Information Center (NCIC). Hardcoded credentials are a well-known vulnerability class catalogued as CWE-798 (and described by OWASP as 'Use of hard-coded password'), in which secrets baked into firmware or source code can be extracted and reused by attackers. A Vulnerability Disclosure Policy (VDP) is the channel through which vendors ask security researchers to report flaws, so the scope of what a VDP excludes matters a great deal. The cameras are typically mounted in public spaces, meaning their threat model must account for physical access by anyone who walks up to the device.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/06/are-your-local-police-using-flock-safety-alprs-scan-immigrants">Are Your Local Police Using Flock Safety ALPRs to Scan for...</a></li>
<li><a href="https://owasp.org/www-community/vulnerabilities/Use_of_hard-coded_password">Use of hard-coded password - OWASP Foundation Hardcoded Credentials CWE-798: Fix Guide - Offensive360 CVE-2026-4832: SNMP Hard-coded Credentials Vulnerability Hardcoded Credentials Vulnerability: Why Immediate Action Matters DSA-2026-079: Security Update for RecoverPoint for Virtual ... CVE-2025-1393: Hard-Coded Credentials Auth Bypass Flaw</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was broadly critical of Flock, with commenters calling hardcoded credentials a sign of 'total incompetence' and attributing the flaws to 'pure laziness aka reduced time to market' rather than genuine engineering difficulty. Several commenters highlighted that Flock's VDP appears written to discourage real vulnerability reports, and one noted that because the devices sit in unsecured public spaces, off-the-shelf hardware and software stacks all but guarantee that attackers with local physical access can succeed.

**Tags**: `#security`, `#surveillance`, `#iot`, `#vulnerability-disclosure`, `#privacy`

---

<a id="item-2"></a>
## [TMLR quizzes authors of 10 desk-rejected papers; most can't explain their own work](https://www.reddit.com/r/MachineLearning/comments/1wid67h/tmlr_reached_out_to_the_authors_of_10_papers/) ⭐️ 8.0/10

TMLR's Co-Editor-in-Chief personally reached out to the authors of ten submissions that had been slated for desk rejection, and the results — published in a Medium post and summarized on r/MachineLearning — were stark: one set of authors withdrew, one said they were unavailable, one scheduled a meeting but never showed up, three could not answer basic questions about the paper, three could discuss high-level ideas but stumbled on technical details, and only one answered all questions (and even that paper was found to contain a major flaw). The episode offers concrete, if anecdotal, evidence that a non-trivial share of journal submissions may be produced by people — or LLM pipelines — who cannot themselves defend the science, which strikes at the heart of peer review's assumption that the submitting author is the paper's author; if such cases are widespread, reviewers and editors bear an ever-growing fraud-detection burden and the credibility of AI/ML publishing is at stake. The Co-EiC explicitly frames this as a non-systematic, small-sample investigation rather than a formal study, so the 10-paper tally should not be read as a measured fraud rate; notably, even the single author who handled every question had a major flaw identified in the paper, suggesting that fluent explanation is not the same as sound research.

reddit · r/MachineLearning · /u/hihey54 · Sep 16, 23:20

**Background**: TMLR (Transactions on Machine Learning Research) is a machine-learning research journal, and its Co-EiC is one of its Co-Editors-in-Chief, the senior editors who make final decisions on manuscripts. A desk rejection is when a journal turns a paper down before sending it out for peer review, usually because the editor judges it out of scope, unsuitable in format, or not a genuine research article — which is exactly why papers flagged for desk rejection are an unusual group to interview, since normally no detailed review ever takes place.

<details><summary>References</summary>
<ul>
<li><a href="https://scientific-publishing.webshop.elsevier.com/publication-process/paper-rejection-common-reasons/">Paper Rejection: Common Reasons | Elsevier Language Services</a></li>
<li><a href="https://authorservices.taylorandfrancis.com/blog/get-published/5-reasons-for-desk-rejection-and-how-to-avoid-them/">5 top reasons for desk rejection – and how to avoid them - Author Services</a></li>
<li><a href="https://www.editage.com/insights/what-is-the-meaning-of-awaiting-eic-decision-in-manuscript-central">Meaning of 'Awaiting EiC Decision' | Editage Insights</a></li>

</ul>
</details>

**Tags**: `#peer-review`, `#ML-research-ethics`, `#TMLR`, `#academic-publishing`, `#LLM-generated-content`

---

<a id="item-3"></a>
## [Cloudflare adds setting to block AI training crawlers while keeping search indexing](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/) ⭐️ 8.0/10

On September 15, Cloudflare announced a new "Disallow AI Training" setting that lets site owners keep their pages indexed by search engines while blocking crawlers that do not meet its requirements for using content in AI training. Apple, Google, and Microsoft have either already complied or committed to complying with those requirements. Cloudflare sits in front of a large share of the web, so a single toggle gives publishers a practical, enforceable way to separate search indexing from AI training without losing their search traffic. It marks a shift from purely voluntary signals like robots.txt toward infrastructure-level content governance, and pushes major AI and search companies to publicly commit to those rules. The setting is configured per domain, and choosing "block" blocks all crawlers that fall under the AI-training policy—including mixed crawlers that both index for search and feed AI training—which means search indexing can also be affected. Cloudflare also says it plans, in early next year, to let sites control the proportion of their content that can be used in AI summaries, and according to coverage, Bing does not yet support the robots.txt opt-out signal.

telegram · zaihuapd · Sep 16, 05:46

**Background**: Websites have traditionally used the robots.txt file to tell crawlers what they may access, but that convention relies on voluntary compliance and does not distinguish between a search engine indexing a page and an AI company scraping it for training data. Cloudflare is a reverse proxy and CDN that serves traffic for a large portion of the internet, so it can enforce such rules at the network edge on behalf of its customers. "Mixed-use" crawlers are bots such as Googlebot, Applebot, and Bingbot that perform search indexing but whose operators may also use fetched content for AI purposes, which is why separating the two use cases has been technically and commercially difficult.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/1/003/108.htm">Cloudflare 推出新设置：可允许搜索引擎爬取，同时拒绝 AI 训练 - IT之家</a></li>
<li><a href="https://developers.cloudflare.com/ai-crawl-control/">Overview · Cloudflare AI Crawl Control docs</a></li>
<li><a href="https://www.bingdada.com/blog/cloudflare-disallow-ai-training-search-crawlers">Cloudflare 新设置：拒绝 AI 训练不伤搜索收录 | Bingdada 技术博客</a></li>

</ul>
</details>

**Tags**: `#AI Crawlers`, `#Cloudflare`, `#AI Training Data`, `#Web Scraping`, `#Content Rights`

---