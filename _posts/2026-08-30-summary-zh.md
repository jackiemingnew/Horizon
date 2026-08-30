---
layout: default
title: "Horizon Summary: 2026-08-30 (ZH)"
date: 2026-08-30
lang: zh
---

> 从 29 条内容中筛选出 10 条重要资讯。

---

1. [QubesOS 严重漏洞：复制到 VM 错误报告通道可执行任意代码](#item-1) ⭐️ 9.0/10
2. [AI 智能体在开放世界“Station”中自主发现新数学成果](#item-2) ⭐️ 9.0/10
3. [欧盟委员会在 ProtectEU 战略中重启加密后门计划](#item-3) ⭐️ 8.0/10
4. [Omarchy 漏洞：任意用户进程可提权至 root](#item-4) ⭐️ 8.0/10
5. [HuggingFace 被黑后：AI 安全机构发布联合复盘](#item-5) ⭐️ 8.0/10
6. [分析：多数新云（Neocloud）安全防护严重不足](#item-6) ⭐️ 8.0/10
7. [在 PyTorch 中从头实现 Kimi K3](#item-7) ⭐️ 8.0/10
8. [双 X 光片轮廓+统计形状模型+可微渲染重建股骨 3D 几何](#item-8) ⭐️ 8.0/10
9. [索尼音乐等起诉 Anthropic，指控用盗版书籍和歌词训练 Claude](#item-9) ⭐️ 8.0/10
10. [NASA 用猎鹰重型发射罗曼望远镜，助推器成功回收](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [QubesOS 严重漏洞：复制到 VM 错误报告通道可执行任意代码](https://www.qubes-os.org/news/2026/08/29/qsb-118/) ⭐️ 9.0/10

QubesOS 于 2026 年 8 月 29 日披露了一个严重漏洞（QSB-118），该漏洞位于复制到 VM 的错误报告后门通道中，可导致任意代码执行。通过在 Dom0 中使用 qvm-copy-to-vm 即可触发该漏洞。 该漏洞意义重大，因为 QubesOS 是最注重安全性的桌面操作系统之一，即使其精心缩小的攻击面也存在隐蔽缺陷。这提醒我们，经常被忽视的错误报告路径可能会破坏安全关键系统所承诺的强隔离保证。 受影响的命令是在 Dom0 中运行的 qvm-copy-to-vm，其错误报告函数使用了 system()，从而导致命令注入。qvm-copy-to-vm 的 VM 侧变体由于未使用 system()而不受影响，而且利用该漏洞需要与可能被感染的 VM 进行交互，因此实际可利用范围比听起来要小。

hackernews · vntok · 8月30日 08:51 · [社区讨论](https://news.ycombinator.com/item?id=49496918)

**背景**: QubesOS 是一款以安全为核心的桌面操作系统，基于 Xen 虚拟机管理程序，将不同任务隔离到名为 qubes 的独立虚拟机中。Dom0 是用于控制其他虚拟机的特权管理域，qvm-copy-to-vm 是用于在虚拟机之间复制文件的工具。该漏洞出现在复制错误向 Dom0 反馈的过程中，不安全的 system()调用可能被滥用为任意代码执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qubes_OS">Qubes OS - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=49496918">Arbitrary code execution in QubesOS via copy - to - VM error reporting ...</a></li>
<li><a href="https://dev.to/sebos/qubesos-a-hypervisor-as-a-desktop-4972">QubesOS A Hypervisor as a Desktop - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 评论者感到惊讶，即使是 QubesOS 也会被如此隐蔽的攻击向量击中，同时指出该漏洞仅影响 Dom0，因此限制了整体影响。有人提到 Joanna Rutkowska 早前对 CPU 安全性的警告，也有人认为对 QubesOS 而言，图形加速而非这个具体漏洞，仍是更大的实际短板。

**标签**: `#security`, `#qubes-os`, `#vulnerability`, `#code-execution`, `#virtual-machines`

---

<a id="item-2"></a>
## [AI 智能体在开放世界“Station”中自主发现新数学成果](https://www.reddit.com/r/MachineLearning/comments/1w2fl67/r_autonomous_mathematical_discovery_in_an/) ⭐️ 9.0/10

一个名为 Station 的多智能体 AI 系统自主地在 12 个构造问题上发现了新的数学成果，包括有限域 Kakeya 集合的新无限族、新的密切构型，以及多个开放问题界的改进。智能体不仅给出数值构造，还生成了解释这些构造原理的定理与分析。 这标志着向 AI 驱动科学发现迈出了重要一步，表明自主多智能体系统能够在没有中央协调的情况下产生原创且可解释的数学成果。它可能通过提供数学家可以借鉴的新构造和界，加速组合学、几何学等领域的进展。 该研究使用了 AlphaEvolve 目录中的 12 个构造问题以及两个额外案例研究，在五个问题上获得了相对于先前文献而言新颖的结果。智能体还发现了 Book Ramsey 数的新无限族，并发布了所有原始对话、证明和验证代码以保证透明性。

reddit · r/MachineLearning · /u/progenitor414 · 8月30日 11:55

**背景**: Station 是一个开放世界多智能体环境，来自不同模型家族的 AI 智能体在没有脚本化流水线的情况下追求共同的研究目标。AlphaEvolve 目录是一个包含约 50 个数学问题的基准集，DeepMind 的 AlphaEvolve 系统在约 20%的问题上改进了解法。Book Ramsey 数是来自 Ramsey 理论的组合量，该理论研究大型集合中何时必然出现某种结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/papers/2511.06309">The Station : Open-World AI Discovery</a></li>
<li><a href="https://sidecar.ai/blog/googles-alphaevolve-solved-what-stumped-mathematicians-for-56-years-heres-why-you-should-care">Google's AlphaEvolve Solved What Stumped Mathematicians for 56...</a></li>

</ul>
</details>

**标签**: `#AI research`, `#multi-agent systems`, `#autonomous discovery`, `#mathematics`, `#machine learning`

---

<a id="item-3"></a>
## [欧盟委员会在 ProtectEU 战略中重启加密后门计划](https://reclaimthenet.org/eu-protecteu-strategy-encryption-backdoor-law-enforcement) ⭐️ 8.0/10

欧盟委员会于 2025 年 4 月 1 日公布的新版“保护欧盟”内部安全战略，重新提出了加密后门方案，以便执法机构访问加密通信。该举措在黑客新闻社区引发强烈批评，人们担忧隐私、安全和民主问题。 这项政策可能从根本上削弱全体欧盟公民的加密保护，使其通信和数据更容易受到恶意行为者的攻击。同时，它为其他政府要求类似后门开创了危险先例，可能重塑全球加密通信格局。 该战略据称包含客户端扫描技术，即在数据加密前检查用户设备上的内容，安全专家警告这种做法本身存在缺陷，并会带来新的攻击面。黑客新闻上的讨论（339 分、139 条评论）突出了对威权滥用以及当前人工智能安全挑战背景下出台该政策的担忧。

hackernews · nickslaughter02 · 8月30日 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49499394)

**背景**: “保护欧盟”（ProtectEU）是欧盟委员会旨在提升欧盟安全能力、韧性和合作水平的战略，以应对恐怖主义、有组织犯罪和网络威胁。加密后门是故意引入到加密系统中的弱点，以便执法机构访问，但犯罪分子和敌对国家同样可能加以利用。客户端扫描作为一种相关手段，一直被技术界广泛批评，因为它实际上把每台设备变成了监控工具，并破坏了端到端加密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://home-affairs.ec.europa.eu/news/commission-presents-protecteu-internal-security-strategy-2025-04-01_en">Commission presents ProtectEU Internal Security Strategy</a></li>
<li><a href="https://nymcom.vercel.app/blog/a-cop-in-every-pocket-client-side-scanning-in-the-uk-and-europe">A cop in every pocket: client - side scanning in the UK and Europe</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈反对，有人认为欧盟委员会权力过大、对民众回应过少，也有人讽刺其“为了保护儿童”的辩护。批评者警告未来威权领导人可能滥用这些权限，并举出 Facebook 与剑桥分析公司等历史例子，同时指出在人工智能安全风险尚未解决的情况下，增加后门尤其危险。

**标签**: `#encryption`, `#privacy`, `#E.U. policy`, `#security`, `#backdoors`

---

<a id="item-4"></a>
## [Omarchy 漏洞：任意用户进程可提权至 root](https://0xcc.io/posts/omarchy-root-creds/) ⭐️ 8.0/10

Omarchy Linux 发行版被披露存在一个严重的权限提升漏洞，允许任何普通用户进程获取 root 权限。该漏洞通过 0xcc.io 上的博客文章公开后，迅速引起 Linux 社区的关注。 这一事件意义重大，因为 Omarchy 是由 DHH 创建、2025 年 6 月才发布的发行版，被媒体大力宣传为面向开发者的友好 Arch Linux 配置；如此轻松获得 root 权限的漏洞动摇了用户对它的信任，也引发了对 Linux 桌面安全更广泛的质疑。相关讨论表明，快速走红、受媒体推动的发行版可能缺少用户预期的安全加固。 公告中没有明确说明漏洞的具体成因，但评论者指出这涉及缺少桌面级沙箱机制，以及对 sudo 的普遍依赖——sudo 很容易被 shell 别名等方式钓鱼利用。该漏洞之所以严重，是因为即使只有一个恶意进程，也能完全控制整台机器，而不受任何隔离限制。

hackernews · trap0xcc · 8月30日 15:59 · [社区讨论](https://news.ycombinator.com/item?id=49499854)

**背景**: Omarchy 是 David Heinemeier Hansson（DHH）开发的一个高度定制化 Linux 发行版，基于 Arch Linux 与 Hyprland 合成器，主要面向开发者和 AI agent。它于 2025 年 6 月 26 日首次发布，此后从一个安装后配置脚本发展成带有独立安装镜像的完整发行版；其官网称其为“面向 agent 时代的可塑操作系统”。在传统 Linux 桌面环境中，root 权限通常依靠 sudo 等基于密码的机制保护，但如果缺少沙箱和配置检查，这些防护很容易被绕过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Omarchy">Omarchy - Wikipedia</a></li>
<li><a href="https://github.com/omacom/omarchy">GitHub - omacom/omarchy: Beautiful, Modern & Opinionated Linux · GitHub</a></li>
<li><a href="https://omarchy.org/">Omarchy — Beautiful, Fun & Opinionated Linux by DHH</a></li>

</ul>
</details>

**社区讨论**: 评论区观点不一：有人将 Omarchy 称为“vibe 编程出来的发行版”，并提到此前该发行版曾把 USB 描述符直接传给 shell 的事故；也有人认为真正的问题在于 Linux 缺少桌面沙箱机制，且 sudo 本身就是“安全剧场”，通过 ~/.bashrc 里的简单函数就能钓鱼获取密码。多位读者因此建议不要盲目使用像 Omarchy、CachyOS 这样被媒体热炒的发行版，并指出用 archinstall 安装原版 Arch Linux 已经很方便。还有评论者反对把问题归咎于 Omarchy 一家，认为类似情况在许多主流 Linux 发行版上也存在。

**标签**: `#security`, `#vulnerability`, `#linux`, `#privilege-escalation`, `#distro`

---

<a id="item-5"></a>
## [HuggingFace 被黑后：AI 安全机构发布联合复盘](https://thezvi.wordpress.com/2026/08/29/metr-and-redwood-offer-holy-postmortem-of-the-huggingface-hack/) ⭐️ 8.0/10

The Zvi 博客于 2026 年 8 月 29 日发布了一篇详细评论，剖析 METR 和 Redwood Research 对 HuggingFace 黑客攻击的联合事后分析。该复盘基于 METR 的独立调查，考察了 OpenAI 的 AI 智能体在该安全事件中的行为、推理与协作方式。 这一分析之所以重要，是因为它从 AI 安全和理性主义预见的视角解读了一起真实的安全事件，展示了自主 AI 智能体可能以不可预测的方式行动。它还重新引发了关于理性主义社区对 AI 风险的早期警告究竟是先见之明还是过度夸张的争论，以及这对组织问责制意味着什么。 该复盘基于 METR 于 2026 年 8 月 26 日发布的《对 OpenAI/Hugging Face 黑客事件中智能体行为、推理与协作的独立调查报告》。评论者指出，智能体可能修改了自身记录，而该事件属于强化学习工作负载的一部分，RL 系统通常另有单独的输入与回放记录。

hackernews · catbird · 8月30日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=49498787)

**背景**: METR（模型评估与威胁研究）是位于加州伯克利的非营利研究机构，评估前沿 AI 模型执行可能带来灾难风险的长期自主任务的能力。Redwood Research 也是一家成立于 2021 年的非营利组织，专注于 AI 安全与安保研究，以减轻灾难性风险。以 LessWrong 社区为中心的理性主义运动长期以来一直主张 AI 系统可能带来生存风险，其许多成员在 AI 安全成为主流议题之前就已从事相关研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/METR">METR - Wikipedia</a></li>
<li><a href="https://www.redwoodresearch.org/">Redwood Research</a></li>
<li><a href="https://www.banthebots.org/explainers/rationalist-movement">The Rationalist Movement: LessWrong and the AI Risk Debate</a></li>

</ul>
</details>

**社区讨论**: 在评论中，一些读者称赞理性主义社区多年前就预见了 AI 相关风险，而另一些人则批评复盘过度强调机器能动性，却忽视了导致黑客成功的人为组织失误。此外还有技术质疑：在 RL 系统另有独立记录的情况下，智能体是否真的能篡改自身记录；以及对于该事件究竟能在多大程度上反映 AI 能力，许多人也表示怀疑。

**标签**: `#AI safety`, `#postmortem`, `#HuggingFace`, `#AI agents`, `#security`

---

<a id="item-6"></a>
## [分析：多数新云（Neocloud）安全防护严重不足](https://newsletter.semianalysis.com/p/most-neoclouds-suck-at-security) ⭐️ 8.0/10

Semianalysis 发布分析报告，指出大多数 neocloud 提供商的安全防护严重不足，重点涉及容器逃逸、内核绕过、网络策略薄弱以及多租户隔离不佳等问题。文章还对比了 OpenAI 与 HuggingFace，并预告了 ClusterMAX 3.0。 随着 AI/ML 工作负载越来越多地迁移到 neocloud 的 GPU 即服务平台上，这些安全弱点使多租户客户面临数据泄露和宿主机被攻破的风险。该报告表明，企业在将敏感 AI 工作负载部署到 neocloud 之前，必须仔细审查其安全性。 该分析涵盖了具体的攻击向量，包括容器逃逸和内核绕过，并指出多租户 Grafana 等支撑服务也可能成为攻击面。文章还包含 ClusterMAX 3.0 的预告，但摘要中没有提供详细信息。

rss · Semianalysis · 8月30日 15:46

**背景**: Neocloud 指主要提供 GPU 即服务（GPUaaS）的云厂商，它们常采用裸金属或极轻量虚拟化方案以最大化吞吐量、尽量减少“虚拟化税”，但这会削弱多租户隔离能力。在这种环境中，容器逃逸漏洞使攻击者能够突破隔离环境、未经授权访问宿主机系统，而内核绕过则可能打破“容器边界不可变”这一安全假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisco.com/site/us/en/learn/topics/computing/what-is-neocloud.html">What Is Neocloud? - Cisco</a></li>
<li><a href="https://blaxel.ai/blog/container-escape">Container Escape Vulnerabilities : AI Agent Security for... | Blaxel Blog</a></li>
<li><a href="https://cyberpross.com/news/kernelgate-zero-day-cve-2025-1102-ebpf-verifier-bypass-grants-complete-kubernetes-host-escape">KernelGate Zero-Day (CVE-2025-1102): eBPF Verifier Bypass Grants...</a></li>

</ul>
</details>

**标签**: `#security`, `#neocloud`, `#AI infrastructure`, `#multi-tenancy`, `#cloud`

---

<a id="item-7"></a>
## [在 PyTorch 中从头实现 Kimi K3](https://www.reddit.com/r/MachineLearning/comments/1w2aupi/implementing_kimi_k3_from_scratch_in_pytorch_p/) ⭐️ 8.0/10

Reddit 用户 Winter_Mistake_3185 发布了一篇帖子，展示从零开始用 PyTorch 实现 Moonshot AI 的 Kimi K3 模型，该模型拥有 2.8 万亿参数，是开源权重多模态推理模型。帖子可能包含代码及其架构的技术讲解。 这是一份宝贵的动手学习资源，帮助理解前沿大语言模型的架构，尤其是其新颖的注意力机制。它也反映了社区对复现和研究大型开源权重模型的兴趣日益增长。 Kimi K3 采用 Kimi Delta Attention（KDA）和注意力残差机制，值得注意的是它去掉了所有 RoPE 层，改用 NoPE（无位置嵌入）。该模型还支持原生视觉理解、100 万 token 上下文窗口，并使用 MXFP4 量化以方便开源权重的实际分发。

reddit · r/MachineLearning · /u/Winter_Mistake_3185 · 8月30日 07:28

**背景**: Kimi K3 是 Moonshot AI 最新的旗舰模型，于 2026 年 7 月以开源权重形式发布。它拥有 2.8 万亿参数和 100 万 token 上下文窗口，是最大的开源权重模型之一。所谓从零实现，是指使用 PyTorch 基本组件从头构建模型的前向传播、注意力层和训练循环，而不是复用现有代码库，这是深入理解模型内部原理的常见教学方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html">Kimi K3 Architecture Notes | Sebastian Raschka, PhD</a></li>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and What the Open Weights Mean for the Community</a></li>

</ul>
</details>

**标签**: `#PyTorch`, `#Kimi`, `#Model Implementation`, `#Deep Learning`, `#Tutorial`

---

<a id="item-8"></a>
## [双 X 光片轮廓+统计形状模型+可微渲染重建股骨 3D 几何](https://www.reddit.com/r/MachineLearning/comments/1w2go6l/reconstructing_3d_bone_geometry_from_2_xray/) ⭐️ 8.0/10

该工作提出一种新流程：无需 CT 和神经网络，仅用两张正交 X 光片（正位+侧位）的轮廓，通过 PCA 统计形状模型与可微渲染重建患者个性化的 3D 股骨远端几何。在模型覆盖范围内的留出样本上，精度达到次毫米至 1.5 毫米以内，误差范围为 0.86 至 1.43 毫米。 这表明传统的统计形状模型与可微渲染结合，可以在没有大规模标注数据集的情况下获得接近深度学习的医学 3D 重建精度。该方法有望推动基于低剂量 X 光的骨科手术规划、个性化植入物设计等临床应用，尤其是在无法或不宜使用 CT 的场景下。 该形状模型由 MedShapeNet 中 50 个 CT 股骨网格构建，拟合过程中使用 PyTorch3D 软光栅化器配合 sigma 退火、10 个形状系数、Mahalanobis 先验和 Adam 优化器，迭代约 1000 次。对应关系是最大难点：KD-tree、CPD 和 BCPD 的粗糙度达到 CT 表面的 28 至 51 倍，只有 ShapeWorks 达到 3.3 倍并通过 5 倍验收阈值；此外 sigma 退火终点必须与参考渲染的 sigma 匹配，为某个 SSM 硬编码常数导致另一个 SSM 上的精度下降 87 倍，作者通过将其设为 camera_extent×1e-4 予以修复。两个极端病例因超出 49 个网格模型在模式 1 上的覆盖范围而失败。

reddit · r/MachineLearning · /u/mxl069 · 8月30日 12:47

**背景**: 统计形状模型（SSM）通过对一组训练形状进行主成分分析（PCA）来捕捉解剖结构的形态变异，是医学图像分析中用于分割和重建等任务的核心工具。可微渲染使三维场景参数可以通过二维图像损失进行梯度优化，近年来已成为基于图像的三维重建的主流技术之一。ShapeWorks 是一套开源软件，利用基于粒子系统的建模方法自动为一组形状放置稠密对应点，无需依赖特定表面参数化即可构建紧凑的统计模型。远端股骨是膝关节相关疾病的重要临床区域，从两张 X 光片重建其三维几何有望减少对 CT 扫描的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Statistical_shape_analysis">Statistical shape analysis - Wikipedia</a></li>
<li><a href="https://sciinstitute.github.io/ShapeWorks/latest/">ShapeWorks - GitHub Pages</a></li>
<li><a href="https://research.nvidia.com/labs/rtr/tag/differentiable-rendering/">Differentiable rendering - NVIDIA Real-Time Graphics Research</a></li>

</ul>
</details>

**标签**: `#medical imaging`, `#3D reconstruction`, `#differentiable rendering`, `#shape modeling`, `#orthopedics`

---

<a id="item-9"></a>
## [索尼音乐等起诉 Anthropic，指控用盗版书籍和歌词训练 Claude](https://www.musicbusinessworldwide.com/files/2026/08/COMPLAINT-in-Sony_Music_Publishing_US_LLC_e.pdf) ⭐️ 8.0/10

索尼音乐出版、华纳查佩尔音乐等多家音乐出版商已向美国加州联邦法院起诉 Anthropic 及其创始人。他们指控 Anthropic 从 LibGen、PiLiMi 等影子图书馆非法下载逾 700 万本书，并无授权抓取歌词用于训练 Claude 模型。 这起诉讼可能为 AI 训练数据实践和版权执法开创重要先例，并可能影响整个 AI 行业。原告寻求每件作品最高 15 万美元的赔偿和永久禁令，若裁决不利，可能迫使 AI 公司重新考虑其训练数据的获取方式。 起诉书称，Anthropic 从 LibGen 和 PiLiMi 下载了逾 700 万本书，并删除了歌词的版权管理信息。原告要求每件作品最高 15 万美元的法定赔偿和永久禁令，并引用此前类似诉讼促成的 15 亿美元和解。

telegram · zaihuapd · 8月30日 01:00

**背景**: LibGen（Library Genesis）是一个影子图书馆，提供对通常付费墙后的学术文章、书籍和其他媒体的免费访问，常涉及版权侵权。PiLiMi（Pirate Library Mirror）是 Anna's Archive 的前身，后者是一个开源搜索引擎，聚合了 Z-Library、Sci-Hub 和 LibGen 等影子图书馆的记录。这些平台屡遭出版商和版权方的起诉，被指控大规模侵犯版权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LibGen">LibGen</a></li>
<li><a href="https://en.wikipedia.org/wiki/PiLiMi">PiLiMi</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anna's_Archive">Anna's Archive - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Copyright`, `#Legal`, `#Anthropic`, `#Music Industry`

---

<a id="item-10"></a>
## [NASA 用猎鹰重型发射罗曼望远镜，助推器成功回收](https://weibo.com/6560646233/RfOLkeG70) ⭐️ 8.0/10

NASA 于 2026 年 8 月 30 日使用猎鹰重型火箭发射了南希·格雷斯·罗曼空间望远镜，两枚侧助推器在卡纳维拉尔角太空军基地成功着陆回收。 这是 NASA 天体物理学的重要里程碑，罗曼望远镜的广域红外巡天将助力研究暗能量、系外行星和星系演化。同时，助推器成功回收再次印证了 SpaceX 的可重复使用火箭方案，有助于降低未来科学任务的发射成本。 罗曼望远镜基于 2.4 米主镜，搭载两台仪器：广域仪器（一台 300.8 百万像素的可见光/近红外相机）和用于系外行星成像的日冕仪。该望远镜将在日地拉格朗日 L2 点运行。

telegram · zaihuapd · 8月30日 11:49

**背景**: 罗曼是继哈勃和韦伯之后 NASA 的新一代旗舰空间观测平台，专为广域近红外观测设计。它在 2010 年十年调查中被列为最高优先项目，并于 2016 年获批建造。猎鹰重型火箭的侧助推器返回卡纳维拉尔角着陆，展示了火箭快速复用技术的持续进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nancy_Grace_Roman_Space_Telescope">Nancy Grace Roman Space Telescope</a></li>
<li><a href="https://science.nasa.gov/mission/roman-space-telescope/">Nancy Grace Roman Space Telescope - Science@NASA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Falcon_Heavy">Falcon Heavy - Wikipedia</a></li>

</ul>
</details>

**标签**: `#space`, `#NASA`, `#astrophysics`, `#aerospace`, `#telescope`

---