---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 35 条内容中筛选出 3 条重要资讯。

---

1. [Shopify 将移动应用从 React Native 迁回原生 Swift 和 Kotlin](#item-1) ⭐️ 8.0/10
2. [研究者质疑能否放心把未发表的数学成果交给 OpenAI](#item-2) ⭐️ 8.0/10
3. [微软将 Rust 列为内部开发的一级语言](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Shopify 将移动应用从 React Native 迁回原生 Swift 和 Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 宣布将其旗舰移动应用从 React Native 迁移回完全原生的 iOS 和 Android 代码库，分别使用 Swift 和 Kotlin 编写。这篇工程博客文章在 Hacker News 上引发了大规模讨论（约 670 分、447 条评论），话题涵盖跨平台框架、迁移成本，以及大语言模型辅助重写是否让此类迁移变得更便宜。 Shopify 是放弃 React Native 的最知名公司之一，其决定为整个行业重新回归原生移动开发的趋势增添了动力。由于它是一个具有全球规模的电商大型应用，这一举动向其他团队释放出信号：跨平台带来的节省可能抵不上“最低共同标准”式用户体验和长期维护的代价。 讨论指出，该应用拥有庞大且成熟的功能面，社区成员提到现代大语言模型（例如配合 Maestro 等 UI 测试工具的 codex 类编码智能体）可以自动完成大量机械化的移植工作，但打磨细节和平台专属优化仍需人工投入。评论者也警告说，所谓“大语言模型让迁移变得极其便宜”的说法被夸大了，因为在 2026 年之前就有工程师在不借助大语言模型的情况下完成了类似的 RN 到原生重写。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 是 Meta 推出的开源 UI 框架，允许开发者用 JavaScript 和 React 为 iOS、Android 及其他平台构建应用，并在各平台间共享同一套代码库。Swift 是苹果用于 iOS 的原生语言，Kotlin 则是谷歌为 Android 提供一等支持的语言；分别使用它们可以完全访问平台 API 并发挥最佳性能，但需要维护两套独立的代码库和团队。近二十年来，业界一直在争论跨平台框架是否真能减少工程人力，还是仅仅以更差的单平台体验来换取人员成本的节省。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native - Wikipedia</a></li>
<li><a href="https://reactnative.dev/">React Native · Learn once, write anywhere</a></li>
<li><a href="https://arxiv.org/abs/2410.08806">[2410.08806] Don't Transform the Code, Code the Transforms: Towards Precise Code Rewriting using LLMs</a></li>

</ul>
</details>

**社区讨论**: 总体情绪偏向支持离开 React Native，但评论者对其原因存在分歧：一位工程师称他们用编码智能体配合 Maestro 在一夜之间完成了 90% 的自动化移植，另一个人则反驳“大语言模型让迁移变得可负担”的说法，因为他在大语言模型工具成熟前就手工完成过类似的重写。一位长期观察者指出，团队反复假设跨平台框架能削减人力，最终却发现既得到了“最低共同标准”的应用，又没有获得承诺的节省；还有多人认为，在代码日益由模型生成的今天，React Native 最大的卖点——让 Web 开发者也能开发移动应用——正在被削弱。

**标签**: `#React Native`, `#Mobile Development`, `#Swift`, `#Kotlin`, `#Cross-Platform`

---

<a id="item-2"></a>
## [研究者质疑能否放心把未发表的数学成果交给 OpenAI](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

mathstodon.xyz 数学社区 Mastodon 实例上的一则帖子在 Hacker News 引发热议（约 577 分、579 条评论），讨论数学家能否安全地把未发表的研究交给 OpenAI，焦点集中在署名权和保密性上。评论者争论 OpenAI 的模型是否会把用户在对话中透露的想法带入后续的预训练，还是说那些超人水平的成果完全来自针对可验证数学的大规模强化学习。 这一事件凸显了 AI 用于科学研究时更深层的信任问题：如果前沿实验室能够从使用其模型的研究者那里吸收未发表的想法，数学及其他领域中传统的署名与优先权规范就可能瓦解。这也呼应了《莱顿人工智能与数学宣言》等既有担忧——对 AI 证明和专有模型的依赖会扭曲研究议程，并让无法获得这些资源的研究者处于劣势。 技术上的关键争议在于：模型的参数究竟能否在预训练阶段记住并从用户对话中出现的想法里泛化，还是说这些结果来自对可验证数学问题、依赖海量算力的强化学习；有评论者指出训练数据比模型本身大好几个数量级。一个反复出现、更为怀疑的观点是：在得知某重大证明可能已落入训练数据之后不久，OpenAI 从一个仍在训练中的模型生成了大约 3000 亿个输出 token，看起来像是“平行构建”证据。

hackernews · pred_ · 9月10日 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**背景**: 预训练是语言模型从海量文本语料中学习统计规律的阶段，而强化学习（RL）则是后续阶段，通过奖励模型正确解题（例如答案可核验的数学题）来优化它。由于前沿实验室对模型权重和训练数据配比保密，外界很难判断某个具体成果究竟来自通用推理，还是来自对用户输入的“记忆”。传统数学研究依赖公开的署名与优先权，因此一旦想法来源存疑，在该领域的敏感度尤其高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Leiden_Declaration_on_Artificial_Intelligence_and_Mathematics">Leiden Declaration on Artificial Intelligence and Mathematics</a></li>
<li><a href="https://www.nature.com/articles/s41567-025-03042-0">Mathematical discovery in the age of artificial intelligence</a></li>
<li><a href="https://mastodonservers.net/server/1470-mathstodon">Mathstodon Mastodon Server Instance</a></li>

</ul>
</details>

**社区讨论**: 整体情绪对 OpenAI 持怀疑态度。一条高赞评论把 OpenAI 比作人类合作者：如果一个人拿走了别人分享的想法却不加署名地发表，会被视为极不道德，因此许多人认为同样的标准也应适用于 OpenAI。也有人认为两种解释可以同时成立，还有评论者认为这无需多虑，因为相关工作“不过是在可验证领域里的暴力穷举”。

**标签**: `#OpenAI`, `#research-ethics`, `#AI-for-math`, `#trust`, `#Hacker-News`

---

<a id="item-3"></a>
## [微软将 Rust 列为内部开发的一级语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

在 Rust 基金会发布的一篇客座文章中，微软正式将 Rust 认定为内部开发的“一级语言”，使其与 C++、C# 和 TypeScript 并列，成为微软支持力度最大的语言之一。这一工程地位意味着 Rust 在微软内部将获得一流的工具链、构建与支持投入。 这一认定对 Rust 而言是主流层面的重要背书，表明一家在 C/C++ 领域根基深厚的平台厂商认为该语言已能胜任大规模企业级系统开发，从而降低了在新项目中采用 Rust 的机构性阻力。这也意味着所有在 C 和 C++ 工具链上举足轻重的主流操作系统厂商，如今都已在系统编程语言上做了多元化布局。 社区讨论提到微软公开表达的雄心：借助自动化工具，到 2030 年将约 10 亿行 C/C++ 代码转换为 Rust；此外还有一个值得关注的技术细节——Rust 的 LLVM 后端据称已被 MSVC 后端替换。需要注意的是，这些内容多为战略表态与传闻，而非已落地的技术版本发布，因此具体的工具链时间表仍不明确。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**背景**: Rust 是一门通用系统编程语言，最初由 Mozilla 创建，并于 2015 年发布首个稳定版本；它通过“借用检查器”（borrow checker）在编译期而非依赖垃圾回收来保证内存安全。这一点很重要，因为内存安全问题历来在 C 和 C++ 代码库（包括微软自家的代码库）的安全漏洞中占据很大比例。在微软，“一级语言”指的是公司官方支持用于内部工程的语言，意味着它能获得与旗舰语言相当的专业构建工具、文档与生态投入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier - 1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language)</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/overview/what-s-new-for-msvc?view=msvc-170">What's new for MSVC Build Tools | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的相关讨论（576 分、313 条评论）总体积极，评论者认为这一举措证明 Rust 已不再是“稚嫩”的语言，而是 C++ 和 C# 的成熟竞争者，并把 MSVC 后端集成称为真正的重磅消息。也有人补充了具体背景，如微软 10 亿行代码迁移目标以及 DARPA 资助的 C 到 Rust 自动化翻译研究；部分评论指出 Zig、Odin 等更新的“更好的 C/C++”替代方案仍较为粗糙，并争论这究竟是战略层面的背书还是一项技术突破。

**标签**: `#rust`, `#microsoft`, `#systems-programming`, `#memory-safety`, `#programming-languages`

---