---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> 从 43 条内容中筛选出 13 条重要资讯。

---

1. [Firefox 编译为 WebAssembly 可在浏览器内运行](#item-1) ⭐️ 9.0/10
2. [日本购入 2.75 万块英伟达 Rubin 芯片打造机器人主权 AI](#item-2) ⭐️ 9.0/10
3. [Moonshot 发布 Kimi K3 开源权重前沿 AI 模型](#item-3) ⭐️ 8.0/10
4. [LM Studio Bionic：面向开放模型的 AI 智能体](#item-4) ⭐️ 8.0/10
5. [Roc 编译器从 Rust 重写到 Zig](#item-5) ⭐️ 8.0/10
6. [Thinking Machines Lab 发布开源权重模型 Inkling](#item-6) ⭐️ 8.0/10
7. [Linus Torvalds 声明 Linux 不反对 AI](#item-7) ⭐️ 8.0/10
8. [QLoRA 默认学习率 2e-4 对小数据集是错误的](#item-8) ⭐️ 8.0/10
9. [ExTernD：实现高精度 LLM 量化的三元分解方法](#item-9) ⭐️ 8.0/10
10. [知网将删除将 AI 列为作者的论文](#item-10) ⭐️ 8.0/10
11. [欧盟裁定谷歌开放安卓与搜索数据给竞争对手](#item-11) ⭐️ 8.0/10
12. [1Password 集成 Claude，AI 登录无需密码](#item-12) ⭐️ 8.0/10
13. [Truth Social 将向华尔街出售特朗普帖子的快速访问权限](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox 编译为 WebAssembly 可在浏览器内运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter 将 Firefox 的 Gecko 引擎编译为 WebAssembly，使得整个浏览器能通过基于 WebSocket 的 Wisp 协议在另一个浏览器内运行。 这展示了在沙箱化的 WebAssembly 环境中运行完整浏览器引擎的可行性，为浏览器隔离、便携式浏览和新颖的应用架构开辟了可能性。 该项目利用了 Gecko 强大的单进程支持，估计使用了价值 25,000 美元的 AI token，但通过 Claude Max 订阅降低了实际成本。所有网络流量都通过 Wisp 协议经由 Puter 的服务器代理，HTTPS 连接支持端到端加密。

rss · Simon Willison · 7月16日 23:34

**背景**: WebAssembly（WASM）是一种二进制指令格式，允许用 C++ 等语言编写的代码在浏览器中以接近原生速度运行。Gecko 是 Mozilla 在 Firefox 中使用的浏览器引擎。单进程模式简化了像浏览器这样复杂的 GUI 应用向 WASM 的编译。Wisp 协议提供了一种低开销的方式，通过单个 WebSocket 代理 TCP 和 UDP 连接，这是因为 WebAssembly 代码无法直接打开网络套接字。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gecko_(software)">Gecko (software) - Wikipedia</a></li>
<li><a href="https://wiki.mozilla.org/Gecko:Overview">Gecko:Overview - MozillaWiki</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low ...</a></li>

</ul>
</details>

**社区讨论**: 在 Hacker News 上，评论者对这一技术成就表示惊叹，但有人指出该项目需要大量服务器扩展以应对流量。AI 辅助编程的使用也被认为是该项目可行的因素之一。

**标签**: `#WebAssembly`, `#Firefox`, `#browser`, `#compilation`, `#demo`

---

<a id="item-2"></a>
## [日本购入 2.75 万块英伟达 Rubin 芯片打造机器人主权 AI](https://www.bloomberg.com/news/articles/2026-07-16/japan-to-buy-nvidia-rubin-chips-to-build-sovereign-ai-for-robots) ⭐️ 9.0/10

日本宣布通过新成立的公司 Noetra 购买 2.75 万块英伟达 Rubin 芯片，建设大型数据中心并开发面向机器人的本土基础 AI 模型，该项目获得 3873 亿日元（约 24 亿美元）政府拨款。 这一举措是日本推动主权 AI 的重大尝试，旨在减少对外国技术的依赖，并与美中在机器人领域竞争，目标到 2040 年占据全球机器人市场 30%以上份额，可能重塑全球 AI 和机器人格局。 Noetra 由总裁田场广信领导，计划明年 3 月发布首个 AI 模型，并在数年内推出机器人专用版本。合作伙伴包括软银、丰田支持的 Preferred Networks 和 NEC。

telegram · zaihuapd · 7月16日 10:59

**背景**: 主权 AI 指国家为发展独立 AI 能力、减少对外国供应商关键依赖所做的努力。英伟达 Rubin 架构以天体物理学家 Vera Rubin 命名，是采用 3nm 制程和 HBM4 内存的下一代 GPU/CPU 平台，计划 2026 年第三季度发布。日本希望打造除中美之外的“第三种选择”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rubin_(microarchitecture)">Rubin (microarchitecture) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_AI">Sovereign AI</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#sovereign AI`, `#robotics`, `#Japan`, `#chips`

---

<a id="item-3"></a>
## [Moonshot 发布 Kimi K3 开源权重前沿 AI 模型](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

Moonshot AI 发布了 Kimi K3，这是一个拥有 2.8 万亿参数、100 万 token 上下文窗口的开源权重前沿模型，定价为每百万 token $3/$15，具有竞争力。 此次发布挑战了只有美国实验室才能生产前沿 AI 的观念，可能推动成本下降并加速高级 AI 能力的商品化。 Kimi K3 拥有 100 万 token 上下文窗口，定价与 Anthropic 的 Sonnet 系列相当，但对于中国开源权重模型而言，这个价格非常高。

hackernews · vincent_s · 7月16日 14:46 · [社区讨论](https://news.ycombinator.com/item?id=48935342)

**背景**: 开源权重模型允许用户下载并在自己的硬件上运行，但可能不包含完整的训练数据或代码。上下文窗口指模型一次能处理的文本量；100 万 token 足以处理大型文档或长对话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.innovatrixinfotech.com/blog/context-windows-explained-1-million-tokens-architecture">1 Million Token Context Window: What It Means for Builders ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Kimi K3 的定价对中国模型来说较高，但如果真的能与 Sol/Fable 等前沿模型竞争，则价格合理。一些人讨论中国实验室是否通过商品化 AI 来推销硬件，而另一些人则指出了巨大的训练成本。

**标签**: `#AI`, `#model release`, `#pricing`, `#Chinese AI`, `#frontier intelligence`

---

<a id="item-4"></a>
## [LM Studio Bionic：面向开放模型的 AI 智能体](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 8.0/10

LM Studio 推出了 Bionic，一个使用开源大语言模型处理编码、文档创建和复杂工作任务的 AI 智能体平台，支持本地运行或云端连接。 此次发布将 LM Studio 从聊天界面扩展为完整的智能体工具，使强大的开放模型能用于实际任务，同时为企业提供成本控制和数据安全保障。 Bionic 支持带本地转录的语音输入，在 Work 项目中自动检查点，灵活的执行方式包括本地、LM Link 或 LM Studio Secure Cloud 以运行更大模型。

hackernews · minimaxir · 7月16日 20:18 · [社区讨论](https://news.ycombinator.com/item?id=48939662)

**背景**: LM Studio 是一款流行的桌面应用，允许用户本地发现、下载和运行大语言模型。现在它通过 Bionic 从聊天工具演变为智能体平台，能够使用开放模型自主执行任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic, a new AI agent app for ... - 9to5Mac</a></li>
<li><a href="https://lmstudio.ai/blog/introducing-lm-studio-bionic">Introducing LM Studio Bionic: the AI agent for open models</a></li>

</ul>
</details>

**社区讨论**: 创始人 Yagil 提供了免费额度供用户测试特定模型上的 Bionic。用户 inventor7777 称赞其在 Qwen3.6 35B 上的表现，但也指出一些粗糙之处。其他人讨论了与苹果的潜在竞争和企业用例，也有人对商业模式转变表示担忧。

**标签**: `#LM Studio`, `#AI agent`, `#open models`, `#local LLM`, `#coding`

---

<a id="item-5"></a>
## [Roc 编译器从 Rust 重写到 Zig](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

Roc 语言创始人 Richard Feldman 宣布，Roc 编译器正从 Rust 重写为 Zig，理由是 Zig 的低级内存控制和更快的构建速度。 这次重写凸显了系统编程中内存安全与底层控制之间的实际权衡，可能影响其他考虑从 Rust 转向 Zig 以提升性能的编译器项目。 重写针对 Roc 的编译器（当前生成机器码），利用了 Zig 的`ReleaseSafe`模式等功能，可在运行时捕获 use-after-free 错误。文章指出构建时间改进是主要因素。

hackernews · jorangreef · 7月16日 11:39 · [社区讨论](https://news.ycombinator.com/item?id=48933149)

**背景**: Roc 是 Richard Feldman 正在开发的一种快速、友好的函数式语言。Rust 以无需垃圾收集的内存安全著称，而 Zig 则通过放弃部分安全保证来优先实现底层控制和更快的编译。Roc 编译器最初用 OCaml 原型实现，然后改用 Rust 实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.roc-lang.org/">The Roc Programming Language</a></li>
<li><a href="https://github.com/roc-lang/roc">GitHub - roc-lang/roc: A fast, friendly, functional language. Docs | Roc roc/docs/mini-tutorial-new-compiler.md at main · roc-lang/roc The Complete Roc Guide: From Zero to Expert - kodikra The Rise of Roc: A Game-Changer in Functional Programming Understanding Roc: Functional and separate from the runtime</a></li>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**社区讨论**: 社区评论争论了编译器开发中安全担忧是否被夸大，有人质疑 Zig 的运行时检查，也有人称赞增量构建。用户对用 Rust 的安全性换取 Zig 的速度表达了复杂情绪。

**标签**: `#Rust`, `#Zig`, `#compiler`, `#Roc`, `#programming languages`

---

<a id="item-6"></a>
## [Thinking Machines Lab 发布开源权重模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Thinking Machines Lab 发布了 Inkling，一个拥有 9750 亿参数、基于 Apache 2.0 许可的开源权重混合专家多模态模型，在 45 万亿 token 的文本、图像、音频和视频数据上训练。 此次发布为美国开源模型生态系统增添了强有力的竞争者，可与中国的开源模型抗衡，并为微调提供了一个具有竞争力的基础，促进了 AI 研究的可访问性和定制化。 Inkling 共有 9750 亿参数，每个 token 激活 410 亿，采用混合专家架构，支持多模态（文本、图像、音频、视频）。较小的 Inkling-Small（2760 亿参数，120 亿激活）仍在测试中。

rss · Simon Willison · 7月16日 15:35

**背景**: 混合专家（MoE）是一种神经网络架构，将计算分散到多个专门的子网络（专家）中，每个输入只激活一部分专家，从而能用更低的计算成本构建更大的模型。开源权重模型允许任何人下载并对模型权重进行微调，促进了透明度和社区驱动的发展。Inkling 填补了前沿封闭模型与小型开源模型之间的空白，为定制化提供了一个强大的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**标签**: `#open-weights`, `#mixture-of-experts`, `#multimodal`, `#AI model`, `#Thinking Machines Lab`

---

<a id="item-7"></a>
## [Linus Torvalds 声明 Linux 不反对 AI](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linux 的创始人和顶级维护者 Linus Torvalds 公开声明，Linux 不是一个反 AI 的项目，AI 是一个明显有用的工具，并敦促反对者可以分叉项目或离开。 来自 Linux 内核社区最具影响力人物的权威声明可能改变关于 AI 在开源开发中作用的持续辩论的平衡，可能鼓励在内核开发中更广泛地采用 AI 工具。 Torvalds 在 Linux Media 邮件列表中发表了这一声明，强调虽然 AI 还有其他问题（比如其经济影响），但其有用性已不再存疑。他表示任何怀疑这一点的人实际上都没有使用过 AI。

rss · Simon Willison · 7月16日 13:26

**背景**: Linus Torvalds 是 Linux 内核的创建者和长期维护者，Linux 内核是最成功的开源项目之一。内核社区对于是否采用 AI 生成的代码或 AI 工具有过辩论，一些成员表达了对质量、许可和伦理问题的担忧。Torvalds 作为仁慈独裁者的地位使得他的声明在引导项目方向方面具有重要分量。

**标签**: `#linus-torvalds`, `#linux`, `#artificial-intelligence`, `#open-source`

---

<a id="item-8"></a>
## [QLoRA 默认学习率 2e-4 对小数据集是错误的](https://www.reddit.com/r/MachineLearning/comments/1uy1z8b/the_qlora_2e4_default_is_wrong_under_10k_samples/) ⭐️ 8.0/10

一位实践者发现，对于小于 1 万样本的数据集，广泛采用的 QLoRA 微调学习率 2e-4 并非最优；将学习率降至 1e-4 并增加训练轮数可显著提升评估性能。 许多教程和工具硬编码了 2e-4 的默认值，导致实践者在出现问题时归咎于数据或模型，而真正原因是超参数选择。这一见解可以为任何在小规模自定义数据集上进行微调的人节省数周的调试时间。 作者报告称，使用 2e-4 时模型在小数据集上在一个 epoch 内就过拟合，而降低到 1e-4 并训练 5 个 epoch 获得了最佳评估结果。他们提出一个规则：样本数超过 3 万时使用 2e-4，低于 1 万时从 1e-4 或更低开始，介于两者之间则进行调优。

reddit · r/MachineLearning · /u/Pretty-Ad774 · 7月16日 12:50

**背景**: QLoRA（量化低秩适配）是一种将量化与 LoRA 相结合的技术，可以在消费级 GPU 上高效微调大型语言模型。学习率是一个关键超参数；在小数据集上学习率过高可能导致过拟合。默认值 2e-4 源于 Alpaca 数据集（5.2 万样本），并被盲目复制到许多教程和代码库中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unsloth.ai/docs">Unsloth Docs | Unsloth Documentation</a></li>
<li><a href="https://github.com/artidoro/qlora">GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub</a></li>
<li><a href="https://lightning.ai/pages/community/lora-insights/">Finetuning LLMs with LoRA and QLoRA: Insights from Hundreds of Experiments - Lightning AI</a></li>

</ul>
</details>

**标签**: `#QLoRA`, `#fine-tuning`, `#learning rate`, `#small datasets`, `#machine learning`

---

<a id="item-9"></a>
## [ExTernD：实现高精度 LLM 量化的三元分解方法](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

该论文提出了 ExTernD，一种将权重矩阵分解为两个三元矩阵和一个对角缩放矩阵的后训练量化方法，通过增加秩实现任意高的精度，同时仅略微增加显存使用。 该方法通过扩展秩而不显著增加内存，解决了三元量化固有的精度损失问题，有望实现近乎无损精度的超高效 LLM 推理。 ExTernD 使用两个三元矩阵和一个内部分角缩放矩阵，内部秩可以任意大以达到目标精度；实验结果显示其显存仅略高于标准量化方法。

reddit · r/MachineLearning · /u/LMTLS5 · 7月16日 13:31

**背景**: 后训练量化（PTQ）通过将权重从浮点数转换为低位格式（如三元值{-1,0,1}）来减小模型大小并加速推理。然而，标准的三元量化常常导致大型语言模型（LLMs）的精度显著下降。ExTernD 通过分解权重矩阵并允许灵活的秩扩展克服了这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2211.10438">[2211.10438] SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2407.11534">[2407.11534] LRQ: Optimizing Post-Training Quantization for Large Language Models by Learning Low-Rank Weight-Scaling Matrices</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Quantization`, `#Post-training quantization`, `#Model efficiency`

---

<a id="item-10"></a>
## [知网将删除将 AI 列为作者的论文](https://www.zaobao.com.sg/news/china/story20260716-9371836) ⭐️ 8.0/10

中国最大的学术平台知网宣布，将下架那些将 DeepSeek、Gemini 等 AI 工具列为作者的论文，并明确 AI 不能对科研诚信负责。 这一政策明确了 AI 不能作为学术出版物的作者，回应了关于科研问责和诚信的日益增长的担忧，并为全球其他学术平台和出版商树立了先例。 知网强调，AI 不具备民事主体资格，无法承担论文真实性、学术核查和追责等责任；若在研究或写作中使用 AI，作者应在研究方法或致谢中说明。

telegram · zaihuapd · 7月16日 07:45

**背景**: 知网（中国国家知识基础设施）是中国主要的学术数据库，收录期刊、学位论文和会议论文。DeepSeek 是一款引起关注的中国 AI 模型。生成式 AI 的兴起导致了一些将 AI 列为共同作者的投稿，引发了关于作者身份和伦理的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CNKI">CNKI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI authorship`, `#academic publishing`, `#CNKI`, `#policy`, `#DeepSeek`

---

<a id="item-11"></a>
## [欧盟裁定谷歌开放安卓与搜索数据给竞争对手](https://www.theverge.com/policy/966438/eu-google-android-ai-interoperability-search-data-dma) ⭐️ 8.0/10

欧盟委员会根据《数字市场法》裁定，谷歌必须向符合条件的竞争对手开放部分安卓系统功能和谷歌搜索数据。第三方 AI 助手（如 ChatGPT、Claude）将获得与谷歌 Gemini 同等的系统权限和数据访问。 这一裁决迫使谷歌向竞争对手分享其严格控制的平台，可能彻底重塑移动生态和 AI 助手领域的竞争格局。它为 DMA 下的守门人平台如何为新兴 AI 服务实现互操作设定了先例。 谷歌仍可依据隐私和安全标准评估访问申请，但相关限制须符合欧盟规定。该裁决仅适用于安卓和谷歌搜索，不涉及其他谷歌服务，且基于 DMA 对守门人平台的互操作义务。

telegram · zaihuapd · 7月16日 13:19

**背景**: 《数字市场法》（DMA）是欧盟针对大型在线平台（指定为“守门人”）的法律，要求它们确保数字市场公平开放。谷歌（Alphabet）于 2023 年 9 月被指定为守门人，涉及安卓和搜索等服务。DMA 规定守门人必须在特定条件下允许第三方与其核心平台服务互操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_Markets_Act">Digital Markets Act - Wikipedia</a></li>
<li><a href="https://digital-markets-act.ec.europa.eu/index_en">Digital Markets Act (DMA) - European Union</a></li>

</ul>
</details>

**标签**: `#欧盟`, `#数字市场法`, `#谷歌`, `#Android`, `#AI助手`

---

<a id="item-12"></a>
## [1Password 集成 Claude，AI 登录无需密码](https://9to5mac.com/2026/07/16/1password-now-lets-claude-sign-in-to-websites-without-seeing-your-passwords/) ⭐️ 8.0/10

1Password 在 Mac 端推出与 Claude 的集成，允许 AI 代理代为登录网站，而密码和二次验证码完全不会被 Claude 获取。凭证通过安全通道直接注入网页，用户需通过生物识别逐条审批当前任务所需的登录项。 这一集成将密码管理与 AI 自动化结合，同时保持了强大的隐私保障，因为凭证绝不会进入 Claude 的上下文或记忆。它可能为需要自动化重复登录的用户（如测试或数据录入）简化工作流程，且不损害安全性。 该功能目前面向 Mac 端的 1Password 商业、家庭及个人版用户开放，需同时安装 1Password 与 Claude 的桌面及浏览器扩展。如果自动填充后提交失败，已填写的内容会立即被擦除，权限仅限于当前会话。

telegram · zaihuapd · 7月16日 15:54

**背景**: 1Password 是一款流行的密码管理器，将登录凭证和其他敏感数据存储在加密保管库中。Claude 是 Anthropic 开发的 AI 助手。该集成允许 Claude 作为代理代表用户执行登录，但通过安全通道确保 AI 永远不会看到实际的密码或二次验证码，解决了 AI 代理访问敏感数据时的常见隐私担忧。

**标签**: `#password management`, `#AI integration`, `#security`, `#Claude`, `#1Password`

---

<a id="item-13"></a>
## [Truth Social 将向华尔街出售特朗普帖子的快速访问权限](https://www.cnn.com/2026/07/16/business/truth-social-data-wall-street) ⭐️ 8.0/10

特朗普媒体科技集团宣布推出 Truth API，这项数据服务将以毫秒级延迟提供 Truth Social 上排名前 10 账号的实时帖子，自 2026 年 8 月 1 日起向机构投资者开放。 该服务可能为高频交易者提供信息优势，因为特朗普的帖子曾因关税、伊朗等议题引发市场波动，这引发了将总统通讯货币化以牟利的伦理担忧。 该 API 面向机构金融客户，定价尚未公布；它仅提供前 10 个账号的访问权限，TMTG 将其视为从其专有数据中获取高利润经常性收入的来源。

telegram · zaihuapd · 7月17日 01:02

**背景**: Truth Social 已成为特朗普发布政策声明的主要渠道，他关于关税、伊朗及霍尔木兹海峡的帖子曾引发股市和油市剧烈波动。高频交易（HFT）利用算法在毫秒级内执行交易，通常从微小的价格变化中获利。实时获取影响市场的帖子与 HFT 的结合可能加剧波动性并引发公平性担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/16/trump-truth-social-wall-street-traders-api.html">Truth Social launches service to give Wall Street traders an ...</a></li>
<li><a href="https://marketchameleon.com/articles/b/2026/7/16/trump-media-launches-truth-api-institutional-market-impact">Trump Media Unveils Truth API: Real-Time Access to ...</a></li>

</ul>
</details>

**标签**: `#Truth Social`, `#API`, `#Wall Street`, `#high-frequency trading`, `#ethics`

---