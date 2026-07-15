---
layout: default
title: "Horizon Summary: 2026-07-15 (EN)"
date: 2026-07-15
lang: en
---

> From 31 items, 13 important content pieces were selected

---

1. [Stripe and Advent Offer Over $53B to Acquire PayPal](#item-1) ⭐️ 9.0/10
2. [Musk: X to open-source all code unconditionally](#item-2) ⭐️ 9.0/10
3. [Inkling: Open-Weights Multimodal Model with Audio](#item-3) ⭐️ 8.0/10
4. [Gemma 4 26B runs at 5 tokens/sec on 13-year-old CPU, no GPU](#item-4) ⭐️ 8.0/10
5. [Prioritize Mental Health and Communication in Development](#item-5) ⭐️ 8.0/10
6. [Seeking JEPA Devil's Advocacy in Robot Learning](#item-6) ⭐️ 8.0/10
7. [New Method Disentangles Convolutional Neuron Using Hadamard Product](#item-7) ⭐️ 8.0/10
8. [DeepSeek Annual Revenue Nears $500M, V4 API Gross Margin Over 50%](#item-8) ⭐️ 8.0/10
9. [零售业没有“赛道”了：山姆零食店拼多多争同一笔钱](#item-9) ⭐️ 8.0/10
10. [Google and Epic Withdraw Motions, Third-Party App Stores Coming to Google Play on July 22](#item-10) ⭐️ 8.0/10
11. [DeepSeek Completes First Funding Round, Tencent Becomes Top External Shareholder](#item-11) ⭐️ 8.0/10
12. [Telegram Launches Serverless Platform for Bots](#item-12) ⭐️ 8.0/10
13. [ASML Plans Price Hikes for Chipmaking Equipment](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stripe and Advent Offer Over $53B to Acquire PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 9.0/10

Stripe and private equity firm Advent International have jointly offered to acquire PayPal for more than $53 billion, according to sources. This acquisition would consolidate major payment processors under one umbrella, raising significant antitrust concerns and potentially reshaping the online payments landscape. The deal would combine Stripe with PayPal, Venmo, Braintree, and Xoom; critics note Stripe currently blocks merchants in cannabis and adult industries that PayPal allows, and PayPal's bank charter could offer Stripe new regulatory flexibility.

hackernews · rvz · Jul 15, 03:32 · [Discussion](https://news.ycombinator.com/item?id=48915953)

**Background**: Stripe is a leading online payment processor favored by startups and tech companies, while PayPal is an older, widely-used platform with consumer brand recognition. The acquisition would create a dominant player in card-not-present transactions, potentially leading to higher fees and fewer choices for merchants. Antitrust regulators may require the divestiture of assets like Venmo or Braintree to approve the deal.

**Discussion**: Community comments express strong concerns about market consolidation, with users worried about Stripe raising fees and its selective enforcement of policies on cannabis and adult industries. Some note that PayPal's bank charter could benefit Stripe, but overall sentiment is negative due to potential loss of competition and increased control over payment processing.

**Tags**: `#acquisition`, `#payments`, `#antitrust`, `#fintech`, `#stripe`

---

<a id="item-2"></a>
## [Musk: X to open-source all code unconditionally](https://x.com/elonmusk/status/2077361679034118271) ⭐️ 9.0/10

Elon Musk announced that after a security audit, X's entire codebase will be open-sourced unconditionally, and third-party reviewers will verify the running code matches the open-source repository. This move could set a new standard for transparency in large social media platforms, potentially increasing user trust but also raising technical and security challenges. The open-sourcing will happen after a security vulnerability review, and third-party auditors will confirm the deployed code matches the open-source repository.

telegram · zaihuapd · Jul 15, 13:32

**Background**: Open-sourcing code means making source code publicly available for anyone to view, modify, and distribute. X (formerly Twitter) is a major social media platform. This announcement follows Musk's previous calls for algorithmic transparency and his purchase of Twitter in 2022.

**Tags**: `#open-source`, `#Twitter`, `#transparency`, `#software trust`, `#Elon Musk`

---

<a id="item-3"></a>
## [Inkling: Open-Weights Multimodal Model with Audio](https://thinkingmachines.ai/news/introducing-inkling/) ⭐️ 8.0/10

Thinking Machines AI released Inkling, an open-weights multimodal model that natively supports audio, along with a fine-tuning platform called Tinker. Inkling provides a strong open-weights base for enterprises to customize and fine-tune models locally, potentially reducing dependence on closed APIs and lowering costs for specialized tasks. Inkling claims to be the largest open-weights model with audio support, and is available in GGUF and NVFP4 formats for local deployment via llama.cpp and Unsloth.

hackernews · vimarsh6739 · Jul 15, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48924912)

**Background**: An open-weights model is an AI model whose trained parameters (weights) are publicly released, allowing anyone to download, inspect, and fine-tune them. Unlike fully open-source models, open-weights models may not include all training data or code. This approach enables customization and local deployment while the original developer retains control over the model's license and commercial use.

<details><summary>References</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**Discussion**: Community members praised Inkling as the strongest open-weights multimodal model with audio support, and noted that its business model (open base with paid fine-tuning platform Tinker) could make it a viable alternative to closed models. Some also expressed hope that Thinking Machines could fill the role of an 'American DeepSeek'.

**Tags**: `#open-weights`, `#multimodal`, `#audio`, `#AI model`, `#local LLM`

---

<a id="item-4"></a>
## [Gemma 4 26B runs at 5 tokens/sec on 13-year-old CPU, no GPU](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

A blog post demonstrates running Google's Gemma 4 26B model (a Mixture-of-Experts architecture) at 5 tokens per second on a 13-year-old Intel Xeon server with no GPU, using CPU-only inference and quantization. This achievement challenges the assumption that large language models require modern GPUs, highlighting the potential for local inference on legacy hardware and sparking debate about the cost-effectiveness of local versus cloud-based inference. The model is Gemma 4 26B A4B, a 26B-parameter MoE model with 4B active parameters, quantized to 4-bit to fit in memory. The CPU is a dual-socket Xeon E5-2697 v2 from ~2013, with the inference framework using CPU-specific optimizations like SIMD and thread parallelism.

hackernews · neomindryan · Jul 15, 15:34 · [Discussion](https://news.ycombinator.com/item?id=48922434)

**Background**: Gemma 4 is a family of open models from Google, featuring both dense and Mixture-of-Experts (MoE) architectures. The 26B A4B variant activates only 4B parameters per token, reducing computation. Running LLMs on CPUs is typically slow due to limited memory bandwidth and lack of GPU parallelism, but quantization and specialized frameworks can make it feasible on older hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview - Google AI for Developers</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>
<li><a href="https://www.techplained.com/run-llms-without-gpu">Run LLMs Without GPU: CPU Benchmarks... | TechPlained</a></li>

</ul>
</details>

**Discussion**: Comments are mixed: some users praise the technical feat and predict even larger models will run on consumer hardware by 2027, while others question the cost efficiency, noting that cloud inference can be cheaper per token when accounting for electricity and hardware depreciation. Several users share their own CPU inference benchmarks with different models.

**Tags**: `#AI`, `#LLM`, `#inference`, `#optimization`, `#hardware`

---

<a id="item-5"></a>
## [Prioritize Mental Health and Communication in Development](https://ramones.dev/posts/mental-health/) ⭐️ 8.0/10

The author published a personal reflection on mental health challenges in software development, advocating for self-awareness and open communication. This topic is highly relevant to the developer community, as mental health issues are prevalent yet often stigmatized, and the discussion can help reduce isolation and encourage seeking support. The author sets a goal for end of 2027 to stop making stupid mistakes by planning every task, and the comments highlight challenges faced by neurodivergent individuals.

hackernews · ramon156 · Jul 15, 11:27 · [Discussion](https://news.ycombinator.com/item?id=48919198)

**Background**: Mental health is a recognized concern in the software industry, with high rates of burnout, anxiety, and depression. Neurodivergence, such as ADHD or autism, is increasingly discussed as a factor that affects work performance and communication. The post fits into a broader conversation about improving well-being in tech.

**Discussion**: Commenters emphasize that neurodivergence is not something one can simply overcome with planning systems, and that self-acceptance and understanding one's own working style are crucial. One discussion thread explores the distinction between diagnosis and root cause, noting that ADD may be the root cause of many difficulties described.

**Tags**: `#mental health`, `#software development`, `#personal growth`, `#neurodivergence`, `#communication`

---

<a id="item-6"></a>
## [Seeking JEPA Devil's Advocacy in Robot Learning](https://www.reddit.com/r/MachineLearning/comments/1uxcryc/looking_for_jepa_devil_advocates_r/) ⭐️ 8.0/10

A researcher on Reddit is asking for critical perspectives on JEPA models used as world models in robot learning, specifically seeking counterarguments to the optimistic views presented by Yann LeCun. This discussion is important because JEPA models represent a potential new direction in AI for robotics, but blind acceptance could overlook fundamental flaws; critical analysis is essential for the field to progress. The poster notes that LeCun dismisses LLMs and RL while promoting JEPA, raising doubts about whether the approach is oversold; they want to understand practical downsides compared to other world model approaches.

reddit · r/MachineLearning · /u/Amazing-Coat5160 · Jul 15, 17:34

**Background**: JEPA (Joint Embedding Predictive Architecture) learns representations by predicting abstract future states rather than reconstructing pixels, differing from generative models. It is a key component of Yann LeCun's vision for AI that can learn world models for tasks like robot planning.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.meta.com/blog/yann-lecun-ai-model-i-jepa/">I-JEPA: The first AI model based on Yann LeCun’s vision for ...</a></li>
<li><a href="https://github.com/AI-in-Transportation-Lab/awesome-jepa">AI-in-Transportation-Lab/awesome-jepa - GitHub</a></li>

</ul>
</details>

**Tags**: `#JEPA`, `#world models`, `#robot learning`, `#Yann LeCun`, `#machine learning research`

---

<a id="item-7"></a>
## [New Method Disentangles Convolutional Neuron Using Hadamard Product](https://www.reddit.com/r/MachineLearning/comments/1uwya70/mechanistic_interpretability_a_first_paper_on/) ⭐️ 8.0/10

A researcher developed a technique using the Hadamard product of a neuron's receptive field and its weights to cluster patterns detected by a 1x1 convolutional neuron in InceptionV1, yielding clean monosemantic clusters for concepts like cars, cats, and dogs. This work provides a new interpretability tool for convolutional neural networks, potentially aiding in understanding how these models process visual concepts. It also reveals evidence that gradient descent deliberately encodes low-value patterns with balanced positive and negative weights. The method focuses on the mixed4e-55 neuron in InceptionV1 and uses clustering on the Hadamard product of the receptive field and weight matrices. The author found that low-valued clusters, such as letters, had all dependent neurons firing on the same concept with evenly distributed positive and negative weights, suggesting deliberate noise injection by gradient descent.

reddit · r/MachineLearning · /u/narang_27 · Jul 15, 06:59

**Background**: Mechanistic interpretability aims to reverse-engineer neural networks to understand their internal computations. The Hadamard product is an element-wise matrix multiplication used here to combine receptive field and weight information. Monosemanticity refers to a neuron or feature that represents a single, distinct concept, which is rare in standard neurons but can be revealed through techniques like dictionary learning or this clustering approach.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hadamard_product_(matrices)">Hadamard product (matrices) - Wikipedia</a></li>
<li><a href="https://transformer-circuits.pub/2023/monosemantic-features/index.html">Towards Monosemanticity: Decomposing Language Models With ...</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#convolutional neural networks`, `#neuron analysis`, `#AI interpretability`

---

<a id="item-8"></a>
## [DeepSeek Annual Revenue Nears $500M, V4 API Gross Margin Over 50%](https://www.theinformation.com/articles/deepseeks-annualized-revenue-nears-500-million-boosting-fundraise-ipo-plans) ⭐️ 8.0/10

DeepSeek's annualized revenue has reached between $400 million and $500 million, driven by enterprise and developer API usage, and its V4 API gross margin exceeds 50%. The company is also planning a fundraising round targeting 50 billion RMB at a valuation of about 500 billion RMB (~$74 billion). This demonstrates that DeepSeek's cost-efficient AI models can achieve significant revenue and profitability, challenging dominant players like OpenAI and Anthropic. The high valuation and planned fundraising signal strong investor confidence in DeepSeek's growth trajectory and the potential for Chinese AI companies to compete globally despite chip export restrictions. The annualized revenue is calculated by extrapolating recent monthly revenue and is not actual full-year realized revenue. DeepSeek's V4 API charges much less than competitors like OpenAI, but achieves over 50% gross margin through optimized infrastructure that reduces the number of chips needed to run models. The company plans to bring in overseas investors, including from the Middle East, and allow investments in US dollars.

telegram · zaihuapd · Jul 15, 07:04

**Background**: DeepSeek is a Chinese AI company founded in 2023 by Liang Wenfeng and backed by hedge fund High-Flyer. It gained attention for training models like DeepSeek-V3 and DeepSeek-R1 at a fraction of the cost of US rivals, using fewer and less advanced chips due to export restrictions. Its open-weight models (e.g., MIT License) have been praised for cost-effectiveness, and its success triggered a sharp drop in Nvidia's stock in early 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://grokipedia.com/page/deepseek">DeepSeek</a></li>
<li><a href="https://www.deepseek.com/en/">DeepSeek</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI revenue`, `#API pricing`, `#fundraising`, `#AI infrastructure`

---

<a id="item-9"></a>
## [零售业没有“赛道”了：山姆零食店拼多多争同一笔钱](https://mp.weixin.qq.com/s/dAHAVxglD-F1RovjcvqCRw) ⭐️ 8.0/10

Chinese retail vertical era ends as Sam's Club, snack discount stores, and Pinduoduo compete for same household spending, with trust and convenience key.

telegram · zaihuapd · Jul 15, 09:01

**Tags**: `#retail`, `#China`, `#consumer behavior`, `#e-commerce`, `#market research`

---

<a id="item-10"></a>
## [Google and Epic Withdraw Motions, Third-Party App Stores Coming to Google Play on July 22](https://www.theverge.com/policy/965792/google-epic-withdraw-injunction-third-party-app-stores-coming-google-play) ⭐️ 8.0/10

Google and Epic Games have withdrawn their motions regarding the court injunction, requiring Google to allow third-party app stores on Google Play starting July 22, 2026. This represents a major antitrust policy shift for Google's app distribution ecosystem, potentially increasing competition and giving users more choices. Developers may see new distribution channels, while Google faces renewed pressure on its control over Android apps. Third-party stores must pay a $5,000 annual security review fee and must not distribute outside the US, among other requirements. Developers can opt out if they do not want their apps listed in third-party stores, and a separate 'Registered App Store' program will apply outside the US later in 2026.

telegram · zaihuapd · Jul 15, 11:15

**Background**: Sideloading has always been possible on Android, allowing users to install apps from outside official stores. Google's new 'Registered App Store' program aims to give verified third-party stores system-level installation privileges, initially outside the US. This court ruling forces Google to host rival stores within Play itself in the US, marking a significant shift in Android's app distribution model.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/Registered+App+Stores/67459588">Registered App Stores - 百度百科</a></li>

</ul>
</details>

**Tags**: `#antitrust`, `#app store`, `#Google`, `#Epic Games`, `#policy`

---

<a id="item-11"></a>
## [DeepSeek Completes First Funding Round, Tencent Becomes Top External Shareholder](https://www.cls.cn/detail/2427193) ⭐️ 8.0/10

DeepSeek has completed its first round of financing, with Tencent emerging as the largest external shareholder through a complex shareholding structure. The company has also launched a large-scale recruitment drive and plans to release its full V4 model this month. This investment from major tech and investment firms signals strong confidence in DeepSeek's AI capabilities, potentially reshaping the competitive landscape of large language models in China. The upcoming V4 model could further advance the state of the art in open-source AI. Tencent holds over 33% of the investment platform Hangzhou Chengyu, which owns 8.52% of DeepSeek, making it the largest external shareholder. The V4 model is reported to have 284 billion total parameters with 13 billion activated per token, supporting 1 million token context length.

telegram · zaihuapd · Jul 15, 12:56

**Background**: DeepSeek, founded in 2023, focuses on developing leading general AI models and has released several open-source models with hundreds of billions of parameters. The company uses self-built training frameworks and a cluster of tens of thousands of GPUs. Code agents are AI-powered tools that assist developers in writing code, such as Huawei's CodeArts or Cursor.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/">DeepSeek | 深度求索</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2036707452293535593">Deepseek-V4模型结构与源码解析 - 知乎</a></li>
<li><a href="https://deepseekv4.wiki/">DeepSeek V4 - 使用入口｜实战教程｜最新信息</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#融资`, `#AI`, `#腾讯`, `#大模型`

---

<a id="item-12"></a>
## [Telegram Launches Serverless Platform for Bots](https://core.telegram.org/bots/serverless) ⭐️ 8.0/10

Telegram has officially launched a serverless platform that allows developers to run bot and Mini App backend code directly on Telegram's infrastructure, eliminating the need for self-managed servers. This simplifies deployment and reduces operational overhead for developers, making it easier to build and scale Telegram bots and Mini Apps without managing infrastructure. Developers write plain JavaScript modules and deploy with a single command (npx tgcloud push). The code runs in an isolated V8 sandbox close to the Bot API, with a built-in SQLite database.

telegram · zaihuapd · Jul 15, 16:00

**Background**: Traditionally, hosting a Telegram bot required setting up a server, managing containers, and handling scaling. Serverless computing abstracts away server management, allowing developers to focus on code. Telegram's new platform provides a native solution integrated with its ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://core.telegram.org/bots/serverless">Telegram Serverless</a></li>

</ul>
</details>

**Tags**: `#telegram`, `#serverless`, `#bots`, `#javascript`, `#cloud`

---

<a id="item-13"></a>
## [ASML Plans Price Hikes for Chipmaking Equipment](https://news.bloomberglaw.com/artificial-intelligence/asml-plans-price-increases-on-chipmaking-equipment-information) ⭐️ 8.0/10

ASML, the dominant supplier of photolithography equipment, plans to increase prices for both EUV and DUV machines. TSMC is resisting the EUV price hike, while some Chinese chipmakers have accepted a 10% increase for DUV tools. This move could increase costs for semiconductor manufacturers worldwide, potentially impacting chip prices and supply chains. It also highlights the geopolitical dimension, as China's access to advanced DUV equipment remains limited while EUV exports are already restricted. ASML's CFO Roger Dassen stated that the current environment gives the company better pricing power, and advanced EUV lithography capacity is nearly fully booked through the end of 2027. The proposed DUV price increase is specifically 10%.

telegram · zaihuapd · Jul 15, 16:49

**Background**: ASML is the only company that produces extreme ultraviolet (EUV) lithography machines, which use 13.5 nm wavelength light to create the finest features on advanced chips. Deep ultraviolet (DUV) lithography uses longer wavelengths (e.g., 193 nm) and is essential for a broader range of chip nodes. While EUV is critical for cutting-edge processes like 5nm and 3nm, DUV is used for less advanced but still vital chips, and its export to China has been subject to trade restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EUV_lithography">EUV lithography - Wikipedia</a></li>
<li><a href="https://www.eetimes.com/deep-uv-lithography-processing-the-best-kept-secret-of-euv-lithography/">DUV Lithography : EUV Lithography ’s Best Kept Secret - EE Times</a></li>

</ul>
</details>

**Tags**: `#ASML`, `#semiconductor equipment`, `#lithography`, `#chip manufacturing`, `#trade policy`

---