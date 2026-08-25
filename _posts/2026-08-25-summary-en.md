---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 39 items, 12 important content pieces were selected

---

1. [Apple unveils M6 and M5 Ultra chips for a big AI compute leap](#item-1) ⭐️ 9.0/10
2. [OpenAI's Custom Jalapeño Chip Beats Nvidia Blackwell in Tests](#item-2) ⭐️ 9.0/10
3. [NVIDIA First Tests Vera Rubin NVL72, DeepSeek Throughput Soars 30x](#item-3) ⭐️ 9.0/10
4. [FDA Authorizes First Wearable for Continuous Ketone and Glucose Monitoring](#item-4) ⭐️ 8.0/10
5. [Apple Unveils Mac Studio with M5 Max and M5 Ultra for Local AI](#item-5) ⭐️ 8.0/10
6. [Nitter Receives Cease and Desist, Instances Shut Down](#item-6) ⭐️ 8.0/10
7. [Firefox 157 Enables JPEG XL by Default on All Platforms](#item-7) ⭐️ 8.0/10
8. [SpaceX Officially Announces Starbase LA Launch Site in Louisiana](#item-8) ⭐️ 8.0/10
9. [Continual Learning Can Democratize Frontier AI, Says SovereignAI Report](#item-9) ⭐️ 8.0/10
10. [Qwen Previews Qwen3.8-Flash-Next, Open-Source Model on Next-Gen Qwen4 Architecture](#item-10) ⭐️ 8.0/10
11. [GPT-5.6 Sol Designs Custom CPU in Turing Complete, Runs Doom](#item-11) ⭐️ 8.0/10
12. [Anthropic to Tell Investors of $30 Trillion Potential Revenue, Tops SpaceX](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Apple unveils M6 and M5 Ultra chips for a big AI compute leap](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 9.0/10

Apple announced the M6 and M5 Ultra chips on August 25, 2026. The M6 is Apple's first 2nm chip with a 12-core CPU, 12-core GPU, and dual 16-core Neural Engine, while the M5 Ultra is Apple's first quad-die chip and its most powerful chip ever. This is a major milestone for Apple silicon, delivering a substantial leap in performance and AI compute for Macs. It will likely intensify competition in the PC and workstation market and could reshape how pro and AI-heavy workloads are handled on Apple devices. The M5 Ultra fuses two dual-die M5 Max chips using next-generation UltraFusion technology to form a quad-die architecture, aimed at heavy AI workloads. The M6, built on a 2nm process, is designed to deliver a revolutionary leap in everyday performance and power efficiency.

hackernews · interpol_p · Aug 25, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49433292)

**Background**: Apple began transitioning Macs from Intel to its own Apple silicon with the M1 chip in 2020. M-series chips integrate CPU, GPU, neural processing unit, and unified memory on a single package, with UltraFusion technology used to combine smaller dies into larger, more powerful chips. The M6 and M5 Ultra represent the latest evolution of this strategy, pushing performance and AI compute to new levels.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M6 and M5 Ultra for a big leap in performance and AI compute - Apple</a></li>
<li><a href="https://techcrunch.com/2026/08/25/apple-debuts-its-most-powerful-chip-ever-in-m5-ultra-and-m6/">Apple debuts its 'most powerful chip ever' in M5 Ultra and M6 | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_m1_chip">Apple m1 chip</a></li>

</ul>
</details>

**Discussion**: Commenters were generally impressed with the performance gains, with one user noting a tangible difference when testing the M5 Pro in an Apple Store and another comparing the competitive dynamic to the late 1990s. However, several expressed concerns about pricing, with one calculating that a fully maxed-out Apple Studio could reach nearly $25,000, and others discussing a Bloomberg rumor that Apple may skip M6 Pro, Max, and Ultra variants to focus on an AI-capable M7 chip.

**Tags**: `#apple-silicon`, `#hardware`, `#ai-compute`, `#mac`

---

<a id="item-2"></a>
## [OpenAI's Custom Jalapeño Chip Beats Nvidia Blackwell in Tests](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

OpenAI published first benchmark results for Jalapeño, its self-designed inference ASIC co-developed with Broadcom. On the InferenceX suite, it performed 1.5x–1.9x more AI work per kilowatt at peak throughput, showed 1.7x–3.6x lower end-to-end latency, and delivered 2.1x–4.1x higher performance in high-interaction scenarios than Nvidia's GB200/GB300 Blackwell systems across GPT-OSS 120B, DeepSeek R1 670B, and Kimi K2.5 1T models. This is a direct challenge to Nvidia's dominance in AI hardware: a hyperscaler's custom ASIC outperforming Nvidia's best shipping inference chips on throughput-per-watt and latency. It also threatens Nvidia's CUDA software moat and could push AI chip competition toward price/performance, affecting every hyperscaler and AI startup's procurement decisions. Jalapeño is rated at 700W but sustained no more than 550W in real-world tests. The comparison used Nvidia's GB300/GB200 rather than the just-starting-to-ship Vera Rubin, and the chip is not intended for training; OpenAI plans to deploy it in its own data centers by the end of 2026, with a second generation in deep development and a third in design.

hackernews · Semianalysis · Aug 25, 14:06 · [Discussion](https://news.ycombinator.com/item?id=49434378)

**Background**: An ASIC (application-specific integrated circuit) is a chip customized for particular tasks rather than general-purpose use, offering better speed, power efficiency, and silicon utilization. Nvidia's Blackwell is the GPU architecture powering Nvidia's latest GB200/GB300 AI accelerators. Throughput per MW — AI work such as generated tokens divided by power consumption — is the key efficiency metric in AI data centers, where power is the ultimate constraint. OpenAI's move reflects a trend among large AI labs to design custom inference silicon for cost savings and independence from Nvidia.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/openais-first-gen-jalapeno-asic-blows-competition-out-of-the-park-performs-1-5x-to-1-9x-more-work-per-kilowatt-than-nvidias-blackwell-chips-while-threatening-the-cuda-moat/">OpenAI's First-Gen Jalapeno ASIC Blows Competition Out Of The Park, Performs 1.5x to 1.9x More Work Per Kilowatt Than NVIDIA's Blackwell Chips, While Threatening The CUDA Moat</a></li>
<li><a href="https://en.wikipedia.org/wiki/Application-specific_integrated_circuit">Application-specific integrated circuit - Wikipedia</a></li>
<li><a href="https://developer.nvidia.com/blog/scaling-token-factory-revenue-and-ai-efficiency-by-maximizing-performance-per-watt/">Scaling Token Factory Revenue and AI Efficiency by Maximizing Performance per Watt | NVIDIA Technical Blog</a></li>

</ul>
</details>

**Discussion**: Commenters framed the news as a negotiating lever to extract better pricing from Nvidia and as a sign of a maturing inference-chip market, with parallels drawn to the early 3D GPU wars (3dfx, Riva, PowerVR). Others speculated about baking model weights directly into future chips and noted that human brains are still ~22x more energy-efficient than current AI inference.

**Tags**: `#AI hardware`, `#OpenAI`, `#semiconductors`, `#Nvidia`, `#ASIC`

---

<a id="item-3"></a>
## [NVIDIA First Tests Vera Rubin NVL72, DeepSeek Throughput Soars 30x](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/) ⭐️ 9.0/10

NVIDIA published the first on-chip benchmarks for its next-generation Vera Rubin NVL72 rack-scale system, showing up to 30x higher per-megawatt throughput and up to 35x lower cost per million tokens on DeepSeek-V4-Pro agentic coding tasks compared with GB300. The company also announced the Groq 3 LPX inference accelerator and the Vera CPU, with SpaceXAI revealing plans to deploy the Vera CPU. This is a major hardware milestone that could reshape AI infrastructure economics, making large-scale reasoning and agentic workloads dramatically cheaper and more energy-efficient. It underscores NVIDIA's push toward rack-scale co-design for agentic AI and intensifies competitive pressure on AMD and custom silicon vendors. Vera Rubin NVL72 integrates 72 Rubin GPUs and 36 Vera CPUs in a single rack-scale system built for agentic reasoning. The Groq 3 LPX, entering full production, runs Gemma 4 31B at 3,400 output tokens per second, the fastest recorded for that model, and a full rack can harness up to 256 LP30 accelerators. The Vera CPU is purpose-built for agentic AI work such as code execution, tool use, and sandboxing, delivering twice the efficiency and 50% higher speed than traditional rack-scale CPUs.

telegram · zaihuapd · Aug 25, 14:48

**Background**: Vera Rubin NVL72 is the second generation of NVIDIA's Oberon rack-scale architecture, emphasizing extreme co-design of CPUs and GPUs rather than standalone accelerators. Early results from engineering samples show that this co-design delivers major inference gains, especially for reasoning-heavy AI agents that require many sequential steps. The deep integration of Vera CPU and Rubin GPU allows for lower data movement and higher utilization, which translates directly into the throughput and cost improvements reported in the benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">NVIDIA Vera Rubin NVL72 | Co-Designed Infrastructure for Agentic AI</a></li>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/">NVIDIA Advances Vera Rubin Inference With New LPX ... | NVIDIA Blog</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-cpu/">Next Gen Data Center CPU | NVIDIA Vera CPU</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#AI Hardware`, `#Vera Rubin`, `#DeepSeek`, `#Inference`

---

<a id="item-4"></a>
## [FDA Authorizes First Wearable for Continuous Ketone and Glucose Monitoring](https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar) ⭐️ 8.0/10

The U.S. FDA has authorized the first wearable device that continuously monitors both ketone levels and blood sugar, marking a milestone in metabolic health technology. This authorization expands continuous monitoring beyond glucose to include ketones in a single device. This matters because people with diabetes, especially type 1, must track both glucose and ketones to avoid diabetic ketoacidosis (DKA), and a single continuous device could simplify management. It may also open the door to more sophisticated automated insulin delivery systems and broader metabolic health monitoring. The device continuously measures both glucose and ketone levels using sensors, replacing the need for separate fingerstick tests for ketones. However, while continuous glucose monitoring is well established, continuously measuring ketones (beta-hydroxybutyrate) in interstitial fluid is newer and may have accuracy limitations compared to blood tests.

hackernews · sunnynagra · Aug 25, 19:07 · [Discussion](https://news.ycombinator.com/item?id=49439017)

**Background**: Ketone bodies — acetoacetate, beta-hydroxybutyrate, and acetone — are produced by the liver when the body burns fat for energy instead of glucose, such as during fasting, low-carb diets, or insulin deficiency. Continuous glucose monitors (CGMs) use a small sensor under the skin to track glucose levels in interstitial fluid in real time, helping people with diabetes manage their condition. Measuring ketones is especially important for people with type 1 diabetes, as high ketone levels can signal diabetic ketoacidosis, a dangerous condition.

<details><summary>References</summary>
<ul>
<li><a href="https://www.niddk.nih.gov/health-information/diabetes/overview/managing-diabetes/continuous-glucose-monitoring">Continuous Glucose Monitoring - NIDDK</a></li>
<li><a href="https://my.clevelandclinic.org/health/body/25177-ketones">Ketones: What They Are, Function, Tests & Normal Levels</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ketone_bodies">Ketone bodies - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed cautious optimism, with some welcoming the device for blood sugar detection and hope for automated glucose control. Others raised skepticism about the accuracy of noninvasive sensing, questioned the practical utility of ketone monitoring for average diabetics, and highlighted reimbursement concerns. One commenter also shared a YouTube warning related to the topic.

**Tags**: `#FDA`, `#wearables`, `#diabetes`, `#glucose monitoring`, `#health tech`

---

<a id="item-5"></a>
## [Apple Unveils Mac Studio with M5 Max and M5 Ultra for Local AI](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) ⭐️ 8.0/10

Apple has introduced a new Mac Studio powered by the M5 Max and M5 Ultra chips, with the M5 Ultra offering up to a 36-core CPU, an 80-core GPU, and 512GB of unified memory. The announcement positions the Mac Studio as Apple's most powerful Mac for running large language models entirely on-device. This is a significant step for local AI, as the M5 Ultra's massive memory and bandwidth let developers run billion-parameter models without cloud dependencies. It could accelerate on-device AI workflows and put Apple in a stronger position against dedicated AI workstation hardware. The M5 Ultra uses a quad-die architecture built with next-generation UltraFusion, combining two M5 Max dies and delivering up to 1.2TB/s of memory bandwidth. External connectivity includes Thunderbolt 5 at 120Gb/s, and the M5 family adds a Neural Accelerator integrated into each GPU core.

hackernews · interpol_p · Aug 25, 13:03 · [Discussion](https://news.ycombinator.com/item?id=49433316)

**Background**: Apple's M-series chips use a unified memory architecture, where the CPU and GPU share the same pool of high-bandwidth memory, which is especially useful for AI workloads. The M5 generation introduced a next-generation GPU with a dedicated Neural Accelerator per core, and the M5 Ultra extends this by fusing two M5 Max dies. Earlier Ultra chips, like the M1 Ultra, also used UltraFusion to scale performance. Running AI models locally means processing happens on-device rather than in the cloud, which can improve privacy and reduce latency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/">Apple introduces new Mac Studio with M5 Max and M5 Ultra - Apple</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M1_Ultra">Apple M1 Ultra</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly excited about Apple embracing local AI, with one noting it is 'really awesome' and predicting it will pay off. However, several raised concerns about pricing, calling the memory costs 'insanity,' and one noted the press release uses 'up to' 46 times. A technical commenter estimated roughly 1000+ tokens/s prefill and 50+ tokens/s generation for DeepSeek V4 on an M5 Ultra, calling it 'quite usable and near parity to cloud,' while another argued 512GB is not future-proof for models beyond 1 trillion parameters without clustering.

**Tags**: `#apple`, `#mac-studio`, `#hardware`, `#local-ai`, `#m5`

---

<a id="item-6"></a>
## [Nitter Receives Cease and Desist, Instances Shut Down](https://github.com/zedeus/nitter/issues/1442) ⭐️ 8.0/10

The Nitter project announced it has received cease and desist letters, prompting maintainers to take down all public instances indefinitely while awaiting legal advice. The news was shared in a GitHub issue and quickly sparked wide discussion. This legal action threatens one of the most popular privacy-focused alternative frontends for X (Twitter), affecting users who rely on it to browse tweets without tracking or an account. It also raises concerns about the future of similar open-source projects that depend on accessing large platforms' data. According to a maintainer's comment, the project received cease and desist letters and all Nitter instances are expected to remain down for the foreseeable future. The exact legal demands and the sender were not disclosed in the initial announcement.

hackernews · Banditoz · Aug 25, 17:08 · [Discussion](https://news.ycombinator.com/item?id=49437283)

**Background**: Nitter is a free and open-source alternative frontend for Twitter/X focused on privacy and performance, allowing users to view profiles, tweets, and media without tracking, ads, or an account. It was widely used by people who wanted to read X content without logging in, and by those concerned about data collection. The project's shutdown highlights the legal vulnerability of third-party frontends that rely on scraping or unauthorized access to platform data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter</a></li>
<li><a href="https://nitter.tiekoetter.com/about">nitter .tiekoetter.com</a></li>

</ul>
</details>

**Discussion**: Community reactions mix frustration and resignation: many note they only used Nitter because organizations like local councils still communicate primarily via X, and some hope this will push people away from the platform. Others point out the irony of X being called a 'public town square' while requiring an account to view content, and a few call on companies to support community projects instead of issuing legal threats.

**Tags**: `#nitter`, `#cease-and-desist`, `#open-source`, `#privacy`, `#legal`

---

<a id="item-7"></a>
## [Firefox 157 Enables JPEG XL by Default on All Platforms](https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA?pli=1) ⭐️ 8.0/10

Firefox 157 will enable JPEG XL image format support by default across all platforms. This marks a major milestone for the format's adoption in browsers, aligning with Chromium's similar move. Cross-browser support for JPEG XL is a significant step for the image format, potentially leading to faster web image loading and better compression than legacy formats. Users and developers will benefit from broader interoperability and reduced storage and bandwidth costs. Both Firefox and Chromium are reportedly using the Rust-based jxl-rs implementation, which may prompt questions about Apple's C++ libjxl. The format is standardized as ISO/IEC 18181 and competes with AVIF, though it offers more features.

hackernews · yboris · Aug 25, 17:55 · [Discussion](https://news.ycombinator.com/item?id=49437946)

**Background**: JPEG XL is a next-generation image format developed by the JPEG committee, Google, and Cloudinary. It supports both lossy and lossless compression and is designed to supersede formats like JPEG, PNG, GIF, and WebP. Browser support has been gradually expanding since its standardization in 2022, and this default enablement in Firefox represents a notable increase in availability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>
<li><a href="https://caniuse.com/jpegxl">JPEG XL image format | Can I use... Support tables for HTML5 ...</a></li>
<li><a href="https://jpeg.org/jpegxl/">JPEG - JPEG XL</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the move and noted Chromium's similar plan, while some pondered Apple's possible response given its existing C++ libjxl implementation. Others asked whether older platforms like Windows 7/8 would be supported, and one user wondered how many people still haven't heard of JPEG XL in 2026.

**Tags**: `#JPEG XL`, `#Firefox`, `#browser`, `#image format`, `#web standards`

---

<a id="item-8"></a>
## [SpaceX Officially Announces Starbase LA Launch Site in Louisiana](https://www.spacex.com/sites/starbase-la) ⭐️ 8.0/10

SpaceX has officially announced Starbase LA, a new Starship launch site in Louisiana, confirming months of speculation. According to reports, the project is an enormous $100 billion investment featuring 10 launch pads. Starbase LA gives SpaceX a strategic new launch site with direct access to Sun-synchronous orbits, which are valuable for Earth-observation and Starlink missions. The site is also expected to deliver decades of construction jobs to one of the poorest coastal regions in the U.S. Space.com reports the project includes 10 launch pads and will launch next-generation Starlink satellites aboard Starship. The new site is separate from SpaceX's existing Starbase facility in Boca Chica, Texas.

hackernews · bilsbie · Aug 25, 16:37 · [Discussion](https://news.ycombinator.com/item?id=49436822)

**Background**: SpaceX's Starbase in Boca Chica, Texas, is the company's main Starship testing and production facility. Louisiana offers a favorable location for launching Sun-synchronous orbit (SSO) satellites, which pass over any given point on Earth at roughly the same local time daily, ideal for Earth observation and reconnaissance. The state's low-lying coastal terrain and existing industrial infrastructure also make it attractive for a large-scale rocket site.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spacex.com/sites/starbase-la">SpaceX - Starbase, LA</a></li>
<li><a href="https://www.space.com/space-exploration/private-spaceflight/spacex-announces-enormous-usd100-billion-starbase-louisiana-starship-launch-site">Starbase Louisiana: SpaceX announces enormous $100 billion ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starbase">SpaceX Starbase - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are broadly enthusiastic about the economic boost for coastal Louisiana, with one noting it could mean 10–20 years of work for welders, concrete workers, and tradespeople. Others expressed skepticism about Musk timelines, and some pointed out that parts of the official page's copy appear duplicated, raising questions about whether it was written by an LLM.

**Tags**: `#SpaceX`, `#aerospace`, `#launch site`, `#Louisiana`, `#technology`

---

<a id="item-9"></a>
## [Continual Learning Can Democratize Frontier AI, Says SovereignAI Report](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/) ⭐️ 8.0/10

A new technical report from tri-fair-lab argues that continual learning on readily available open-weight models can let a wide range of institutions achieve frontier-level AI performance. The report also introduces Thomson, a general-purpose frontier model trained with a focus on high-stakes professional work, with open weights released. This challenges the assumption that only a few heavily funded players can build frontier models, potentially reshaping AI accessibility and governance. By showing a viable path to SovereignAI with substantially lower compute and personnel budgets, it could enable universities, governments, and mid-sized companies to independently build, deploy, and govern AI. Thomson is trained via continual learning that combines a modern mid- and post-training stack with safeguards for plasticity and stability, making minimal high-impact parameter interventions. Evaluations show a distinctive π-shaped performance pattern: broad capability gains across many domains, including un-targeted ones, while almost completely avoiding the catastrophic forgetting typical of narrow domain adaptation.

reddit · r/MachineLearning · /u/Forsaken_Scientist · Aug 25, 10:30

**Background**: Continual learning is a machine learning paradigm that lets a model keep learning from new data over time without forgetting previously acquired knowledge, unlike traditional training on a fixed static dataset. Open-weight models are AI models whose trained parameters are publicly released, allowing anyone to download, study, and fine-tune them. SovereignAI refers to an organization's capability to independently build, deploy, and govern AI use, a concept that has gained attention due to the concentration of frontier AI development among a few well-funded players.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/continual-learning">What is continual learning? - IBM</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>

</ul>
</details>

**Tags**: `#continual learning`, `#frontier models`, `#open weights`, `#SovereignAI`, `#AI democratization`

---

<a id="item-10"></a>
## [Qwen Previews Qwen3.8-Flash-Next, Open-Source Model on Next-Gen Qwen4 Architecture](https://www.modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) ⭐️ 8.0/10

Qwen has launched a preview page on ModelScope for Qwen3.8-Flash-Next, a multimodal Mixture-of-Experts (MoE) model built on the next-generation Qwen4 architecture. The open-source download is scheduled for August 26, 2026, at 23:00 (UTC+8), and the model will be released in both standard and FP8 versions. This announcement gives the AI community an early look at architectural advances that will underpin the upcoming Qwen4 series, signaling that Alibaba's Qwen team is committed to open-sourcing its next-generation technology. By releasing a multimodal MoE model ahead of Qwen4, the team may accelerate adoption of efficient sparse models and spur ecosystem development. The preview page does not yet list parameter count, benchmark performance, or a full technical report. The model will be offered in a standard full-precision format and an FP8 quantized version, and the release date is more than a year away, so specifications may change before launch.

telegram · zaihuapd · Aug 25, 12:59

**Background**: Mixture of Experts (MoE) is a machine learning technique that divides a model into multiple specialized sub-networks, or 'experts,' each handling a subset of input data, which can improve efficiency and enable massive scale. FP8 is an 8-bit floating-point format designed to accelerate deep learning training and inference while reducing memory and bandwidth demands. Qwen is Alibaba Cloud's family of large language models; Qwen3 introduced MoE architecture at scale, and Qwen4 represents a further architectural evolution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2209.05433">[2209.05433] FP8 Formats for Deep Learning - arXiv.org</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Qwen`, `#AI/ML`, `#Open Source`, `#Multimodal`, `#MoE`

---

<a id="item-11"></a>
## [GPT-5.6 Sol Designs Custom CPU in Turing Complete, Runs Doom](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coder-gets-doom-running-on-a-custom-cpu-designed-by-gpt-5-6-sol-game-viewport-is-overlaid-on-a-pulsing-schematic-of-the-cpu-in-turing-completes-sandbox-environment) ⭐️ 8.0/10

AI enthusiast Angel demonstrated that GPT-5.6 Sol designed a custom CPU called Codex-R32, built entirely from logic gates in the Turing Complete sandbox, and used it to boot and play the 1993 classic Doom. The game viewport is overlaid on a live pulsing schematic of the processor's gate-level circuits. This marks a significant milestone in AI-assisted hardware design, showing that a language model can synthesize a complete, executable CPU from fundamental logic components. It demonstrates potential for AI to aid in chip design and verification workflows, though it currently runs only in a simulated environment. The CPU runs PureDOOM, a dependency-free single-header C port of Doom, compiled to RV32IM machine code and executed directly on the simulated hardware. When a netizen joked about running Crysis next, Angel had the AI reply that it would need a GPU, several gigabytes of RAM, and a circuit diagram visible from space.

telegram · zaihuapd · Aug 25, 15:23

**Background**: Turing Complete is an educational puzzle game that challenges players to build computers from basic logic gates, components, architecture, and assembly. RV32IM is a RISC-V instruction set architecture combining the base integer instruction set with the multiplication/division extension, commonly used in processor education and verification. PureDOOM is a single-header, dependency-free port of Doom that runs without video, input, sound, or music, making it easy to embed in emulation or simulation projects.

<details><summary>References</summary>
<ul>
<li><a href="https://store.steampowered.com/app/1444480/Turing_Complete/">Turing Complete on Steam Turing Complete Turing Complete Turing Complete - Steam Community Turing Complete - Play Online Turing Complete on Itch.io Game Turing Complete - Download Turing Complete Walkthrough | Thomas Tran</a></li>
<li><a href="https://github.com/Daivuk/PureDOOM">Daivuk/ PureDOOM : Pure DOOM - Single Header Doom Source Port ...</a></li>
<li><a href="https://ic.unicamp.br/~edson/disciplinas/mc404/material-riscv/extra/RISC-V-refcard.pdf">RV32IM assembly instructions reference card Prof. Edson Borin ...</a></li>

</ul>
</details>

**Discussion**: The community reaction was playful, with a netizen joking about running Crysis on the CPU next. Angel relayed the AI's witty reply about needing a GPU, extra RAM, and an enormous circuit diagram, which highlights both the achievement's impressiveness and its scale limitations.

**Tags**: `#AI`, `#CPU Design`, `#Turing Complete`, `#Doom`, `#GPT-5.6`

---

<a id="item-12"></a>
## [Anthropic to Tell Investors of $30 Trillion Potential Revenue, Tops SpaceX](https://www.wsj.com/tech/ai/anthropic-expected-to-tell-investors-it-sees-over-30-trillion-in-potential-revenue-a611efea) ⭐️ 8.0/10

Anthropic, the developer of Claude, is expected to tell investors that its potential revenue opportunity exceeds $30 trillion. That figure would surpass the record $28.5 trillion projection previously made by SpaceX. This projection is significant because it signals Anthropic's ambitious valuation of the AI market opportunity, potentially reshaping investor expectations. If realized, it would exceed SpaceX's record and underscore the outsized financial bets being placed on AI companies. The figure is a 'potential revenue opportunity' metric, a theoretical maximum under ideal conditions rather than an actual revenue forecast. The $30 trillion figure is speculative and represents the size of the market Anthropic believes it could address, not guaranteed revenue.

telegram · zaihuapd · Aug 25, 17:32

**Background**: Anthropic is an American AI company that developed Claude, a series of large language models released as an AI chatbot in March 2023. The 'potential revenue' concept refers to the maximum income a business could generate from all sales opportunities under ideal circumstances, which is distinct from actual revenue affected by market conditions and competition. SpaceX's previous $28.5 trillion projection had already stretched the limits of this seldom-used financial metric.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://dealhub.io/glossary/potential-revenue/">What is Potential Revenue? | DealHub AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Business`, `#Finance`, `#LLM`

---