---
layout: default
title: "Horizon Summary: 2026-10-17 (EN)"
date: 2026-10-17
lang: en
---

> From 37 items, 5 important content pieces were selected

---

1. [Claude Solves NIST Elliptic Curve Seed Mystery](#item-1) ⭐️ 8.0/10
2. [Jake Archibald benchmarks JPEG XL vs AVIF for web images](#item-2) ⭐️ 8.0/10
3. [37-Year-Old OpenBSD Kernel Bug Exploited in New Research](#item-3) ⭐️ 8.0/10
4. [ORL speeds up diffusion LLMs to 2,788 tokens/s on one RTX 5090](#item-4) ⭐️ 8.0/10
5. [Court Documents Reveal How Telegram Hands User Data to U.S. Authorities](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Solves NIST Elliptic Curve Seed Mystery](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 8.0/10

Anthropic's Claude AI discovered that the NIST elliptic curve seeds for P-192, P-224, P-256, P-384, and P-521 were not produced by any hash algorithm, but were the output of the C library's lrand48 pseudo-random number generator seeded with Unix timestamps. The find was made in under half an hour and resolves a cryptographic mystery that had stood for roughly 25 years. The result restores public confidence that the curve seeds were generated through an ordinary, verifiable process rather than being deliberately chosen to embed a hidden backdoor, a fear intensified by past episodes such as Dual_EC_DRBG. It also highlights how AI tools can accelerate hard mathematical detective work, and Anthropic donated the associated bounty to the Internet Security Research Group (ISRG). The fifth binary-field seed, B-163, remains unexplained; the simplest hypothesis is that it was generated the same way but a digit was mistyped during publication. Even with the method confirmed, the discovery does not prove that no candidate seeds were searched over and discarded—since the curves were reportedly generated over a period of months, discarded candidates would be invisible to this analysis.

hackernews · ahlCVA · Oct 16, 18:55 · [Discussion](https://news.ycombinator.com/item?id=50122800)

**Background**: NIST published the P-192 through P-521 elliptic curves in 2000 in FIPS 186-2, and these curves underpin much of modern cryptography, including ECDSA signatures. ANSI X9.62 specified that the curves be generated 'verifiably at random' by taking an arbitrary seed, hashing it with SHA-1, and deriving the curve coefficient b from the output. Because the NSA reportedly supplied the seeds in 1997, and because a seed is only as trustworthy as its provenance, cryptographers long demanded that the original seed-generation process be shown to be innocuous; Filippo Valsorda even offered a $12,000 bounty for solving it.

<details><summary>References</summary>
<ul>
<li><a href="https://words.filippo.io/seeds-bounty/">Announcing the $12k NIST Elliptic Curves Seeds Bounty</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/bounty-offered-for-secret-nsa-seeds-behind-nist-elliptic-curves-algo/">Bounty offered for secret NSA seeds behind NIST elliptic curves algo</a></li>
<li><a href="https://www.anthropic.com/research/ecdsa-curve-origins">Claude reveals ECDSA curve origins \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Commenters were largely delighted, with one joking about an NSA employee 'quietly giggling to themselves for the last quarter century' and another summing up the saga as '13 years of tinfoil hats for srand48(time(NULL)).' A more skeptical thread noted that confirming the production method does not rule out deliberate selection, since candidate seeds generated and discarded over months cannot be observed. Others praised Anthropic for choosing the higher bounty and donating it to ISRG, and one commenter suggested the unexplained B-163 seed is likely just a typo in the published number.

**Tags**: `#cryptography`, `#elliptic-curves`, `#NIST`, `#random-number-generator`, `#Claude-AI`

---

<a id="item-2"></a>
## [Jake Archibald benchmarks JPEG XL vs AVIF for web images](https://jakearchibald.com/2026/jpeg-xl-vs-avif/) ⭐️ 8.0/10

Web-platform engineer Jake Archibald published a hands-on comparison of JPEG XL (JXL) and AVIF for web delivery, benchmarking file sizes and visual quality on photos, screenshots and illustrations. His post triggered a large Hacker News discussion (183 points, 142 comments) that dug into encoding speed, quality artifacts and practical ffmpeg settings. Image bytes are one of the largest remaining performance costs on the web, so the choice between JXL and AVIF directly affects page weight, bandwidth and rendering quality for every site. The debate also highlights that format choice alone is not enough: encoder maturity and settings often matter more than the container format itself. Community members noted that libjxl's high-effort modes (effort >7) are extremely slow — reportedly 9 to 46 seconds per image, 50–180x its default — because of an iterative Butteraugli perceptual-metric optimization loop, though alternative encoders like jixel achieve similar results in seconds. Others shared concrete ffmpeg recipes for AVIF with alpha/PNG-transparency handling, and pointed out that better JXL encoders can cut lossless screenshot sizes by roughly 30–39%.

hackernews · farlight · Oct 16, 16:12 · [Discussion](https://news.ycombinator.com/item?id=50120224)

**Background**: JPEG XL is a next-generation image format supporting both lossy and lossless compression, developed by the JPEG committee together with Google and Cloudinary, and designed to improve on legacy JPEG while remaining efficiently decodable in software. AVIF is a rival format from the Alliance for Open Media, built on the AV1 video codec, and is already widely supported in browsers. Both formats use lossy compression, which reduces file size by discarding data and can introduce visible compression artifacts such as banding or lost highlight detail.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>
<li><a href="https://shortpixel.com/blog/what-is-avif-and-why-is-it-good/">What is AVIF and why is it good? - ShortPixel Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compression_artifact">Compression artifact - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Sentiment was mixed but technically rich: several commenters praised AVIF for production use and shared tuned ffmpeg settings, while others argued the AVIF-rendered F1 image visibly erases and invents highlight detail on the car, which they see as proof of AVIF's weakness for critical imagery. A recurring counterpoint was that JXL's current encoders are still immature, so Archibald's file-size numbers understate what the format can achieve with better tooling.

**Tags**: `#image-compression`, `#web-performance`, `#jpeg-xl`, `#avif`, `#codecs`

---

<a id="item-3"></a>
## [37-Year-Old OpenBSD Kernel Bug Exploited in New Research](https://calif.io/research/big-fish) ⭐️ 8.0/10

A security researcher published a detailed writeup titled "Big Fish" that discloses and demonstrates exploitation of a 37-year-old kernel vulnerability in OpenBSD. The work shows the bug survived for decades in a codebase widely regarded as one of the most heavily audited in the open-source world. OpenBSD's reputation rests on its security-first philosophy and proactive source auditing, so an exploitable kernel bug lurking for 37 years challenges assumptions about how much review alone can guarantee. It is also a compelling case study on the practical limits of fuzzing and static analysis for certain classes of kernel bugs. Community members noted that the same flaw appears to have been accidentally fixed in NetBSD during a rewrite of that code in August 1999, suggesting the bug persisted only in the shared lineage of BSD kernels. Debate centered on whether the bug was reachable through fuzzing or static analysis, or whether it required a human reasoning about a specific exploitation primitive.

hackernews · rs_rs_rs_rs_rs · Oct 16, 14:44 · [Discussion](https://news.ycombinator.com/item?id=50118977)

**Background**: OpenBSD is a free, open-source Unix-like operating system known for its strong emphasis on security, correctness, and code transparency, including continuous auditing of its base system. Fuzzing is an automated testing technique that feeds invalid, unexpected, or random data into a program to trigger crashes and vulnerabilities, while static analysis inspects source code without executing it to find potential defects. This research illustrates how both automated approaches can miss bugs that require reasoning about exploit primitives.

<details><summary>References</summary>
<ul>
<li><a href="https://www.liquidweb.com/blog/what-is-openbsd/">What is OpenBSD ? Overview & Latest Features | Liquid Web</a></li>
<li><a href="https://www.lenovo.com/us/en/glossary/openbsd/">What is OpenBSD ? Secure Open-Source Operating... | Lenovo US</a></li>

</ul>
</details>

**Discussion**: Commenters praised the writeup's presentation style, with one joking about the OpenBSD-release-style graphics and looking forward to a theme song. Several noted the bug was accidentally fixed in NetBSD in August 1999, and a key discussion thread debated whether fuzzing or static analysis could realistically have caught this class of bug or whether it required a human thinking about the exploit primitive.

**Tags**: `#security`, `#kernel`, `#openbsd`, `#vulnerability-research`, `#exploitation`

---

<a id="item-4"></a>
## [ORL speeds up diffusion LLMs to 2,788 tokens/s on one RTX 5090](https://www.reddit.com/r/MachineLearning/comments/1x7qgr0/research_2788_tokenss_on_a_single_rtx_5090_with_a/) ⭐️ 8.0/10

A research team released ORL (On-Policy Residual Learning), a post-training method for diffusion language models that trains on fresh, self-generated residual trajectories and adds an Adjacent Entropy Contraction (AEC) loss to reduce uncertainty faster per denoising step. Combined with their custom inference engine dlmrt, they report up to 2,788 tokens/s for LLaDA-2.1-mini + ORL on a single RTX 5090, 7,708 tokens/s for DiffusionGemma 26B MoE + ORL in NVFP4 on 8× B200, and roughly 6.9× end-to-end throughput gains plus a HumanEval pass@1 rise from 82.9% to 89.6% on QwenDLM-4B. Models, training code, evaluation pipeline, and the inference engine are all open sourced. Diffusion language models can refine many tokens in parallel, but they have historically needed too many denoising passes to be competitive with autoregressive decoding on latency. ORL claims to attack exactly that bottleneck while also improving accuracy, and it is being released with an open inference engine, which could make parallel diffusion decoding practically usable for low-latency, single-request serving rather than just a research curiosity. All headline numbers are for single-request decoding at batch size 1 and are peak results on specific benchmarks, not averages across arbitrary prompts; LLaDA-2.1-mini only needed 4.2M self-generated training tokens and 36 H100 GPU-hours of post-training. The comparison against speculative decoding is an end-to-end system comparison rather than an isolated algorithmic one: ORL runs on dlmrt, while DFlash and EAGLE3 run on vLLM, and the results are self-reported and not yet peer reviewed.

reddit · r/MachineLearning · /u/arty_photography · Oct 16, 20:03

**Background**: Autoregressive LLMs generate text one token at a time from left to right, so latency scales with sequence length. Diffusion language models (dLLMs) instead start from a corrupted or masked sequence and iteratively denoise it, allowing many tokens to be refined and finalized in parallel, but they only pay off if the model can converge to a good answer in few forward passes. ORL is a post-training recipe that teaches an existing dLLM to carry forward and refine its own previous predictions as residual context, and dlmrt is a companion inference engine that captures the whole denoising loop in a single CUDA graph and executes it on the GPU to avoid per-step CPU launch and synchronization overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Introspective-Diffusion/ORL/blob/main/">ORL: On-Policy Residual Learning for Diffusion Language Models</a></li>
<li><a href="https://arxiv.org/abs/2508.10875">[2508.10875] A Survey on Diffusion Language Models - arXiv.org Diffusion Language Models: An Experimental Analysis Diffusion Language Models (dLLMs) - emergentmind.com (PDF) Diffusion-based Large Language Models Survey - ResearchGate Awesome Diffusion Language Models Diffusion-based Large Language Models Survey</a></li>
<li><a href="https://www.truefoundry.com/blog/sglang-vs-vllm-vs-tensorrt-llm">SGLang vs vLLM vs TensorRT-LLM: Choosing an Inference Engine</a></li>

</ul>
</details>

**Tags**: `#diffusion-language-models`, `#LLM-inference`, `#open-source`, `#GPU-optimization`, `#machine-learning-research`

---

<a id="item-5"></a>
## [Court Documents Reveal How Telegram Hands User Data to U.S. Authorities](https://www.404media.co/heres-what-telegram-giving-data-to-the-u-s-government-looks-like/) ⭐️ 8.0/10

Newly released court documents show that Telegram provided a user's phone number, user ID, and IP address to U.S. law enforcement in response to a U.S. court order, stating in its letter that it did so "voluntarily" while simultaneously disputing U.S. jurisdiction. The disclosure is tied to a case involving Mahmoud Al-Muhtadi, who is accused of participating in the October 7, 2023 attacks in Israel, and the filings indicate Telegram had handed over data on 2,253 users to U.S. authorities as of January of this year. The documents offer rare, concrete evidence of how a platform long marketed as privacy-friendly actually cooperates with U.S. law enforcement, which could reshape user trust and expectations around messaging-app confidentiality. They also put the spotlight on the unresolved legal question of jurisdiction — whether a company headquartered outside the U.S. must comply with American court orders — a tension that affects every global communications platform. The user data disclosed in the Al-Muhtadi case consisted of a phone number, a user ID, and an IP address — metadata rather than message content — and Telegram framed the handover as voluntary even as it contested U.S. jurisdiction, a positioning that leaves its legal obligations ambiguous. The figure of 2,253 users whose data was disclosed as of January suggests such requests are more routine than the company's public messaging implies.

telegram · zaihuapd · Oct 16, 14:57

**Background**: Telegram is a messaging app known for positioning itself as a privacy-focused alternative to rivals, but its architecture distinguishes between ordinary cloud chats, which are stored on Telegram's servers, and opt-in "secret chats" that use end-to-end encryption; only the latter is designed so that the company itself cannot read the contents. Because the disclosed items here are identifiers and network metadata rather than message text, the case illustrates how much a platform can hand over without breaking encryption at all. Telegram has also long been headquartered outside the United States, which is why its argument over U.S. jurisdiction is central to the dispute rather than a technicality.

**Tags**: `#Telegram`, `#privacy`, `#surveillance`, `#data disclosure`, `#law enforcement`

---