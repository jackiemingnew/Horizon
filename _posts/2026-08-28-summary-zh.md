---
layout: default
title: "Horizon Summary: 2026-08-28 (ZH)"
date: 2026-08-28
lang: zh
---

> 从 30 条内容中筛选出 10 条重要资讯。

---

1. [Cloudflare 通过五项 Rust 优化为 DNS 缓存节省 100 TB 内存](#item-1) ⭐️ 9.0/10
2. [提示注入攻击攻破 Claude Code 自动模式](#item-2) ⭐️ 9.0/10
3. [谷歌发布 Gemini-3.5-Transcribe：高精度语音转文字并支持函数调用](#item-3) ⭐️ 8.0/10
4. [法官裁定特朗普政府将 Anthropic 列入黑名单属非法](#item-4) ⭐️ 8.0/10
5. [数据分析揭示 Claude 的独特词汇模式](#item-5) ⭐️ 8.0/10
6. [开发者 84 天成功反编译 N64 游戏《滑雪小子》](#item-6) ⭐️ 8.0/10
7. [谷歌推出 Gemini Omni 1.1 Flash，支持 AI 视频生成与扩展](#item-7) ⭐️ 8.0/10
8. [英伟达季度营收 962 亿美元，首次给出 70%增长指引](#item-8) ⭐️ 8.0/10
9. [Anhui 开放 AI 控制硬件标准预览，设备集成缩至分钟级](#item-9) ⭐️ 8.0/10
10. [OpenAI 正在开发可一直工作到休眠的常驻 Codex 代理](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare 通过五项 Rust 优化为 DNS 缓存节省 100 TB 内存](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) ⭐️ 9.0/10

Cloudflare 工程师 Sebastiaan Neuteboom 发布了一篇博客文章，介绍了对 Big Pineapple（支撑 1.1.1.1 的平台）DNS 缓存布局所做的五项 Rust 级内存优化。这些改动将每条条目的内存占用降低了 56%，在整个集群中释放了约 100 TB 内存。 这证明了在超大规模场景下，底层系统编程仍然至关重要——每条缓存条目节省几个字节，就能在整个集群中转化为巨大的内存节省。同时也说明 Rust 对内存布局的控制能在生产基础设施中带来实际的成本和容量收益。 Big Pineapple 在任意时刻都要处理超过 2500 亿条 DNS 缓存条目，每条条目多浪费 1 个字节，整个集群就会多消耗约 250 GB 内存。优化聚焦于 DNS 缓存条目在内存中的表示方式，文章中介绍了五项连续改动，共同将每条条目的内存占用减少了 56%。

hackernews · TangerineDream · 8月27日 17:17 · [社区讨论](https://news.ycombinator.com/item?id=49468083)

**背景**: DNS 缓存用于存储最近的 DNS 查询结果，这样重复的域名解析请求无需查询上游服务器即可快速返回。Cloudflare 的 1.1.1.1 是处理海量流量的公共 DNS 解析器，Big Pineapple 是支撑它以及 Gateway DNS、DNS Firewall 和 AS112 的底层平台。在这种规模下，内存效率至关重要，Rust 对数据布局的控制能力使其非常适合此类优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-cache-memory-optimization-1111/">How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache | Cloudflare Blog</a></li>
<li><a href="https://explainx.ai/blog/cloudflare-dns-cache-100-terabytes-memory-optimization-august-2026">Cloudflare Saved 100TB Memory: DNS Cache Rust Deep Dive ...</a></li>
<li><a href="https://mangodeveloper.com/articles/cloudflares-1111-dns-cache-sheds-100-terabytes-through-five-rust-memory-optimizations">Cloudflare's 1.1.1.1 DNS Cache Sheds 100 Terabytes Through ...</a></li>

</ul>
</details>

**社区讨论**: 评论区整体态度积极，并补充了更多技术细节。有人指出一个可能遗漏的优化点——把记录数据直接放在 CacheEntry 成员之后而不是单独分配——但也承认这在 Rust 中可能并不容易。还有人分享了 MaraDNS 中类似的单次 malloc 优化，将黑名单内存从 237 MB 降到 9.5 MB；其他人讨论了结构体对齐问题，并提醒将多个独立 Vec 合并成一个列表可能削弱 Rust 的安全保证。

**标签**: `#DNS`, `#optimization`, `#systems programming`, `#memory`, `#Cloudflare`

---

<a id="item-2"></a>
## [提示注入攻击攻破 Claude Code 自动模式](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 9.0/10

安全研究员 Johann Rehberger 演示了一种针对 Claude Code 默认自动模式的提示注入攻击，通过诱使智能体解压 zip 压缩包并在导入 base64 时执行恶意的本地 struct.py 文件，攻击成功率高达 80%。在某些运行中，自动模式甚至阻止了 Claude 用于终止恶意程序的清理命令。 这一发现动摇了 Anthropic 对 Claude Code 自动模式的安全声明，该模式最近已被设为默认权限模式。它表明 AI 编程智能体从根本上仍易受间接提示注入攻击，且安全机制本身也可能以危险方式失效。 该攻击通过诱使 Claude Code 下载并解压 zip 压缩包实现；解压出的 struct.py 会在 Claude 运行导入 base64 的代码时遮蔽标准库同模块。自动模式的分类器允许了恶意进程的创建，却阻止了用于终止该进程的命令，使安全机制本身成为故障的一部分。

rss · Simon Willison · 8月27日 22:50

**背景**: 提示注入攻击将恶意指令隐藏在外部内容（如文件或网页）中，可覆盖大语言模型的系统指令并引发非预期行为。Claude Code 的自动模式是 Anthropic 的功能，允许 AI 自行做出权限决策，并通过安全机制在操作执行前进行监控——该模式在 2026 年成为默认选项。Python 模块劫持是一种已知的代码执行技术，利用 Python 搜索和加载模块的方式，使本地文件（如 struct.py）能替换同名标准库模块。由于编程智能体会处理不可信内容并执行代码，它们扩大了此类技术的攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude by Anthropic</a></li>
<li><a href="https://github.com/echo-devim/pyjacktrick">GitHub - echo-devim/pyjacktrick: Python module hijacking POC</a></li>
<li><a href="https://www.mdpi.com/2078-2489/17/1/54">Prompt Injection Attacks in Large Language Models and AI ...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#Claude Code`, `#Anthropic`, `#LLM agents`

---

<a id="item-3"></a>
## [谷歌发布 Gemini-3.5-Transcribe：高精度语音转文字并支持函数调用](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 8.0/10

谷歌宣布推出 Gemini-3.5-Transcribe，这是一款新的语音转文字模型，能直接将原始音频转换为准确、精炼、格式化的文本，并能处理噪声、专业术语和语言不流畅问题。该模型还支持函数调用，可将任务委托给其他 Gemini 模型，目前已支持 Gboard Rambler，并即将登陆 Chrome。 这是语音转文字领域的一次重大进展，Gemini-3.5-Transcribe 宣称具有最先进的准确性，并增加了函数调用功能，从而支持更强大的语音驱动工作流。然而，延迟仍然是实际使用中的一个问题，尤其是在实时翻译和转录应用中，速度至关重要。 该模型基于 Gemini 的音频理解能力，可通过 Gemini API 使用。函数调用目前可在 Gemini macOS 应用中工作，并能将图像生成、文件分析等任务委托给其他 Gemini 模型，不过开发者文档明确了其具体范围。

hackernews · k9294 · 8月27日 18:03 · [社区讨论](https://news.ycombinator.com/item?id=49468818)

**背景**: 语音转文字模型将口语转换为书面文本，但传统系统往往难以处理背景噪声、专业术语以及犹豫、重复等不流畅表达。Gemini 3.5 Transcribe 是谷歌推出的新模型，可直接将原始音频转换为准确、精炼的文本，并支持函数调用，即让大语言模型在生成过程中调用外部工具或 API。这使语音交互不仅能完成简单转录，还能触发图像生成、文件分析等复杂任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">Intelligent transcription with Gemini 3.5 Transcribe</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe">Gemini 3.5 Transcribe | Gemini API | Google AI for Developers</a></li>
<li><a href="https://9to5google.com/2026/08/26/gemini-3-5-transcribe/">Google launches Gemini 3.5 Transcribe, which powers Gboard Rambler & is coming to Chrome</a></li>

</ul>
</details>

**社区讨论**: 社区反馈褒贬不一：一些测试者称赞其准确性，但指出延迟是实时应用的关键缺点，并认为 Soniox STT v5 和 Voxtral Mini 3b 是强有力的替代品。有评论者认为函数调用的描述令人困惑，还有评论者报告模型可能会‘简化’精确措辞，偶尔改变原意。

**标签**: `#speech-to-text`, `#Gemini`, `#Google AI`, `#STT`, `#machine learning`

---

<a id="item-4"></a>
## [法官裁定特朗普政府将 Anthropic 列入黑名单属非法](https://www.nytimes.com/2026/08/27/technology/anthropic-government-blacklisting-ruling.html) ⭐️ 8.0/10

2026 年 8 月 27 日，一名法官裁定特朗普政府将 AI 公司 Anthropic 列入黑名单的行为非法，推翻了这一政府行动。该裁决标志着政府在监管 AI 公司方面遭遇法律挫折。 这项裁决意义重大，因为它对政府在 AI 公司上的行政权力形成了制约，并可能为法院审查针对科技公司的政治性政府行为树立先例。它影响到整个 AI 产业，而该产业正面临监管机构和立法者越来越多的审查。 该裁决源于对特朗普政府试图将 Anthropic 列入黑名单的诉讼，但具体法律依据和补救措施尚未披露。这一决定可能为法院审查针对 AI 公司的行政行动树立先例，但其实际执行和影响仍不明确。

hackernews · jbegley · 8月28日 02:03 · [社区讨论](https://news.ycombinator.com/item?id=49473522)

**背景**: 黑名单是政府采取的一种行动，用以禁止公司获得联邦合同或安全许可等特定待遇。Anthropic 是一家以 Claude 大语言模型闻名的 AI 安全公司。这项裁决涉及上一届政府能否在没有法律依据的情况下对 AI 公司使用此类措施。新闻中未提供更多背景细节。

**社区讨论**: 评论区对这项非法裁决是否会产生实际效果表示怀疑，并指出法律补救的速度远慢于政治行动。还有评论认为，黑名单可能无意中推动各国走向主权 AI 和自托管，并质疑 Anthropic 能否真正从政府获得赔偿。

**标签**: `#AI policy`, `#Anthropic`, `#government regulation`, `#technology law`, `#legal ruling`

---

<a id="item-5"></a>
## [数据分析揭示 Claude 的独特词汇模式](https://louisabraham.github.io/load-bearing/) ⭐️ 8.0/10

一项对 GitHub 拉取请求描述的数据驱动分析显示，Claude 的写作风格可归类为八种不同模式，其中一种模式在语料库中的占比从 2025 年初的 1.0%增长到 2026 年中期的 45%。该项目由 Louis Abraham 创建，通过 GitHub Actions 每天更新。 这些发现为识别 AI 生成的文本提供了一种可量化的方法，并引发了对训练反馈循环的紧迫质疑——模型可能正在退化为狭窄的文体单一文化。这影响着 AI 检测研究、LLM 训练实践，以及所有依赖自然风格模型输出的群体。 该分析聚焦于 GitHub 拉取请求描述而非任意文本，按词汇使用而非主题对它们进行分组。作者表示，数据集和分析通过 GitHub Actions 每天更新，并正在添加搜索栏，计划扩展到每天 1000 个 PR。

hackernews · Labo333 · 8月27日 08:59 · [社区讨论](https://news.ycombinator.com/item?id=49461817)

**背景**: “承重词汇”（load-bearing vocabulary）是指在模型输出中承担不成比例权重的词语和短语，赋予 AI 生成文本可辨识的风格指纹。文体计量学（stylometry）通过研究这类指纹来区分人类与机器写作，相关研究表明机器文本通常比人类文本更统一。训练数据中 AI 内容比例的上升可能形成反馈循环：基于 AI 生成文本训练的模型会逐渐丧失文体多样性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/louisabraham/load-bearing">GitHub - louisabraham/load-bearing: The load-bearing ...</a></li>
<li><a href="https://topaihubs.com/articles/claude-s-load-bearing-vocabulary-unpacking-the-ai-s-core-language-insights">Claude's "Load-Bearing Vocabulary": Unpacking the AI's Core ...</a></li>
<li><a href="https://academic.oup.com/dsh/advance-article/doi/10.1093/llc/fqag064/8714041">Stylometric detection of AI-generated texts: evidence from human and machine-written essays | Digital Scholarship in the Humanities | Oxford Academic</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了该页面简洁直观的呈现方式以及作者不偏不倚的框架，作者本人也表示感谢，并提到项目每天自动更新。几位评论者担忧 Claude 及其他模型的输出模式正在恶化，质疑训练数据中 AI 内容是否过多，或 RLHF 是否不够优化。还有评论者询问统计依据的是相对频率还是绝对数量，指出人类的提交消息通常比 Claude 短得多。

**标签**: `#AI`, `#LLM`, `#Claude`, `#data analysis`, `#NLP`

---

<a id="item-6"></a>
## [开发者 84 天成功反编译 N64 游戏《滑雪小子》](https://blog.chrislewis.au/decompiling-a-nintendo-64-game-in-84-days/) ⭐️ 8.0/10

Chris Lewis 发布了一篇详细博文，记录了在 84 天内完整反编译 N64 游戏《滑雪小子》（Snowboard Kids）的全过程。该项目展示了现代逆向工程工作流，可能结合了 LLM 辅助工具与传统技术。 这一成就表明，得益于工具链和 AI 辅助的进步，复古游戏的反编译项目正变得越来越快、越来越容易上手。这可能会鼓励更多爱好者投身类似项目，拓宽经典游戏在保存与模组生态中的可能性。 该反编译项目聚焦于 N64 上相对冷门的游戏《滑雪小子》，并在 84 天内完成——对于一款主机的完整游戏而言，这个时间相当短。作者的工作流很可能结合了自动反编译器、手工汇编分析以及 LLM 辅助，将 MIPS 汇编转换为可读的 C 代码。

hackernews · knackers · 8月27日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49466006)

**背景**: N64 反编译是指对基于 MIPS 架构的 ROM 进行逆向分析，重建出可编译且输出与原始二进制一致的可读 C 源码。常用的工具有 N64Split 和链接器重插入技术，通过逐个函数将汇编替换为等效 C 代码。近年来，像 LLM4Decompile 这样的基于大语言模型的反编译器在自动化部分流程方面展现了潜力。Super Mario 64 等成功的反编译项目为现代 PC 移植和社区模组铺平了道路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.retroreversing.com/N64Reversing">N64 Reversing Introduction - Retro Reversing (Reverse ... N64 Reversing Introduction · RetroReversing Nintendo 64 (Project Reality) · RetroReversing - GitHub Pages GitHub - RetroReversing/retroReversing: Awesome website for ... GitHub - joeedh/n64disasm: [wip] N64 Reverse Engineering Tool</a></li>
<li><a href="https://github.com/albertan017/LLM4Decompile">GitHub - albertan017/LLM4Decompile: Reverse Engineering: Decompiling Binary Code with Large Language Models · GitHub</a></li>
<li><a href="https://readonlymemo.com/decompilation-projects-and-n64-recompiled-list/">Decompilation projects and N64 Recompiled PC ports list ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区反应积极，称赞作者的成就以及更广泛的 decomp/recomp 项目浪潮。一些用户强调 LLM 辅助工作流是此类工作的“倍增器”，另一些人则对反编译和重新编译老游戏的法律地位提出疑问。还有多条评论提到了相关项目，例如《龙骑传说》的 recomp 项目以及受《黄金眼》启发的游戏《Agent 64》。

**标签**: `#reverse engineering`, `#decompilation`, `#N64`, `#retro gaming`, `#LLM`

---

<a id="item-7"></a>
## [谷歌推出 Gemini Omni 1.1 Flash，支持 AI 视频生成与扩展](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) ⭐️ 8.0/10

谷歌发布了 Gemini Omni 1.1 Flash，这是一款可通过 Gemini API 和 Google AI Studio 使用的多模态模型。它支持视频生成，可将场景扩展至最长 40 秒，提供关键帧控制、360p 草稿生成以及 1080p 或 4K 输出。 此次发布表明谷歌持续押注视频生成 AI，与 OpenAI 放弃 Sora 形成对比。它为开发者提供了更可控、更高质量的视频生成工具，可能推动世界模型相关研究，并对更广泛的创意产业产生影响。 场景扩展基于最初的 10 秒片段，以 10 秒为增量逐步延长，最长累计至 40 秒。该模型原生支持多模态，可同时处理文本、图像、音频和视频，并支持指定首尾关键帧以及低分辨率草稿以加快迭代。

hackernews · saretup · 8月27日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49467922)

**背景**: Gemini Omni 是谷歌面向快速、对话式视频生成与编辑而设计的多模态模型系列。开发者可以通过 Interactions API 使用自然语言来优化和编辑生成的视频。场景扩展是一种让 AI 延续已生成片段的技术，从而构建更长、更连贯的序列，而不是局限于单次短片段生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/">Build with Gemini Omni 1.1 Flash - The Keyword</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/omni">Generate and edit videos with Gemini Omni Flash</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash">Gemini Omni Flash | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者持谨慎乐观态度，但更关注其局限性：有人指出该模型仍无法将生成视频与已有音频同步，不像 Minimax H3 等工具。还有人调侃给谷歌的提示词工程应加上“确保页面在 Firefox 中也能正常打开”，另一些评论则讨论了 AI 声音对影视和配音演员的影响，以及谷歌在视频生成上的战略投入。

**标签**: `#AI`, `#Google`, `#Gemini`, `#video-generation`, `#machine-learning`

---

<a id="item-8"></a>
## [英伟达季度营收 962 亿美元，首次给出 70%增长指引](https://mp.weixin.qq.com/s/JTZ_ZJ_pn5vgrI_1QUyWNw) ⭐️ 8.0/10

英伟达公布 2027 财年第二季度营收 962.21 亿美元，同比增长 106%；数据中心收入 890 亿美元，同比增长 117%。首席财务官科莱特·克雷斯首次给出 2028 财年约 70%的营收增长指引，下一代 Vera Rubin 平台已在本月量产出货。 这标志着 AI 基础设施支出的一个重要转折点，计算能力正直接转化为收入来源。首次提前一年给出增长指引，表明英伟达对下一代平台持续需求充满信心，将影响整个 AI 硬件生态。 据 CFO 称，2028 财年约 70%的增长指引受限于供给。Vera Rubin 预计在第三季度贡献约 20%的数据中心收入，其 NVL72 平台采用支持自适应压缩的新型 Transformer Engine，并配备第三代机密计算技术。

telegram · zaihuapd · 8月27日 08:51

**背景**: 英伟达的财年与日历年错开，2027 财年始于 2026 年 1 月。随着 AI 训练和推理需求激增，数据中心业务已成为其主导收入来源。Vera Rubin 是 Blackwell 架构的继任者，整合了拥有 88 个定制 ARM 核心的 Vera CPU、NVLink 6 互联以及包含 3360 亿晶体管的 Rubin GPU，旨在支撑大规模推理和智能体 AI 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/rubin/">Infrastructure for Scalable AI Reasoning | NVIDIA Vera Rubin Platform</a></li>
<li><a href="https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/">NVIDIA Rubin GPU : 336B Transistors, T Orders [2026]</a></li>
<li><a href="https://www.smbom.com/news/46475">NVIDIA Vera Rubin & Rubin Ultra: Next-Gen AI Infrastructure - SmBom</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#earnings`, `#AI`, `#data center`, `#GPU`

---

<a id="item-9"></a>
## [Anhui 开放 AI 控制硬件标准预览，设备集成缩至分钟级](https://www.anthropic.com/news/model-hardware-standard-research-preview) ⭐️ 8.0/10

Anthropic 发布了其模型硬件标准（MHS）的研究预览，这是一项让 AI 智能体安全操控物理实验室与机器人设备的共享规范。该标准将设备集成时间从数周甚至数月缩短到分钟级，并计划在完成安全评估后开源。 这标志着 AI 智能体向物理世界操作迈出了重要一步，有望加速生物技术、机器人和量子计算等领域的自动化进程。早期合作成果——例如 QuEra 的 AI 控制器在 99.3% 的情况下无需人工干预即可恢复量子计算机的激光锁定——展示了近期的实际影响力。 该预览最初面向一批精选的科研实验室和先进制造商开放，包括基因泰克、卡内基梅隆大学和 QuEra。MHS 规范既定义了 AI 智能体应如何与硬件交互，也规定了必须遵守的安全边界；只有在安全评估完成后才计划开源。

telegram · zaihuapd · 8月28日 01:38

**背景**: AI 智能体通常通过 API 与软件交互，但显微镜、液体处理器、机械臂等物理设备缺乏统一接口，导致每次集成都需要定制开发，耗时费力。模型硬件标准旨在提供一种共享协议，使同一套智能体能以最小改动部署到不同硬件上。Anthropic 的预览是早期尝试，旨在为 AI 应如何（以及不应如何）控制真实世界设备制定行业通用规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-hardware-standard-research-preview">Previewing the Model Hardware Standard \ Anthropic</a></li>
<li><a href="https://www.cnbc.com/2026/08/27/anthropic-pushes-into-physical-world-with-new-standard-to-help-ai-agents-operate-machines.html">Anthropic pushes into physical world with new standard to help AI agents operate machines</a></li>
<li><a href="https://www.wired.com/story/anthropic-standard-ai-agents-coming-to-the-physical-world/">This Is How Anthropic Thinks AI Agents Should Navigate the Physical World | WIRED</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI hardware control`, `#robotics`, `#standards`, `#research`

---

<a id="item-10"></a>
## [OpenAI 正在开发可一直工作到休眠的常驻 Codex 代理](https://www.wired.com/story/openai-is-developing-a-persistent-ai-agent/) ⭐️ 8.0/10

据报道，OpenAI 正在为其命令行编程代理 Codex 开发一种“常驻模式”，使其能够持续运行直到被休眠。该代理在完成请求后可自主创建后续任务，并支持跨会话工作，OpenAI 已确认正在测试，但暂无近期上线计划。 这代表了向更自主的 AI 代理迈出的重要一步，可能会减少持续人工提示的需求，从而改变软件工程工作流程。如果成功，它可能为整个行业的长时运行代理设定新标准。 常驻模式内置了“主动性”设定，允许 Codex 依据对用户的了解，自行创建后续任务并在跨会话中执行。但改动用户自身系统之外的内容仍须事先获得批准。

telegram · zaihuapd · 8月28日 02:47

**背景**: Codex 是 OpenAI 推出的基于终端的编程代理，其生成的代码补丁符合人类编程偏好。当前的 AI 代理通常在短暂且受限的会话中运行，几分钟或几小时后即停止；而采用休眠机制的常驻代理可以卸载上下文、关闭会话，并在稍后恢复检查点以继续执行，从而节省计算资源并支持更长的自主任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gizmodo.com/nevertheless-openai-persists-with-new-always-on-agent-2000804088">Nevertheless, OpenAI Persists With New Always-On Agent</a></li>
<li><a href="https://docs.lobstercage.ai/concepts/hibernation">Hibernation — LobsterCage Docs</a></li>
<li><a href="https://openai.com/index/introducing-codex/">Introducing Codex | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI agents`, `#Codex`, `#persistent execution`, `#software development`

---