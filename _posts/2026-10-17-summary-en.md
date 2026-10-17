---
layout: default
title: "Horizon Summary: 2026-10-17 (EN)"
date: 2026-10-17
lang: en
---

> From 34 items, 2 important content pieces were selected

---

1. [DeepSeek releases V4.1-Flash-1017 with coding benchmark gains](#item-1) ⭐️ 8.0/10
2. [Claimed Untethered Jailbreak for iPhone 18 Pro Survives Reboots](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek releases V4.1-Flash-1017 with coding benchmark gains](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) ⭐️ 8.0/10

DeepSeek published DeepSeek-V4.1-Flash-1017 on Hugging Face and its API, describing it as a minor update to DeepSeek-V4.1-Flash that nonetheless delivers substantial improvements across reasoning, coding, and agentic tasks. On the company's own news page, the new version is shown beating Sol 5.6 on 10 of 11 coding benchmarks. The release keeps pressure on OpenAI and Anthropic in the coding-assistant market, and the Hacker News thread (657 points, 556 comments) shows developers increasingly weighing throughput, latency, and transparency against raw benchmark scores. For teams building multi-agent coding pipelines, a cheaper, faster model that is competitive on benchmark suites can shift real production choices. Per the model card and OpenRouter listing, V4.1-Flash is a sparse multimodal Mixture-of-Experts model with a 552B-parameter backbone that activates only 8B parameters on input and 16B on output, supports contexts up to one million tokens, and is the first model built on DeepSeek's Causal Encoder-Decoder (CED) architecture. The comparison target cited by the community is Sol 5.6, not the newer Sol 6.1, so the benchmark lead is against a prior-generation model.

hackernews · theykk · Oct 17, 08:21 · [Discussion](https://news.ycombinator.com/item?id=50129045)

**Background**: DeepSeek is a Chinese AI lab known for releasing open-weight models whose weights can be downloaded from Hugging Face rather than only accessed through a paid API. Mixture-of-Experts (MoE) models keep a very large total parameter count but route each token through only a small subset of experts, which cuts inference cost and latency — the reason a 552B-parameter model can still feel fast. Coding benchmarks such as SWE-bench, HumanEval, and LiveCodeBench score models by running generated code against unit tests, and 'Sol' and 'Opus' here refer to competing frontier models from OpenAI and Anthropic respectively.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek -ai/ DeepSeek - V 4 . 1 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4.1-flash">DeepSeek V 4 . 1 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">Introducing DeepSeek - V 4 . 1 - Flash : smarter, faster, more efficient.</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree DeepSeek is not clearly ahead of Sol or Gemini on raw benchmarks, but argue it 'feels' better because of high tokens-per-second and low time-to-first-token, plus the openness of its chain-of-thought with no random cyber-review blocks. A hands-on multi-agent code-review test on a 200+ file C++ codebase undercut that impression somewhat: DeepSeek via its own API took about 20 minutes to surface one relevant P1 issue, while GPT 5.6 Sol took 5m30s and GPT 6.1 Sol 4m30s for more relevant findings, and GLM 5.3 Flash took over an hour. Several users framed the release as evidence of the value of a diverse model ecosystem and said they are switching back to DeepSeek for writing code.

**Tags**: `#AI/ML`, `#LLM release`, `#DeepSeek`, `#coding benchmarks`, `#model comparison`

---

<a id="item-2"></a>
## [Claimed Untethered Jailbreak for iPhone 18 Pro Survives Reboots](https://x.com/calif_io/status/2111080240978223545?s=20) ⭐️ 8.0/10

Researcher @calif_io claims to have demonstrated a public untethered jailbreak for the iPhone 18 Pro on a fully patched iOS release that persists across reboots and requires no computer, which would be the first publicly shown full untethered jailbreak since iOS 9. The claimed chain combines abuse of the cryptex subsystem, TSS signing-ticket spoofing, and a PAC bypass, reportedly landing just after Apple shipped 273 vulnerability fixes on September 14. If verified, this would be a landmark security-research result: a full untethered chain on modern hardware directly defeats the three mitigations Apple has invested in most heavily — signed system volumes, server-side firmware signing, and pointer authentication. It would matter to Apple's platform-security teams, jailbreak and exploit developers, and anyone relying on iOS as a hardened endpoint, and it would sharpen the argument that even aggressively patched releases still carry full-chain exploit paths. The claim rests on a short single-source tweet with no technical write-up, no CVE identifier, and no vendor or independent confirmation, so treat the three-layer chain as unverified. Each layer is individually plausible on paper — cryptex containers, TSS ticket validation, and PAC-signed pointers are all real, heavily-defended components — but chaining all three into a persistent, computer-free jailbreak on a current flagship is exactly the part that needs independent replication.

telegram · zaihuapd · Oct 17, 10:34

**Background**: A jailbreak removes iOS's restrictions on running unsigned code; an "untethered" jailbreak keeps working after a normal reboot without re-running an exploit from a computer, which is far harder than a tethered or semi-tethered one. Cryptex is Apple's mechanism for mounting sealed, cryptographically signed auxiliary system volumes, and TSS (Ticket Signing Server) is the Apple service that issues signing tickets controlling which firmware images a device will accept, which is why TSS spoofing is central to downgrades and persistent exploits. PAC (Pointer Authentication Codes) is an ARM mitigation that signs pointers so attackers cannot redirect control flow by corrupting them, and a kernel PAC bypass is a required step for essentially any modern jailbreak on A12-and-later chips.

<details><summary>References</summary>
<ul>
<li><a href="https://theapplewiki.com/wiki/PAC_Bypasses">PAC Bypasses - The Apple Wiki</a></li>
<li><a href="https://github.com/tihmstar/tsschecker">GitHub - tihmstar/tsschecker: a powerfull tool to check tss signing ...</a></li>
<li><a href="https://discussions.apple.com/thread/254340117">is Cryptex a standard part of the ios sys… - Apple Community</a></li>

</ul>
</details>

**Tags**: `#iOS jailbreak`, `#security research`, `#exploit chain`, `#PAC bypass`, `#Apple`

---