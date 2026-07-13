---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> 从 34 条内容中筛选出 4 条重要资讯。

---

1. [Claude Code 与 OpenCode 的 Token 开销对比](#item-1) ⭐️ 8.0/10
2. [LLM 创造价值，但前沿实验室可能无法获得它](#item-2) ⭐️ 8.0/10
3. [半侵入式脑机接口 NEO 助瘫痪患者重新握笔](#item-3) ⭐️ 8.0/10
4. [Grok Build CLI 紧急更新关闭代码上传](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Code 与 OpenCode 的 Token 开销对比](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 8.0/10

一项研究发现，Claude Code 每次请求会发送约 33,000 token 的开销，而 OpenCode 仅发送约 7,000 token，表明 Claude Code 在 token 使用上存在显著的低效。 这种 token 开销直接增加了用户成本并降低了工作流效率，因为许多开发者按 token 付费或拥有有限的订阅。这一发现可能促使用户转向更高效的替代方案，如 OpenCode。 该研究记录了每个工具与 Anthropic 端点之间的请求，捕获了所有请求和使用块。它指出 Claude Code 的低效源于其缓存策略和 harness token 使用，不过作者承认存在一个注意事项，并计划进行后续研究以提供定性结果。

hackernews · systima · 7月12日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48883275)

**背景**: 像 Claude Code 和 OpenCode 这样的 AI 编码助手使用语言模型生成代码，并根据处理的 token 数量产生 token 成本。'Harness token' 是指系统提示和超出用户实际输入的开销 token。社区已经观察到一些工具 aggressively 消耗 token，导致 'tokenflation'。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zbuild.io/resources/news/opencode-vs-claude-code-vs-cursor-2026">OpenCode vs Claude Code vs Cursor in 2026... | ZBuild</a></li>
<li><a href="https://thoughts.jock.pl/p/ai-coding-harness-agents-2026">Claude Code vs Codex vs Aider vs OpenCode vs Pi 2026</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，Claude Code 中的子代理可能会消耗大量 token，一些用户怀疑 Anthropic 故意夸大 token 使用量以推动订阅。作者还回应了关于衡量正确指标的批评，并计划添加定性比较。

**标签**: `#AI coding tools`, `#token efficiency`, `#Claude Code`, `#OpenCode`, `#cost optimization`

---

<a id="item-2"></a>
## [LLM 创造价值，但前沿实验室可能无法获得它](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html) ⭐️ 8.0/10

George Hotz 发表了一篇博客文章，认为虽然 LLM 产生了实际的生产力提升和价值，但像 OpenAI 和 Anthropic 这样的前沿 AI 实验室被高估了，因为它们可能无法捕获这些价值。这篇文章挑战了这些公司基于炒作的价值评估。 这一批评意义重大，因为它质疑了前沿 AI 实验室的基本商业模式，指出即使 AI 改变了经济，实验室本身也可能无法盈利。这加剧了关于 AI 炒作、开源与专有模型以及真正价值所在之处的持续辩论。 Hotz 特别指出，LLM 带来的广泛生产力提升并不一定会转化为构建它们的实验室的收入，因为许多价值被用户和下游应用程序捕获。他还注意到进步的快速步伐，像 Sonnet 4 和 Opus 4.5 这样的模型不断改变人们的看法。

hackernews · therepanic · 7月12日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48883343)

**背景**: “价值捕获”一词指的是公司将其创造的价值转化为利润的能力。在科技领域，许多创新（例如互联网）创造了巨大价值，但开创它们的公司并不总能捕获这些价值。像 OpenAI 和 Anthropic 这样的前沿实验室以 AGI 的承诺筹集了数十亿美元，但它们的收入模式依赖于订阅费和代币销售。Hotz 认为，开源模型和用户驱动的分支可能削弱它们捕获价值的能力。

**社区讨论**: 评论者大多同意 Hotz 关于价值捕获的论点，SwellJoe 称其是对前沿实验室行为的精辟解释。其他人指出，生产力提升是真实的，但通常以私有的、一次性软件的形式出现，因此难以衡量。有些人表达了对开源可持续性的担忧，因为容易的分叉减少了向上游贡献的动力。

**标签**: `#LLMs`, `#AI hype`, `#value capture`, `#productivity`, `#open source`

---

<a id="item-3"></a>
## [半侵入式脑机接口 NEO 助瘫痪患者重新握笔](https://www.zaobao.com.sg/news/china/story20260712-9199066) ⭐️ 8.0/10

由博睿康和清华大学共同开发的半侵入式脑机接口系统 NEO 已在中国获批上市，并通过一枚硬币大小的无线植入物，成功帮助一名 36 岁高位截瘫患者重新实现抓握和书写能力。 这标志着中国首款获批上市的植入式脑机接口产品的重要里程碑，可能为数千名颈段脊髓损伤瘫痪患者提供新的康复途径。 截至 2026 年 3 月 13 日，NEO 已完成 36 例临床手术并取得注册证；中国已有 32 位颈段脊髓损伤患者接受了半侵入式脑机接口植入。

telegram · zaihuapd · 7月12日 14:39

**背景**: 脑机接口分为侵入式、非侵入式和半侵入式三类。像 NEO 这样的半侵入式脑机接口将电极放置在脑表面（皮层脑电图）而非深入组织，在信号质量与风险降低之间取得平衡。这种方法被认为比全侵入式系统更安全，同时提供比非侵入式更高的信号保真度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/minds-interface-bridging-thought-technology-bci-neuranet-ai-otbae">The Mind's Interface : Bridging Thought and Technology with BCI</a></li>
<li><a href="https://inf.news/en/tech/a7581e47af3584317d16626ad7fd1556.html">Brain-computer interface, waiting for the birth of a medical device - iNEWS</a></li>
<li><a href="https://www.sango-automation.com/news/the-first-clinical-trial-implantation-of-brain-82641280.html">The First Clinical Trial Implantation Of Brain-computer Interface Products in Shanghai Was Successfully Completed - Industry News - News</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#medical technology`, `#neurotechnology`, `#China`, `#rehabilitation`

---

<a id="item-4"></a>
## [Grok Build CLI 紧急更新关闭代码上传](https://www.reddit.com/r/LocalLLaMA/comments/1ut7tis/comment/ox4zamk/?utm_source=share&amp;utm_medium=web3x&amp;utm_name=web3xcss&amp;utm_term=1&amp;utm_content=share_button) ⭐️ 8.0/10

7 月 13 日，Grok 服务器端新增了一个 disable_codebase_upload 字段并返回 true，从而禁用了代码上传功能。此前有研究员披露，该 CLI 默认会上传整个代码库及密钥文件。 此次更新解决了一个严重的隐私和安全漏洞，该漏洞可能导致敏感代码和凭据泄露。它展示了项目方对用户关切的快速响应，但也凸显了 AI 编码工具在默认行为上需要更高的透明度。 服务器端字段名为 disable_codebase_upload，默认值为 true，意味着现在所有 Grok Build CLI 会话的代码上传均被阻止。上传的具体机制未公开详细说明，但研究员的披露指出默认会上传包括密钥文件在内的整个代码库。

telegram · zaihuapd · 7月13日 00:52

**背景**: Grok Build CLI 是一款基于终端的编程代理，连接到 xAI 的 Grok API，旨在辅助完成复杂编程任务。它最近更新为由 Grok 4.5 驱动。默认情况下，该 CLI 会上传用户的整个代码库及敏感文件，这构成了显著的隐私风险。这一事件与其他 AI 编程助手无意中暴露专有代码的案例类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>

</ul>
</details>

**标签**: `#Grok`, `#AI Safety`, `#Privacy`, `#CLI Update`, `#Code Leak`

---