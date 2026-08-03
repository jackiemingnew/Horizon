---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 34 条内容中筛选出 14 条重要资讯。

---

1. [Qwen 发布 3.8-Max：2.4 万亿参数模型，下周开源权重](#item-1) ⭐️ 9.0/10
2. [为何 LLM 更青睐领域专家](#item-2) ⭐️ 8.0/10
3. [OpenAI 盘点数学与理论计算机科学中的十项 AI 进展](#item-3) ⭐️ 8.0/10
4. [文章主张：开发者工具必须开源，AI 代理才能直接修改维护](#item-4) ⭐️ 8.0/10
5. [ComfyUI 即日支持 MiniMax H3：开放权重、原生音频与 2K 视频](#item-5) ⭐️ 8.0/10
6. [数据库研究员 Andy Pavlo 加入 ClickHouse，创立 ClickHouse Labs](#item-6) ⭐️ 8.0/10
7. [Jane Street 开源基于 OCaml 的 UI 库 Bonsai](#item-7) ⭐️ 8.0/10
8. [Rust 项目目标：不可移动类型和保证析构函数](#item-8) ⭐️ 8.0/10
9. [SQLite 严重 CVE 还是 LLM 垃圾信息？](#item-9) ⭐️ 8.0/10
10. [Kimi K3 架构深度解析：压缩记忆与潜在专家路由](#item-10) ⭐️ 8.0/10
11. [美国犯罪实验室 DNA 设备曝漏洞，30 年证据面临篡改风险](#item-11) ⭐️ 8.0/10
12. [美 50 名警员被控滥用车牌摄像头窥探前任](#item-12) ⭐️ 8.0/10
13. [英伟达 170HX 矿卡被破解：显存解锁至 80GB，二手价暴涨](#item-13) ⭐️ 8.0/10
14. [苹果就英国 iCloud 后门要求提起法律挑战](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen 发布 3.8-Max：2.4 万亿参数模型，下周开源权重](https://qwen.ai/blog?id=qwen3.8) ⭐️ 9.0/10

Qwen 于 2026 年 3 月 4 日发布了其迄今最强的模型 Qwen 3.8-Max，总参数达 2.4 万亿，激活参数为 950 亿。模型权重将于下周开源，这是 Qwen 首次对外开源 Max 级别模型的权重。 这是开源大模型生态的一个里程碑事件：Qwen 的 Max 级模型此前一直闭源，此次开源将极大降低开发者和研究者获取前沿规模能力的门槛。2.4 万亿参数的稀疏 MoE 规模，以及在编码和长周期任务上的强劲表现，可能重塑开源权重模型之间的竞争格局。 Qwen 3.8-Max 基于 Qwen 3.5 架构，该架构结合了 Gated DeltaNet 与稀疏混合专家（MoE）路由。在编码测试中，模型可自主运行超过 10 天完成项目构建与自我进化，并在 24 小时内参加 WWW2025 多模态对话意图识别竞赛，击败了 526 支队伍中的 458 支；目前模型已通过 QwenCloud 提供 API 服务。

telegram · zaihuapd · 8月3日 02:31

**背景**: 混合专家（Mixture of Experts, MoE）是一种神经网络技术，将模型拆分为多个专门的子模型（即“专家”），并在每次输入时仅激活其中一小部分，从而在保持可承受计算成本的同时实现超大参数量。Qwen 3.5 引入了混合架构，将 Gated Delta Network（一种线性注意力机制）与稀疏 MoE 路由相结合，扩展了上下文长度并提高了推理效率。目前主流大模型供应商（包括 GPT-4、DeepSeek、Mistral 等）都在其大规模模型中采用了某种形式的 MoE 架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://trilogyai.substack.com/p/deep-dive-qwen-35-brings-native-multimodality">[Deep Dive] Qwen 3.5 Brings Native Multimodality and Long Context to Small Open Models</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-0.8B">Qwen/Qwen3.5-0.8B · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Qwen`, `#Open Source`, `#Model Release`

---

<a id="item-2"></a>
## [为何 LLM 更青睐领域专家](https://www.seangoedecke.com/llms-reward-expertise/) ⭐️ 8.0/10

肖恩·格德克（Sean Gedecke）的文章认为，大语言模型（LLM）对已有深厚领域知识的用户格外有利，因为专家能更好地引导、验证并基于 AI 输出进行构建。该文挑战了“LLM 能让新手与专家平起平坐”的常见假设。 这一观点很重要，因为它反驳了“LLM 使专业知识民主化”的说法；相反，LLM 可能拉大专家与新手之间的生产力差距。这对软件工程及其他知识密集型领域应用 AI 具有直接影响。 文章以技术短板（如 CSS）为例，说明 AI 能填补知识缺口，但也可能妨碍深入学习。社区评论补充了更多细节，指出提示词风格以及向模型“表明专家身份”会显著影响输出质量。

hackernews · MaxMussio · 8月3日 21:13 · [社区讨论](https://news.ycombinator.com/item?id=49161518)

**背景**: 大语言模型是一种基于海量文本训练的人工智能系统，能根据提示生成回答。常见说法是它们能让任何人随意提问，从而降低专业知识门槛；但这篇文章认为恰恰相反：要有效使用模型，需要先具备相关知识来引导模型、判断其输出，并将其整合到专业工作之中。讨论中还提到“放大镜”类比，即 LLM 会反映用户自身的认知与表述框架。

**社区讨论**: 评论总体表示支持，但也带有保留。有用户质疑文章核心论点，举出 Anthropic 一位数学家的提示词其实很简单；也有用户强调要向模型“表明专家身份”（比如说明自己的学术背景），这会显著改变回答质量。还有用户用“放大镜”类比：LLM 会放大用户自身的思考，因此谨慎的专家用户受益，而把它当作大脑替代品的人则不会。

**标签**: `#LLMs`, `#AI productivity`, `#expertise`, `#software engineering`, `#human-AI interaction`

---

<a id="item-3"></a>
## [OpenAI 盘点数学与理论计算机科学中的十项 AI 进展](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 8.0/10

OpenAI 发布了一篇题为《数学与理论计算机科学中的十项进展》的综述文章，重点介绍近期人工智能和大语言模型加速数学问题求解与定理证明发现的成果。由于所提供的内容未列出具体进展，但整体与自动定理证明和证明助手的趋势一致。 这篇综述的意义在于，它表明一家重要 AI 实验室将严谨数学视为大语言模型的关键前沿，可能重塑定理发现和验证的方式。如果这一趋势持续，AI 辅助证明工具将影响数学家、计算机科学家以及依赖形式验证的领域。 这篇文章是一份精选综述，而非单一新突破，且现有内容并未逐一列出这十项进展。社区讨论指出，现有模型擅长通过大量计算处理证明和反驳猜想，但仍然缺乏人类形成猜想所需的直觉。

hackernews · milkshakes · 8月3日 16:27 · [社区讨论](https://news.ycombinator.com/item?id=49157930)

**背景**: 自动定理证明(ATP)是自动推理的一个子领域，目标是用计算机程序证明数学定理，它曾是计算机科学发展的重要推动力。证明助手(proof assistant)又称交互式定理证明器，是让人类与机器协作编写并机械验证形式化证明的软件工具。近期许多工作开始让这些工具使用人工智能来自动化普通数学的形式化，这正是 OpenAI 这篇综述所处的背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proof_assistant">Proof assistant</a></li>
<li><a href="http://leodemoura.github.io/blog/2026-2-18-proof-assistants-in-the-age-of-ai/">Proof Assistants in the Age of AI — Leonardo de Moura</a></li>

</ul>
</details>

**社区讨论**: 评论者们的态度在兴奋与焦虑之间分化：有人认为 AI 的数学能力正呈指数级发展，也有人对研究中人类角色的消逝感到悲伤。有评论指出，计算机现在能更容易地生成和验证可计算问题的解，但并非所有数学都会被自动解决。另有人引用道格拉斯·亚当斯的话，认为当前模型虽无法'直觉'产生猜想，却能通过人类无法做到的大量运算迅速反驳猜想；还有用户分享了其中两个问题的直观解释链接。

**标签**: `#AI`, `#mathematics`, `#theoretical computer science`, `#LLMs`, `#research`

---

<a id="item-4"></a>
## [文章主张：开发者工具必须开源，AI 代理才能直接修改维护](https://blog.exe.dev/devtools-must-be-open-source) ⭐️ 8.0/10

exe.dev 上的一篇新文章主张，开发者工具必须保持开源，以便 AI 代理能够直接修改和维护它们，而不是依赖配置文件或插件系统。这篇文章在 Hacker News 上引发了激烈讨论，共 165 条评论，围绕这一愿景的可行性和效率展开辩论。 随着 AI 辅助开发日益普及，开发者工具的许可证和架构将决定 AI 代理能否真正定制和维护它们所使用的软件。这场争论影响维护者、用户以及整个开源生态系统，并引发了关于可持续性和能源消耗的思考。 文章建议设置一个夜间 cron 任务，让 LLM 获取上游更改并将所有本地更改变基，然后验证软件是否仍能正常工作。批评者则认为这种做法既浪费又不可靠，因为 AI 可能会破坏工作流，并且维护分支实际会涉及真正的合并冲突工作。

hackernews · bryanmikaelian · 8月3日 14:15 · [社区讨论](https://news.ycombinator.com/item?id=49156111)

**背景**: 开源开发者工具长期以来赋予用户检查和修改代码的自由，但现实中很少有程序员有时间这样做。AI 软件开发代理是一种能够自主执行软件开发生命周期部分环节的系统，一些人认为它们使开源最初设想的“用户自行修改”变得切实可行。自我修改的 AI 代码是一种新兴方法，强调适应性和效率，但也引发了关于可维护性和可靠性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spiralscout.com/blog/ai-self-modifying-code">Embracing Self - Modifying AI Code in Modern Software Development</a></li>
<li><a href="https://github.com/flatlogic/awesome-ai-software-development-agents">GitHub - flatlogic/awesome- ai - software - development - agents ...</a></li>

</ul>
</details>

**社区讨论**: 评论者观点分歧明显：Simon Willison 认为 LLM 改变了局面，使开源的原始自由理想更加可行；kelnos 则强烈反对取消配置文件、为简单改动而重建编辑器，认为这非常低效。theamk 将夜间 AI 变基方案形容为“地狱”，因为 AI 可能破坏工作流；lalitmaganti 认为这过于理想化，因为维护分支需要实际工作和冲突解决。

**标签**: `#open-source`, `#devtools`, `#LLM`, `#AI-assisted-development`, `#software-engineering`

---

<a id="item-5"></a>
## [ComfyUI 即日支持 MiniMax H3：开放权重、原生音频与 2K 视频](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 8.0/10

ComfyUI 宣布对 MiniMax H3 提供 day-0 支持，这是一款支持原生音频和 2K 视频生成的开放权重多模态模型。优化将内存占用降低 66%，从 123.6 GB 降至 42.5 GB，从而可以在本地 GPU 上运行。 这标志着开放权重视频生成的重要一步，让个人创作者能够在消费级 GPU 上使用先进的 2K 视频与音频模型。这也巩固了 ComfyUI 作为本地生成式 AI 工作流首选节点式界面的地位。 该模型的调制权重约占总参数的 40%，可以被剪枝并替换为查找表（lookup table）而不会造成质量损失。结合动态 VRAM 卸载，最小模型变体可以在 RTX 3060 上运行，但生成时间仍然可观——在 16GB RTX 4070 Ti Super 上生成 10 秒 480p 片段约需 10 分钟。

hackernews · vblanco · 8月3日 13:34 · [社区讨论](https://news.ycombinator.com/item?id=49155629)

**背景**: ComfyUI 是一个开源的、基于节点的生成式 AI 界面和推理引擎，用户可以通过连接节点来构建工作流。MiniMax H3 是一系列多模态视频生成模型，可以根据文本生成视频、让静态图像动起来，或在两帧之间进行变换，并支持原生音频。开放权重模型会公开发布训练后的参数，使本地部署和开发者进一步创新成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Comfy-Org/MiniMax-H3">Comfy-Org/ MiniMax - H 3 · Hugging Face</a></li>
<li><a href="https://hailuoai.video/tools/minimax-h3">MiniMax H 3 Multimodal AI Video Model | Hailuo AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表现出浓厚兴趣：有人质疑这种剪枝技术是否能推广到 LLM，另一些人则指出在 16GB RTX 4070 Ti Super 上效果令人印象深刻，尽管生成速度较慢。还有人称赞输出质量尤其是鼠标渲染方面的飞跃，但也有人认为美学观感“平庸而千篇一律”。

**标签**: `#AI/ML`, `#Open Weights`, `#Video Generation`, `#ComfyUI`, `#Local Inference`

---

<a id="item-6"></a>
## [数据库研究员 Andy Pavlo 加入 ClickHouse，创立 ClickHouse Labs](https://clickhouse.com/blog/andy-pavlo-joins-clickhouse) ⭐️ 8.0/10

知名数据库研究者、卡内基梅隆大学教授 Andy Pavlo 将加入 ClickHouse，创立专注于数据库系统的行业研究机构 ClickHouse Labs。该消息已在 ClickHouse 官方博客上公布。 此举加强了学术数据库研究与领先开源 OLAP 数据库公司之间的联系，可能影响 ClickHouse 的长期架构与创新方向。在资金日益向人工智能集中的背景下，这也表明数据库研究仍能获得产业界投入。 ClickHouse Labs 的目标是成为一流的行业研究机构，而不是一个只提出想法、与产品隔离的实验室。Pavlo 以 CMU 数据库小组的公开课和数据库基准测试工作而闻名，评论者希望这些教学资源能以 ClickHouse 赞助的形式继续下去。

hackernews · nikolay_sivko · 8月3日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49156011)

**背景**: ClickHouse 是一款开源的列式数据库管理系统，面向在线分析处理（OLAP），能够基于大规模数据集实时生成分析报表。将 ClickHouse 商业化的 ClickHouse, Inc. 已累计融资超过 6.5 亿美元，在 2025 年 5 月完成 C 轮融资后估值约为 63.5 亿美元。Pavlo 是卡内基梅隆大学的副教授，他在数据库系统方面的教学与研究成果使他成为该领域广受认可的人物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://clickhouse.com/blog/andy-pavlo-joins-clickhouse">Andy Pavlo joins ClickHouse to establish ClickHouse Labs</a></li>
<li><a href="https://en.wikipedia.org/wiki/ClickHouse">ClickHouse</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极且常带个人色彩：评论者向 Pavlo 表示祝贺，称这是 ClickHouse 在人才吸引上的重大胜利，并回忆从他 CMU 公开课学习的经历。也有人提出实质性问题，例如好奇 ClickHouse、Trino 等快速 OLAP 引擎将如何应对存储计算分离和数据摄入，并呼吁 ClickHouse 在政府资助减少之际资助学术数据库研究。

**标签**: `#database`, `#ClickHouse`, `#OLAP`, `#research`, `#industry`

---

<a id="item-7"></a>
## [Jane Street 开源基于 OCaml 的 UI 库 Bonsai](https://github.com/janestreet/bonsai) ⭐️ 8.0/10

Jane Street 已发布 Bonsai，这是一个开源的 OCaml UI 库，用于构建动态、响应式 Web 应用。它使得后端和前端都能使用相同的语言和类型，并已在 GitHub 上公开。 它的重要性在于让 OCaml 开发者能够跨全栈共享类型和业务逻辑，提升安全性并减少重复工作。这也展示了 Jane Street 对 OCaml 生态的投入，为以 JavaScript 为中心的前端框架提供了一种强有力的替代方案。 Bonsai 部分受 Elm 启发，并通过 Js_of_ocaml 编译为 JavaScript。它驱动了 Jane Street 几乎所有内部 Web 应用，从公司目录到显示并交互交易系统的工具；不过，当前仓库中快速指南和“thinking in bonsai”页面的文档链接是缺失的。

hackernews · KolmogorovComp · 8月3日 08:29 · [社区讨论](https://news.ycombinator.com/item?id=49152842)

**背景**: OCaml 是一种通用、高级、多范式的编程语言，以安全性和表现力著称，常用于金融、静态分析和形式化验证。Bonsai 利用 Js_of_ocaml 将 OCaml 编译为 JavaScript，使开发者能够完全留在 OCaml 生态内构建前端应用，这与大多数 Web 技术栈相比实属罕见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/janestreet/bonsai">GitHub - janestreet / bonsai : A library for building dynamic webapps...</a></li>
<li><a href="https://en.wikipedia.org/wiki/OCaml_programming_language">OCaml programming language</a></li>

</ul>
</details>

**社区讨论**: 评论者对全栈类型共享的可能性感到兴奋，有用户表示一直在等待这一功能。其他人指出了文档文件缺失的问题，并询问 DOM 的更新方式（直接更新还是 diff）；还有人将 Bonsai 与另一种 OCaml 转 JS 的方案 Melange 进行比较；也有人认为生成出来的 UI 虽然性能好，但外观并不美观。

**标签**: `#OCaml`, `#UI framework`, `#Jane Street`, `#functional programming`, `#frontend development`

---

<a id="item-8"></a>
## [Rust 项目目标：不可移动类型和保证析构函数](https://github.com/rust-lang/rust-project-goals/blob/main/src/2026/move-trait.md) ⭐️ 8.0/10

一个 Rust 项目目标提议添加不可移动类型和保证析构函数，旨在最终取代 Pin 机制。

hackernews · paavohtl · 8月3日 06:42 · [社区讨论](https://news.ycombinator.com/item?id=49152023)

**标签**: `#rust`, `#programming-languages`, `#type-system`, `#memory-safety`, `#async`

---

<a id="item-9"></a>
## [SQLite 严重 CVE 还是 LLM 垃圾信息？](https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops/) ⭐️ 8.0/10

JFrog 的分析指出，近期许多针对 SQLite 的“严重”CVE 实际上是 LLM 工具生成的误报，并非真实漏洞。该报告凸显了 AI 生成的垃圾信息正涌入漏洞数据库的趋势。 这很重要，因为误报会降低 CVE 数据库的信噪比，使安全团队更难识别真正的威胁。同时也为攻击者通过虚假报告淹没系统提供了可乘之机，损害了漏洞管理体系的公信力。 该分析聚焦于 SQLite CVE，显示 LLM 生成的提交往往缺乏适当验证，并将问题错误地归类为严重级别。JFrog 指出，虽然 LLM 也能发现合法 CVE，但未经验证的 AI 提交会带来严重的可信度风险。

hackernews · ymir_e · 8月3日 11:28 · [社区讨论](https://news.ycombinator.com/item?id=49154332)

**背景**: CVE（通用漏洞与披露）是一个公开维护的已知网络安全漏洞字典，由 MITRE 和 CVE 编号机构管理，条目会加入国家漏洞数据库（NVD）。“AI 垃圾信息”指的是 AI 工具大规模生成的低质量、常不准确的内容；在网络安全领域，它越来越多地出现在漏洞赏金报告和 CVE 提交中，声称存在实际上并不存在的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/National_Vulnerability_Database">National Vulnerability Database - Wikipedia</a></li>
<li><a href="https://www.cve.org/">CVE : Common Vulnerabilities and Exposures</a></li>
<li><a href="https://www.darkreading.com/cyber-risk/ai-slop-kill-cybersecurity-storytelling-we-let-it">How to Stop AI Slop in Cybersecurity Storytelling</a></li>

</ul>
</details>

**社区讨论**: 评论者担心 AI 生成的误报会降低信噪比，使合法 CVE 更难被发现，也有人指出 LLM 确实能发现真实漏洞。还有人强调，未经验证的提交可能被利用为大规模洪水攻击的载体，并将这一趋势比作新一代“脚本小子”使用他们并不理解的工具。一位评论者指出，这会给被要求修补所有 CVE 的组织带来实际负担。

**标签**: `#LLM`, `#Security`, `#CVE`, `#Vulnerability Management`, `#AI`

---

<a id="item-10"></a>
## [Kimi K3 架构深度解析：压缩记忆与潜在专家路由](https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the) ⭐️ 8.0/10

SemiAnalysis 发表了对 Kimi K3 架构的深入技术分析，重点介绍了压缩记忆、跨深度注意力、潜在专家路由和推理性能。文章深入剖析了该大语言模型的新颖机制。 这一分析具有重要意义，因为 Kimi K3 代表了 AI 模型架构创新的重要一步，可能对效率和长上下文处理产生影响。这些见解对关注大语言模型系统的 AI/ML 工程师和研究人员很有价值，可能影响未来的模型扩展和推理优化。 根据 SemiAnalysis 的介绍，文章涵盖了用于减小 KV 缓存大小的压缩记忆技术、实现跨层交互的跨深度注意力，以及专家混合模型中的潜在专家路由。这些机制被视为提升推理性能和长上下文推理能力的方法。

rss · Semianalysis · 8月3日 19:42

**背景**: 大语言模型依赖 Transformer 架构，其自注意力机制让每个 token 能注意到序列中的所有其他 token，但在长序列下会带来很高的内存开销。压缩记忆等技术可以减少上下文所需的存储，而专家混合（MoE）模型使用路由网络只为每个 token 激活少量专家参数。跨深度注意力则将标准自注意力扩展到不同层之间。这篇文章属于提升 LLM 效率和长上下文性能的持续研究背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.15443">[2502.15443] When Compression Meets Model Compression: Memory-Efficient Double Compression for Large Language Models</a></li>
<li><a href="https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html">11.7. The Transformer Architecture — Dive into Deep Learning 1.0.3 documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#architecture`, `#inference`, `#memory`

---

<a id="item-11"></a>
## [美国犯罪实验室 DNA 设备曝漏洞，30 年证据面临篡改风险](https://www.wsj.com/tech/cybersecurity/security-flaw-placed-30-years-of-dna-evidence-at-risk-of-hacking-1932775a) ⭐️ 8.0/10

研究人员在美国多数犯罪实验室使用的 DNA 分析设备中发现一个安全漏洞，并借助 Anthropic 的 Claude 生成的 AI 代码，在大约 45 分钟内篡改了 DNA 扫描数据且未触发警报。Thermo Fisher Scientific 已于 7 月私下承认该漏洞，并于上周五发布高危公告，同时推出增加数字签名的软件更新以保护文件。 该漏洞威胁到美国 200 多家实验室自 1995 年以来近 30 年的法医 DNA 证据完整性。一旦被利用，可能动摇刑事定罪的可信度，并暴露出法医领域缺乏统一网络安全监管的问题。 该漏洞涉及以专有 ABIF 格式存储的 FSA 文件，其中包含毛细管电泳运行产生的电泳图数据。研究人员的修改文件没有被常见的分析软件标记；Thermo Fisher 表示目前尚无实际利用案例，并正与 CISA 协调，但对在审或已结案件的影响仍不明确。

telegram · zaihuapd · 8月3日 05:15

**背景**: 法医 DNA 分析依赖自动化基因分析仪，例如 Thermo Fisher 的 Applied Biosystems 系列仪器，它们通过毛细管电泳分离并检测 DNA 片段。输出结果以电泳图形式记录，并保存为 FSA 文件，其中包含原始数据、仪器设置和运行信息，用于生成 DNA 图谱。由于这些文件被当作证据使用，篡改可能改变 DNA 图谱且不留下明显痕迹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electropherogram">Electropherogram</a></li>
<li><a href="https://fileinfo.com/extension/fsa">FSA File - What is an .fsa file and how do I open it?</a></li>
<li><a href="https://www.thermofisher.com/us/en/home/life-science/sequencing/sanger-sequencing/sanger-sequencing-technology-accessories.html">Applied Biosystems Genetic Analysis Systems | Thermo Fisher Scientific - US</a></li>

</ul>
</details>

**标签**: `#security`, `#forensics`, `#DNA analysis`, `#vulnerability`, `#cybersecurity`

---

<a id="item-12"></a>
## [美 50 名警员被控滥用车牌摄像头窥探前任](https://www.washingtonpost.com/technology/2026/08/02/how-police-officers-used-vast-network-cameras-spy-their-exes/) ⭐️ 8.0/10

《华盛顿邮报》2026 年 8 月 2 日发布的调查发现，美国至少有 50 名执法人员被指控滥用车牌识别系统，其中 46 起案件涉及 Flock Safety 摄像头。26 起案件中，警员窥探妻子、女友、前任或心仪的女性。 该调查揭露了警方系统性地滥用大规模监控工具，凸显了快速扩张的车牌读取器行业在隐私和监管方面的严重漏洞。Flock 运营着超过 12 万台摄像头，每月记录 200 亿次车牌扫描，此类滥用行为表明亟需更严格的监督和问责。 其中一起案件涉及佐治亚州警察局长 Michael Steffman，他约 600 次搜索前女友 Bakely 及其女儿的车牌；他于 2025 年 11 月被捕，2026 年 4 月开庭前自杀身亡。Flock 表示滥用难以完全杜绝，并推出了可选的“审计辅助”功能；目前仅 13 个州要求审计，至少 8 个州将滥用定为犯罪。

telegram · zaihuapd · 8月3日 09:03

**背景**: 自动车牌识别（ALPR）系统使用人工智能摄像头捕捉并分析过往车辆图像，存储位置、日期和时间等详细信息。Flock Safety 是这些系统的主要提供商，其摄像头已安装在美国 6000 多个社区，形成了一个强大的监控网络，引发了重大的隐私担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers...</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#privacy`, `#law enforcement`, `#ethics`, `#government technology`

---

<a id="item-13"></a>
## [英伟达 170HX 矿卡被破解：显存解锁至 80GB，二手价暴涨](https://finance.sina.com.cn/tech/roll/2026-08-03/doc-inikzqsf4659769.shtml) ⭐️ 8.0/10

亚利桑那州立大学研究人员公开了英伟达 CMP 170HX 矿卡的破解方案，利用 Falcon 安全协处理器的栈溢出漏洞绕过官方 OTP 熔丝锁定，将显存最高解锁至 80 GB，FP32 算力从 0.39 TFLOPS 暴增至 94 TFLOPS。 该破解将一款廉价、受限的矿卡转化为可用于 AI 推理的高性能 GPU，性能接近 A100，导致二手市场价格剧烈波动。同时，它也暴露出基于 OTP 熔丝的硬件限制存在安全漏洞，对 GPU 安全性和二手市场均有深远影响。 解锁后的显卡据称可在 Windows 和 Linux 下直接运行 AI 图像生成及大语言模型推理，但长期稳定性与不同批次的解锁上限仍存在风险。国内二手价从 300–500 元飙升至 3000–4000 元，海外市场甚至有 1500 美元的报价。

telegram · zaihuapd · 8月3日 11:29

**背景**: CMP 170HX 是英伟达 2021 年推出的专用加密货币矿卡，采用与 A100 相同的 GA100 核心，但通过一次性可编程（OTP）熔丝人为限制了 PCIe、算力和显存。Falcon 安全协处理器是英伟达 GPU 内部负责安全启动与固件操作的微控制器，因此成为此类攻击的主要目标。该漏洞利用 Falcon 中 DMA 相关的无界溢出获取代码执行权限，进而修改被熔丝强制的寄存器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kentino.com/products/nvidia-cmp-170hx-64-gb-hbm2e-modified-ex-mining">NVIDIA CMP 170 HX 64 GB HBM2e (Modified, Ex- Mining ) – Kentino</a></li>
<li><a href="https://nvidia.github.io/open-gpu-doc/Falcon-Security/Falcon-Security.html">NVIDIA Falcon Security</a></li>

</ul>
</details>

**标签**: `#security`, `#hardware`, `#GPU`, `#exploit`, `#AI`

---

<a id="item-14"></a>
## [苹果就英国 iCloud 后门要求提起法律挑战](https://www.ft.com/content/2cc9c96a-0e5b-4c33-a95a-3d11072a145c?syn-25a6b1a6=1) ⭐️ 8.0/10

苹果已向英国调查权力法庭提起法律申诉，挑战英国政府要求其允许访问英国用户加密 iCloud 云备份的「技术能力通知」。此前，苹果已于 2025 年 2 月在英国下架了高级数据保护功能。 本案将考验英国政府强制科技公司构建后门命令的合法性，对加密、隐私和国家安全产生重大影响。结果可能为全球政府如何要求访问用户加密数据树立先例。 这份「技术能力通知」依据 2016 年《调查权力法》签发，据报道要求苹果保留访问高级数据保护所保护内容的能力。苹果一直主张任何后门都会削弱所有用户的安全性；隐私组织 Privacy International 和 Liberty 也提起了申诉，法庭已定于下月举行案件管理听证。

telegram · zaihuapd · 8月3日 15:40

**背景**: 在英国，2016 年《调查权力法》（又称「窥探者宪章」）允许内政部发布「技术能力通知」，强制服务提供商为合法访问数据提供技术能力。调查权力法庭是审理此类监控权力申诉的独立法院。苹果的 iCloud 高级数据保护功能提供端到端加密，意味着正常情况下连苹果也无法访问数据；后门则会打破这种保护。英国最初要求访问影响英美用户的备份数据，在美国抗议后撤回，随后又发布了仅针对英国用户的新通知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technical_capability_notice">Technical capability notice</a></li>
<li><a href="https://en.wikipedia.org/wiki/Investigatory_Powers_Tribunal">Investigatory Powers Tribunal</a></li>
<li><a href="https://support.apple.com/en-us/108756">How to turn on Advanced Data Protection for iCloud - Apple Support</a></li>

</ul>
</details>

**标签**: `#Apple`, `#iCloud`, `#encryption`, `#privacy`, `#law`

---