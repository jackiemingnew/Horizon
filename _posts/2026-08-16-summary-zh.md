---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> 从 29 条内容中筛选出 6 条重要资讯。

---

1. [Anthropic 公布 Claude 系统提示词，引发 AI 透明度讨论](#item-1) ⭐️ 8.0/10
2. [模型故意变笨？文章引发关于 AI 设计方向的讨论](#item-2) ⭐️ 8.0/10
3. [Qwen 3.8 27B 表现出色，但默认过度思考](#item-3) ⭐️ 8.0/10
4. [SSOG-Attention：一种亚二次方、可扩展的 SDPA 替代方案](#item-4) ⭐️ 8.0/10
5. [对 ECA-Net 核心假设的质疑：跨通道交互并非关键](#item-5) ⭐️ 8.0/10
6. [Anthropic 第二季营收超 115 亿美元，同比增长 14 倍，拟今秋 IPO](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 公布 Claude 系统提示词，引发 AI 透明度讨论](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 发布了 Claude 系统提示词的发布说明，公开了用于塑造模型行为的实际提示词，涉及 Opus 4.8、Claude Fable 5 和 Claude Mythos 5 等版本。社区对这些变更进行了详细分析，包括 Simon Willison 整理的 git 提交历史。 这是领先 AI 实验室罕见的透明度举措，揭示了模型行为如何在系统层面被引导和约束。这对 AI 安全、问责制以及公众对 LLM 行为的理解具有重大意义，也使研究者能够追踪提示词随时间的演变。 系统提示词包含当前日期信息、行为指导（例如在危机情况下优先用户福祉）以及反幻觉指令（例如检查图像是否上传、引导用户查看官方支持页面）。Simon Willison 创建了一个 git 仓库来重构提示词历史并展示各版本间的差异。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**背景**: LLM 中的系统提示词是预定义的指令，用来引导模型行为并优先于用户输入，确保在不同上下文中响应的一致性。它们通常告诉模型它是什么、用途是什么，并包含约束和行为规则。Anthropic 的 Claude 网页界面和移动应用在每次对话开始都会使用系统提示词，而这次公布的发布说明让外界得以罕见地一窥主流 AI 实验室如何落实安全与对齐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs</a></li>
<li><a href="https://simonwillison.net/2025/May/25/claude-4-system-prompt/">Highlights from the Claude 4 system prompt</a></li>
<li><a href="https://promptengineering.org/system-prompts-in-large-language-models/">System Prompts in Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 社区总体对这一透明度举措持积极态度，Simon Willison 提供了 git 提交历史来分析变更。评论者就系统提示词是否反映了真正的模型智能或只是常识展开讨论，也有人担心论坛会删除对 AI 持批评态度的帖子。还有评论指出，系统提示词只是塑造模型行为的更大体系中的一层。

**标签**: `#AI`, `#LLM`, `#Anthropic`, `#system prompts`, `#transparency`

---

<a id="item-2"></a>
## [模型故意变笨？文章引发关于 AI 设计方向的讨论](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

一篇博文认为，AI 模型正有意地变得更“笨”——把事实性知识从模型权重中转移到工具和检索系统里。文章称这是一种刻意的设计选择，而不是扩展模型规模的失败。 这预示着大语言模型的构建和评估方式可能出现转变——从记忆事实转向基于外部知识进行推理。它挑战了传统上对参数化知识的重视，并引发了对基准测试有效性的质疑。 博文引用了 SimpleQA 基准，其中 Gemini 2.5 Pro 在禁止使用工具的情况下以 53% 的事实召回率领先。文章还设想了一个未来：由于权重中的知识以“年”而非“周”为单位过期，模型卡将不再列出知识截止日期。

hackernews · hruvhwe · 8月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**背景**: 检索增强生成（RAG）是一种让大语言模型在生成回答之前先从外部文档中检索相关信息的技术，能够减少幻觉并降低频繁重训练的需求。工具使用则进一步让模型调用外部 API。这场争论的核心在于：知识应该存放在模型权重中，还是存放在外部、可插拔的源里，以及推理与事实回忆是否可以被清晰地区分开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>
<li><a href="https://grokipedia.com/page/Tool_use_in_large_language_models">Tool use in large language models</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/open-weight-models/">What are Open Source and Open Weight Models? - Analytics Vidhya</a></li>

</ul>
</details>

**社区讨论**: 评论者大多围绕文章的设想展开讨论：有人赞赏针对特定领域使用可插拔知识库的想法，也有人批评这篇文章过时且疑似由 AI 生成，指出 Gemini 2.5 Pro 已是 16 个月前的模型。还有人提到 Cactus 的 14 MB 工具调用模型“Needle”，认为这一趋势正在成为现实；也有怀疑者提醒，这类讨论像是脱离现实约束的科幻式畅想。

**标签**: `#AI`, `#LLMs`, `#knowledge bases`, `#tool use`, `#benchmarks`

---

<a id="item-3"></a>
## [Qwen 3.8 27B 表现出色，但默认过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 8.0/10

阿里巴巴 Qwen 实验室于周五发布了 Qwen 3.8 27B，这是一款采用 Apache 2.0 许可、拥有 270 亿参数且支持视觉的大语言模型。该模型自报的基准测试成绩显示，其性能较 Qwen 3.6 27B 以及更大规模的闭源 Qwen 3.7-Plus 均有提升。 此次发布为开发者和爱好者提供了一个竞争力强、可在配置不错的笔记本电脑上流畅运行的开源权重模型，扩展了本地 AI 的能力。然而，其默认的“极高（xhigh）”推理力度设置可能使模型在消费级硬件上慢得离谱且消耗大量 token，这是关键的可用性问题。 Simon Willison 通过 LM Studio 测试了 17GB 的 Q4_K_M 量化版本；默认 8,192 token 的上下文被思考过程直接耗尽，因此他改用 262,144 token 的最大上下文。生成一张 SVG 图像约耗时 21 分钟，消耗了 22,276 个推理 token，最终产出 3,223 个输出 token。

rss · Simon Willison · 8月16日 22:00

**背景**: Qwen（通义千问）是阿里云推出的一系大语言模型，既可通过付费 API 使用，也可作为开源权重下载。模型参数规模（以十亿计）通常代表其能力水平，27B 是一个适合在性能较强的笔记本电脑上本地部署的实用规格；视觉语言模型则能同时处理图像和文本。全新的 Qwen3.8 系列引入了可配置的“推理力度”参数，用于在回复深度与速度、成本之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/vlms">Vision Language Models Explained - Hugging Face</a></li>
<li><a href="https://www.ibm.com/think/topics/llm-parameters">What Are LLM Parameters? | IBM</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#LLM`, `#Open Source`, `#Qwen`, `#Local Models`

---

<a id="item-4"></a>
## [SSOG-Attention：一种亚二次方、可扩展的 SDPA 替代方案](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 8.0/10

一种名为 SSOG（可分离高斯和）的新型注意力机制被提出，它用查询令牌引导的学习高斯原子替代缩放点积注意力（SDPA），将复杂度从 O(N²·d)降至 O(N·√N·d)。该方法已在公开仓库中实现，并附带一篇博客文章。 这直接解决了 Transformer 中的二次方可扩展性瓶颈——它们越来越多地被用于长序列和高分辨率图像。如果结果可靠，SSOG 将在大规模视觉和语言模型的训练与推理中显著提升速度并降低内存占用。 实验表明，SSOG 在 CIFAR-100 上优于 SDPA，在 ImageNet-1K 上表现相当且收敛更快。作者说明部分代码和博客内容使用了 AI 辅助，完整代码与结果已发布在 GitHub 上。

reddit · r/MachineLearning · /u/4rtemi5 · 8月16日 10:06

**背景**: 缩放点积注意力（SDPA）会计算所有查询令牌与键令牌之间的两两相似度，导致 O(N²)复杂度，在长输入下代价过高。SSOG 改为在每个注意力头学习少量高斯原子，并根据查询对它们进行几何引导，由于这些原子可分解为可分离的高斯和，计算量降至亚二次方。亚二次方注意力一直是扩展 Transformer 以处理更长上下文和高分辨率输入的热门研究方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/rpisoni_a-few-gaussians-is-all-you-need-ssog-attention-activity-7494799597622525952-mgd2">A Few Gaussians Is All You Need: SSOG-Attention That Steers ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Attention_(machine_learning)">Attention (machine learning) - Wikipedia</a></li>
<li><a href="https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/JamesPoetzscher.pdf">Near-Infinite Sub-Quadratic Convolutional Attention</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#attention mechanisms`, `#efficient transformers`, `#scalability`, `#Gaussian approximation`

---

<a id="item-5"></a>
## [对 ECA-Net 核心假设的质疑：跨通道交互并非关键](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 8.0/10

Reddit 上的一篇分析认为，高效通道注意力（ECA）模块在通道均值上使用一维卷积在概念上有缺陷，因为通道顺序是任意的。国际象棋残局表上的实验表明，核大小 k=1 的 ECA 性能与 k=3 几乎一样好，这与论文中“跨通道交互至关重要”的说法相矛盾。 ECA-Net 是一种被高度引用（12000 次引用）的注意力机制，用于以低成本提升 CNN 性能。如果其设计依据具有误导性，研究人员和工程师可能会重新考虑如何选择或设计通道注意力模块；这一批评也揭示了卷积归纳偏置与通道维度之间更广泛的错配。 作者在 6 子国际象棋残局表库上测试了多种通道门控，该表库允许从完整状态空间进行无偏采样。报告的平均测试准确率包括：ECA（k=3）为 96.68%，ECA（k=1）为 96.61%，PerChannelGate 为 96.65%，表明跨通道交互对 ECA 的性能贡献不大。

reddit · r/MachineLearning · /u/arkuto · 8月16日 10:13

**背景**: 高效通道注意力（ECA）是 Wang 等人于 2019 年（CVPR 2020）提出的通道注意力模块，旨在改进 Squeeze-and-Excitation（SE）网络：它避免降维，并使用一维卷积进行局部跨通道交互。标准卷积假设空间/时间局部性和平移不变性，但特征图中通道的顺序是任意的，因此沿通道维度应用一维卷积类似于在表格数据上使用 CNN。国际象棋残局表库是完整、已解决的数据集，非常适合在无数据集偏差的情况下隔离架构效应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA-Net: Efficient Channel Attention for Deep Convolutional Neural Networks</a></li>
<li><a href="https://arxiv.org/abs/1709.01507">[1709.01507] Squeeze-and-Excitation Networks</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#attention-mechanisms`, `#paper-analysis`, `#cnn`, `#efficient-channel-attention`

---

<a id="item-6"></a>
## [Anthropic 第二季营收超 115 亿美元，同比增长 14 倍，拟今秋 IPO](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

Anthropic 2026 年第二季初步营收超过 115 亿美元，较去年同期的 7.87 亿美元增长逾 14 倍，也高于第一季的 47.3 亿美元。当季调整后营业利润转正，彭博社援引文件披露了这一数据。 这标志着领先 AI 实验室之一的重大商业里程碑，表明大语言模型公司能够快速扩大收入并实现经营性盈利。这也为今年秋季可能进行的大型 IPO 铺平道路，可能重塑投资者对 AI 基础设施和模型商业化的预期。 这些数字为初步数据，仍可能调整。公司正在筹备可能于今秋启动的大型 IPO；第一季 47.3 亿美元的收入数字则显示了环比增长轨迹。

telegram · zaihuapd · 8月16日 07:26

**背景**: Anthropic 是一家以开发 Claude 系列大语言模型而闻名的人工智能公司，定位上与 OpenAI、Google 形成竞争。这类实验室通常需要大量投入算力和人才来运转，因此在 IPO 前实现调整后营业利润转正是一个值得关注的转折点。

**标签**: `#AI`, `#Anthropic`, `#Revenue`, `#IPO`, `#Business`

---