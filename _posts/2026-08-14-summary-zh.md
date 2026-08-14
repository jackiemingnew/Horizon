---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 33 条内容中筛选出 11 条重要资讯。

---

1. [GLM-5.3 发布展示涌现的网络能力](#item-1) ⭐️ 9.0/10
2. [Qwen 3.8 27B 模型凭借高效能与强劲性能备受好评](#item-2) ⭐️ 8.0/10
3. [RustDesk 为 Wayland 带来真正的无人值守远程访问](#item-3) ⭐️ 8.0/10
4. [为何 Claude Opus 5 的省略式文风让人用起来更糟](#item-4) ⭐️ 8.0/10
5. [编译器将《毁灭战士》渲染器变成 21B 参数 Transformer](#item-5) ⭐️ 8.0/10
6. [torch-preflight：面向 PyTorch 代码和显存估算的新 linter 工具](#item-6) ⭐️ 8.0/10
7. [AI 机器人实验室年测 300 万人体组织样本，或淘汰动物测试](#item-7) ⭐️ 8.0/10
8. [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](#item-8) ⭐️ 8.0/10
9. [法官责令谷歌一周内放宽第三方应用商店安装限制](#item-9) ⭐️ 8.0/10
10. [PostgreSQL 修复 to_char 高危堆溢出漏洞，可执行任意代码](#item-10) ⭐️ 8.0/10
11. [苹果携手阿里自研中国专属 AI 模型](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM-5.3 发布展示涌现的网络能力](https://z.ai/blog/glm-5.3) ⭐️ 9.0/10

Z.ai 发布了 GLM-5.3，这是其最新的旗舰模型，基于与 GLM-5.2 相同的基础模型，所有改进均来自后训练。该模型在编程、长时程任务方面表现出显著提升，并据称涌现出漏洞发现与利用等网络能力。 此次发布意义重大，因为它表明后训练可以解锁意想不到的能力，引发了对 AI 安全与网络安全的重要关切。该模型涌现出的网络技能可能影响组织进行漏洞研究和红队演练的方式，同时加剧前沿 AI 实验室之间的竞争。 GLM-5.3 采用 MIT 开源许可证，拥有 100 万 token 的上下文窗口。社区用户报告称，它在红队演练中成功发现了 WP 插件中的 0day 漏洞、实现了 RCE 利用以及内核漏洞适配；Z.ai 还在 cvd.z.ai 建立了漏洞披露页面。

hackernews · pella · 8月14日 05:19 · [社区讨论](https://news.ycombinator.com/item?id=49294997)

**背景**: 大型语言模型（LLM）通过预测文本来训练，但随着规模扩大，它们可能展现出“涌现能力”——即未被明确训练却意外出现的能力。后训练是指在基础模型训练完成之后进行的微调和对齐技术，如今已成为竞争性 AI 模型的关键差异点。GLM-5.3 与 GLM-5.2 使用相同的基础模型，因此其新能力完全来自后训练阶段，这说明了在不重新训练基础模型的情况下可以取得多大的进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM-5.3 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://openlm.ai/glm-5.2/">GLM-5.3 - openlm.ai</a></li>
<li><a href="https://kingy.ai/blog/glm-5-3-specs-benchmarks-api-how-to-use/">GLM-5.3 Just Launched: Specs, Benchmarks, API & How to Use It</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论总体积极且热烈，用户称赞该模型的性能和 Z.ai 的写作风格。一些用户分享了令人印象深刻的红队结果，另一些用户则对大规模漏洞扫描和负责任披露表示担忧，指出 Anthropic 的 Project Glasswing 等模型也能发现这些问题。还有评论者将 GLM-5.3 与 Sol、Fable 和 Mythos 5 等其他前沿模型进行比较，认为它已接近领先基准，但仍不是从现有提供商切换的充分理由。

**标签**: `#AI`, `#Cybersecurity`, `#LLM`, `#GLM`, `#Vulnerability Research`

---

<a id="item-2"></a>
## [Qwen 3.8 27B 模型凭借高效能与强劲性能备受好评](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

阿里巴巴 Qwen 团队发布了 Qwen3.8-27B，这是一个拥有 270 亿参数的开源模型，具备出色的基准测试成绩和高效的本地运行能力。在部分编程和推理测试中，其成绩可与更大规模商业系统匹敌甚至超越。 这次发布意义重大，因为它表明小型高效模型能挑战昂贵的大规模 AI，降低了开发者和研究者的使用门槛。由于能在笔记本和消费级 GPU 上流畅运行，它有望扩大前沿 AI 的普及范围，并减少对昂贵云端 API 的依赖。 根据社区测试，Qwen3.8-27B 在 DeepSWE 上以 42.2 比 40 的成绩击败了 Opus 4.7 Max（配合 Claude Code）。Unsloth 已发布 GGUF 量化版本，用户已在笔记本和 RTX 4090 显卡上运行该模型，效果令人满意。

hackernews · erdaltoprak · 8月14日 15:00 · [社区讨论](https://news.ycombinator.com/item?id=49299605)

**背景**: Qwen 是阿里云的开源大语言模型系列，许多模型采用 Apache 2.0 等宽松许可证发布。在大语言模型中，参数是决定模型行为的已学习数值权重，因此 27B 模型拥有 270 亿个这样的权重；较小的参数规模通常意味着更低的硬件要求和更快的推理速度，但如果架构不佳，质量也可能受到影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://huggingface.co/Qwen">Org profile for Qwen on Hugging Face, the AI community building the...</a></li>
<li><a href="https://jbu.io/2025/10/20/understanding-llm-parameters/">Understanding LLM Parameters</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，Simon Willison 等用户称赞模型能在笔记本上生成准确图像，还有用户强调其高效性。虽然有些人质疑它是否真正能与 Opus 相比，但许多人更看重速度和成本，也有部分人期待同样规模的 MoE 新模型。

**标签**: `#AI`, `#Machine Learning`, `#LLM`, `#Qwen`, `#Open Source`

---

<a id="item-3"></a>
## [RustDesk 为 Wayland 带来真正的无人值守远程访问](https://rustdesk.com/blog/unattended-remote-access-wayland/) ⭐️ 8.0/10

RustDesk 在其新发布的博客文章中宣布支持 Wayland 上的真正无人值守远程访问。这意味着 Linux 用户现在可以远程连接到基于 Wayland 的机器并在无人交互确认的情况下控制它。 这填补了 Linux 远程桌面用户长期面临的一个空白，因为 Wayland 的安全模型让无人值守远程访问比旧的 X11 系统困难得多。同时也巩固了 RustDesk 作为 TeamViewer、AnyDesk 等专有工具的开源替代品的地位。 Wayland 是一种定义显示服务端（合成器）与客户端之间通信的协议，因此远程桌面实现方式与旧 X11 模型不同。官方博客将此功能称为“真正的”无人值守访问，暗示此前 Wayland 上的连接仍需要某种形式的交互式确认。

hackernews · rustdesk · 8月14日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=49300759)

**背景**: RustDesk 是一款开源远程桌面软件，支持 Windows、macOS、Linux 和 Android，并可通过自建服务器使用，是 TeamViewer、AnyDesk 等专有产品的替代方案。Wayland 是一种旨在取代 Linux 及其他类 Unix 操作系统上 X11 窗口系统的通信协议，使用该协议的显示服务端被称为 Wayland 合成器。无人值守远程访问允许设备在无人现场接受连接请求的情况下被远程访问，同时仍然执行身份验证和访问控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustdesk.com/">RustDesk: Open-Source Remote Desktop with Self-Hosted Server ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wayland_(display_server_protocol)">Wayland (display server protocol)</a></li>
<li><a href="https://www.manageengine.com/remote-desktop-management/unattended-remote-access.html">Free Unattended Remote Access Software - ManageEngine Remote ...</a></li>

</ul>
</details>

**社区讨论**: 评论区中，有用户询问 RustDesk 是否支持从客户端到主机的话筒音频透传，也有人指出一个关于自建服务器连接未加密的 GitHub issue。还有用户将 RustDesk 与 VNC 以及基于 SSH 的解决方案（如通过 Tailscale 使用 Remmina）进行比较，并有人询问它和 VNC 有何区别。总体来看，讨论体现出浓厚兴趣，同时也暴露出对功能完整性和安全性的担忧。

**标签**: `#Remote Desktop`, `#Wayland`, `#RustDesk`, `#Open Source`, `#Linux`

---

<a id="item-4"></a>
## [为何 Claude Opus 5 的省略式文风让人用起来更糟](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) ⭐️ 8.0/10

一篇新博客文章及其 Hacker News 讨论对 Claude Opus 5 的沟通风格提出批评，认为该模型虽然能力更强，但省略式表达、过多的元对话和无益的批评使其使用体验更差。用户表示已换回 Opus 4.8 或改用 OpenAI 的 Sol 模型，以摆脱令人疲惫的交互。 这一批评凸显了模型能力并非决定 LLM 可用性的唯一因素，沟通风格会显著影响用户满意度和工作效率。随着 AI 模型深入日常工作流程，Anthropic 等提供商在追求基准分数的同时，也必须考虑语气和清晰度，以留住用户。 具体抱怨包括句子绕圈后才落回要点、为了变换动词而常用无生命名词作主语，以及不断出现“说实话”“承认错误”之类的自我评论。部分用户承认 Opus 5 在工程问题解决上更出色，但觉得它过于挑剔，且在没有严格限定指令时容易偏离主题，因此写文章时更愿意用 Opus 4.8。

hackernews · numeri · 8月14日 10:12 · [社区讨论](https://news.ycombinator.com/item?id=49296740)

**背景**: Claude Opus 5 是 Anthropic 的旗舰大语言模型，专注于高难度的编程、推理和长周期智能体（agentic）任务。尽管它在基准测试中表现出色，但用户通过自然语言与其交互，因此其写作风格直接决定了使用体验。近期关于 AI 生成文本的讨论已识别出省略式表达和元对话等模式，即模型绕弯子或对自己的思考过程作评论，读起来容易让人疲倦。该新闻正是将这些已知问题用于对 Opus 5 的专门批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5">Claude Opus 5 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing">Wikipedia:Signs of AI writing - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论区普遍认同这一批评，称 Opus 5 的写作组织过于绕弯、过度道歉且批评无益。部分用户表示已换回 Opus 4.8 或改用 OpenAI 的 Sol 模型，但同时承认 Opus 5 的问题解决能力更强。还有人怀疑该模型实际上更小或更省成本，基准分数的提升主要是营销手段。

**标签**: `#AI`, `#LLM`, `#UX`, `#Claude`, `#Model Critique`

---

<a id="item-5"></a>
## [编译器将《毁灭战士》渲染器变成 21B 参数 Transformer](https://www.reddit.com/r/MachineLearning/comments/1voazhm/i_compiled_dooms_renderer_into_a_21bparameter/) ⭐️ 8.0/10

一个名为 Torchwright 的自定义编译器将《毁灭战士》的渲染算法转换为一个 21B 参数的 transformer 检查点，该检查点生成像素绘制命令来渲染 E1M1 关卡画面，全程无需训练。在 NVIDIA B200 上生成一帧约需 40 分钟，而原版《毁灭战士》在 486 处理器上能达到 35 FPS。 这展示了一种新颖的方法：将任意算法直接编译成 transformer 权重，而不是通过训练来学习。它拓展了 transformer 作为可编程机器的能力边界，并为验证和解释模型行为开辟了新可能性。 宿主程序只有 43 行 Python 代码；计算图本身要长得多，但会被编译进 transformer 内部。单帧渲染包含 3,614 个 token 的提示和 53,747 个生成的 token，在 B200 上大约每天只能渲染 35 帧。

reddit · r/MachineLearning · /u/notforrob · 8月14日 15:50

**背景**: Transformer 是一种神经网络架构，通过关注输入的不同部分来处理序列。通常，其权重是在大型数据集上训练得到的，而 Torchwright 则是先构造一个固定的计算图，再直接算出 transformer 的权重，使模型执行该计算图。《毁灭战士》的渲染器是负责从场景数据绘制 3D 世界的软件，因此它是一个被编译进权重的复杂程序。最终生成的检查点是标准的 Hugging Face 模型，无需特殊代码即可加载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ood.dev/posts/calculator/">A calculator, compiled into a transformer — Out of Distribution</a></li>
<li><a href="https://towardsdatascience.com/i-built-a-tiny-computer-inside-a-transformer/">I Built a Tiny Computer Inside a Transformer | Towards Data Science</a></li>
<li><a href="https://medium.com/data-science-collective/i-built-a-tiny-computer-inside-a-transformer-e3000a0019b3">I Built a Tiny Computer Inside a Transformer | by Sean Moran | Data Science Collective | Medium</a></li>

</ul>
</details>

**标签**: `#transformers`, `#compiler`, `#doom`, `#neural networks`, `#machine learning`

---

<a id="item-6"></a>
## [torch-preflight：面向 PyTorch 代码和显存估算的新 linter 工具](https://www.reddit.com/r/MachineLearning/comments/1vo8vv0/a_linter_for_pytorch_torchpreflight_p/) ⭐️ 8.0/10

开发发布了 torch-preflight，这是一个静态分析工具，无需导入或执行代码就能捕捉常见的 PyTorch 编码错误，并估算显存占用。该工具可通过 pip install torch-preflight 安装，目前实现了 13 条 lint 规则。 PyTorch 训练失败常常浪费昂贵的 GPU 机时，而该工具的目标是在工作流早期就抓住这些坑。通过将 lint 检查与显存估算相结合，它帮助开发者及团队避免昂贵的试错成本，并优化资源利用率。 该工具通过静态分析进行校验，因此无需 GPU 或安装 PyTorch 即可使用。在单块 T4 上对四个模型进行测试，显存估算值与实测峰值误差在 4%以内；工具还会列出可让运行适配目标 GPU 的代码修改建议，并给出每项修改可节省的 GiB。

reddit · r/MachineLearning · /u/LeJanbandhu · 8月14日 14:30

**背景**: PyTorch 使用 autograd 构建动态计算图，以跟踪运算并实现自动微分。常见的错误例如跨迭代保存损失张量，会让整个计算图被保留直到 GPU 内存耗尽；而忘记调用 zero_grad()会导致梯度累积错误。在分布式训练中，DistributedSampler 确保各进程（rank）看到不同的数据，torch-preflight 会检查此类模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html">A Gentle Introduction to torch.autograd — PyTorch Tutorials 2 ...</a></li>
<li><a href="https://github.com/pytorch/pytorch/blob/main/torch/utils/data/distributed.py">pytorch/torch/utils/data/distributed.py at main · pytorch/pytorch</a></li>

</ul>
</details>

**标签**: `#PyTorch`, `#linter`, `#debugging`, `#machine learning`, `#GPU`

---

<a id="item-7"></a>
## [AI 机器人实验室年测 300 万人体组织样本，或淘汰动物测试](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 8.0/10

位于旧金山南部的生物科技初创公司 Vivodyne 已将其 AI 机器人实验室规模化，每年可开展超过 300 万次受控人体组织实验。该系统的 12 个"蜂巢"实验室可测试活体人体组织，容量是美国全部临床试验总和的两倍。 如果该平台得到验证，将极大加速药物研发，并减少对动物实验的依赖——目前约 90%的临床试验在通过动物测试后仍告失败。它还能生成海量人体生物学数据，用于训练人类生物学 AI 模型，从而变革药物开发方式。 据 Helena 项目页面介绍，Vivodyne 的机器人平台可同时测试超过 1 万个独立的人体组织。该公司称其实验室培养的组织与活体人体组织无异，并能生成表型组、转录组和蛋白质组等多维度数据，为构建首个人类生物学世界模型提供基础。

telegram · zaihuapd · 8月14日 01:48

**背景**: 候选药物在进入人体试验前通常先在动物身上测试，但动物模型往往无法预测人体反应——约 90%的临床药物在动物实验中表现良好后仍遭失败。人体组织工程和器官芯片技术旨在提供更接近生理状态的测试方式，而 AI 可将实验设计与分析自动化、规模化。Vivodyne 将自主机器人、实验室培养的 3D 人体组织与 AI 相结合，构建高通量测试平台，以生成与人体相关的数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vivodyne.com/">Vivodyne | Make biology computable</a></li>
<li><a href="https://www.helena.org/projects/vivodyne/">Vivodyne | Helena</a></li>
<li><a href="https://www.businesswire.com/news/home/20260812148428/en/Vivodyne-Launches-the-Worlds-Largest-Human-Biological-Datacenter-to-Train-the-First-World-Model-of-Human-Biology">Vivodyne Launches the World’s Largest Human Biological Datacenter...</a></li>

</ul>
</details>

**标签**: `#AI`, `#biotechnology`, `#drug discovery`, `#robotics`, `#animal testing`

---

<a id="item-8"></a>
## [小红书开源 dots3-note：280B MoE 仅 16B 激活参数](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

小红书 dots 实验室发布了 dots3-note preview，这是 dots3 系列首个开放权重模型，权重已上线 Hugging Face。这个 280B 参数的混合专家模型每次仅激活 16B 参数，支持 512K 上下文，可处理文字、图片、视频和音频，并引入了新的 TEMPO 强化学习方法和两个智能体基准。 这是一个重要的开放权重发布：280B 的超大规模 MoE 骨干仅需 16B 激活参数即可完成推理，大幅降低了前沿模型的使用门槛。同时它引入了用于长程智能体的 TEMPO 强化学习方法和真实场景基准，有望缩小智能体在测试与真实使用之间的表现差距。 该模型是多模态 MoE，可在 512K 词元的上下文中处理文字、图片、视频和音频。据公告，TEMPO 通过自批判和测试时价值估计来训练智能体；此次发布还包含 VibeSearchBench，它由 200 个双语长程搜索任务组成，采用用户人设驱动、逐步揭示信息需求，并以无固定模式（schema-free）的知识图谱进行评测。

telegram · zaihuapd · 8月14日 08:27

**背景**: 混合专家（MoE）模型拥有大量专用参数，但每个 token 只经过其中一部分，因此模型可以做到“总参数 280B、激活参数仅 16B”。这种结构能在不按比例提高推理成本的情况下扩大训练规模。VibeSearchBench 的推出是因为现有搜索基准往往使用过度明确的查询、单轮交互和固定模式的评测，不符合现实中用户与智能体协作、逐步明确意图的搜索行为。开放权重模型让研究者和开发者可以直接检查、微调并自托管模型，而无需依赖封闭 API。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://vibebench.github.io/VibeSearchBench.github.io/">VibeSearchBench — Benchmarking Long-horizon Proactive Search ...</a></li>
<li><a href="https://arxiv.org/abs/2605.27882">[2605.27882] VibeSearchBench: Benchmarking Long-horizon ...</a></li>

</ul>
</details>

**标签**: `#MoE`, `#Open-Source`, `#LLM`, `#Reinforcement Learning`, `#Multimodal`

---

<a id="item-9"></a>
## [法官责令谷歌一周内放宽第三方应用商店安装限制](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 8.0/10

美国地区法官詹姆斯·多纳托(James Donato)下令谷歌移除阻止直接安装第三方安卓应用商店的多余警告和步骤，并要求在一周内完成。该指令是 Epic 诉 Google 案补救措施的一部分，此前陪审团认定谷歌在安卓应用分发领域构成非法垄断。 该裁决可能重塑安卓应用分发格局，让用户更容易安装替代应用商店，从而增强竞争并降低开发者的准入门槛。它直接执行了对谷歌的反垄断判决，并可能影响安卓在全球范围内处理侧载(sideloading)的方式。 法院特别指出谷歌的多步骤‘吓阻页面’——例如要求用户先点击‘查看详情’页面后‘安装’按钮才会出现——是蓄意制造的‘反竞争摩擦’。谷歌必须让安装第三方商店像安装普通安卓应用一样直接简单。

telegram · zaihuapd · 8月14日 09:55

**背景**: Epic Games(堡垒之夜开发商)于 2020 年起诉谷歌，指控其在 Play 商店中存在垄断行为，包括与制造商和开发商签订限制性协议。2023 年，陪审团裁定谷歌在安卓应用分发和应用内支付市场构成非法垄断，第九巡回上诉法院后来维持了该判决。侧载——即从官方商店之外安装应用——在安卓上被允许，但谷歌添加了警告和额外步骤，法院认为这些设计意在阻止用户。今天的指令正是为消除这种反竞争摩擦而采取的补救措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Epic_Games_v._Google">Epic Games v. Google - Wikipedia</a></li>
<li><a href="https://www.mintz.com/insights-center/viewpoints/2025-08-06-ninth-circuit-upholds-jury-verdict-against-and-remedies">Ninth Circuit Upholds Jury Verdict Against and Remedies Imposed Upon Google in Epic Games Monopolization Antitrust Suit | Mintz</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#Google`, `#Android`, `#app stores`, `#legal`

---

<a id="item-10"></a>
## [PostgreSQL 修复 to_char 高危堆溢出漏洞，可执行任意代码](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL 披露了 CVE-2026-14669，这是 to_char(timestamptz) 函数中的一个堆缓冲区溢出漏洞，攻击者可利用特制的 POSIX 时区缩写以低权限数据库账户执行任意代码。修复版本计划为 18.6、17.11、16.15、15.19 和 14.24，其中 18.5 因回归问题被跳过。 该漏洞 CVSS 评分为 8.8，可能导致服务器完全沦陷：攻击者仅需一个低权限数据库账户，就能以 PostgreSQL 服务进程的操作系统权限执行任意代码。由于所有受支持的 PostgreSQL 版本均受影响，生产环境必须立即打补丁。 该溢出发生在 to_char() 处理超长的 POSIX 时区缩写（针对带时区的时间戳值）时。此次小版本更新不需要转储数据库或运行 pg_upgrade，只需更新程序文件并重启服务即可。

telegram · zaihuapd · 8月14日 14:35

**背景**: 堆缓冲区溢出是指程序向堆分配的内存缓冲区写入超出其容量的数据，可能导致内存损坏，甚至被利用来执行任意代码。PostgreSQL 的 to_char() 函数可将时间戳、间隔和数值转换为格式化字符串，而 POSIX 时区规范使用类似 EST5EDT 的字符串定义时区。精心构造的时区字符串可触发溢出，使已认证用户提升权限。虽然 ASLR 等现代缓解措施会提高利用难度，但该漏洞依然非常危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://orbisappsec.com/blog/heap-buffer-overflow-in-darktables-color-chart-how">Heap Buffer Overflow in darktable's Color | Orbis AppSec</a></li>
<li><a href="https://www.postgresql.org/docs/current/datatype-datetime.html">PostgreSQL: Documentation: 18: 8.5. Date/Time Types</a></li>
<li><a href="https://www.postgresql.org/docs/current/datetime-posix-timezone-specs.html">PostgreSQL: Documentation: 18: B.5. POSIX Time Zone Specifications</a></li>

</ul>
</details>

**标签**: `#postgresql`, `#security`, `#cve`, `#vulnerability`, `#database`

---

<a id="item-11"></a>
## [苹果携手阿里自研中国专属 AI 模型](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 8.0/10

苹果已在中国市场专门训练了一款大语言模型，并获得阿里巴巴支持，改变了此前依赖第三方 AI 模型的策略。Apple Intelligence 预计在未来数月随 iOS 更新在华上线，且苹果的生成式 AI 服务已在中国网信办完成备案，苹果或将成为首家获准在华提供自有 AI 模型的外国公司。 这标志着苹果在华 AI 战略的重大转变，使公司能更好地掌控中国市场的 AI 体验，同时应对中国严格的监管要求。若获批，苹果将为其他寻求在华提供自有 AI 服务的外国科技公司开创先例，重塑与百度、阿里、字节跳动等本土厂商的竞争格局。 据路透社报道，苹果专门为中国市场训练了这一模型，并获得阿里巴巴支持；中国网信办已于上月对苹果的生成式 AI 服务进行备案。另有博客文章指出，该备案编号为 Shanghai-AppleZhiNeng-202506160057，于 2026 年 7 月 15 日公布，结束了近两年的监管停滞期。

telegram · zaihuapd · 8月14日 14:47

**背景**: Apple Intelligence 是苹果在 2024 年 6 月发布的一套 AI 功能，集成于 iOS、iPadOS 和 macOS，包括写作工具、图像生成、通知摘要以及 ChatGPT 集成。根据中国的《生成式人工智能服务管理暂行办法》，在中国境内向公众提供生成式 AI 服务需要向网信办备案，外国公司还需面对更严格的审查。苹果此前在中国市场依赖第三方模型，如今则与阿里巴巴合作自研模型，以更好地符合本地法规并保持对用户体验的掌控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence</a></li>
<li><a href="https://sftpmac.com/en/blog/20260716-apple-intelligence-china-approved-qwen-baidu-decision-guide.html">2026 Apple Intelligence Approved in China : Qwen + Baidu... | SFTPMAC</a></li>
<li><a href="https://www.twobirds.com/en/insights/2023/china/what-you-need-to-know-about-china’s-new-generative-ai-measures">What You Need to Know About China ’s New Generative AI Measures</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#regulatory`

---