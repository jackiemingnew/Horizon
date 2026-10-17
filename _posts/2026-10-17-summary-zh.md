---
layout: default
title: "Horizon Summary: 2026-10-17 (ZH)"
date: 2026-10-17
lang: zh
---

> 从 37 条内容中筛选出 5 条重要资讯。

---

1. [Claude 破解 NIST 椭圆曲线种子之谜](#item-1) ⭐️ 8.0/10
2. [Jake Archibald 实测 JPEG XL 与 AVIF 的网页图像表现](#item-2) ⭐️ 8.0/10
3. [安全研究员披露并利用 OpenBSD 一个长达 37 年的内核漏洞](#item-3) ⭐️ 8.0/10
4. [ORL 让扩散语言模型在单张 RTX 5090 上达到 2788 tokens/s](#item-4) ⭐️ 8.0/10
5. [法院文件曝光 Telegram 向美国政府移交用户数据的细节](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude 破解 NIST 椭圆曲线种子之谜](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 8.0/10

Anthropic 的 Claude AI 发现，NIST 椭圆曲线 P-192、P-224、P-256、P-384 和 P-521 的种子并非由任何哈希算法生成，而是 C 标准库中 lrand48 伪随机数生成器以 Unix 时间戳作为种子所产生的输出。这一发现仅用不到半小时便完成，解决了一个悬置约 25 年的密码学谜团。 这一结果恢复了公众对曲线种子是通过普通且可验证的方式生成、而非被刻意选取以植入隐藏后门的信心，而这种担忧曾因 Dual_EC_DRBG 等事件被大幅放大。它还凸显了 AI 工具如何加速艰深的数学侦探工作，同时 Anthropic 将相关赏金捐赠给了互联网安全研究小组（ISRG）。 第五个二元域种子 B-163 仍无法解释，最可能的假设是它原本也以同样方式生成，但在发布过程中被误写了一位数字。即便该生成方法已被确认，此发现也并不能证明当年没有对候选种子进行搜索和丢弃——由于这些曲线据称是跨越数月时间生成的，被丢弃的候选值在这类分析中是不可见的。

hackernews · ahlCVA · 10月16日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

**背景**: NIST 于 2000 年在 FIPS 186-2 中发布了 P-192 至 P-521 椭圆曲线，这些曲线支撑着包括 ECDSA 签名在内的现代密码学。ANSI X9.62 规定，曲线应通过取一个任意种子、用 SHA-1 对其进行哈希、再由输出派生曲线系数 b 的方式“可验证地随机”生成。由于据称种子是 NSA 于 1997 年提供的，而一个种子是否可信取决于其来源，密码学家们长期要求公开证明种子的原始生成过程是无害的；Filippo Valsorda 甚至为此悬赏 12000 美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://words.filippo.io/seeds-bounty/">Announcing the $12k NIST Elliptic Curves Seeds Bounty</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/bounty-offered-for-secret-nsa-seeds-behind-nist-elliptic-curves-algo/">Bounty offered for secret NSA seeds behind NIST elliptic curves algo</a></li>
<li><a href="https://www.anthropic.com/research/ecdsa-curve-origins">Claude reveals ECDSA curve origins \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论者大多感到欣喜，有人开玩笑说某位 NSA 员工“在过去四分之一个世纪里一直在暗自窃笑”，还有人把整件事概括为“13 年的阴谋论，结果只是 srand48(time(NULL))”。也有更为怀疑的声音指出，确认生成方法并不能排除当年的刻意挑选，因为数月间生成并被丢弃的候选种子无从观察。也有人称赞 Anthropic 选择了更高的赏金并将其捐给 ISRG，还有评论者认为无法解释的 B-163 种子很可能只是公布数字中的一处笔误。

**标签**: `#cryptography`, `#elliptic-curves`, `#NIST`, `#random-number-generator`, `#Claude-AI`

---

<a id="item-2"></a>
## [Jake Archibald 实测 JPEG XL 与 AVIF 的网页图像表现](https://jakearchibald.com/2026/jpeg-xl-vs-avif/) ⭐️ 8.0/10

Web 平台工程师 Jake Archibald 发布了一篇针对网页交付场景的 JPEG XL（JXL）与 AVIF 实测对比，在照片、截图和插画上比较了文件体积与视觉质量。该文在 Hacker News 上引发大规模讨论（183 分、142 条评论），深入探讨了编码速度、质量伪影以及实用的 ffmpeg 参数设置。 图像字节数仍是网页性能中最大的开销之一，因此 JXL 与 AVIF 之间的选择会直接影响每个网站的页面体积、带宽消耗和渲染质量。这场讨论还说明，仅仅选定格式并不够：编码器的成熟度与参数设置往往比容器格式本身更关键。 社区成员指出，libjxl 的高 effort 模式（effort 大于 7）速度极慢——据称每张图需 9 到 46 秒，是默认设置的 50 至 180 倍——原因是它运行了基于 Butteraugli 感知误差指标的迭代优化循环，不过像 jixel 这样的替代编码器可在数秒内得到相近结果。还有人分享了处理 alpha 透明通道（PNG 透明）的 AVIF ffmpeg 具体命令，并指出使用更好的 JXL 编码器可将无损截图的体积再缩小约 30%–39%。

hackernews · farlight · 10月16日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=50120224)

**背景**: JPEG XL 是新一代图像格式，同时支持有损与无损压缩，由 JPEG 委员会联合 Google 和 Cloudinary 开发，目标是在超越旧版 JPEG 的同时仍能在纯软件环境下高效解码。AVIF 则是开放媒体联盟（Alliance for Open Media）推出的竞争格式，基于 AV1 视频编解码器，并已在浏览器中得到广泛支持。两种格式都使用有损压缩，通过丢弃数据来减小体积，因此可能产生可见的压缩伪影，例如色带或高光细节丢失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>
<li><a href="https://shortpixel.com/blog/what-is-avif-and-why-is-it-good/">What is AVIF and why is it good? - ShortPixel Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compression_artifact">Compression artifact - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 整体情绪褒贬不一但技术含量很高：一些评论者称赞 AVIF 适合生产环境并分享了调优后的 ffmpeg 参数，另一些人则认为 AVIF 渲染的 F1 赛车图片明显抹去了车身高光并生成了看似合理的替代细节，并将其视为 AVIF 在关键影像上存在短板的证据。一个反复出现的反驳观点是，JXL 目前的编码器仍不成熟，因此 Archibald 给出的体积数据低估了该格式在更好工具链下的潜力。

**标签**: `#image-compression`, `#web-performance`, `#jpeg-xl`, `#avif`, `#codecs`

---

<a id="item-3"></a>
## [安全研究员披露并利用 OpenBSD 一个长达 37 年的内核漏洞](https://calif.io/research/big-fish) ⭐️ 8.0/10

一位安全研究员发布了题为《Big Fish》的详细研究报告，公开披露并演示了如何利用 OpenBSD 内核中一个长达 37 年的漏洞。这项研究表明，这个漏洞在被公认为开源界审计最严格的代码库之一中存活了数十年。 OpenBSD 的声誉建立在其安全优先的理念和主动源码审计之上，因此一个潜伏 37 年仍可被利用的内核漏洞，动摇了对人工代码审查究竟能提供多少保障的假设。它同时也是一份极具说服力的案例研究，揭示了模糊测试与静态分析在应对某些类型内核漏洞时的实际局限。 社区成员指出，同一缺陷似乎在 1999 年 8 月 NetBSD 重写相关代码时被意外修复，暗示该漏洞仅保留在 BSD 内核的共同血脉之中。讨论焦点在于：这个漏洞能否通过模糊测试或静态分析被发现，还是必须依靠人类对特定利用原语进行推理才能识别。

hackernews · rs_rs_rs_rs_rs · 10月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50118977)

**背景**: OpenBSD 是一款免费、开源的类 Unix 操作系统，以高度重视安全性、正确性和代码透明著称，并对其基础系统进行持续审计。模糊测试（fuzzing）是一种自动化测试技术，通过向程序输入无效、异常或随机数据来触发崩溃与漏洞；而静态分析则在不运行代码的情况下检查源码以发现潜在缺陷。这项研究说明，这两种自动化手段都可能漏掉那些需要对利用原语进行推理才能发现的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.liquidweb.com/blog/what-is-openbsd/">What is OpenBSD ? Overview & Latest Features | Liquid Web</a></li>
<li><a href="https://www.lenovo.com/us/en/glossary/openbsd/">What is OpenBSD ? Secure Open-Source Operating... | Lenovo US</a></li>

</ul>
</details>

**社区讨论**: 评论者对这篇报告的呈现方式表示赞赏，有人还打趣其 OpenBSD 发布版风格的配图，并期待主题曲。多位评论者指出该漏洞在 1999 年 8 月被 NetBSD 意外修复，而一条关键讨论则围绕以下问题展开：模糊测试或静态分析是否真有可能发现这类漏洞，还是必须依靠人类对利用原语的思考。

**标签**: `#security`, `#kernel`, `#openbsd`, `#vulnerability-research`, `#exploitation`

---

<a id="item-4"></a>
## [ORL 让扩散语言模型在单张 RTX 5090 上达到 2788 tokens/s](https://www.reddit.com/r/MachineLearning/comments/1x7qgr0/research_2788_tokenss_on_a_single_rtx_5090_with_a/) ⭐️ 8.0/10

研究团队发布了 ORL（On-Policy Residual Learning，同策略残差学习），一种针对扩散语言模型的训练后优化方法：它直接在当前模型新生成的残差轨迹上训练，并引入「相邻熵收缩」（AEC）损失，让每个去噪步骤更快地降低不确定性。配合自研推理引擎 dlmrt，他们报告在单张 RTX 5090 上 LLaDA-2.1-mini + ORL 达到 2788 tokens/s，在 8× B200 上以 NVFP4 运行 DiffusionGemma 26B MoE + ORL 达到 7708 tokens/s，QwenDLM-4B 端到端吞吐提升约 6.9×，HumanEval pass@1 从 82.9% 提升到 89.6%。模型、训练代码、评测流程和推理引擎均已开源。 扩散语言模型可以并行地细化和定稿多个 token，但过去需要的去噪步数太多，在延迟上一直难以与自回归解码竞争。ORL 声称正好瞄准这一瓶颈，同时还提升了精度，并且连同开源推理引擎一起发布，这可能让并行扩散解码在低延迟、单请求的场景中真正可用，而不再只是研究上的新奇事物。 所有亮眼数字都来自 batch size 为 1 的单请求解码，并且是特定基准上的峰值结果，而非任意提示下的平均值；LLaDA-2.1-mini 的后续训练仅需 420 万个自生成 token 和 36 个 H100 GPU 小时。与投机解码的对比属于端到端系统级对比而非纯算法对比：ORL 使用 dlmrt，而 DFlash 和 EAGLE3 跑在 vLLM 上，并且这些结果均为团队自报、尚未经过同行评审。

reddit · r/MachineLearning · /u/arty_photography · 10月16日 20:03

**背景**: 自回归大模型从左到右一次生成一个 token，因此延迟随序列长度线性增长。扩散语言模型（dLLM）则从被破坏或掩码的序列出发，迭代地去噪，从而可以并行地细化和定稿大量 token，但只有当模型能在很少的前向次数内收敛到好答案时，这种并行性才有价值。ORL 是一种训练后配方，教已有的 dLLM 把自身先前的预测作为残差上下文继续携带并逐步精炼；dlmrt 则是配套的推理引擎，它把整个去噪循环捕获进一张 CUDA 图并在 GPU 上执行，从而避免每一步由 CPU 启动和同步带来的开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Introspective-Diffusion/ORL/blob/main/">ORL: On-Policy Residual Learning for Diffusion Language Models</a></li>
<li><a href="https://arxiv.org/abs/2508.10875">[2508.10875] A Survey on Diffusion Language Models - arXiv.org Diffusion Language Models: An Experimental Analysis Diffusion Language Models (dLLMs) - emergentmind.com (PDF) Diffusion-based Large Language Models Survey - ResearchGate Awesome Diffusion Language Models Diffusion-based Large Language Models Survey</a></li>
<li><a href="https://www.truefoundry.com/blog/sglang-vs-vllm-vs-tensorrt-llm">SGLang vs vLLM vs TensorRT-LLM: Choosing an Inference Engine</a></li>

</ul>
</details>

**标签**: `#diffusion-language-models`, `#LLM-inference`, `#open-source`, `#GPU-optimization`, `#machine-learning-research`

---

<a id="item-5"></a>
## [法院文件曝光 Telegram 向美国政府移交用户数据的细节](https://www.404media.co/heres-what-telegram-giving-data-to-the-u-s-government-looks-like/) ⭐️ 8.0/10

新公开的法院文件显示，Telegram 在回应美国法院命令时，向执法部门提供了某名用户的手机号、用户 ID 和 IP 地址，并在信函中称这是「自愿」提供，同时又不承认自己受美国司法管辖。该披露与穆罕默德·穆赫塔迪（Mahmoud Al-Muhtadi）一案相关，他被指参与 2023 年 10 月 7 日对以色列的袭击；文件还显示，截至今年 1 月，Telegram 已向美方提供了 2253 名用户的数据。 这些文件提供了罕见的实证，说明一个长期以隐私友好为卖点的平台实际上是美国执法部门如何配合的，这可能重塑用户对通讯应用保密性的信任与预期。它同时把焦点放在一个尚未解决的法律问题上：总部设在美国境外的公司是否有义务遵守美国法院命令——这一矛盾关系到每一家全球性的通讯平台。 在穆赫塔迪一案中披露的用户数据包括手机号、用户 ID 和 IP 地址，属于元数据而非消息内容本身；Telegram 一边称此次移交是「自愿」的，一边又质疑美国的司法管辖，这种姿态使其法律义务显得含糊不清。截至 1 月已披露 2253 名用户数据这一数字，说明此类请求可能比该公司公开宣传中所暗示的更加常规化。

telegram · zaihuapd · 10月16日 14:57

**背景**: Telegram 是一款以隐私保护为卖点的通讯应用，其架构区别对待两类聊天：普通云端聊天存储在 Telegram 服务器上，而可选的「私密聊天」才采用端到端加密，只有后者在设计上保证公司自己也读不到内容。由于本案披露的是手机号、用户 ID、IP 地址等标识符和网络元数据，而非消息正文，这一案例说明平台无需破坏加密也能交出大量信息。Telegram 的总部长期设在美国境外，这也是其围绕美国司法管辖权的抗辩成为争议核心、而非细枝末节的原因。

**标签**: `#Telegram`, `#privacy`, `#surveillance`, `#data disclosure`, `#law enforcement`

---