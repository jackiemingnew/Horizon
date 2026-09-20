---
layout: default
title: "Horizon Summary: 2026-09-20 (EN)"
date: 2026-09-20
lang: en
---

> From 28 items, 4 important content pieces were selected

---

1. [Samsung to More Than Double HBM4 and HBM4E Output](#item-1) ⭐️ 8.0/10
2. [Qwen Image 2.1: 7B Open-Weight Text-to-Image Model with Native Transparency](#item-2) ⭐️ 8.0/10
3. [AI-Fabricated Intel Nearly Triggered US Boarding of Chinese Ship](#item-3) ⭐️ 8.0/10
4. [大脑由两个不同的器官构成 原始部分负责生理功能 另一部分负责独特思考推理能力](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Samsung to More Than Double HBM4 and HBM4E Output](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) ⭐️ 8.0/10

Samsung is expected to more than double its production of HBM4 and HBM4E high-bandwidth DRAM, according to industry sources cited in a September 2026 report, in response to surging demand from AI accelerator makers. The expansion signals that the Korean memory giant intends to fight harder for share in the next-generation HBM market currently led by SK hynix. HBM supply is widely seen as the single tightest link in the AI accelerator supply chain, so Samsung's extra capacity could ease allocation pressure for Nvidia, AMD and other chip designers planning HBM4-based parts. It also intensifies the three-way contest between Samsung, SK hynix and Micron, and could shape memory pricing across the whole DRAM market. HBM4 is defined by a 2,048-bit interface and a logic-based base die, with Samsung advertising stacks of up to 64 GB and 4 TB/s of bandwidth built on its 1c DRAM and a 4 nm foundry logic die, while HBM4E pushes toward 16-layer stacks. The output plan covers both generations, but the report does not specify absolute wafer or bit volumes, and Samsung's ability to hit those numbers still depends on yields, which have reportedly been improving toward the 80% range.

hackernews · giuliomagnifico · Sep 20, 17:38 · [Discussion](https://news.ycombinator.com/item?id=49778029)

**Background**: High Bandwidth Memory (HBM) is DRAM that is vertically stacked into multiple dies and packaged right next to a GPU or AI accelerator, giving far more bandwidth than conventional DDR memory at the cost of complexity and price. Each generation multiplies the width and speed of the interface — HBM3E carried roughly 1.15–1.2 TB/s per stack, while HBM4 jumps to a 2,048-bit interface and puts a logic die at the base to allow semi-custom designs. Because AI training and inference are heavily memory-bandwidth bound, accelerator shipments are effectively gated by how much HBM the memory makers can produce, which is why capacity announcements like this one move the whole AI hardware ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://shattered.io/hbm4-memory-nvidia-rubin-yield-2026/">HBM 4 Memory Hits 80% Yield, Powers Nvidia Rubin</a></li>
<li><a href="https://semiconductor.samsung.com/dram/hbm/">HBM | DRAM | Samsung Semiconductor Global</a></li>

</ul>
</details>

**Discussion**: Commenters argued that the real bottleneck for Chinese AI accelerators is HBM output rather than processors or ASML lithography tools, noting that Huawei's Ascend volumes are limited by CXMT's HBM capacity. Others praised die thinning getting mainstream attention, debated why HBM is not yet practical as primary consumer memory, predicted a memory glut and plunging prices after the shortage, and regretted that the AI-driven HBM boom will make consumer DRAM more expensive.

**Tags**: `#HBM4`, `#Samsung`, `#AI hardware`, `#semiconductor manufacturing`, `#memory`

---

<a id="item-2"></a>
## [Qwen Image 2.1: 7B Open-Weight Text-to-Image Model with Native Transparency](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

Qwen released Image 2.1, a 7B-parameter open-weight text-to-image model that is dramatically smaller than the 20B Qwen-Image 1 while adding native RGBA transparency output, native 2048×2048 (2K) generation, and substantially improved text rendering. Unlike many earlier Qwen releases, it ships under a notably more restrictive license rather than Apache 2.0. Because the model is only 7B parameters, it can realistically run on consumer-grade local hardware, which matters for designers and developers who want private, offline image generation. Its native transparency and strong text rendering target real design workflows (UI mockups, layered assets, marketing graphics) where open-weight models have historically lagged behind closed models like GPT-Image-2. The model generates at native 2K resolution rather than upscaling into it, supports editing across up to 10 reference images, and can produce regular or transparent RGBA images, edit transparent layers, and extract subjects from photographs within a single model. The main caveat is licensing: it is no longer Apache-licensed, which restricts commercial reuse compared with prior Qwen releases.

hackernews · jmillikin · Sep 20, 13:09 · [Discussion](https://news.ycombinator.com/item?id=49775499)

**Background**: Open-weight models are AI systems whose trained parameters (weights) are published for download, but the license determines whether you may modify, fine-tune, or redistribute them; open weights are not the same as fully open-source AI. Qwen is Alibaba Cloud's model family, historically released under permissive licenses like Apache 2.0, and is one of the most widely used Chinese open-weight families. Text-to-image diffusion models conventionally output only RGB images, so transparent backgrounds usually require a separate background-removal step, and rendering legible text inside generated images has long been a known weakness of these models.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen-Image-2.1">Qwen/Qwen- Image -2.1 · Hugging Face</a></li>
<li><a href="https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight">Qwen- Image -2.1 in ComfyUI: Open-Weight Image Generation and...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**Discussion**: Hacker News discussion (457 points, 148 comments) was largely positive: commenters highlighted the dramatic size reduction from 20B to 7B, the rarity of native transparency support, and text rendering that one prompt-to-UI developer called "much, much better than anything else on the open weights market right now" after side-by-side comparison with gpt-image-2. The most consistent criticism was the shift away from Apache licensing, and one commenter observed that local image generation currently feels ahead of local code generation in quality and speed.

**Tags**: `#image-generation`, `#open-weights`, `#qwen`, `#diffusion-models`, `#licensing`

---

<a id="item-3"></a>
## [AI-Fabricated Intel Nearly Triggered US Boarding of Chinese Ship](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship) ⭐️ 8.0/10

According to a CNN report published on September 18, a US Special Operations Command intelligence analyst used an AI chatbot to fuse open-source intelligence with classified signals intelligence, and the model incorrectly identified the cargo manifest of a Chinese ship. The analyst then used AI again to package that flawed conclusion into a properly formatted formal intelligence report that was distributed up the command chain, prompting an interdiction plan in which armed personnel were prepared to board and military aircraft had already taken off — until officials dug into the report's provenance shortly before execution and discovered the whole thing was AI-generated and the cargo information was wrong. This is a rare documented case of an AI hallucination propagating up a real military decision chain far enough to nearly trigger an armed interdiction of a foreign vessel, which turns abstract AI-safety concerns about hallucination and human-in-the-loop oversight into a concrete national-security and diplomatic risk. It is likely to intensify scrutiny of how defense and intelligence agencies validate machine-generated analysis, and of who is accountable when an AI-generated error reaches the point of using force. The report passed through multiple command levels before anyone questioned it, suggesting that the model's fluent, correctly formatted output substituted for substantive verification of the underlying cargo data. CNN's account rests on four people familiar with the matter, two of whom said armed personnel were ready to board and aircraft had already launched, and the operation was halted only in the final moments when officials traced the report back to its AI origin.

telegram · zaihuapd · Sep 20, 03:07

**Background**: The case involves intelligence fusion, which combines different collection disciplines: OSINT (open-source intelligence) drawn from publicly available material, and SIGINT (signals intelligence) gathered by intercepting communications and electronic signals. AI hallucination refers to an AI system generating false or misleading information presented as fact — large language models are prone to this because they produce statistically plausible text rather than verified statements. US Special Operations Command is the unified command responsible for special operations forces, and an interdiction or boarding operation against a vessel is a high-stakes action with serious diplomatic consequences.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence ) - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-hallucinations">What Are AI Hallucinations ? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_intelligence_gathering_disciplines">List of intelligence gathering disciplines - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#Hallucination`, `#Military AI`, `#AI Governance`, `#National Security`

---

<a id="item-4"></a>
## [大脑由两个不同的器官构成 原始部分负责生理功能 另一部分负责独特思考推理能力](https://www.solidot.org/story?sid=85426) ⭐️ 8.0/10

Stanford researchers identify two distinct brain progenitor cell populations, suggesting the brain develops as two separately evolved organs rather than a single organ.

telegram · zaihuapd · Sep 20, 12:11

**Tags**: `#neuroscience`, `#brain development`, `#evolution`, `#Otx2/Gbx2`, `#Nature`

---