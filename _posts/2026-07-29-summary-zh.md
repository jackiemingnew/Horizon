---
layout: default
title: "Horizon Summary: 2026-07-29 (ZH)"
date: 2026-07-29
lang: zh
---

> 从 43 条内容中筛选出 9 条重要资讯。

---

1. [开源引擎在 M 系列 Mac 上仅用 2GB 内存运行 Gemma 4 26B](#item-1) ⭐️ 9.0/10
2. [通过 Copilot 在 Word 中自我复制的 AI 蠕虫攻击](#item-2) ⭐️ 9.0/10
3. [月之暗面融资 35 亿美元，估值 350 亿美元](#item-3) ⭐️ 9.0/10
4. [Mitchell Hashimoto 基于开源 libghostty 创办 Superlogical](#item-4) ⭐️ 8.0/10
5. [Handbook.md 研究显示长政策文档无法可靠约束 AI 代理](#item-5) ⭐️ 8.0/10
6. [马修·格林：AI 破解密码的完美时机](#item-6) ⭐️ 8.0/10
7. [用 Claude 发现加密算法弱点](#item-7) ⭐️ 8.0/10
8. [俄罗斯指控 Telegram 创始人杜罗夫协助恐怖活动，发出国际通缉](#item-8) ⭐️ 8.0/10
9. [报告称 Hugging Face 广泛用于生成深度伪造裸照](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [开源引擎在 M 系列 Mac 上仅用 2GB 内存运行 Gemma 4 26B](https://github.com/drumih/turbo-fieldfare) ⭐️ 9.0/10

TurboFieldfare，一个用 Swift 和 Metal 编写的开源推理引擎，通过从 SSD 流式传输路由专家，在任意 M 系列 Mac 上仅用约 2GB 内存运行 4 位量化的 Gemma 4 26B-A4B-IT 模型。 这一突破使得在低内存 Mac（8GB 或 16GB）上运行 26B 参数的混合专家模型成为可能，而此前这些设备无法容纳该模型，从而无需昂贵硬件升级即可普及端侧 AI 能力。 该引擎在 8GB M2 MacBook Air 上达到 5–6 tok/s，在 M5 MacBook Pro 上达到 31–35 tok/s，通过小型专家缓存和有界并行 pread 将 SSD 读取与 GPU 计算重叠。它还包含一个实验性的 OpenAI 兼容本地服务器，支持流式输出和工具调用。

hackernews · gitpusher42 · 7月29日 15:05 · [社区讨论](https://news.ycombinator.com/item?id=49098510)

**背景**: 像 Gemma 4 这样的混合专家（MoE）模型采用稀疏架构，每个 token 只激活一部分“专家”，从而减少计算量。该模型的 4 位量化权重约占用 14GB，但传统推理需要将所有权重加载到 RAM 中。TurboFieldfare 仅将共享层和 KV 缓存（存储先前的注意力键/值）保留在 RAM 中，同时按需从 SSD 流式传输所需的专家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2202.09368">[2202.09368] Mixture-of-Experts with Expert Choice Routing Intro to Routing: Mixture-of-Experts and Expert Choice [2510.04694] Multilingual Routing in Mixture-of-Experts Mixture-of-Experts with Expert Choice Routing - NeurIPS Mixture-of-Experts with Expert Choice Routing - Google Research Top-K Routing: Expert Selection in Mixture of Experts Models Parameter-Efficient Routed Fine-Tuning: Mixture-of-Experts ...</a></li>
<li><a href="https://huggingface.co/blog/not-lain/kv-caching">KV Caching Explained: Optimizing Transformer Inference Efficiency</a></li>
<li><a href="https://www.emergentmind.com/topics/4-bit-model-quantization">4-Bit Model Quantization</a></li>

</ul>
</details>

**社区讨论**: 社区成员对这一工程壮举印象深刻，有人指出这与 llama.cpp 中基于 mmap 的方法有相似之处。一位用户分享了针对旧版 macOS 的编译调整，另一位询问在 Jetson 等非 Mac 平台上的运行情况。整体反馈积极，称赞这一实用的端侧 AI 进展。

**标签**: `#inference engine`, `#on-device AI`, `#Gemma 4`, `#model compression`, `#Swift/Metal`

---

<a id="item-2"></a>
## [通过 Copilot 在 Word 中自我复制的 AI 蠕虫攻击](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 9.0/10

安全研究员 Håkon Måløy 发现了一种提示注入变体，其中隐藏在 Word 文档中的指令会促使 Microsoft Copilot 将攻击传播到新文档，形成自我复制的蠕虫。该技术已在 144 天前负责任地向 Microsoft 披露，但目前尚无全面缓解措施。 这标志着首次展示利用 AI 文档助手的自我复制蠕虫，对广泛部署 Copilot 的企业环境构成重大安全威胁。它凸显了 LLM 混淆指令与数据的根本脆弱性，可能导致大规模数据泄露和恶意软件传播。 该攻击利用了 Copilot 无法区分用户提示与文档内容的漏洞；隐藏指令（例如白色文本）被解释为命令，导致 Copilot 修改文档并将指令复制到新文件中，实现蠕虫式传播。由于当前 AI 架构本质上混淆了指令与数据，此类攻击尚未得到缓解。

rss · Simon Willison · 7月29日 18:43

**背景**: 提示注入是一种网络安全攻击手段，恶意输入会导致 LLM 产生意外行为，通常通过诱使模型忽略原始指令来实现。传统的提示注入攻击需要用户交互，而这一新变体增加了自我复制功能，使其成为蠕虫。此前 IBM 和多伦多大学关于 AI 蠕虫的研究已在生成式 AI 系统中展示了类似能力，但这是首次专门针对 Microsoft Word 的 Copilot 集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://www.ibm.com/think/insights/malicious-ai-worm-targeting-generative-ai">Researchers develop malicious AI ‘worm’ targeting generative AI systems | IBM</a></li>
<li><a href="https://www.utoronto.ca/news/u-t-researchers-demonstrate-ai-worm-could-target-any-online-device">U of T researchers demonstrate AI worm could target any online device | University of Toronto</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者表达了深切担忧，认为只要 AI 无法区分指令与数据，此类攻击就从根本上无法修复。一些用户报告已卸载 Copilot 并在本地禁用 AI 功能。其他人指出，类似白色文本的混淆技术仍然有效，显示了缓解措施的困难。

**标签**: `#prompt injection`, `#security`, `#AI`, `#Microsoft Word`, `#worm`

---

<a id="item-3"></a>
## [月之暗面融资 35 亿美元，估值 350 亿美元](https://www.bloomberg.com/news/articles/2026-07-29/china-s-moonshot-ai-passes-funding-goal-to-hit-35-billion-value) ⭐️ 9.0/10

月之暗面（Moonshot AI）完成一轮 35 亿美元融资，投后估值达 350 亿美元，远超最初 10 亿至 20 亿美元的目标。此轮融资由突破性模型 Kimi K3 推动，该模型性能接近 OpenAI 和 Anthropic 的前沿水平。 巨额融资和估值表明中国 AI 公司能够产出达到世界水平的模型并冲击全球市场，Kimi K3 的发布引发了科技股抛售，让人想起 2025 年初的'DeepSeek 时刻'。 Kimi K3 拥有 2.8 万亿参数，采用名为 Kimi Delta Attention (KDA)的混合线性注意力机制，上下文窗口达 100 万 token。月之暗面已启动新一轮融资，pre-money 估值 500 亿美元，并计划最早今年在香港 IPO。

telegram · zaihuapd · 7月29日 10:12

**背景**: 月之暗面是一家中国 AI 初创公司，开发了 Kimi 聊天机器人和大型语言模型。其 2023 年的第一个版本以支持 12.8 万 token 而闻名。开源权重的 Kimi K2 于 2025 年 7 月发布，旗舰模型 Kimi K3 于 2026 年 7 月 16 日公开发布并承诺开放源码。'DeepSeek 时刻'一词在 2025 年初 DeepSeek 的 R1 模型引发股市动荡后被提出，Kimi K3 类似的市场影响使该术语再次流行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and What the Open Weights Mean for the Community</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#Moonshot AI`, `#Kimi K3`, `#LLM`

---

<a id="item-4"></a>
## [Mitchell Hashimoto 基于开源 libghostty 创办 Superlogical](https://www.superlogical.com/) ⭐️ 8.0/10

Mitchell Hashimoto 宣布成立新公司 Superlogical，该公司将基于开源库 libghostty 构建商业终端应用，此前他已将该库捐献给了非营利组织。 此举展示了一种可持续的开源商业模式：公司在社区拥有的基础库之上构建专有产品，同时确保库本身对所有人免费。这可能激励其他开发者效仿，将核心基础设施捐给非营利组织，同时将上层应用商业化。 Superlogical 将与其他用户一样基于 MIT 许可使用 libghostty，并计划将共享终端工作上游化，使整个生态系统受益。该库源自 Hashimoto 创建的快速 GPU 加速终端模拟器 Ghostty。

hackernews · yan · 7月29日 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49098965)

**背景**: Ghostty 是一个快速、功能丰富、跨平台的终端模拟器，使用平台原生 UI 和 GPU 加速。libghostty 是 Ghostty 的核心库，负责 VT 序列解析、光标管理和文本重排。Mitchell Hashimoto 是 HashiCorp 及 Terraform 等工具的创始人，在创办 Superlogical 之前已将 Ghostty 捐赠给非营利组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty-org/ghostty: 👻 Ghostty is a fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.</a></li>

</ul>
</details>

**社区讨论**: 社区成员赞赏将所有权移交给非营利组织并在此基础上构建公司的模式，称之为一种干净的做法。有人将其架构与历史上的组件技术（如 OLE/COM）相比较，也有人对模糊的标题表示不满，倾向于更具信息性的标题。

**标签**: `#open-source`, `#terminal`, `#business-model`, `#ghostty`, `#mitchell-hashimoto`

---

<a id="item-5"></a>
## [Handbook.md 研究显示长政策文档无法可靠约束 AI 代理](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

一项新的 arXiv 研究（标题为'handbook.md'）表明，长政策文档无法可靠地约束 AI 代理，揭示了当前长上下文模型和量化技术的根本局限性。 这一发现挑战了 AI 代理能够有效遵循长篇政策指令的普遍假设，对在金融、医疗和法律合规等受监管环境中部署代理具有重大影响。 该研究强调，模型 KV 缓存的极端量化以及设计不佳的推理采样器加剧了这一问题，即使拥有 100 万 token 上下文窗口的模型在实践中也会失败。

hackernews · spIrr · 7月29日 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49096969)

**背景**: 大型语言模型（LLM）具有有限的上下文窗口，决定了它们一次能处理多少 token。为了降低内存和计算成本，模型通常使用量化技术，降低权重和激活值的精度。长政策文档超出有效上下文容量，导致代理'遗忘'或错误应用指令。诸如 RAG 和内存缓冲等技术被提出来绕过这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/ai/what-is-quantization/">What is quantization in machine learning?</a></li>
<li><a href="https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents">Effective context engineering for AI agents \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区讨论（275 分，177 条评论）基本同意该研究的结论，用户指出长上下文模型夸大了自身能力。一位用户将失败归因于极端量化和不良采样器，并提倡本地推理。另一位用户将 AI 代理的失误与人类在遵循长政策时的局限性相类比。

**标签**: `#AI agents`, `#long context`, `#policy compliance`, `#model limitations`, `#arXiv`

---

<a id="item-6"></a>
## [马修·格林：AI 破解密码的完美时机](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

马修·格林指出，我们正处于从传统密码学向后量子算法过渡的历史性时刻，并认为这是 AI 推进密码分析的绝佳时机。他提到了 HAWK 等正在考虑的标准，以及 AI 可能削弱或增强对新难题信心的可能性。 如果 AI 能够成功破解或验证后量子候选算法，将直接影响未来全球加密标准的安全性。这一评论对决定采用哪些算法的研究人员和政策制定者至关重要。 格林特别提到了 HAWK——一种参与 NIST PQC 标准化过程的基于格的签名方案，并引用了 Impagliazzo 的“Minicrypt”世界。他认为，假设 AI 不破解所有难题，AI 驱动的密码分析可以产生更强大的文献。

rss · Simon Willison · 7月29日 18:18

**背景**: 后量子密码学（PQC）旨在创建能够抵御量子计算机攻击的加密方案，量子计算机可能破解当前的 RSA 和 ECC 算法。NIST 正在主导标准化工作，HAWK 是候选之一。Impagliazzo 的五世界理论对可能的计算复杂性场景进行了分类；Minicrypt 是一个存在单向函数但公钥密码学不可能的世界。向 PQC 的过渡是一项庞大的全球工程，使得严格的密码分析变得紧迫。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nist.gov/pqc">Post-quantum cryptography | NIST</a></li>
<li><a href="https://hawk-sign.info/">Hawk</a></li>
<li><a href="https://blog.computationalcomplexity.org/2004/06/impagliazzos-five-worlds.html">Computational Complexity: Impagliazzo 's Five Worlds</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#AI`, `#cryptanalysis`, `#security`

---

<a id="item-7"></a>
## [用 Claude 发现加密算法弱点](https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/#atom-everything) ⭐️ 8.0/10

Anthropic 的研究人员使用他们的 Claude Mythos 模型，发现了后量子签名方案 HAWK 和减轮版 AES 中的数学缺陷，该工作耗时 60 小时，API 费用约 10 万美元。 这表明大型语言模型能够协助高级密码学研究，可能加速漏洞发现过程，并减少仅依赖人类直觉的需求。该工作还引入了新的基准 CryptanalysisBench，用于评估 LLM 在密码分析中的能力。 发现的弱点对当前计算机系统无实际影响，但研究人员分享了所用提示词，其中包括人类指导以推动模型寻找更有价值的发现。相关论文《CryptanalysisBench: Can LLMs do Cryptanalysis?》描述了与苏黎世联邦理工学院、特拉维夫大学和海法大学合作创建的评估框架。

rss · Simon Willison · 7月28日 22:45

**背景**: 密码哈希函数是数字签名和密码存储中使用的单向数学运算，具有原像抗性和碰撞抗性等特性。HAWK 是一种基于格的后量子数字签名方案，已提交至 NIST 后量子密码标准化流程，旨在抵抗经典计算机和量子计算机的攻击。AES（高级加密标准）是一种对称分组密码，密钥长度可为 128、192 或 256 比特，轮数相应变化（AES-128 为 10 轮）；攻击减轮版本是研究密码安全裕度的常见方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">Advanced Encryption Standard - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hash_(cryptography)">Hash (cryptography)</a></li>
<li><a href="https://hawk-sign.info/">Hawk</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#AI`, `#Claude`, `#security`, `#research`

---

<a id="item-8"></a>
## [俄罗斯指控 Telegram 创始人杜罗夫协助恐怖活动，发出国际通缉](https://www.interfax.ru/russia/1106228) ⭐️ 8.0/10

俄罗斯联邦安全局（FSB）依据《刑法》第 205.1 条第 1.1 款，对 Telegram 创始人帕维尔·杜罗夫提起协助恐怖活动的刑事指控，并将其列入国际通缉名单。 此举标志着俄罗斯对大型科技平台法律压力的重大升级，引发了对言论自由和平台责任的担忧。这可能为政府针对科技领袖的内容审核决策制定先例。 FSB 指控 Telegram 管理层拒绝删除被乌克兰情报机构及恐怖组织用于协调袭击的频道和机器人，导致人员伤亡和数十亿卢布损失。杜罗夫是根据一项具体的反恐条款被起诉的。

telegram · zaihuapd · 7月29日 05:56

**背景**: Telegram 是由帕维尔·杜罗夫创立的加密消息应用，他因用户数据争议于 2014 年离开俄罗斯。该平台曾因加密和内容审核问题与俄罗斯当局关系紧张。《刑法》第 205.1 条涉及协助恐怖活动，刑罚严厉。

**标签**: `#Telegram`, `#Pavel Durov`, `#Russia`, `#terrorism`, `#legal`

---

<a id="item-9"></a>
## [报告称 Hugging Face 广泛用于生成深度伪造裸照](https://www.theverge.com/ai-artificial-intelligence/971723/hugging-face-nudify-deepfake-undress-women-children) ⭐️ 8.0/10

欧洲非营利组织 AI Forensics 于 7 月 28 日发布报告，指出 Hugging Face 上排名前九的图像编辑模型中有七个能轻松用于生成非自愿深度伪造裸照，包括儿童。研究人员设置的蜜罐在 7 天内收到逾 1000 条请求，其中 73%涉及性内容，近 7%针对未成年人。 这暴露了开源 AI 平台在内容安全和模型滥用方面的严重漏洞，引发了紧迫的伦理与法律问题。该发现强调了平台责任，可能影响女性和儿童的隐私与安全。 报告指出 Hugging Face 几乎没有平台级防护措施，与其禁止非自愿性内容及儿童裸照的政策相矛盾。AI Forensics 建议增加提示词过滤与输出扫描机制，以阻止有害图像生成。

telegram · zaihuapd · 7月29日 08:20

**背景**: Hugging Face 是流行的开源模型托管和分享平台。深度伪造技术利用 AI 生成逼真的虚假图像或视频。蜜罐是一种网络安全工具，用于诱捕攻击者以监控其行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7642531705475776546">网 络 安 全 蜜 罐 管理系统（ HoneyPot ...</a></li>
<li><a href="https://yeasy.gitbook.io/agentic_ai_guide/di-si-bu-fen-wei-lai-zhan-wang/11_future/11.1_security">11.1 安全边界：提示词注入与防御策略 | 智能体AI 权威指南 | Agentic AI Guide</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#deepfake`, `#Hugging Face`, `#content moderation`, `#platform safety`

---