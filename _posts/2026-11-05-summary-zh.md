---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05
lang: zh
---

> 从 38 条内容中筛选出 10 条重要资讯。

---

1. [月之暗面开源 Kimi K3.1 Pro 权重](#item-1) ⭐️ 9.0/10
2. [AI 漏洞挖掘迫使软件业偿还 40 年技术债](#item-2) ⭐️ 8.0/10
3. [Go 提出全新 encoding/json/v2 API，带来更快更严格的 JSON 处理](#item-3) ⭐️ 8.0/10
4. [Anthropic 公布大语言模型可证明推理研究进展](#item-4) ⭐️ 8.0/10
5. [腾讯发布开放权重模型 Hy4，主打游戏开发并开源科学模型](#item-5) ⭐️ 8.0/10
6. [NKI 层内 megakernel 将单台 Trainium2 上 GLM-5.3-Flash 的解码步从 32.2 ms 降至 24.2 ms](#item-6) ⭐️ 8.0/10
7. [B200 实测：循环 Transformer 省显存存储，但不省 HBM 带宽](#item-7) ⭐️ 8.0/10
8. [甲骨文在美国施压下取消与腾讯 70 亿美元 AI 芯片租赁协议](#item-8) ⭐️ 8.0/10
9. [华为告知客户：昇腾 960DT 的 HBM 内存需自行采购](#item-9) ⭐️ 8.0/10
10. [蓝牙 HDT 标准正式发布：LE 峰值速率提升至 7.5 Mbps](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [月之暗面开源 Kimi K3.1 Pro 权重](http://platform.kimi.ai/) ⭐️ 9.0/10

月之暗面在 Hugging Face 上发布了 Kimi K3.1 Pro 的开放权重，这是一个原生多模态智能体模型，总参数 2.8T、激活参数 104B、上下文窗口约 100 万 token，也是 K3.1 系列的首个模型。官方同步在 platform.kimi.ai 开放 API，选择 kimi-k3.1-pro 即可调用，接口兼容 OpenAI 与 Anthropic 规范，权重以 MXFP4 量化形式发布。 万亿参数级别的开放权重目前仍然罕见，因此这次发布让研究者和自托管团队获得了一个前沿级别的多模态智能体模型，可以审查、微调并在不依赖闭源厂商的情况下运行。同时兼容 OpenAI 与 Anthropic 两套接口，也降低了已经基于这些 SDK 构建的团队的迁移成本，进一步加大了对闭源前沿实验室和其他开放权重竞争者的压力。 即便采用 MXFP4 这种 4 位微缩放格式（可将权重显存占用压缩到 BF16 的大约四分之一），2.8T 参数仍需要约 1.4 TB 的存储空间，因此真正自托管基本需要多卡节点而非单台工作站。104B 的激活参数量让单 token 计算量保持在适中水平，但全部专家仍需常驻内存，真正的瓶颈是显存容量与互联带宽。

telegram · zaihuapd · 11月4日 15:47

**背景**: Kimi K3.1 Pro 采用混合专家（MoE）架构：并非每个 token 都跑全部参数，而是由路由器只激活一小部分专家子网络，因此总参数（内存中加载的全部专家）可以远多于激活参数（单个 token 实际用到的那部分）。MXFP4 是一种 4 位浮点量化方案，在一组数值（通常为 32 个）之间共享一个很小的指数缩放因子，精度明显优于朴素的 4 位舍入，同时能缩小模型体积并在新一代加速卡上提升推理速度。“原生多模态”意味着视觉能力从训练之初就融入模型，而非事后拼接；“智能体”则表明工具调用与多步任务执行是模型的一等能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi -K3 · Hugging Face</a></li>
<li><a href="https://www.kapilsharma.dev/posts/mxfp4-visualizer/">Understanding MXFP4 Quantization | Kapil Sharma</a></li>
<li><a href="https://osfoundry.io/articles/mixture-of-experts-explained">Mixture of Experts Explained: Total vs Active Parameters ...</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分化：有人认为该模型是“刷榜型”（benchmaxxed），称其相比 DeepSeek V4.1-Flash 提升有限，或在其他实验室的内部基准上得分不高；但也有实践者反驳称，自己的测试显示这是一个非常强的开放模型，只是略微落后于前沿。另一些人关注实际可用性——本地运行大约需要 8 卡 B300 节点，而 OpenRouter 等第三方推理服务商已在托管该模型，吞吐量约为月之暗面官方端点的一倍，暗示成本仍有进一步下降的空间。

**标签**: `#open-weights`, `#large-language-models`, `#multimodal`, `#mixture-of-experts`, `#moonshot-kimi`

---

<a id="item-2"></a>
## [AI 漏洞挖掘迫使软件业偿还 40 年技术债](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability) ⭐️ 8.0/10

IEEE Spectrum 的一篇分析文章认为，由 AI 驱动的漏洞挖掘正在迫使软件行业正视约 40 年来积累的技术债，并在 Hacker News 上引发了大规模讨论（约 1066 分、634 条评论）。文章将 AI 不仅视为新的攻击工具，更视为一种审计力量，它把既有代码库中长期被忽视的弱点暴露出来。 如果 AI 能以人类无法企及的规模审计代码，那么开源界长期存在的“总会有人审过这段代码”的假设或许终于能真正兑现，而所有维护遗留系统的组织都应预期迎来持续的补丁修复浪潮。这会把安全投入从被动的应急响应，转向对设计层面缺陷的大规模补救。 讨论中最尖锐的反驳是：许多技术债并非可以用精准补丁修掉的差一错误，而是需要重构甚至重新设计，因此 AI 可能带来的只是“与功能无关的修复工作”的无休止循环，而非真正的债务偿还。评论者还援引《哥德尔、艾舍尔、巴赫》指出，完美的安全系统不仅在工程上不可能，在理论上也不可能，因此目标应是提升健壮性而非彻底了结。

hackernews · pseudolus · 11月4日 11:52 · [社区讨论](https://news.ycombinator.com/item?id=50364336)

**背景**: 技术债是一个比喻，指软件设计中为图快而留下的捷径，随着后续修改变得更困难、更高风险，这笔“利息”会不断累积。传统漏洞挖掘依赖人工审计和模糊测试，其规模远小于代码库本身；而大语言模型和 AI 辅助分析工具如今让大规模扫描代码弱点变得廉价。开源社区长期信奉“林纳斯定律”——“只要有足够多的眼睛，所有 bug 都无处遁形”，但这一假设在实践中往往并未真正被检验。

**社区讨论**: Hacker News 上的讨论参与度很高，但对标题式论断持怀疑态度：最有力的反驳认为，AI 驱动的修复可能只是与功能无关工作的无休止循环，而非真正的债务偿还，而且许多缺陷需要重构而非窄范围的补丁。也有人更为乐观，希望 AI 审计能顺带挖出国家机构掌握的各种 0-day，并真正兑现开源代码被他人审计的承诺；另有讨论串借用《哥德尔、艾舍尔、巴赫》论证任何系统都无法做到绝对安全。

**标签**: `#AI/ML`, `#cybersecurity`, `#technical-debt`, `#vulnerability-research`, `#software-engineering`

---

<a id="item-3"></a>
## [Go 提出全新 encoding/json/v2 API，带来更快更严格的 JSON 处理](https://go.dev/blog/jsonv2) ⭐️ 8.0/10

Go 团队正式提出了新的 encoding/json/v2 包（以及配套的 encoding/json/jsontext），作为标准库 JSON 处理的重大修订版本，计划随 Go 1.27 发布。原有的 v1 encoding/json 包保持不变，现有导入依然可用，但可以通过新增的配置选项让底层引擎切换为 v2 行为。 JSON 处理是 Go 标准库中使用最广泛的部分之一，因此这次重新设计几乎影响每一个需要序列化数据的 Go 服务，Go 团队称反序列化速度最高可提升 10 倍。该提案也迫使整个生态正视长期存在的各种行为怪癖，以及无数现有项目需要承担的迁移成本。 迁移并非完全即插即用：v2 在重复键处理、非法 UTF-8 处理、nil 集合、字段名大小写不敏感匹配以及字节数组编码为 Base64 字符串等方面都改变了行为，并且取消了大家熟悉的 MarshalIndent，改用更繁琐的 jsontext 选项。Go 团队提供了专门的迁移指南，说明如何安全地启用 v2，包括可恢复 v1 遗留行为的配置选项。

hackernews · olexsmir · 11月4日 17:52 · [社区讨论](https://news.ycombinator.com/item?id=50369106)

**背景**: Go 的 encoding/json 包自 Go 1.0 以来基本没有变化，它基于反射实现，使用方便但速度相对较慢，而且对畸形输入较为宽容。v2 的推进方式与 math/v2 等标准库修订一脉相承：保留旧包仍可导入，同时在带版本号的子包中提供更严格、更快速、配置更显式的新 API。jsontext 子包负责底层的词法解析与格式化，从而与 json 包中的类型映射逻辑分离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/doc/jsonv2-migration">encoding/json/v2 Migration Guide - The Go Programming Language</a></li>
<li><a href="https://github.com/golang/go/issues/71497">encoding / json / v 2 : new API for encoding / json · Issue #71497...</a></li>
<li><a href="https://pkg.go.dev/encoding/json">json package - encoding / json - Go Packages</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上对这一重新设计持肯定态度，但不少人提出了迁移痛点——有人对取消 MarshalIndent 感到遗憾，认为等价代码复杂且不直观，写快速脚本时尤其麻烦。也有人质疑 JSON 作为“简单”格式的名声，毕竟每种语言都仍在它上面投入大量精力；还有人谈到未来大部分 Go 代码可能由大模型编写，而开发者依然看重 Go 的性能与安全性。

**标签**: `#Go`, `#JSON`, `#standard library`, `#API design`, `#encoding/json/v2`

---

<a id="item-4"></a>
## [Anthropic 公布大语言模型可证明推理研究进展](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

Anthropic 发布了一项研究，介绍名为 FlashProve 的系统，它能让模型提供方（证明者）以密码学方式向用户（验证者）证明某条回复确实由某个特定的大型混合专家（MoE）语言模型生成。该公司表示，该方案生成约 6.5 MB 的承诺（commitment），可覆盖约 1600 万次请求，之后提供方需要重新生成承诺，并且每次请求都附带一份证明。 目前 API 客户基本上只能“信任”自己付费调用的模型就是实际作答的模型，因此模型被悄悄替换、路由器降级或权重被未披露地修改都很难被发现。可密码学证明的推理将为企业客户和受监管行业用户提供具体的验证手段，而围绕它的讨论也正在影响人们对开源权重与闭源权重问责方式的看法。 代价相当可观：有评论者提到约 90–100 倍的计算开销，而且校验证明本身在 24 线程上约需 17 秒（单线程约 21 秒），其中还包括离线阶段的检查。此外，这类证明只能证明所执行的确实是承诺的那份权重，并不能说明输出质量如何，而 GPU 的非确定性仍然是精确重放计算的一大实际障碍。

hackernews · ltononro · 11月4日 17:17 · [社区讨论](https://news.ycombinator.com/item?id=50368626)

**背景**: 可验证计算让证明者能够说服验证者某次计算被正确执行，而无需验证者自己重做全部工作，这一思想因零知识证明和区块链领域的“zkML”项目而广为流传。将之应用于大语言模型推理非常困难，因为 Transformer 前向计算涉及数十亿参数和大量非算术运算，把它们表达为证明电路代价极高；Lagrange 的 DeepProve-1 以及学术界的 ZK-LLM 研究直到最近才开始覆盖完整的模型推理。Anthropic 的 FlashProve 针对混合专家（MoE）模型，这类模型每个 token 只激活一部分参数，这既改变了证明成本，也改变了权重承诺的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/provable-inference">Progress on provable inference for large language models \ Anthropic</a></li>
<li><a href="https://github.com/JamesPetrie/zkllm-entropy">GitHub - JamesPetrie/zkllm-entropy · GitHub</a></li>
<li><a href="https://lagrange.dev/blog/deepprove-1">DeepProve-1: The First zkML System to Prove a Full LLM Inference</a></li>

</ul>
</details>

**社区讨论**: 讨论意见不一：一位自称曾是 MARS 研究员的评论者表示，这项工作建立在他所开发的 VerInf 之上，并抱怨连选用 400B Maverick 模型这一决定都几乎没有署名。另一些人则质疑其经济性，认为对于开放权重模型，直接以确定性方式重算一遍即可，或者让多个独立推理提供方运行同一个非批处理提示词以获得更廉价概率性保证，并指出在权重闭源的情况下签名响应是退而求其次的方案。

**标签**: `#provable inference`, `#LLM security`, `#cryptography`, `#zero-knowledge proofs`, `#Anthropic`

---

<a id="item-5"></a>
## [腾讯发布开放权重模型 Hy4，主打游戏开发并开源科学模型](https://hy.tencent.ai/research/hy4) ⭐️ 8.0/10

腾讯发布了新一代混合专家（MoE）基础模型 Hy4，总参数量约 770B、每 token 激活约 49B，上下文窗口超过 100 万 token，跻身当前最强的开放权重模型之列。同时，腾讯开源了两个与 Hy4、Hyra 2.0 共同开发的科学基础模型——用于单细胞表征的 HyCell 和用于物理场建模的 HyPDE，并表示模型权重和系统卡将在未来几天内公布。 中国实验室推出接近前沿水平的开放权重模型，缩小了可自由下载的模型与闭源专有 API 之间的差距，这对研究人员、初创公司以及不愿或无法依赖单一供应商的用户意义重大。它对游戏开发的特殊优化（包括针对 Unreal Engine、Unity 和 Godot 的引擎层适配）以及免费开放的科研模型表明，开放权重正从附属策略变成一种有竞争力的分发方式。 腾讯自己也承认 Hy4 与顶级闭源模型仍有明显差距，尤其是在研究级数学、长程编码、模型自我改进和高级视觉问答等内部基准上，并表示将继续扩大预训练和后训练规模。第三方测试还显示出性价比上的取舍：在 Plotly 的数据分析基准中，Hy4 落在 GPT-6.1 Sol 与 GPT-6.1 Terra 之间，但速度明显偏慢，有时每个问题会发起数十次查询。

hackernews · Philpax · 11月4日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=50365780)

**背景**: Hy4 采用混合专家（MoE）架构，即每个 token 只激活一部分参数，因此推理成本比同等总参数量的稠密模型更低。“开放权重”意味着训练好的参数可以下载，任何人都能在本地运行或微调，但它并不完全等同于完全开源，因为训练数据和代码可能仍未公开。HyCell（单细胞生物学）和 HyPDE（用于物理场的偏微分方程）这类科学基础模型是在科学数据而非通用文本上训练的领域专用模型，而对游戏开发的侧重则体现了把编码能力向引擎脚本、玩法逻辑和资产管线方向调优的努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hy.tencent.ai/research/hy4">hy . tencent .ai/research/ hy 4</a></li>
<li><a href="https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/">Tencent Launches Hy4, Joining the Ranks of the... - Tencent</a></li>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent / Hy 4-preview · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 评论整体偏正面：有人称赞腾讯开放科研工具与美国实验室限制研究用途形成鲜明对比，也有人认为针对 Unreal、Unity、Godot 的适配确实很有意思。不少人对腾讯坦承与闭源模型存在差距表示认可，而一份基准测试则指出 Hy4 工作非常细致但速度很慢，每个问题会运行数十次查询。

**标签**: `#llm`, `#open-weights`, `#tencent`, `#game-development`, `#foundation-models`

---

<a id="item-6"></a>
## [NKI 层内 megakernel 将单台 Trainium2 上 GLM-5.3-Flash 的解码步从 32.2 ms 降至 24.2 ms](https://www.reddit.com/r/MachineLearning/comments/1xo0yuq/p_nki_layer_megakernels_for_glm53flash_on_aws/) ⭐️ 8.0/10

RunAnywhere 开源了 trnrt——一个基于 NKI 的推理引擎，可在单台 AWS trn2.48xlarge 实例上服务 GLM-5.3-Flash（320B 混合专家模型、100 万 token 上下文），并公开了细粒度的解码步耗时剖析。对早期构建的剖析显示，在 batch 1 下某个 KDA 线性注意力层中，递推数学只占注意力那一半的 2%，而 mHC 预投影占 36%、XLA 胶水代码占 33%、转置占 10%、流混合占 10%。在把每个层的一半重写为单个 NKI kernel 之后，batch-8 的解码步从 32.2 ms（10 月 17 日构建）降到 24.2 ms（11 月 1 日构建），其中融合的稀疏注意力层与合并发布的 KDA 和 MoE kernel 各贡献了每步 3.2 ms 的节省。 相比 GPU，Trainium2 的公开资料少得多，而且这类模型没有现成的服务路径：最新的 vLLM Neuron 插件并未注册任何 GLM 模型，NxD Inference 又处于维护模式，因此这项工作为想在 AWS 自研芯片上跑大型 MoE 模型的人填补了真实空白。解码步的大部分时间花在框架开销而非模型数学上这一结论，加上具体可复用的重写规则和失败经验，给系统工程师的是一套可迁移的方法论，而不只是一个基准数字。 设计遵循三条规则：把工作集留在每个物理 NeuronCore 的 28 MiB SBUF 上，使只有层的输入、输出和流式权重穿越 HBM；把权重流拆分到逻辑核的两个物理核上（单程序可达 340–400 GB/s，双程序合计 672–708 GB/s）；当某个集合通信阻塞下一个操作时，把它搬进 kernel 内部，因为 XLA 下下一个 kernel 必须等待整个 all-reduce 完成。在 batch-8 每步剩余的 24.2 ms 中，6.1 ms 是内存下限，10.0 ms 是超出下限的引擎忙碌时间，4.6 ms 是 kernel 内部等待，2.8 ms 是暴露的集合通信，0.7 ms 为空闲——作者也提醒：没有原厂 AWS 或 GPU 基线，本次构建未做任务级评测，且稀疏注意力 prefill 中仍保留一处近似，使下一 token 的对数概率偏移 0.012–0.021 nats，并在 448 个位置中的 3 个改变了最高概率 token。

reddit · r/MachineLearning · /u/WildCard727 · 11月4日 21:47

**背景**: NKI（Neuron Kernel Interface）是 AWS 面向 Trainium 芯片内计算单元 NeuronCore 的底层裸金属编程语言，可直接控制片上内存和指令调度，而不依赖高层图编译器。SBUF 是 NeuronCore 的片上暂存内存，HBM 则是往返代价高得多的片外高带宽内存，因此 kernel 融合——把中间结果留在片上——是降低延迟的主要手段。megakernel 把整个解码步或整个层融合进一次持久化 kernel 启动，以消除逐算子启动开销和跨 kernel 的 HBM 流量，这一思路由 GPU 上的 Mirage/MPK 和 Hazy Research 等工作推广开来。GLM-5.3-Flash 是 320B 的混合专家模型，每个 token 只激活一部分参数，并把 KDA（带递推状态的线性注意力）与面向 100 万 token 上下文的稀疏注意力结合；大量跨芯片集合通信则源自把如此大的模型切分到 trn2.48xlarge 的 16 个 NeuronCore 上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/328113/20260928/aws-trainium-runs-real-time-ai-video-generation-without-nvidia-nki-kernel-playbook-published.htm">AWS Trainium Runs Real-Time AI Video Generation Without NVIDIA...</a></li>
<li><a href="https://theorempath.com/topics/megakernels">Megakernels . End-to-End Fused LLM Inference Kernels</a></li>
<li><a href="https://github.com/allenkchau/trainium-kernel-fusion">allenkchau/ trainium - kernel -fusion: Transformer inference on AWS ...</a></li>

</ul>
</details>

**标签**: `#inference-optimization`, `#aws-trainium`, `#kernel-fusion`, `#mixture-of-experts`, `#llm-serving`

---

<a id="item-7"></a>
## [B200 实测：循环 Transformer 省显存存储，但不省 HBM 带宽](https://www.reddit.com/r/MachineLearning/comments/1xnskvt/do_looped_transformers_save_hbm_traffic_profiling/) ⭐️ 8.0/10

一项新的性能剖析研究（已开源代码与 Nsight Compute 原始数据）在 NVIDIA B200 上测量了 Huginn 式循环 Transformer 的实际内存行为。在微基准中，八次 matmul 共享同一份 72 MiB 权重时，比使用八份相同权重副本的同一链条快 24%，且几乎不从 HBM 读取数据；但当权重达到 288 MiB、超出 L2 容量后，这一优势完全消失。在随机权重的完整 Huginn Core 中，八次迭代的耗时约为单次迭代的八倍，从 HBM 读取的数据量也约为八倍。 在迭代间复用同一套权重的循环架构，在 2025–2026 年已成为一条重要的扩展路线（如 Huginn、Ouro 等），并常被宣传为效率上的优势，因此这一具体的负面结果澄清了“省存储”并不自动等于“省带宽”。这一区别会直接影响此类模型的设计方式以及 kernel 的编写方式，例如能否借助持久化 kernel 把循环权重常驻片上。 这些测量基于随机权重的 Huginn Core 教学实现，而非训练好的模型，因此结果刻画的是内存行为，而不是端到端的推理质量。关键阈值似乎是 L2 缓存：能装进 L2 的共享权重只需读取一次并在各次迭代中复用，而更大的权重集合无论是否共享，每次迭代都要重新从 HBM 取回。

reddit · r/MachineLearning · /u/2dayyy6 · 11月4日 16:26

**背景**: 循环 Transformer 会把同一套权重复用多次：在读出层之前，将共享的某一层、某个块或整个堆栈反复作用于一个隐状态；这一思想可追溯到 2018 年的 Universal Transformers，并由 Huginn 等模型在大规模上重新带回。HBM 是存放 GPU 模型权重与激活值的高带宽显存，在受内存带宽限制的负载中，把数据从 HBM 搬入片上缓存的开销往往会主导运行时间，这正是“能装进缓存”与“超出缓存”成为鲜明分水岭的原因。Nsight Compute 是 NVIDIA 的 CUDA kernel 性能分析器，本文用它来获取每个 kernel 从 HBM 读取的字节数、耗时等指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/clutch-61/awesome-loop-transformers">GitHub - clutch-61/awesome-loop-transformers: Bilingual ...</a></li>
<li><a href="https://developer.nvidia.com/nsight-compute">Nsight Compute | NVIDIA Developer</a></li>
<li><a href="https://arxiv.org/abs/2610.23036">[2610.23036] Towards Looped Models Done Right, Part I ...</a></li>

</ul>
</details>

**标签**: `#transformers`, `#GPU-memory-bandwidth`, `#HBM`, `#performance-profiling`, `#LLM-efficiency`

---

<a id="item-8"></a>
## [甲骨文在美国施压下取消与腾讯 70 亿美元 AI 芯片租赁协议](https://www.tradingview.com/news/seekingalpha:e51e68f4d094b:0-oracle-cancels-7b-ai-chip-lease-with-tencent-amid-us-concerns-ft/) ⭐️ 8.0/10

据《金融时报》报道，甲骨文（Oracle）已取消与腾讯价值约 70 亿美元的五年期 AI 芯片租赁协议，此前美国官员向甲骨文表达了担忧，特朗普政府随后施加了压力。该协议原本将让腾讯获得最多约 10 万枚先进 AI 芯片的使用权，这些芯片部署在甲骨文位于东南亚的多个数据中心，首付款约占合同总额的 30%。 此次取消是迄今最清晰的案例之一，表明华盛顿将出口管制的审视范围从芯片直接销售延伸到第三国算力安排，实际上封堵了中国 AI 企业获取受限硬件的离岸通道。这说明美国的芯片政策现在不仅决定中国企业能买什么，还决定它们能在哪里、向谁租用算力，这一约束可能拖慢中国 AI 训练算力的扩张，并令类似的跨境租赁交易降温。 该协议采用租赁而非买卖的形式：腾讯租用甲骨文东南亚数据中心的算力，而不取得硬件所有权，约 30%首付，其余在五年内分摊支付。涉事芯片仅被描述为“先进 AI 芯片”；由于华盛顿的出口管制以及北京对本国数据中心使用外国 AI 硬件的限制，这些芯片无法在中国大陆境内使用。

telegram · zaihuapd · 11月4日 11:01

**背景**: 美国的出口管制限制了哪些先进 AI 加速器（其中最典型的是英伟达的高端 GPU）可以卖给中国企业，后续多轮规则还把中转转售和充当中间人的第三国数据中心纳入监管范围。与此同时，北京推动国内数据中心优先采用国产芯片而非外国加速器，这意味着腾讯无法直接在中国境内部署同样的硬件。租用部署在海外的算力因此成为一种有吸引力的变通方案，因为中国企业并不取得芯片所有权；而监管机构如今正把这类离岸安排视为需要封堵的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/ai/oracle-kills-7bn-tencent-ai-chip-deal-under-trump-pressure">Oracle Kills $ 7 BN Tencent AI Chip Deal Under Trump... | ZeroHedge</a></li>
<li><a href="https://nypost.com/2026/11/04/business/oracle-nixes-7b-chip-leasing-deal-with-chinas-tencent-after-trump-admin-pushback-report/">Oracle nixes $ 7 B chip leasing deal with China's Tencent after Trump...</a></li>
<li><a href="https://diesignal.com/articles/tencent-signs-7-billion-five-year-lease-for-100-000-oracle-ai-chips-18f11e57">Tencent Leases 100,000 Oracle AI Chips in $ 7 Billion Five-Year Deal</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Oracle`, `#Tencent`, `#US-China tech`, `#export controls`

---

<a id="item-9"></a>
## [华为告知客户：昇腾 960DT 的 HBM 内存需自行采购](https://thenextweb.com/news/huawei-hbm-smuggling-samsung-sk-hynix-ascend-960dt) ⭐️ 8.0/10

据 The Information 报道（The Next Web 转述），华为已告知部分客户，下一代旗舰 AI 芯片昇腾 960DT 将主要使用三星和 SK 海力士的 HBM，并要求客户自行解决内存来源，原因是中国本土厂商的 HBM 产能不足。报道援引深圳一位芯片经纪人的话说，单颗 HBM3E 的价格已从一年前的数百美元涨到约 4000 美元。 这一披露表明，即便是华为最先进的国产 AI 加速卡，瓶颈也更多落在内存而非计算逻辑上，缺口只能靠灰色渠道填补。这会推高中国 AI 数据中心运营商的整机成本，也说明先进内存出口管制正在重塑中国 AI 算力建设的成本结构。 报道描述了这样的走私路径：把 HBM 颗粒重新植球焊到性能极弱的处理器上，以处理器编码报关运至香港，再由人随身携带入境，最后加热拆下——这条劳动密集的路线解释了每颗约 4000 美元的价格。昇腾 960DT 是华为第六代昇腾 960 系列中的训练/Decode 版本，与主打 Prefill 的 960PR 共享同一代微架构，但在显存子系统上明显偏向高带宽，因此对 HBM 的依赖是结构性的，而非偶然。

telegram · zaihuapd · 11月4日 14:52

**背景**: HBM（高带宽内存）是把 DRAM 垂直堆叠成单一封装、通过超宽接口连接的存储技术，能让 AI 加速卡以足够快的速度喂饱计算单元；HBM3E 是当前的主流世代，被用于英伟达 H200 等产品。该市场由三星、SK 海力士和美光主导，长鑫等中国厂商仍处于早期阶段，TrendForce 估计到 2027 年中国供应商在 HBM 市场的份额仍不到 2%。美国的出口管制限制先进 HBM 对华销售，这也是相关货源要经由香港等中转地的原因。华为在 9 月 17 日的全联接大会 2026 上公布了昇腾 960 系列，称研发进度超出预期、整体性能较上一代翻番。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mirrorfrog.com/docs/cards/huawei/ascend-960dt/">Huawei Ascend 960DT (昇腾 960DT) | AI 算力卡百科 | 233 款 AI 芯片...</a></li>
<li><a href="https://www.199it.com/archives/1860209.html">TrendForce：2027年 中 国 供应商 HBM 份额不到2%， HBM ...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2083900025302671798">华为 HC2026 公布 960DT 完整参数，2027 年 Q1 面世</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#HBM`, `#AI chips`, `#semiconductor supply chain`, `#export controls`

---

<a id="item-10"></a>
## [蓝牙 HDT 标准正式发布：LE 峰值速率提升至 7.5 Mbps](https://www.bluetooth.com/press/bluetooth-high-data-throughput-opens-a-new-chapter-in-wireless-performance/) ⭐️ 8.0/10

11 月 4 日，蓝牙技术联盟（SIG）宣布正式采纳 Bluetooth HDT（High Data Throughput，高数据吞吐量）标准，作为蓝牙 Core 7.0 的可选特性，把蓝牙 LE 的最高速率从 2 Mbps 提升至 7.5 Mbps，接近原来的四倍，同时改善容量、能效与可靠性。首个标准化应用场景是高端无线音频，支持无损与高解析度音频，相关产品预计 2027 年前后推出。 这次带宽跃升移除了无损高解析度无线音频面临的最大技术障碍之一——在这一领域，蓝牙此前一直落后于有线连接以及各类私有 2.4 GHz/5 GHz 方案。如果 2027 年的时间表如期落地，将重塑耳机厂商、音频编解码方案商和蓝牙芯片设计公司的产品规划，也可能把 LE 推向音频之外更高吞吐量的应用场景。 HDT 是一个可选特性，并设计为可与旧设备兼容共存，这意味着连接两端都必须支持该特性才能达到更高速率；扣除协议开销后，实际吞吐量仍会低于 7.5 Mbps 的物理层标称值。该技术仍工作在拥挤的 2.4 GHz 频段，干扰与共存问题依然是影响音频时延与稳定性的现实挑战。

telegram · zaihuapd · 11月5日 01:39

**背景**: 蓝牙 LE（低功耗蓝牙）是蓝牙家族中主打低功耗的分支，自 2016 年蓝牙 5 引入 2M PHY 以来，其空中最大速率一直停留在 2 Mbps。这一上限正是无线传输无损或高解析度音频的关键瓶颈，因为 24bit/96kHz 这类格式所需的持续带宽远超常见蓝牙编解码器所能承载的水平。此后蓝牙技术联盟持续迭代核心规范，如今把 HDT 打包进 Core 7.0 版本；文中所说的 PHY 指物理层调制方式，它决定了空中的原始比特率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/354478/bluetooth-sig-announces-bluetooth-high-data-throughput">Bluetooth SIG Announces Bluetooth High Data... | TechPowerUp</a></li>
<li><a href="https://www.androidauthority.com/bluetooth-hdt-lossless-wireless-audio-3731705/">Bluetooth HDT could standardize lossless wireless audio</a></li>

</ul>
</details>

**标签**: `#Bluetooth`, `#wireless`, `#audio`, `#standards`, `#HDT`

---