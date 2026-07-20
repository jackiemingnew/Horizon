---
layout: default
title: "Horizon Summary: 2026-07-20 (EN)"
date: 2026-07-20
lang: en
---

> From 34 items, 11 important content pieces were selected

---

1. [Critical no-gadget RCE in Fastjson 1.x](#item-1) ⭐️ 9.0/10
2. [Zhipu Completes All-Domestic-Chip AI Data Center](#item-2) ⭐️ 9.0/10
3. [China's open-weights AI strategy is winning](#item-3) ⭐️ 8.0/10
4. [Romania land registry database wiped by hacker](#item-4) ⭐️ 8.0/10
5. [AI writing detection on arXiv: up to 39% flagged by 2026](#item-5) ⭐️ 8.0/10
6. [Kimi K3 and Qwen 3.8 Challenge Anthropic in Open-Weight Race](#item-6) ⭐️ 8.0/10
7. [US Legislation Proposed to Boost Open Models Against Chinese AI](#item-7) ⭐️ 8.0/10
8. [Altman Email Reveals OpenAI's Strategic Open-Source Move](#item-8) ⭐️ 8.0/10
9. [Reddit discusses LeCun's JEPA and world models](#item-9) ⭐️ 8.0/10
10. [US may restrict use of Chinese open-weight AI models after Kimi K3](#item-10) ⭐️ 8.0/10
11. [Study: Apps for US troops embed Chinese/Russian code](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Critical no-gadget RCE in Fastjson 1.x](https://x.com/k_firsov/status/2078872293745570032) ⭐️ 9.0/10

A critical remote code execution vulnerability has been disclosed in Fastjson versions 1.2.68 through 1.2.83, which does not require enabling autoType or any classpath gadgets, and is exploitable on JDK 8, 17, and 21. This vulnerability is significant because Fastjson is widely used in Java applications, and the lack of an official patch leaves millions of deployments at risk; immediate migration to Fastjson2 or enabling SafeMode is required to prevent exploitation. The vulnerability works without autoType being enabled and without relying on any classpath gadgets, making it particularly dangerous; Fastjson 1.x support ended in October 2024, and the only mitigations are upgrading to Fastjson2 or enabling SafeMode via JVM parameters or configuration files.

telegram · zaihuapd · Jul 20, 14:32

**Background**: Fastjson is a popular JSON parsing library for Java that supports a feature called AutoType, which allows specifying the actual type during deserialization. Historically, AutoType has been exploited for deserialization RCE attacks. Classpath gadgets are commonly used in such attacks, but this vulnerability bypasses that need. SafeMode, introduced in Fastjson 1.2.68, disables AutoType entirely and is recommended as a hardening measure.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/alibaba/fastjson/wiki/enable_autotype">enable_autotype · alibaba/fastjson Wiki · GitHub</a></li>
<li><a href="https://github.com/alibaba/fastjson/wiki/fastjson_safemode_en">fastjson_safemode_en · alibaba/fastjson Wiki</a></li>
<li><a href="https://jfrog.com/blog/cve-2022-25845-analyzing-the-fastjson-auto-type-bypass-rce-vulnerability/">CVE-2022-25845 - Fastjson RCE vulnerability analysis</a></li>

</ul>
</details>

**Tags**: `#fastjson`, `#RCE`, `#security vulnerability`, `#Java`, `#critical`

---

<a id="item-2"></a>
## [Zhipu Completes All-Domestic-Chip AI Data Center](https://www.bloomberg.com/news/articles/2026-07-20/z-ai-completes-giant-data-center-with-chinese-chips-to-train-ai) ⭐️ 9.0/10

Zhipu (Z. AI) has completed a 1-gigawatt data center that uses only Chinese-made chips, and it has begun partial operations to train its GLM large language models. This milestone demonstrates significant progress in China's AI chip self-sufficiency and reduces reliance on foreign hardware like NVIDIA, potentially reshaping the global AI hardware landscape and geopolitical dynamics. The data center has a power capacity of 1 gigawatt, enough to power about 750,000 homes simultaneously, and it is one of the largest facilities built by a Chinese AI lab. Zhipu operates multiple computing clusters each containing over 10,000 chips.

telegram · zaihuapd · Jul 20, 15:43

**Background**: GLM (General Language Model) is a series of open-weight large language models developed by Z. AI (formerly Zhipu AI). The first GLM model was published in March 2021, and it gained attention as ChatGLM in 2023. The latest version, GLM-5.2, is designed for long coding tasks and agentic workflows. China has been striving to develop domestic AI chips due to US export restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>
<li><a href="https://www.businessinsider.com/what-is-glm-5-2-chinese-ai-coding-model-2026-6">What is GLM-5.2? Another open-source Chinese AI model has Silicon Valley's attention.</a></li>

</ul>
</details>

**Tags**: `#AI`, `#data center`, `#China`, `#domestic chips`, `#GLM`

---

<a id="item-3"></a>
## [China's open-weights AI strategy is winning](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

An analysis argues that China's open-weights AI approach is surpassing US proprietary models, citing historical trends where free and open options dominate markets. This could reshape the global AI landscape by making powerful models more accessible and affordable, challenging the dominance of US companies like OpenAI and Anthropic. Open-weights models are not fully open-source; they allow free download and customization but hosting costs remain. The article claims 80% of startups use Chinese models, but some commenters dispute this figure.

hackernews · benwerd · Jul 20, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48979269)

**Background**: Open-weight models are AI models whose core components are publicly released, allowing anyone to download and run them on their own infrastructure. This contrasts with proprietary models like GPT-4, which are only accessible via API. Historically, free and low-end options (e.g., PCs, Linux) have often defeated expensive proprietary systems in computing markets.

<details><summary>References</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://openai.com/global-affairs/open-weights-and-ai-for-all/">Open weights and AI for all | OpenAI</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree that open-weights will win, but dispute specific claims like '80% of startups using Chinese models'. Some note that open-weights are not fully open-source, and hosting costs can be high. Historical parallels to PCs and Linux are widely cited to support the argument.

**Tags**: `#AI`, `#open-weights`, `#China`, `#open-source`, `#technology strategy`

---

<a id="item-4"></a>
## [Romania land registry database wiped by hacker](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) ⭐️ 8.0/10

A hacker wiped Romania's entire land registry database, but the agency had offline backups and is rebuilding its network. The hacker claimed to have deleted backups, but officials confirmed they still have copies to restore data. This incident threatens land ownership records and could cause societal chaos if data is permanently lost. It highlights critical infrastructure vulnerabilities and alleged corruption in government IT contracts. The agency is migrating its applications to Romania's Government Cloud, coordinated by the Special Telecommunications Service (STS), expected to complete by July 22. The hacker was identified as Zakaria Mahdjoub from Oran, Algeria.

hackernews · speckx · Jul 20, 13:28 · [Discussion](https://news.ycombinator.com/item?id=48978605)

**Background**: Land registries are critical for proving property ownership; losing such data can trigger legal and economic turmoil. Similar incidents, like South Korea's data center fire that erased 900TB of government data without backups, underscore the importance of offline copies.

**Discussion**: Commenters attribute the breach to corruption, claiming government IT contracts go to cronies who neglect security. They also note that offline backups likely saved the day, preventing long-term chaos. Some question extradition risks for the Algerian hacker.

**Tags**: `#cybersecurity`, `#data breach`, `#critical infrastructure`, `#Romania`, `#corruption`

---

<a id="item-5"></a>
## [AI writing detection on arXiv: up to 39% flagged by 2026](https://unslop.run/blog/measuring-ai-writing-on-arxiv) ⭐️ 8.0/10

A study measured AI writing in arXiv papers from 2021 to 2026 using a detector tuned to avoid false positives, finding that by January 2026 about 39% of papers were flagged as AI-written, with computer science peaking at 65%. This highlights the rapid adoption of LLMs in academic writing and raises concerns about academic integrity and the reliability of detection methods, especially given community tests showing high false positive rates on pre-LLM texts. The detector used perplexity and burstiness measures, with a threshold set to maintain a pre-ChatGPT false positive rate of 0.4%, yet community members found that papers written in 2011-2015 scored up to 74% machine-written.

hackernews · dopamine_daddy · Jul 20, 16:36 · [Discussion](https://news.ycombinator.com/item?id=48981206)

**Background**: Detecting AI-generated text is challenging because LLMs can produce text indistinguishable from human writing. Common methods include perplexity analysis, which measures how predictable the text is to a language model, and burstiness, which captures sentence length variation. These metrics are not definitive and can misclassify human-written text, especially in formal academic writing. OpenAI's own AI classifier was retired due to low accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://cacm.acm.org/research/the-science-of-detecting-llm-generated-text/">The Science of Detecting LLM-Generated Text – Communications of the ACM</a></li>
<li><a href="https://aifreetextpro.com/blog/how-ai-detectors-work">How AI Detectors Work: Perplexity & Burstiness Explained (2026)</a></li>
<li><a href="https://www.linkedin.com/pulse/openais-ai-text-classifier-accuracy-limitations-sana-uqaili-rzhic">OpenAI’s AI Text Classifier: Accuracy, Limitations, and Implications</a></li>

</ul>
</details>

**Discussion**: Community comments point out significant false positives: one user uploaded papers from 2011-2015 and got 27%-74% machine-written scores, questioning whether they wrote like an LLM or LLMs learned from them. Others note that detectors cannot distinguish between identical human and AI sentences, and that academic text inherently has low perplexity.

**Tags**: `#AI writing detection`, `#arXiv`, `#academic integrity`, `#LLM impact`, `#machine learning`

---

<a id="item-6"></a>
## [Kimi K3 and Qwen 3.8 Challenge Anthropic in Open-Weight Race](https://www.emergingtrajectories.com/lh/frontier-lab-economics/) ⭐️ 8.0/10

Moonshot AI released Kimi K3, a 2.8-trillion-parameter open-weight model with a 1-million-token context window, and Alibaba Cloud released Qwen 3.8, both challenging closed models like Anthropic's. These releases intensify competition in the rapidly commoditizing AI model market. The open-weight releases signal a potential shift toward commoditization, where frontier models become good enough for most tasks, reducing the strategic advantage of closed-source labs like Anthropic. This could force AI companies to differentiate via hardware integration or specialized applications rather than raw model performance. Kimi K3 features 2.8 trillion parameters and open weights promised by July 2026, while Qwen 3.8 is part of Alibaba's Qwen family under open licenses. The community notes that models like Fable (likely a frontier model) quickly lost their exclusivity as alternatives emerged, highlighting shortening hype cycles.

hackernews · cl42 · Jul 20, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48980019)

**Background**: Open-weight models are AI systems whose learned parameters are publicly available for download, enabling customization and deployment without vendor lock-in. Kimi K3 is one of the largest open-weight models, while Qwen models from Alibaba are widely used in open-source AI. The discussion reflects concerns that AI commoditization benefits hardware companies like ASIC makers, as model value shifts to inference efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen</a></li>
<li><a href="https://unrollnow.com/status/2077830229968683203">Thread By @ Kimi _Moonshot - Introducing Kimi K 3 : Open...</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/open-weight-models/">What are Open Source and Open Weight Models ? | Analytics Vidhya</a></li>

</ul>
</details>

**Discussion**: Commenters debate whether open-weight models will commoditize AI, with one user arguing the winner will be whoever burns models to ASICs fastest. Another discusses Anthropic's potential conflict of interest in the Figma board resignation, while others echo that models are rapidly reaching a plateau where closed-source advantages diminish.

**Tags**: `#AI`, `#LLM`, `#open source`, `#Anthropic`, `#commoditization`

---

<a id="item-7"></a>
## [US Legislation Proposed to Boost Open Models Against Chinese AI](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

Ben Thompson proposed that the U.S. pass a law making data collection for AI training explicit fair use and barring terms of service that prohibit model distillation, aiming to help U.S. open models compete with Chinese counterparts. He also noted that Alibaba's release of Qwen 3.8 Max as open weights may have been influenced by Xi Jinping's recent speech encouraging open source. This proposal addresses the tension between U.S. labs that prohibit distillation of their models while training on unlicensed data, potentially reshaping copyright law and competition dynamics in AI. If enacted, it could accelerate open model development and level the playing field with Chinese AI firms. The proposal explicitly defines collecting data for training models as fair use and bans terms of service that forbid distillation, which is simply querying an API. Thompson argues that stopping distillation is nearly impossible, so the U.S. should lean into a new copyright policy that indemnifies labs and ensures further innovation for everyone.

rss · Simon Willison · Jul 20, 17:09

**Background**: Model distillation is a technique where knowledge from a large model is transferred to a smaller one, often by querying the larger model's API. Open weights models are those where the trained parameters are publicly released, but not necessarily the full source code. The U.S. and China have been competing in AI development, with Chinese models like Qwen gaining prominence.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open models`, `#distillation`, `#copyright`, `#Chinese AI`

---

<a id="item-8"></a>
## [Altman Email Reveals OpenAI's Strategic Open-Source Move](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 8.0/10

A leaked email from Sam Altman to OpenAI's board in October 2022, revealed during the Musk v. Altman trial in 2026, details OpenAI's plan to release a GPT-3-level open-source model that can run locally on consumer hardware, aiming to preempt competitors like Stability AI and discourage new entrants. This email reveals that OpenAI's open-source releases may have been motivated more by competitive strategy than altruism, challenging the narrative around the company's open-source contributions. It also highlights how releasing powerful open models can be used as a strategic tool to control the AI landscape. The email specifies releasing a model with 'approximate capability of GPT-3' that can run locally on consumer hardware, and mentions doing so 'before Stability or someone else does.' The email is from October 1, 2022, before GPT-4 was released, and was exposed in the 2026 court case Musk v. Altman.

rss · Simon Willison · Jul 20, 03:47

**Background**: OpenAI initially positioned itself as an open-source AI research company but later shifted to a more closed model, especially after GPT-3 and GPT-4. Stability AI, known for its open-source image generation model Stable Diffusion, represents a competitor that embraces open-source. Running large language models locally on consumer hardware has become a key area of interest, with models like LLaMA, Mistral, and optimization techniques like quantization making it feasible.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stability_AI">Stability AI</a></li>

</ul>
</details>

**Tags**: `#ai-ethics`, `#sam-altman`, `#open-source`, `#generative-ai`, `#openai`

---

<a id="item-9"></a>
## [Reddit discusses LeCun's JEPA and world models](https://www.reddit.com/r/MachineLearning/comments/1v1i26p/i_just_read_lecuns_recent_thoughts_on_world/) ⭐️ 8.0/10

A Reddit user shared an interview with Yann LeCun where he critiques LLMs for lacking understanding of the physical world and proposes the Joint Embedding Predictive Architecture (JEPA) as a potential solution. The post sparked community debate on whether JEPA is the right path forward. This discussion highlights a critical debate in AI research about moving beyond next-token prediction to more grounded world models. LeCun's influence may steer research focus towards architectures like JEPA, potentially reshaping the future of AI development. JEPA predicts abstract representations of missing data from visible data in a shared latent space, avoiding direct pixel prediction or contrastive forces. LeCun's lab has been developing world models, and he recently left Meta to launch AMI Labs betting on world models over LLMs.

reddit · r/MachineLearning · /u/ConsciousGreenPepper · Jul 20, 10:50

**Background**: Large Language Models (LLMs) like GPT-4 generate text by predicting the next token, but they lack an internal model of the physical world and cannot truly understand or interact with it. World models are AI systems that internally simulate the environment to enable planning and reasoning about actions. Yann LeCun, a Turing Award winner, has long advocated for world models and proposed the Joint Embedding Predictive Architecture (JEPA) as a self-supervised learning method that learns abstract representations of the world. JEPA trains models to predict missing parts of an input in a latent space, rather than predicting pixels directly, making it more suitable for building world models.

<details><summary>References</summary>
<ul>
<li><a href="https://vinesmsuic.github.io/paper-jepa/">JEPA ( Joint - Embedding Predictive Architecture ) | Vines' Log</a></li>
<li><a href="https://bonega.ai/en/blog/yann-lecun-ami-labs-world-models-2026">Yann LeCun Leaves Meta to Bet $3.5 Billion on World Models</a></li>

</ul>
</details>

**Tags**: `#AI`, `#world models`, `#JEPA`, `#Yann LeCun`, `#LLMs`

---

<a id="item-10"></a>
## [US may restrict use of Chinese open-weight AI models after Kimi K3](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi) ⭐️ 8.0/10

The Trump administration is reportedly considering new restrictions to prevent US companies from using Chinese open-weight AI models, following the strong performance of Moonshot AI's Kimi K3 model. If enacted, this policy would reshape the global AI landscape by potentially cutting off US access to cost-effective, high-performance Chinese models, intensifying the US-China tech decoupling and impacting open-source AI development. The restrictions may involve soft measures like procurement rules, Entity List threats, and public pressure rather than an outright ban. White House AI advisor David Sacks criticized OpenAI and Anthropic for pushing the government to eliminate open-source competition.

telegram · zaihuapd · Jul 20, 11:49

**Background**: Open-weight AI models release their trained neural network weights, allowing others to run and fine-tune them, unlike fully closed models. The US has previously used the Entity List to restrict Chinese entities from accessing advanced technology, and chip export controls have been tightened over time. Kimi K3 is reportedly the world's largest open-weights model, built with advanced architecture like Mixture of Experts and Attention Residuals.

<details><summary>References</summary>
<ul>
<li><a href="https://unrollnow.com/status/2077830229968683203">Thread By @ Kimi _Moonshot - Introducing Kimi K 3 : Open...</a></li>
<li><a href="https://medium.com/lets-code-future/open-weight-ai-models-what-they-are-and-why-openais-next-move-matters-f86fe481973a">Open - Weight AI Models : What They Are, and Why... | Medium</a></li>
<li><a href="https://sanctionschecklist.com/denied-persons-list">Denied Persons List & BIS Entity List - US Export Control Screening</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open-source`, `#geopolitics`, `#regulation`, `#Kimi K3`

---

<a id="item-11"></a>
## [Study: Apps for US troops embed Chinese/Russian code](https://www.wired.com/story/apps-marketed-to-us-troops-are-shipping-chinese-and-russian-code/) ⭐️ 8.0/10

A study by Purdue University researchers analyzed over 220 apps marketed to US military personnel and found that nearly two-thirds contain third-party code from China, Russia, and other countries, including the Huawei Software Development Kit (SDK). This raises serious national security concerns because the embedded code, especially from entities like Huawei (already deemed a threat by the US government), could enable remote surveillance or data exfiltration, potentially compromising US military operations and personnel safety. Although no data was observed flowing to Huawei servers, the SDK can receive remote updates, meaning dormant malicious code could be activated later. A survey of 103 military-affiliated individuals found that 76% to 83% were extremely concerned about apps containing code from China, Russia, Iran, or North Korea.

telegram · zaihuapd · Jul 20, 13:42

**Background**: Software supply chain security refers to the risks introduced when applications incorporate third-party code or SDKs. Even legitimate SDKs can become dangerous if the provider is compromised or acts maliciously. Huawei has been restricted by the US government due to alleged ties to the Chinese military and espionage risks. Mobile apps used by military personnel can inadvertently expose sensitive location and behavioral data.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.huawei.com/consumer/en/">HUAWEI Developers</a></li>
<li><a href="https://www.darkreading.com/vulnerabilities-threats/rising-tide-of-software-supply-chain-attacks">The Rising Tide of Software Supply Chain Attacks</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#national security`, `#mobile apps`, `#military`, `#privacy`

---