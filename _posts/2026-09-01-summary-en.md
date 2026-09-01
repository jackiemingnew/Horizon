---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 37 items, 6 important content pieces were selected

---

1. [Tim Cook Steps Down as Apple CEO; John Ternus Takes Over to Focus on AI](#item-1) ⭐️ 9.0/10
2. [Google Removes MV2 Extensions, Including uBlock Origin, from Chrome Web Store](#item-2) ⭐️ 8.0/10
3. [NAT: The Original Sin of Internet Centralization?](#item-3) ⭐️ 8.0/10
4. [Sliding-window attention with sinks outperforms linear attention on long-context reasoning](#item-4) ⭐️ 8.0/10
5. [OpenClaw 2.0 Delivers Largest Update Ever with 16,000 Pull Requests](#item-5) ⭐️ 8.0/10
6. [DeepSeek Releases V4-Flash-Vision-Exp, First Multimodal Model in V4 Family](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Tim Cook Steps Down as Apple CEO; John Ternus Takes Over to Focus on AI](https://www.bloomberg.com/news/articles/2026-08-30/apple-s-new-ceo-john-ternus-takes-reins-from-tim-cook-focusing-on-ai) ⭐️ 9.0/10

Tim Cook stepped down as Apple CEO on August 31, with John Ternus taking over on September 1. Ternus, a 51-year-old hardware engineering veteran, will prioritize shipping AI features, including the delayed Siri upgrade, and Apple plans to unveil its first foldable iPhone at the September 9 event. The leadership change marks a strategic pivot at one of the world's most influential technology companies, making AI the centerpiece of Apple's roadmap. The foldable iPhone would open a major new product category, while the transition could reshape how Apple competes in generative AI. According to the report, the first foldable iPhone will have 12GB of RAM and deep Siri AI integration that combines screen, calendar, and camera data to understand real-world scenes. Tim Cook will remain executive chairman, ensuring continuity during the transition.

telegram · zaihuapd · Aug 31, 10:21

**Background**: Apple is one of the largest and most influential technology companies, known for iPhone, Mac, and services. A CEO transition is rare for Apple, and this one comes as the industry races to adopt AI, with Siri having fallen behind rivals in generative AI features.

**Tags**: `#Apple`, `#CEO transition`, `#Artificial Intelligence`, `#Tim Cook`, `#John Ternus`

---

<a id="item-2"></a>
## [Google Removes MV2 Extensions, Including uBlock Origin, from Chrome Web Store](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

Google has removed all remaining Manifest V2 extensions from the Chrome Web Store, including the popular ad blocker uBlock Origin. This marks the completion of the transition to Manifest V3, which was announced years ago. This change affects millions of users who rely on powerful MV2 ad blockers like uBlock Origin, potentially making them more vulnerable to intrusive ads and malicious content. It also raises concerns about Google's control over the web and the future of ad-blocking technology in Chromium-based browsers. Manifest V3 replaces the long-lived background pages of MV2 with service workers and restricts remote code execution, which limits the filtering capabilities of extensions. While uBlock Origin has a MV3 version called uBlock Origin Lite, it uses declarativeNetRequest rules that are less flexible than the full blocking engine available in Firefox.

hackernews · twapi · Aug 31, 21:10 · [Discussion](https://news.ycombinator.com/item?id=49514878)

**Background**: Manifest V2 is the previous specification for Chrome extensions, allowing long-lived background pages and broad access to web requests. Google announced in 2020 that it would phase out MV2 in favor of MV3, which is designed to improve privacy, security, and performance. uBlock Origin is a free and open-source content blocker that uses dynamic filtering to block ads and malicious domains; it works best on Firefox, which still supports MV2-like APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V3 | Chrome for Developers</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline">Manifest V2 support timeline | Chrome for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The comments reflect strong frustration and distrust toward Google. Many users recommend switching to Firefox, noting that uBlock Origin performs better there and that no single company should have such control over the web. Some also highlight that ad blocking is now a safety issue, especially for less tech-savvy users who may fall for malicious ads.

**Tags**: `#Chrome`, `#Manifest V3`, `#adblock`, `#privacy`, `#uBlock Origin`

---

<a id="item-3"></a>
## [NAT: The Original Sin of Internet Centralization?](https://dreamstation.systems/personal/ntppost.html) ⭐️ 8.0/10

A blog post at dreamstation.systems argues that Network Address Translation (NAT) is a root cause of internet centralization. The resulting discussion gained attention when Rusty Russell, the original implementer of Linux NAT, joined in with firsthand commentary on his design choices. This debate challenges conventional assumptions about network neutrality and end-to-end connectivity, showing how a pragmatic engineering fix contributed to today's client-server-dominated internet. It also highlights tensions between IPv4 address conservation, CGNAT, and the ability for users to host services. Rusty Russell explained that he avoided port reservation in Linux NAT to squeeze more connections into one IP address when the remote address allowed differentiation, which made incoming traffic from a different address unroutable. Commenters note that while ordinary home NAT can be acceptable, CGNAT is widely seen as a more serious threat to user freedom.

hackernews · robinpie · Aug 31, 02:23 · [Discussion](https://news.ycombinator.com/item?id=49504905)

**Background**: Network Address Translation (NAT) maps multiple private IP addresses to a single public IP address, a technique widely adopted to cope with IPv4 address exhaustion. NAT also acts as a basic firewall by blocking unsolicited inbound connections, but it breaks the end-to-end principle that originally defined the internet. This has led some to argue that NAT encouraged a client-server model and made it harder for individuals to run always-available servers, pushing the internet toward data-center-based centralization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Network_address_translation">Network address translation - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/computer-networks/network-address-translation-nat/">Network Address Translation (NAT) - GeeksforGeeks</a></li>
<li><a href="https://www.ietf.org/archive/id/draft-nottingham-avoiding-internet-centralization-01.html">Centralization and Internet Standards</a></li>

</ul>
</details>

**Discussion**: Commenters are split: some agree that NAT was an early blow to the open internet and trained users to see client-server as natural, while others argue that only CGNAT is truly harmful and that regular NAT has protected millions of insecure devices. Rusty Russell's candid account of the original design tradeoffs adds weight to both sides of the debate, with a tone of regret about unintended consequences.

**Tags**: `#NAT`, `#internet architecture`, `#centralization`, `#networking`, `#commentary`

---

<a id="item-4"></a>
## [Sliding-window attention with sinks outperforms linear attention on long-context reasoning](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/) ⭐️ 8.0/10

A new arXiv preprint (2608.28444) reports that Sliding Window Attention (SWA) with attention sinks achieves 2–10x higher performance than linear attention variants on long-context reasoning benchmarks such as Needle-in-a-Haystack and BABILong. The authors argue that the post-training-to-linear-attention pipeline has not been properly compared against simpler baselines and recommend switching to SWA. This challenges the prevailing industry direction of spending post-training compute to produce linear-attention models. If verified, it suggests that a simple, fast, memory-efficient baseline could be superior for long-context reasoning, potentially saving significant resources. The paper focuses on SWA with attention sinks—special tokens that absorb excess attention and stabilize sliding-window generation. It reports that linear attention 'may have shown some promise' but likely needs training from scratch or extensive post-training to match SWA, and the authors 'strongly recommend switching to SWA.'

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Aug 31, 16:35

**Background**: Standard softmax attention has quadratic cost with sequence length, making long-context processing expensive. Sliding window attention restricts each token to attend only within a local window, reducing cost to linear, and attention sinks (retained early tokens) help stabilize generation. Linear attention variants also aim to reduce complexity but often require post-training or training from scratch to maintain performance. Benchmarks like BABILong test reasoning across facts distributed in long contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.28444v1">Sliding - window beats linear attention</a></li>
<li><a href="https://carnotresearch.medium.com/let-the-chaos-sink-in-481c8a37471e">Let the Chaos Sink In. Balancing attention in transformers | Medium</a></li>
<li><a href="https://arxiv.org/abs/2406.10149">[2406.10149] BABILong : Testing the Limits of LLMs with Long ...</a></li>

</ul>
</details>

**Tags**: `#attention`, `#long-context`, `#LLM`, `#efficient transformers`, `#research`

---

<a id="item-5"></a>
## [OpenClaw 2.0 Delivers Largest Update Ever with 16,000 Pull Requests](https://openclaw.ai/blog/openclaw-2-accidentally) ⭐️ 8.0/10

OpenClaw released version 2.0 on August 30, its largest update ever, incorporating over 16,000 pull requests from 933 contributors, including 569 first-time participants. The release overhauls installation, messaging, memory, skills, models, browser, plugins, and security, and introduces shared cloud sessions for multiplayer collaboration. This release signals a major milestone for the open-source AI assistant space, demonstrating strong community momentum and a comprehensive overhaul of the user experience. The scale of contributions — roughly half of all pull requests in the project's history — shows how vibrant and active the OpenClaw community has become. The project went nearly seven weeks without a new release to prepare this update, and it simplifies the installation flow, rebuilds the browser-side experience, and adds shared cloud sessions that allow teams to take over ongoing work. The update touches every core area, from memory and skills to models and security, and runs on a user's own machine through existing chat apps.

telegram · zaihuapd · Aug 31, 04:38

**Background**: OpenClaw is a free and open-source autonomous AI agent that executes tasks using large language models (LLMs) and uses messaging platforms as its main user interface. A pull request is a mechanism in distributed version control systems like Git and GitHub that lets contributors propose, review, and merge code changes; the large number of pull requests here indicates extensive collaborative development. The project aims to provide an open-source AI assistant that runs locally and integrates with chat apps users already have.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw</a></li>
<li><a href="https://openclaw.ai/">OpenClaw — Open -Source AI Assistant</a></li>
<li><a href="https://tbreak.com/openclaw-2-0-rebuilt-browser-app/">OpenClaw 2.0: rebuilt browser app, shared sessions</a></li>

</ul>
</details>

**Tags**: `#OpenClaw`, `#software release`, `#AI assistant`, `#open source`, `#major update`

---

<a id="item-6"></a>
## [DeepSeek Releases V4-Flash-Vision-Exp, First Multimodal Model in V4 Family](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) ⭐️ 8.0/10

DeepSeek released DeepSeek-V4-Flash-Vision-Exp on Hugging Face, an experimental multimodal model built on the V4-Flash architecture with added vision modules and continued training. Its multimodal agent benchmark score (ApexBench) improved from 26.2 to 36.5, while text agent performance stayed roughly flat. This matters because it brings multimodal understanding to the V4 series for the first time and significantly boosts agentic capabilities, making the model more useful for vision-language tasks. Developers and enterprises using DeepSeek models now have access to an experimental model that handles both text and visual inputs through the API. The model weights are available on Hugging Face, and the API accepts the model ID 'deepseek-v4-flash-vision-exp'. It is marked as experimental; ApexBench is an agent benchmark reported by DeepSeek using Pass@1, but the benchmark's task count and creating institution are not fully disclosed.

telegram · zaihuapd · Aug 31, 11:41

**Background**: DeepSeek is a Chinese AI lab known for open-weight large language models such as V3 and V4. The V4-Flash variant is a fast, text-only model, and this experimental release adds vision modules and continues training to unlock multimodal understanding. ApexBench evaluates interactive, multimodal agent performance on real-world tasks like academic poster editing and distributed HPC profiling.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp">deepseek-ai/ DeepSeek - V 4 - Flash - Vision - Exp · Hugging Face</a></li>
<li><a href="https://api-docs.deepseek.com/updates/">DeepSeek API Docs</a></li>
<li><a href="https://www.datalearner.com/en/benchmarks/apexbench">ApexBench: Multimodal Agent Benchmark and Model Scores ...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#multimodal`, `#AI model`, `#vision`, `#agent`

---