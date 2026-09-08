---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 37 items, 9 important content pieces were selected

---

1. [OpenAI Claims Proof Solving Navier-Stokes Millennium Problem, Awaiting Verification](#item-1) ⭐️ 10.0/10
2. [Buckmaster statement accuses OpenAI of appropriating Navier-Stokes work](#item-2) ⭐️ 8.0/10
3. [Qwen3.8 27B Quantization Benchmarked: 4-Bit Holds, 1-Bit Collapses](#item-3) ⭐️ 8.0/10
4. [OpenAI Launches ChatGPT Images 2.5 with Two New API Models](#item-4) ⭐️ 8.0/10
5. [NeurIPS Desk-Rejects 178 Papers Using Flawed AI Detector, Sparking Outcry](#item-5) ⭐️ 8.0/10
6. [Malaysia Eyes Huawei Ascend 910C Chips for Sovereign AI Project](#item-6) ⭐️ 8.0/10
7. [ByteDance Founder Leads Real-Time Spatial Video Model Effort](#item-7) ⭐️ 8.0/10
8. [ASML and TSMC Partner to Move High NA EUV to 12-Inch Photomasks](#item-8) ⭐️ 8.0/10
9. [China Plans Fourfold Increase in AI Computing Power to 9800 EFLOPS by 2030](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Claims Proof Solving Navier-Stokes Millennium Problem, Awaiting Verification](https://www.reddit.com/r/MachineLearning/comments/1wavdi7/openal_says_it_has_cracked_one_of_maths/) ⭐️ 10.0/10

On September 8, 2026, OpenAI announced that an unreleased internal model had produced a proof that a smooth, finite-energy three-dimensional incompressible flow can develop a singularity in finite time, with a formalization in the Lean proof assistant. The company says this establishes statements C and D of Fefferman's official formulation of the Navier-Stokes existence and smoothness problem. If verified, this would be the first solution to a second Millennium Prize Problem and a major breakthrough for mathematics, physics, and fluid dynamics. It could profoundly change the understanding of turbulence and demonstrate that AI can contribute to frontier mathematical research, though independent validation is still required. The claimed proof was not independently verified by the mathematical community or assessed by the Clay Mathematics Institute as of September 2026, and OpenAI reportedly said it would decline the Millennium Prize if offered. The announcement was accompanied by a priority dispute with mathematicians working on closely related blow-up results for the Euler equations, and the method builds on work by Diego Córdoba and Luis Martínez Zoroa from 2023.

reddit · r/MachineLearning · /u/Shizuka_Kuze · Sep 8, 17:42

**Background**: The Navier-Stokes equations are partial differential equations that describe the motion of fluids, and their solutions are widely used in science and engineering. In 2000, the Clay Mathematics Institute listed the Navier-Stokes existence and smoothness problem as one of its seven Millennium Prize Problems, each offering a US$1,000,000 prize for a correct solution. The problem asks mathematicians to either prove that smooth global solutions always exist for the three-dimensional equations or provide a counterexample; by claiming a finite-time singularity, OpenAI is presenting a counterexample. As of 2026, the only Millennium Prize problem officially solved is the Poincaré conjecture.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Navier-Stokes`, `#mathematics`, `#AI research`, `#Millennium Problem`

---

<a id="item-2"></a>
## [Buckmaster statement accuses OpenAI of appropriating Navier-Stokes work](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 8.0/10

Tristan Buckmaster published a public statement (PDF) alleging that OpenAI used his and Levent Alpöge's unpublished mathematical work — including a near-miss Navier–Stokes singularity result — without permission or attribution in a September 2026 announcement of an AI-discovered proof. The statement describes offers, threats, and an attempted priority grab around the Millennium-Prize-adjacent result. The dispute pits academic norms of open, credited research against a major AI lab's closed development practices. If the allegations hold, it would be a serious research-ethics breach with chilling effects on mathematicians who share draft work or use AI tools. Buckmaster and Alpöge say they proved finite-time blowup for smooth-forced equations such as 3D incompressible Euler, porous media, and Boussinesq, but not the full Clay Millennium Navier–Stokes problem. OpenAI acknowledged in a comment that it 'cannot rule out' that de-identified user data helped improve its models.

hackernews · procedurecall · Sep 8, 05:42 · [Discussion](https://news.ycombinator.com/item?id=49605915)

**Background**: The Navier–Stokes equations describe the motion of viscous fluids; whether smooth global solutions always exist in 3D is one of the Clay Mathematics Institute's Millennium Prize problems, worth $1 million. OpenAI's September 2026 announcement claimed an internal model produced a formalized proof that finite-time singularity can occur for a smooth-forced incompressible flow, establishing statements 'C' and 'D' of Fefferman's formulation, but the claim has not been independently verified. Buckmaster and Alpöge's related work is not the full Millennium solution, but could be a stepping stone.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_equations">Navier-Stokes equations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>

</ul>
</details>

**Discussion**: Commenters are sharply critical of OpenAI, accusing it of looking at user data, stealing world-class researchers' work, and threatening them to protect corporate profits. Others note that, unless OpenAI actually used the mathematicians' data, the episode could be ordinary academic priority sniping amplified by AI; but OpenAI's own ambiguity about data use leaves the question open.

**Tags**: `#Navier-Stokes`, `#OpenAI`, `#academic integrity`, `#research ethics`, `#mathematics`

---

<a id="item-3"></a>
## [Qwen3.8 27B Quantization Benchmarked: 4-Bit Holds, 1-Bit Collapses](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) ⭐️ 8.0/10

A Quesma benchmark testing quantized versions of Qwen3.8-27B reports that 4-bit quantization preserves quality, while 2-bit scores lower and 1-bit collapses. The results suggest the practical quality threshold sits at 4 bits for this model. This gives developers practical guidance on how aggressively they can compress Qwen3.8-27B for local inference, where lower bit widths reduce VRAM cost and memory bandwidth. The finding that 4-bit is safe is especially useful for running the 27B model on 24GB graphics cards. The benchmark uses Wilson 95% confidence intervals for run-to-run noise; within those intervals, quality holds steady down to 4-bit, while 2-bit scores noticeably lower. A 1-bit quantization causes catastrophic quality loss. The post does not directly cover KV-cache quantization, which commenters note matters for long-context use.

hackernews · stared · Sep 8, 14:49 · [Discussion](https://news.ycombinator.com/item?id=49611128)

**Background**: Quantization compresses an LLM by representing weights in lower-precision numbers, trading some output quality for dramatically smaller memory footprint and faster inference. Qwen3.8-27B is an open-weight Alibaba model with about 27.78B parameters, licensed under Apache 2.0, and small enough to run locally at 4-bit on 24GB VRAM. Benchmarks like this help users choose quantization levels for local deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.techpillow.co/blog/qwen3-8-27b-alibaba-open-weight-multimodal-model">Qwen 3 .8- 27 B Open-Weight AI Model Benchmarks | TechPillow Blog</a></li>

</ul>
</details>

**Discussion**: Commenters push back on the confidence intervals: one notes Wilson intervals say little about run-to-run noise, while another suggests Qwen3.8-27B compensates for quantization by 'thinking more' at higher thinking levels. Others request KV-cache quantization benchmarks and point out the missing Q3 point matters for sub-16GB cards.

**Tags**: `#quantization`, `#LLM`, `#benchmarking`, `#Qwen`, `#machine learning`

---

<a id="item-4"></a>
## [OpenAI Launches ChatGPT Images 2.5 with Two New API Models](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 8.0/10

On September 8, 2026, OpenAI introduced ChatGPT Images 2.5, which improves multi-turn instruction following, speeds up responses, and better preserves the subjects in reference photos. The release adds two new API model IDs — gpt-image-2.5-sunburst for precision editing and gpt-image-2.5-flare for fast everyday generation. This release matters because it gives developers two specialized image-generation models with different trade-offs between precision and speed, signaling OpenAI's move toward workload-specific APIs. With over 3 billion images generated across ChatGPT Images and the GPT-Image API models, even incremental improvements in instruction following and subject preservation have a large impact on creative and developer tools. OpenAI's documentation says Sunburst is for workflows where editing precision matters most, while Flare is for fast, high-quality everyday generation. The models accept both text and image inputs, and Simon Willison has updated his openai_image.py CLI tool to support passing one or more reference images.

rss · Simon Willison · Sep 8, 22:46

**Background**: ChatGPT Images is OpenAI's image-generation product built on the GPT-Image models available through the API, which have now produced over 3 billion images. Instead of a single flagship model, the 2.5 generation splits into two sibling models — Sunburst and Flare — designed for different workloads. A key area of improvement is multi-turn instruction following, which matters for iterative editing where users upload reference images and refine output through successive prompts.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-5/">Introducing ChatGPT Images 2 . 5 | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-image-2.5-flare">GPT - Image - 2 . 5 Flare Model | OpenAI API</a></li>
<li><a href="https://www.orcarouter.ai/blog/gpt-image-2-5-flare-sunburst">GPT - Image - 2 . 5 Flare vs Sunburst: New OpenAI Image APIs</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#image generation`, `#ChatGPT`, `#API`, `#AI models`

---

<a id="item-5"></a>
## [NeurIPS Desk-Rejects 178 Papers Using Flawed AI Detector, Sparking Outcry](https://www.reddit.com/r/MachineLearning/comments/1wakf62/neurips_deskrejected_178_papers_for_being/) ⭐️ 8.0/10

NeurIPS's Position Paper Track desk-rejected 178 papers (18.4% of submissions) using the proprietary AI detector Pangram, with no human review or appeal process. Tests showed the detector flagged the track chairs' own recent papers at 24–69% confidence, implying they would have been at risk under the same rules. This controversy highlights the dangers of using black-box AI detectors for high-stakes academic decisions, which could unfairly penalize non-native English speakers and erode trust in peer review. It also raises urgent questions about procedural fairness, algorithmic bias, and the accountability of major conferences like NeurIPS. According to the post, Pangram's default settings initially flagged 42.7% of the entire track as 90–100% AI, and the organizers had to shrink detection text windows to reduce the flag rate to 12.7%. Moreover, 22 of the rejected papers were rejected because they scored above 0.5 while the authors denied AI use, and a Stanford study cited shows 61.22% of human-written TOEFL essays are false positives.

reddit · r/MachineLearning · /u/tughanbulut · Sep 8, 10:19

**Background**: Desk rejection is an administrative screening step in academic publishing where papers are rejected before peer review, usually for violating scope or submission rules. Pangram is an AI-detection tool developed by Pangram Labs to identify text generated by large language models; it has been criticized for contributing to 'witch hunts' against AI writing. NeurIPS (Conference on Neural Information Processing Systems) is one of the most prestigious machine-learning conferences, and its 2026 Position Paper Track introduced automated AI screening, triggering debate in the community. The post's author also discloses that they built StrictCite, a deterministic zero-AI citation checker, which may color their perspective.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pangram_(AI_detector)">Pangram (AI detector)</a></li>
<li><a href="https://www.pangram.com/">AI Detector : Free AI Checker for ChatGPT, Claude & Gemini | Pangram</a></li>

</ul>
</details>

**Tags**: `#NeurIPS`, `#AI detection`, `#ethics`, `#academic publishing`, `#algorithmic bias`

---

<a id="item-6"></a>
## [Malaysia Eyes Huawei Ascend 910C Chips for Sovereign AI Project](https://www.businesstimes.com.sg/international/malaysia-eyes-huawei-chips-ai-project-despite-us-warning) ⭐️ 8.0/10

Malaysia is reportedly evaluating Huawei's Ascend 910C chips for its sovereign AI project, a 2 billion ringgit ($494 million) initiative. If finalized, it would make Malaysia the first government to formally choose a Chinese AI accelerator over US products. This decision could reshape AI hardware supply chains and geopolitical tech alliances, as it defies US export warnings. It signals growing acceptance of Chinese AI chips in international markets, potentially affecting US export control policies. The exact number of chips to be purchased remains unclear. The US Trump administration had warned that using Huawei's AI accelerator chips might violate US export regulations, but Malaysia views the decision as purely commercial.

telegram · zaihuapd · Sep 8, 03:35

**Background**: The Huawei Ascend 910C is a high-performance AI accelerator chip developed by Huawei, part of China's effort to build domestic AI computing capacity amid US export controls. Sovereign AI refers to a country's ability to develop, deploy, and govern AI using its own infrastructure, data, and models, ensuring compliance with local laws and strategic interests. Malaysia's consideration of Huawei chips reflects a broader trend of nations seeking AI self-reliance, even as the US tries to limit China's influence in advanced technology.

<details><summary>References</summary>
<ul>
<li><a href="https://www.redhat.com/en/topics/ai/sovereign-ai">What is sovereign AI?</a></li>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#AI chips`, `#Malaysia`, `#geopolitics`, `#sovereign AI`

---

<a id="item-7"></a>
## [ByteDance Founder Leads Real-Time Spatial Video Model Effort](https://www.bloomberg.com/news/articles/2026-09-07/bytedance-founder-joins-ai-elite-in-race-to-perfect-world-models) ⭐️ 8.0/10

ByteDance founder Zhang Yiming is personally overseeing development of a real-time spatial video generation model, with release expected as early as October 2026. The model, based on Seedance, generates interactive virtual worlds for Pico headsets that respond to voice or gestures. This signals ByteDance's push to combine generative AI with spatial computing, potentially lowering VR hardware requirements via cloud offloading. If successful, it could accelerate consumer adoption of VR by enabling real-time conversational world generation. The model reportedly generates video at around 20 frames per second with roughly 0.05 seconds latency, offloading high-intensity computation to the cloud. The launch timeline remains subject to change despite the October 2026 target.

telegram · zaihuapd · Sep 8, 04:05

**Background**: ByteDance's Seedance is an AI video generation model family built on Doubao multimodal technology, supporting text-to-video, image-to-video, and reference-guided creation. Spatial video generation extends conventional AI video by maintaining object coherence across camera perspectives, which is essential for immersive VR experiences like those on Pico headsets. ByteDance founder Zhang Yiming has returned to direct involvement in high-stakes AI projects as competition with rivals like OpenAI and Meta intensifies.

<details><summary>References</summary>
<ul>
<li><a href="https://seeddance.ai/seedance-2-5">Seedance 2.5 — 30s One-Take AI Video with Multimodal... | SeedDance</a></li>
<li><a href="https://www.seedancepro.net/seedance">Seedance AI Video Models</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Video Generation`, `#VR`, `#ByteDance`, `#Spatial Computing`

---

<a id="item-8"></a>
## [ASML and TSMC Partner to Move High NA EUV to 12-Inch Photomasks](https://www.nrc.nl/nieuws/2026/09/08/asml-gaat-samenwerken-met-taiwanese-chipgigant-tsmc-om-zijn-nieuwste-chipmachines-te-upgraden-a4936073) ⭐️ 8.0/10

ASML and TSMC announced an industry partnership on September 7 to move High NA EUV lithography from 6-inch photomasks to 12-inch photomasks. They plan a 12-inch mask pilot line by 2031 and use of the systems in advanced-node mass production by 2033, with TSMC expecting to deploy High NA EUV for advanced-node high-volume manufacturing from 2030. Larger photomasks could improve productivity, lower chipmaking costs, and reduce the stitching constraints that limit very large advanced-node dies. The partnership also positions TSMC as a key shaper of ASML's High NA EUV roadmap, affecting the broader leading-edge semiconductor ecosystem. Current High NA EUV systems use 6-inch masks, whose limited field size can force stitching for large dies or reduce productivity. The 2031 pilot line and 2033 volume-manufacturing targets are still planning-stage goals, and the shift will require changes across mask making, pellicles, and wafer-stage design.

telegram · zaihuapd · Sep 8, 06:55

**Background**: High NA EUV is a next-generation extreme ultraviolet lithography method that uses a numerical aperture of 0.55 to print finer features than earlier EUV tools. A higher numerical aperture also shrinks the printable field, which is why the industry is exploring larger photomask formats and stitching approaches. Photomasks are templates that transfer circuit patterns onto silicon wafers, so moving to a 12-inch format affects the entire mask-making infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/极紫外光刻">极紫外光刻 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#EUV`, `#光刻`, `#ASML`, `#台积电`

---

<a id="item-9"></a>
## [China Plans Fourfold Increase in AI Computing Power to 9800 EFLOPS by 2030](https://www.scmp.com/tech/policy/article/3366733/china-targets-fourfold-boost-ai-computing-capacity-2030-major-tech-push) ⭐️ 8.0/10

China's Ministry of Industry and Information Technology has issued a new five-year plan targeting intelligent computing capacity of 9800 EFLOPS by 2030, roughly four times the current level. The plan also calls for 3.8 trillion yuan in cumulative IT infrastructure investment between 2026 and 2030. This is a major government push to expand AI infrastructure and could reshape national AI competition, as China seeks to reduce reliance on imported chips. The plan demonstrates how governments are treating computing power as strategic infrastructure for AI development. As of late June, China's intelligent computing capacity was 2185 EFLOPS, up 177% year on year, so the 2030 target would require a more than fourfold increase from that baseline. The plan also calls for 'orderly deployment' of GPU clusters with 10,000 or more accelerators, including clusters exceeding 100,000, and better adaptation between domestic chips and infrastructure.

telegram · zaihuapd · Sep 8, 11:23

**Background**: EFLOPS (exaflops) is a measure of computing performance equal to one quintillion (10^18) floating-point operations per second, commonly used to size supercomputers and national compute fleets. 'Intelligent computing' refers to computing resources oriented toward artificial intelligence workloads such as model training and inference. Amid export controls on advanced GPUs, Chinese companies such as Huawei and Cambricon have become major suppliers of domestic AI accelerators, and the government has encouraged adoption of these chips.

<details><summary>References</summary>
<ul>
<li><a href="https://theworldofai.org/ai-glossary/eflops/">What is EFLOPS ( exaFLOPS )? — AI Glossary</a></li>
<li><a href="https://biztechmagazine.com/article/2023/08/what-flops-and-how-does-it-help-supercomputer-performance-perfcon">What Is FLOPS (Floating Point Performance)... | BizTech Magazine</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd">China's homegrown AI accelerators to supply 90% of the country's domestic market, analysts suggest — Cambricon and Huawei expected to be the biggest winners in the shift away from Nvidia and AMD | Tom's Hardware</a></li>

</ul>
</details>

**Tags**: `#China`, `#AI infrastructure`, `#policy`, `#computing capacity`, `#EFLOPS`

---