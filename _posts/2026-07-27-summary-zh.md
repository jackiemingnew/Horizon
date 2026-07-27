---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 30 条内容中筛选出 13 条重要资讯。

---

1. [Bun 的 Rust 重写进展与延迟](#item-1) ⭐️ 9.0/10
2. [月之暗面开源 Kimi K3：2.8 万亿参数模型](#item-2) ⭐️ 9.0/10
3. [Fastjson2 发现严重远程代码执行漏洞](#item-3) ⭐️ 9.0/10
4. [vLLM v0.26.0 发布：新增 Inkling 模型家族与性能优化](#item-4) ⭐️ 8.0/10
5. [法官驳回谷歌利用 DMCA 阻止搜索结果抓取的企图](#item-5) ⭐️ 8.0/10
6. [论坛项目从 React 迁移到 HTMX 以增强交互性](#item-6) ⭐️ 8.0/10
7. [《Paged Out》第 9 期：黑客好奇的技术杂志](#item-7) ⭐️ 8.0/10
8. [观点指南评选 AI 工具，转向智能体系统](#item-8) ⭐️ 8.0/10
9. [六个前沿大模型在个人基准测试中一致呈现左倾偏见](#item-9) ⭐️ 8.0/10
10. [长鑫科技科创板首日暴涨 471%，创最大 IPO](#item-10) ⭐️ 8.0/10
11. [谷歌预告 Gemini 4：迄今最雄心预训练，年底发布](#item-11) ⭐️ 8.0/10
12. [中方驳美方因 AI 蒸馏制裁威胁](#item-12) ⭐️ 8.0/10
13. [中国开始量产国产 DUV 光刻机](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bun 的 Rust 重写进展与延迟](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 9.0/10

Bun 的 Rust 重写已在一个多月前随 Claude Code 发布，但 Bun v1.4 的公开版本因项目负责人 Jarred Sumner 承诺的新增通过的 Node.js 测试数量尚未达成而延迟。 这次从 Zig 到 Rust 的重写是广泛使用的 JavaScript 运行时的一次重大技术转型，将影响性能和安全性。延迟凸显了在大型重写中达成兼容性目标的挑战。 Rust 重写是利用 LLM 完成的机械移植，版本发布将延迟到承诺的 Node.js 测试通过数量达到为止，相关 PR 已提交但尚未合并。Jarred 预计最可能在下周二发布。

hackernews · tomlockwood · 7月27日 11:12 · [社区讨论](https://news.ycombinator.com/item?id=49067854)

**背景**: Bun 是一个快速的全能 JavaScript 运行时，旨在替代 Node.js，最初用 Zig 编写。重写为 Rust 旨在提高内存安全性并利用 Rust 生态系统。过渡过程中使用相同的测试套件以确保兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bun.com/blog/bun-in-rust">Rewriting Bun in Rust | Bun Blog</a></li>
<li><a href="https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/">Rewriting Bun in Rust</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/ bun : Incredibly fast JavaScript runtime , bundler...</a></li>

</ul>
</details>

**社区讨论**: Jarred 确认重写进展顺利并已在 Claude Code 中使用。评论者讨论了使用 LLM 进行移植的权衡，并指出一个独立项目（Buz）声称通过修复原始 Zig 代码实现了更快的构建。

**标签**: `#bun`, `#rust`, `#javascript-runtime`, `#software-engineering`, `#rewrite`

---

<a id="item-2"></a>
## [月之暗面开源 Kimi K3：2.8 万亿参数模型](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 9.0/10

月之暗面（Moonshot AI）在 Hugging Face 上开源了 Kimi K3，这是全球首个 3T 级别的开源模型，总参数量达 2.8 万亿。该模型采用了全新的 Kimi Delta Attention 和 Attention Residuals 架构，支持 100 万 token 的上下文窗口，并在多项基准测试中与前沿模型互有胜负。 Kimi K3 的开源标志着 AI 透明度的重大里程碑，证明了超大规模模型（3T 级别）可以向公众开放。这降低了顶级模型能力的使用门槛，有望加速长程推理、智能体任务和多模态理解等领域的研究与应用开发。 Kimi K3 采用 Stable LatentMoE 框架，共有 896 个专家，每个 token 激活 16 个，训练效率相比 Kimi K2 提升约 2.5 倍。它原生支持文本、图像和视频理解，可使用 Transformers、vLLM、SGLang 等推理框架部署，并支持 MXFP4 量化。

telegram · zaihuapd · 7月27日 15:15

**背景**: 大型语言模型的规模通常以参数量衡量，超过 1 万亿参数的模型因计算成本极高而非常罕见。混合专家（Mixture-of-Experts, MoE）架构允许每个 token 只激活部分参数，从而更高效地扩展模型。月之暗面此前发布了 Kimi K2，而 Kimi K3 在此基础上引入了全新的注意力机制（Kimi Delta Attention 和 Attention Residuals），改进了内存管理和上下文理解能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jianyuh.github.io/attention/2025/12/13/KDA.html">Linear Attention : Kimi Delta Attention | Jianyu Huang’s Blog</a></li>
<li><a href="https://github.com/MoonshotAI/Attention-Residuals">GitHub - MoonshotAI/Attention-Residuals · GitHub</a></li>
<li><a href="https://www.emergentmind.com/topics/kimi-delta-attention">Kimi Delta Attention : Delta ‐Rule Linear Mechanism</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#large language model`, `#Moonshot AI`, `#Mixture of Experts`

---

<a id="item-3"></a>
## [Fastjson2 发现严重远程代码执行漏洞](https://mp.weixin.qq.com/s/LJaul1jNjK9pXRAkoUiMEA) ⭐️ 9.0/10

Fastjson2 被披露存在一个严重的远程代码执行漏洞，影响 2.0.62 及以前的所有版本，目前尚无官方补丁。 该漏洞允许攻击者绕过 AutoType 类型校验并通过恶意 JSON 数据执行任意代码，对使用 Fastjson2 的应用程序构成严重安全威胁。 该漏洞由长亭科技于 2024 年 7 月 27 日披露，项目维护者已确认此问题。然而，PR #7695 被关闭且未合并，所有已发布版本均无正式补丁。

telegram · zaihuapd · 7月27日 10:31

**背景**: Fastjson2 是阿里巴巴开发的高性能 Java JSON 库。AutoType 是一种允许根据 JSON 内容自动反序列化类型的特性，如果限制不当，可能被利用进行远程代码执行攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alibaba.github.io/fastjson2/autotype_cn.html">FASTJSON 2 Autotype机制介绍 | fastjson2</a></li>
<li><a href="https://github.com/alibaba/fastjson2">GitHub - alibaba/fastjson2: 🚄 FASTJSON2 is a Java JSON library with excellent performance.</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#RCE`, `#Fastjson2`, `#Java`

---

<a id="item-4"></a>
## [vLLM v0.26.0 发布：新增 Inkling 模型家族与性能优化](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 正式发布，包含来自 212 位贡献者的 411 次提交，新增了对 Inkling 模型家族的全面支持、DeepSeek-V4 性能优化，以及用于生成模型的 fp32 lm_head 选项。 此版本显著增强了 vLLM 在大规模 LLM 推理方面的能力，特别是新增的 Inkling 模型家族和 DeepSeek-V4 优化，可提升生产部署中的吞吐量和准确性。 Inkling 模型家族支持包括分段 CUDA 图、Hopper FA4 相对注意力、MTP=1 推测解码、LoRA 和 NVFP4 量化。DeepSeek-V4 的改进包括专用路由内核实现 2.94%端到端 TPOT 提升，以及 fused_topk_bias 实现 1.5-2 倍内核加速。

github · khluu · 7月27日 01:06

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎。Inkling 模型家族是由 Thinking Machines Lab 发布的多模态模型。分段 CUDA 图将模型计算拆分成多个片段，以处理 prefill 阶段的可变 token 长度，相比标准 CUDA 图提高了效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/thinkingmachines/Inkling">thinkingmachines/ Inkling · Hugging Face</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#AI/ML`, `#release`, `#performance optimization`

---

<a id="item-5"></a>
## [法官驳回谷歌利用 DMCA 阻止搜索结果抓取的企图](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

美国一名法官裁定谷歌搜索结果页面不属于受版权保护的汇编，驳回了谷歌试图利用《数字千年版权法案》（DMCA）阻止 SerpAPI 等第三方抓取其搜索结果的诉讼。 该裁决为网络抓取的合法性树立了重要先例，可能限制大型平台利用版权法关闭数据提取服务的能力，而这些服务对于市场调研、SEO 和欺诈检测至关重要。 法院认为谷歌的搜索结果页面缺乏版权保护所需的最低限度创造性，因为它们本质上是事实的自动汇编。值得注意的是，该裁决并未涉及谷歌可能提出的其他法律依据，例如合同条款或非法侵入。

hackernews · cdrnsf · 7月27日 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49073513)

**背景**: DMCA 是美国法律，将规避保护版权作品的技术措施定为犯罪。网络抓取是指从网站自动提取数据，常用于比价、内容监控和研究。谷歌已弃用其自己的搜索 API，导致用户依赖第三方抓取工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DMCA">DMCA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Web_scraping">Web scraping</a></li>

</ul>
</details>

**社区讨论**: 评论普遍支持该裁决，用户指出谷歌在抓取他人内容的同时反对被他人抓取是虚伪的。一些用户感叹谷歌没有提供合法的搜索 API，而另一些则强调抓取对于识别虚假 ESTA 网站等诈骗的重要性。

**标签**: `#scraping`, `#DMCA`, `#copyright`, `#search engines`, `#legal`

---

<a id="item-6"></a>
## [论坛项目从 React 迁移到 HTMX 以增强交互性](https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/) ⭐️ 8.0/10

Misago 论坛软件项目宣布从其代码库中移除 React.js，转而采用 HTMX 处理用户界面交互，从客户端 JavaScript 框架转向服务端驱动的超媒体方法。 这一迁移反映了行业向更简单的超媒体驱动 Web 架构发展的趋势，尤其适用于内容密集型应用。它表明 HTMX 能降低客户端复杂性，同时保持动态交互，可能影响其他项目重新考虑重度 JavaScript 框架的使用。 HTMX 通过自定义属性扩展 HTML，支持 AJAX 调用实现部分页面更新，无需编写自定义 JavaScript。但社区成员指出，对于复杂筛选表单等高交互组件，发送大量 HTML 片段可能导致响应变慢。

hackernews · Ralfp · 7月27日 09:58 · [社区讨论](https://news.ycombinator.com/item?id=49067301)

**背景**: HTMX 是由 Carson Gross 创建的开源 JavaScript 库，通过 HTML 属性实现动态 Web 交互，遵循超媒体驱动方法。它与 React 等依赖虚拟 DOM 和客户端状态管理的组件化框架形成对比。Misago 项目是从重型客户端框架迁移到服务端驱动交互的真实案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">Htmx</a></li>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>

</ul>
</details>

**社区讨论**: 社区反馈不一：james2doyle 报告称 HTMX 在处理复杂可筛选列表时因 HTML 负载过大出现性能问题；而 snorremd 和 prologic 赞扬其适合论坛和通用 Web 应用，尤其是在配合服务端事件和 Tailwind 等实用 CSS 框架时。

**标签**: `#HTMX`, `#React`, `#Web Development`, `#Server-Side Rendering`, `#JavaScript Frameworks`

---

<a id="item-7"></a>
## [《Paged Out》第 9 期：黑客好奇的技术杂志](https://pagedout.institute/download/PagedOut_009.pdf) ⭐️ 8.0/10

《Paged Out》第 9 期已作为免费 PDF 发布，内容涵盖亚像素渲染和可计算平铺等深层次技术文章。 该杂志延续了如 2600 和 Phrack 等黑客杂志的传统，提供高质量、深度的技术内容，激发了工程师和黑客的好奇心与社区参与。 值得注意的文章包括《C 语言婴儿步》、第 30 页引用的《亚像素动物园》，以及一篇未署名地重新发现王浩关于可计算平铺工作的文章，该工作将停机问题与多米诺问题联系起来。

hackernews · laurensr · 7月27日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49070138)

**背景**: 亚像素渲染利用红、绿、蓝单个子像素来提高有效分辨率，常用于 LCD 屏幕上的文字渲染。可计算平铺由王浩在 20 世纪 60 年代研究，表明多米诺问题（一组瓷砖是否能平铺平面）等价于停机问题，从而将平铺模式与计算联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Subpixel_rendering">Subpixel rendering</a></li>
<li><a href="https://dl.ifip.org/db/conf/ifipTCS/ifipTCS2008/LafitteW08.pdf">Computability of Tilings .</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，称赞该杂志为“现代 2600”和“设计精美”。一位用户觉得《C 语言婴儿步》很有趣，另一位指出可计算平铺文章未注明地重新发现了王浩的工作，对署名问题提出了批评。

**标签**: `#technical zine`, `#hacker culture`, `#programming`, `#low-level computing`, `#magazine`

---

<a id="item-8"></a>
## [观点指南评选 AI 工具，转向智能体系统](https://simonwillison.net/2026/Jul/27/an-opinionated-guide-to-which-ai-to-use-to-do-stuff/#atom-everything) ⭐️ 8.0/10

Ethan Mollick 更新了 AI 工具选择指南，现在更强调智能体系统而非聊天，并将 Gemini 移除，因为它在 Codex/ChatGPT Work/Cowork 类别中缺乏直接竞品。 该指南为专业人士选择 AI 工具提供了实用的最新建议，反映了行业向自主、多步骤智能体系统的快速转变，这类系统能一次性完成相当于数小时的人类工作。 关键模式包括 OpenAI 的 ChatGPT Work 和 Codex，以及 Anthropic 的 Claude Cowork 和 Code；命名令人困惑，且移动端与桌面端能力不同。

rss · Simon Willison · 7月27日 21:55

**背景**: 智能体 AI 系统无需每步人工审批，即可自主追求目标，与单轮聊天模型形成对比。该指南反映了 AI 能够访问计算机并执行复杂工作流的趋势，超越了简单的问答。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://remolda.com/en/glossary/agentic-ai">Agentic AI — definition | Remolda</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://support.google.com/gemini/answer/17094507?hl=en-CA&co=GENIE.Platform=Android">Use Gemini Spark to manage your tasks & workflows in Gemini Apps...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLMs`, `#agentic systems`, `#model comparison`, `#opinionated guide`

---

<a id="item-9"></a>
## [六个前沿大模型在个人基准测试中一致呈现左倾偏见](https://www.reddit.com/r/MachineLearning/comments/1v8fnzw/evaluated_6_frontier_llms_gpt54_claude_sonnet_46/) ⭐️ 8.0/10

在一项个人评估项目中，对六个前沿大语言模型——GPT-5.4、Claude Sonnet 4.6、Claude Opus 4.7、Gemini Pro、Gemini Flash 和 Grok 4.3——在八个偏见与公平基准测试（共约 20,600 个样本）上进行了测试，结果显示所有模型均表现出左倾政治偏见，其中 Grok 的行为与其自称的右倾倾向相矛盾。 该基准测试提供了前沿大语言模型中系统性政治偏见的独立实证证据，对 AI 公平性研究和模型部署决策至关重要，尤其是当这些模型越来越多地用于内容审核和政策应用时。 值得注意的是，在政治立场测试中，Grok 自称右倾，但在实际内容分类和政策问题回答中表现出左倾行为；在 BBQ 种族相关问题上，拒绝率从 GPT-5.4 的 20.3%到 Claude Sonnet 4.6 和 Gemini Pro 的约 5%不等。

reddit · r/MachineLearning · /u/marggggggggg · 7月27日 22:37

**背景**: 偏见基准测试如 WinoBias（共指消解中的性别偏见）、BBQ（问答偏差基准）和 SeeGULL（具有地理文化覆盖的刻板印象数据集）旨在检测语言模型中的有害偏见。政治立场测试是一个两轴政治意识形态测试，测量经济左-右和社会威权-自由维度。理解模型偏见对于负责任的 AI 部署至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/winobias">WinoBias : Gender Bias in Coreference Benchmark</a></li>
<li><a href="https://github.com/google-research-datasets/seegull">GitHub - google-research- datasets / seegull : SeeGULL is...</a></li>
<li><a href="https://en.wikipedia.org/wiki/The_Political_Compass">The Political Compass - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#bias`, `#fairness`, `#benchmarking`, `#AI ethics`

---

<a id="item-10"></a>
## [长鑫科技科创板首日暴涨 471%，创最大 IPO](https://www.stcn.com/article/detail/4042119.html) ⭐️ 8.0/10

国产存储龙头长鑫科技（CXMT）在科创板上市首日高开 471.59%，报 49.5 元/股，发行价为 8.66 元/股，成为科创板史上最大 IPO。 此次创纪录的 IPO 凸显了中国在存储芯片领域推动国产替代的决心，有望增强投资者对本土芯片企业的信心。长鑫科技将获得巨额资金扩大产能，与三星、SK 海力士等全球巨头竞争。 长鑫科技本次实际募集资金约 579 亿元，若超额配售选择权（绿鞋）全额行使，预计募资总额约 666 亿元，超过 2020 年中芯国际 532 亿元的纪录。公司预计 2026 年上半年归母净利润 500 亿至 570 亿元，同比大幅扭亏。

telegram · zaihuapd · 7月27日 01:29

**背景**: 科创板是上海证券交易所旗下的一个板块，类似纳斯达克，旨在支持科技创新企业上市，上市条件相对宽松。超额配售选择权（绿鞋）允许主承销商在需求强劲时额外发行股票，以稳定上市后股价。长鑫科技是中国 DRAM（动态随机存取存储器）领域的龙头企业，对降低对外国存储芯片的依赖至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hstong.com/sns/status/long/16263179804177497">捷利交易宝 | 【港股打新学堂】第10期： 超 额 配 售 选 择 权 与发 售 量调整 权</a></li>
<li><a href="https://cj.sina.com.cn/articles/view/7879922977/1d5ae152101901akqi?froms=ggmp&vt=4">cj.sina.com.cn/articles/view/7879922977/1d5ae152101901akqi?froms...</a></li>

</ul>
</details>

**标签**: `#半导体`, `#IPO`, `#存储芯片`, `#科创板`, `#国产替代`

---

<a id="item-11"></a>
## [谷歌预告 Gemini 4：迄今最雄心预训练，年底发布](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 8.0/10

谷歌 CEO Sundar Pichai 在 2026 年第二季度财报电话会议上宣布，下一代大模型 Gemini 4 已投入训练，称其为公司迄今为止最具雄心的预训练项目，预计于 2026 年 11 月或 12 月发布。 Gemini 4 代表着谷歌在 AI 前沿领域的持续发力，其发布可能为大语言模型树立新标杆，影响更广泛的 AI 生态系统以及与 OpenAI 等竞争对手的竞争格局。 该模型仍在预训练阶段，Pichai 表示谷歌将优先将算力分配给前沿 AGI 研发。此外，Gemini 3.x Flash 系列将保持几乎每月一次的迭代频率，重点提升智能编码等能力。

telegram · zaihuapd · 7月27日 04:06

**背景**: Gemini 是谷歌的大语言模型系列，与 OpenAI 的 GPT-4 等模型竞争。预训练是指在大量数据上训练模型以学习语言模式，随后进行微调以适用于特定任务。谷歌一直在迭代 Gemini，之前有 Gemini 1.5 和 2.0 等版本，而 Gemini 4 被称为迄今为止最具雄心的版本。

**标签**: `#Google`, `#Gemini`, `#AI`, `#LLM`, `#pre-training`

---

<a id="item-12"></a>
## [中方驳美方因 AI 蒸馏制裁威胁](https://www.mofcom.gov.cn/syxwfb/art/2026/art_7f1622463a7c48ef9fad600ce0ef702f.html) ⭐️ 8.0/10

7 月 27 日，中国商务部驳斥了美国拟以模型蒸馏和知识产权盗窃为由调查并制裁中国人工智能企业的计划，指出蒸馏是行业广泛使用的技术，美国企业也在蒸馏中国模型。 这一回应凸显了围绕人工智能技术日益加剧的地缘政治紧张局势，可能升级贸易冲突，从而扰乱全球 AI 合作和开源模型共享。 商务部指出，近 200 家美国初创企业已呼吁政府不要限制访问中国开源模型，并警告称，如果中方利益受到实质性损害，将采取必要措施维护企业合法权益。

telegram · zaihuapd · 7月27日 11:01

**背景**: 模型蒸馏是一种让较小模型模仿较大、更强模型的技术，常用于降低计算成本。这是 AI 开发中的常见做法，许多公司和研究人员使用开源模型进行蒸馏。美国担忧中国企业利用蒸馏窃取美国 AI 模型的知识产权，而中方认为这是行业标准做法且具有互惠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.volcengine.com/articles/7478160196578377737">大模型" 蒸 馏 "是什么？ - 文章 - 开发者社区 - 火山引擎</a></li>

</ul>
</details>

**标签**: `#AI`, `#geopolitics`, `#model distillation`, `#trade war`

---

<a id="item-13"></a>
## [中国开始量产国产 DUV 光刻机](https://www.theinformation.com/articles/china-starts-mass-producing-homegrown-duv-chipmaking-tools-advance-local-chip-industry) ⭐️ 8.0/10

中国已开始大规模生产自主研发的浸没式深紫外（DUV）光刻机，计划今年生产约 5 台、2027 年约 20 台，将交付中芯国际、华虹半导体等国内厂商。 这标志着中国在减少对外国芯片制造设备依赖方面迈出了重要一步，可能挑战 ASML 的主导地位，尤其在西方收紧出口限制的情况下。 国产 DUV 设备在性能和可靠性上仍落后于 ASML，芯片商需数月测试；部分关键部件来自日本，今年本地供应链延误已影响进度。

telegram · zaihuapd · 7月27日 14:10

**背景**: DUV 光刻机是半导体制造中用于在硅片上印制电路的核心设备。浸没式光刻技术在镜头和晶圆之间使用液体（通常是水）来提高分辨率，可实现 45 纳米以下的特征尺寸。ASML 目前在先进光刻机市场占据主导地位，提供 DUV 和 EUV 设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://min.news/en/digital/0f6b59b4f9f4346928c71bc30fa0125e.html">DUV lithography machine has changed! What are the roads for China...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Immersion_lithography">Immersion lithography</a></li>
<li><a href="https://lifeboat.com/blog/2025/10/netherlands-tightens-export-restrictions-on-microchip-machines-mainly-targeting-asml">Netherlands tightens export restrictions on microchip machines , mainly...</a></li>

</ul>
</details>

**标签**: `#chip manufacturing`, `#DUV lithography`, `#China semiconductor`, `#ASML`, `#geopolitics`

---