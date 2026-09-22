---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22
lang: en
---

> From 37 items, 5 important content pieces were selected

---

1. [Xiaomi Releases MiMo-V2.6 Open LLM Series in Flash and Pro Variants](#item-1) ⭐️ 8.0/10
2. [Bryan Cantrill's Post-Mortem of Sun Microsystems' Failures](#item-2) ⭐️ 8.0/10
3. [xAI Releases Grok 4.7 With 40% More Parameters at Same Price](#item-3) ⭐️ 8.0/10
4. [Cloudflare makes Python Workers generally available](#item-4) ⭐️ 8.0/10
5. [SemiAnalysis Deep-Dive: Mapping MoE Models onto Inference Hardware](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Xiaomi Releases MiMo-V2.6 Open LLM Series in Flash and Pro Variants](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

Xiaomi released the MiMo-V2.6 series, an open-weight LLM family offered in Flash and Pro variants, publishing the RL-tuned checkpoints on Hugging Face as XiaomiMiMo/MiMo-V2.6-Flash-RL and XiaomiMiMo/MiMo-V2.6-Pro-RL alongside a detailed technical report. The company also shared a live RL training dashboard, which it kept public while the model was being trained. The release positions Xiaomi among the labs shipping frontier-class open-weight models, and its unusually granular disclosure of training methodology and live RL progress raises expectations for how transparently other vendors report their training. For developers and researchers, it adds two more capable, freely downloadable options they can self-host or fine-tune instead of relying solely on closed APIs. The Flash variant has 309B total parameters with 15B activated, while Pro scales to 1.02T total with 42B activated, indicating sparse mixture-of-experts architectures; the Flash build also includes a 6-layer audio patch encoder and a 5-layer sliding-window-attention MTP drafter for speculative decoding, and Xiaomi provides an SGLang deployment cookbook. Note that despite the transparency, these are open-weight rather than fully open models, since training data and training code were not released in full.

hackernews · volf_ · Sep 21, 20:12 · [Discussion](https://news.ycombinator.com/item?id=49792730)

**Background**: Open-weight LLMs are models whose trained parameters are publicly downloadable, so anyone can run, modify, or fine-tune them, unlike closed models such as those served only behind an API. Large models like MiMo-V2.6 typically use a mixture-of-experts (MoE) design, where only a small subset of parameters is activated per token, which keeps inference cost far below what the total parameter count would suggest. Reinforcement learning (RL) post-training is the stage where a base model is refined against reward signals to improve reasoning, instruction following, and tool use, and it is precisely this stage that Xiaomi exposed through its public dashboard.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">Introducing MiMo-V2.6 series</a></li>
<li><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL">XiaomiMiMo/MiMo-V2.6-Flash-RL · Hugging Face</a></li>
<li><a href="https://www.linkedin.com/pulse/open-weights-llms-in-depth-analysis-adoption-usage-performance-jha-kymhc">Open - Weights LLMs: In-Depth Analysis of Adoption, Usage, and...</a></li>

</ul>
</details>

**Discussion**: Commenters on Hacker News were broadly positive, with one praising the realtime RL dashboard as an exceptional learning tool and the technical report as unusually comprehensive, even while noting that “open” remains contested. Others compared Chinese and American models mainly on affordability, shared empirical tests such as the SVG pelican prompt for both variants, and cited exact parameter counts; one thread argued China may ultimately win the AI race because of its electricity and grid buildout advantage.

**Tags**: `#AI/ML`, `#LLM`, `#open weights`, `#Xiaomi`, `#model release`

---

<a id="item-2"></a>
## [Bryan Cantrill's Post-Mortem of Sun Microsystems' Failures](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 8.0/10

Bryan Cantrill, a former Sun Microsystems engineer best known as the creator of DTrace, published a detailed retrospective titled "What Sun got wrong" that dissects the strategic and technical missteps that led to the company's decline. The post sparked a large Hacker News discussion (484 points, 270 comments) in which former customers and employees added firsthand context about Sun's sales culture, product decisions, and eventual acquisition by Oracle. Sun's collapse remains one of the most instructive case studies in the tech industry, showing how a company that produced genuinely superior engineering — SPARC servers, Solaris, Java, NFS, ZFS and DTrace — can still lose to cheaper, more customer-friendly competitors. The discussion resonates today because commentators explicitly draw parallels between Sun's inflated valuation during the dot-com bubble and current high-multiple AI and hardware stocks. Commenters highlight two specific blunders as especially damaging: Sun's brief cancellation of Solaris on x86 in 2002, which alienated customers who did not want to be locked into SPARC hardware, and its failure to strike a deal with Google in 2002 after Sun demanded to know how many servers Google operated — a detail Google considered a closely guarded secret. Others note that Sun's thin clients and tools like Pine and vi were beloved by university users despite slow startup times.

hackernews · chmaynard · Sep 21, 14:03 · [Discussion](https://news.ycombinator.com/item?id=49787436)

**Background**: Sun Microsystems was an American computer company founded in 1982 that built high-performance SPARC-based workstations and servers running its proprietary Solaris operating system, and it also created Java, NFS, ZFS and DTrace. At its peak during the late 1990s dot-com boom it was one of the most valuable technology firms in the world, but it struggled through the 2000s and was acquired by Oracle in 2010. Bryan Cantrill worked at Sun for over a decade and later co-founded Oxide Computer, giving his retrospective unusual insider credibility.

**Discussion**: The discussion mixes nostalgia with hard business critique: one commenter recalls that buying from Sun or DEC in the late 1990s meant forced sales meetings and endless quote revisions, to the point that rails and power cords for an Alpha server cost more than a complete Dell server delivered next day. Another argues that Sun was never really interested in running a business and simply tolerated sales to fund building great technology, while a third notes he sold his Sun stock at $70 during the bubble only to see it fall to $7 — a cautionary tale he applies to today's AI stocks.

**Tags**: `#Sun Microsystems`, `#tech history`, `#systems`, `#business strategy`, `#Hacker News`

---

<a id="item-3"></a>
## [xAI Releases Grok 4.7 With 40% More Parameters at Same Price](https://x.ai/news/grok-4-7) ⭐️ 8.0/10

xAI announced Grok 4.7, a frontier model that carries roughly 40% more weights/parameters than Grok 4.6 while keeping API pricing unchanged at $2 per million input tokens and $6 per million output tokens. The release landed almost two weeks later than its originally planned date. Because the model is substantially larger but costs the same per token, xAI appears to be competing on capability-per-dollar rather than on price cuts, which likely squeezes its own margins and raises the bar for rivals. Developers choosing models for coding and agentic workflows are directly affected, since they now weigh Grok 4.7 against Anthropic's Opus line and other frontier options. Community testers report that Grok 4.7 feels noticeably slower and burns more tokens than its predecessor, and one developer (Simon Willison) observed that the low and medium reasoning-effort settings consumed similar token counts while xhigh used fewer tokens than high. He noted he still needs to retry the tests without OpenRouter in the middle to confirm the numbers against the xAI API directly.

hackernews · meetpateltech · Sep 21, 15:50 · [Discussion](https://news.ycombinator.com/item?id=49788838)

**Background**: Grok is the family of large language models from xAI, the American AI company founded by Elon Musk in 2023 and known for its Grok chatbot integrated with X. Grok 4.6 was reported to be a pre-trained model built on a 1.5-trillion-parameter V9 foundation and to incorporate data from the AI coding platform Cursor, which xAI has since acquired. "Parameters" (or weights) are the variables a model learns during training; more of them generally means more capacity, but also higher training and inference cost. Frontier labs now release models on a rapid cadence, and community skepticism about benchmark scores has grown alongside that pace.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/XAI_(company)">XAI (company)</a></li>
<li><a href="https://www.ibm.com/think/topics/model-parameters">What are Model Parameters? | IBM</a></li>

</ul>
</details>

**Discussion**: Sentiment is mixed and largely skeptical: several commenters note that a 40% larger model at the same price means thinner margins and a delayed launch, and they suspect Grok 4.7 was rushed out just before a rumored Opus 5.5 release, with one saying Grok 4.6 "didn't really hack it" for coding and agentic use cases. Others are more positive, welcoming the faster release cadence and predicting a bigger jump with Grok 5 as the team gains experience with large training runs, while one developer shared hands-on token-usage measurements across reasoning-effort levels.

**Tags**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#Model Release`

---

<a id="item-4"></a>
## [Cloudflare makes Python Workers generally available](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

Cloudflare has moved Python Workers from beta to general availability, letting developers write and deploy Python directly on its serverless edge runtime. The release highlights improved package support and upstream WebAssembly contributions that make common Python HTTP clients work inside the Wasm-based runtime. Python is one of the most widely used languages for scripting, data work and backend services, so first-class support on an edge platform removes a major barrier for teams that would otherwise need JavaScript or Rust to deploy at the edge. It also signals growing momentum behind running Python on WebAssembly, which affects how serverless platforms and Python library maintainers think about portability. The GA release leans on Pyodide and the Emscripten toolchain, plus JSPI support in urllib3 that lets HTTP clients route requests through the JavaScript fetch API inside WebAssembly environments. Package standardization is being formalized through PEP 783 (PyEmscripten), though questions about cold-start latency for Wasm-based Workers remain open.

hackernews · torutofu · Sep 21, 13:38 · [Discussion](https://news.ycombinator.com/item?id=49787142)

**Background**: Cloudflare Workers is a serverless platform that runs code across Cloudflare's global edge network instead of a single centralized server, so applications execute close to users. Python Workers executes Python by compiling it to WebAssembly, a portable binary instruction format that runs in a stack-based virtual machine and is designed to bring high-performance code to both web and non-web environments. Because WebAssembly does not natively include Python's C-extension or networking layers, projects like Pyodide and Emscripten are needed to bridge Python packages into that sandboxed runtime.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/">Overview · Cloudflare Workers docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://grokipedia.com/page/Cloudflare_Workers">Cloudflare Workers</a></li>

</ul>
</details>

**Discussion**: Commenters broadly welcomed the milestone: an urllib3 maintainer clarified that Pyodide/Emscripten and JSPI support in urllib3 came from large external contributions, while Wasmer's founder praised Cloudflare's progress on package support and PEP 783 despite competing products. Remaining concerns centered on architectural tradeoffs and cold-start/spin-up latency for Wasm-based Workers, alongside lighthearted jokes about the headline's wording.

**Tags**: `#Cloudflare Workers`, `#Python`, `#WebAssembly`, `#Serverless`, `#Edge Computing`

---

<a id="item-5"></a>
## [SemiAnalysis Deep-Dive: Mapping MoE Models onto Inference Hardware](https://newsletter.semianalysis.com/p/computation-and-data-movement-for) ⭐️ 8.0/10

SemiAnalysis published a technical deep-dive titled "Computation and Data Movement for Inference" that examines how Mixture-of-Experts (MoE) models are mapped onto inference hardware, covering model structure, data flow, and efficient serving strategies. Rather than announcing a new product or benchmark, the piece lays out the systems-level trade-offs that determine how MoE inference actually runs in production. MoE has become the dominant architecture for frontier models because it decouples total parameter count from per-token compute, but that benefit only materializes if the hardware can feed the right experts fast enough. As more labs and enterprises serve MoE models such as Mixtral and larger frontier systems, understanding the compute-versus-data-movement balance directly affects serving cost, latency, and hardware purchasing decisions. The analysis focuses on how expert routing and the resulting all-to-all communication reshape the memory-bandwidth and interconnect requirements of inference, since only a small subset of experts is activated per token while the full weight set must still reside in memory. This makes MoE serving fundamentally memory-capacity and memory-bandwidth bound rather than purely compute bound, a nuance that simpler parameter-count comparisons tend to miss.

rss · Semianalysis · Sep 21, 18:14

**Background**: Mixture-of-Experts models split their weights into many separate "expert" sub-networks and use a router to select only a few experts per token, giving the knowledge capacity of a large model at roughly the compute cost of a much smaller one. The catch is memory: all experts must be stored and, depending on batch size and routing, moved through the system, which is why data movement rather than raw FLOPs often dominates inference time. Prior work such as the paper "Data Movement Is All You Need" made the same point for Transformers more broadly, showing that optimizing memory movement yields large speedups.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2007.00072">DATA MOVEMENT IS ALL YOU NEED: A CASE STUDY ON OPTIMIZING TRANSFORMERS</a></li>
<li><a href="https://localmodel.run/guides/mixture-of-experts">Mixture of experts (MoE) explained for local LLMs · localmodel.run</a></li>
<li><a href="https://medium.com/@kittikawin_ball/you-dont-need-a-phd-to-understand-mixture-of-experts-here-s-the-intuition-in-plain-english-8972d6e7ad51">You Don’t Need a PhD to Understand Mixture of Experts ... | Medium</a></li>

</ul>
</details>

**Tags**: `#MoE`, `#inference`, `#hardware`, `#systems`, `#data movement`

---