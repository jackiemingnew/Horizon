---
layout: default
title: "Horizon Summary: 2026-10-18 (ZH)"
date: 2026-10-18
lang: zh
---

> 从 34 条内容中筛选出 4 条重要资讯。

---

1. [vLLM v0.32.0 发布：新增结构化决策端点，并大幅扩展 NVFP4/FP8 KV 缓存支持](#item-1) ⭐️ 8.0/10
2. [RepRapMicron：开源项目瞄准微米级可自我复制的 3D 打印](#item-2) ⭐️ 8.0/10
3. [Linux 内核 CVE-2026-99999 漏洞可实现 KVM 访客逃逸](#item-3) ⭐️ 8.0/10
4. [谷歌开源 Harness² 递归智能体优化框架](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.32.0 发布：新增结构化决策端点，并大幅扩展 NVFP4/FP8 KV 缓存支持](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 8.0/10

vLLM 发布 v0.32.0，这是由 363 位贡献者（其中 121 位是新贡献者）提交 814 个 commit 的大版本，核心亮点是新增 `POST /v1/systemone` 端点，可针对结构化状态回答 `choice`、`noul` 和 `score` 三类带类型的问题，并且默认启用。该版本还加入了由模型 checkpoint 驱动的通用 `hf` 工具调用解析器与推理（reasoning）解析器（模型若自带 `response_template` 就无需专门的解析器），并将低精度 NVFP4/FP8 KV 缓存支持扩展到 SM8x、SM12x、SM90 和 SM100 GPU，涵盖 SM12x 上的 XQA 解码以及 SM100 上 MiniMax-M3 的稀疏注意力。 vLLM 是使用最广泛的开源大模型推理与 serving 引擎之一，因此这样规模的版本会直接影响所有大规模部署模型的团队：更低精度的 KV 缓存可降低单卡显存占用并提升吞吐，而通用解析器和结构化决策端点则省去了大量针对单个模型的适配代码。这些改动主要利好那些在现代 NVIDIA（以及 ROCm）硬件上运行大量异构模型的团队，因为显存压力和定制成本正是这类团队的主要开销来源。 发布说明给出了若干基于贡献者自有基准的量化收益：在 SM100 上 GLM-5.x 默认使用 FP8 KV 缓存，使每 rank 的 KV 显存减半、吞吐提升 2.3-5.5%，代价是首 token 延迟（TTFT）增加 7-11%；当 `--api-server-count` 大于 1 时，Qwen3-0.6B 的短请求每秒请求数提升 43-85%。该版本还包含重要破坏性变更：放弃 Python 3.10 支持，限制默认 CORS 来源，要求 `transformers` >=5.16.1,<5.20.0 与 `tokenizers` >=0.23.2，移除 cascade attention 与 `mamba_cache_mode="all"`，且 `max_tokens` 不再从上下文窗口中预留；同时还修复了多个安全公告（聊天模板资源耗尽、tokenizer 的 `max_token_id`、P2P ZMQ socket 耗尽）。

github · khluu · 10月18日 06:50

**背景**: vLLM 是一个用于大语言模型推理服务的开源引擎，以 PagedAttention 式的显存管理著称，可在批量推理时保持较高的 GPU 利用率。它的 KV 缓存保存已处理 token 的 key 与 value 张量，避免模型每一步重复计算；而用 FP8 或 4 位 NVFP4 等更低精度格式存储这些张量，可以让更多 token（更长上下文、更大批量）塞进同样的显存。工具调用解析器和推理解析器负责把模型原始输出转换为结构化函数调用或分离出思维链文本；SM8x、SM90、SM100 指 NVIDIA GPU 的计算能力代号（对应 Ampere、Hopper 和 Blackwell 架构），因此“支持 SM100”意味着该特性针对这一代硬件做了专门优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/serving/online_serving/structured_decisions/">Structured Decisions - vLLM</a></li>
<li><a href="https://www.tensormesh.ai/learn/kv-cache-quantization">KV Cache Quantization: FP8, FP4, and What They Cost You</a></li>
<li><a href="https://nvidia.github.io/TensorRT-Edge-LLM/cpp_api/kernels/decoderXQARunner.html">Decoder XQA Runner — TensorRT Edge-LLM</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#release`, `#kv-cache`, `#quantization`

---

<a id="item-2"></a>
## [RepRapMicron：开源项目瞄准微米级可自我复制的 3D 打印](https://github.com/VikOlliver/RepRapMicron/wiki) ⭐️ 8.0/10

由 RepRap 社区资深开发者 Vik Olliver 主导的 RepRapMicron（μRepRap）项目在公开的 GitHub wiki 上公布了其设计文档，目标是作为开源 RepRap 3D 打印机项目的延伸，把制造能力下探到微米级，可实现约 10 微米的特征尺寸。该 wiki 涵盖了硬件设计、工具头与控制软件，并展示了早期打印出的物体以及诸如用一滴异丙醇将零件从 Kapton 胶带上取下的实用工艺记录。 RepRap 最初的愿景是让人人都能拥有一台可自我复制的制造机器，而把这一理念推进到微米分辨率，则为微结构乃至简单微芯片的低成本、分布式制造打开了大门。如果成功，业余 3D 打印与专业微纳加工之间由昂贵光刻和双光子设备划定的界限将明显缩小。 该项目仍在演进之中，较大物体的打印质量仍是难题，因此 10 微米的目标指的是最佳情况下的特征分辨率，而非常规产出。它依靠高分辨率成像与精密运动控制软件来弥合业余硬件与微纳加工之间的差距，且 wiki 以公开方式记录工作流程，而非发表经同行评审的成果。

hackernews · RobotToaster · 10月18日 13:48 · [社区讨论](https://news.ycombinator.com/item?id=50141076)

**背景**: RepRap 是最早的开源自我复制 3D 打印机项目：一台免费的桌面机器，能够打印出用于复制自身的塑料零件，不过电机、电子元件等并非全部都能打印。传统熔融挤出打印机的特征尺寸在数十到数百微米量级，受喷嘴尺寸和挤出物理限制，若要达到个位数微米通常需要双光子聚合或光刻等技术。RepRapMicron 所探讨的，正是一台由 RepRap 式零件搭建、成本低廉的开源机器能否在光学放大下直接在微米尺度操控材料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reprap.org/wiki/RepRapMicron">RepRapMicron - RepRap GitHub - VikOlliver/RepRapMicron: μRepRap - A 3D printer ... RepRapMicron – Hackaday RepRapMicron: an open-source microscale RepRap… · AGI Hunt The Latest From RepRapMicron – Nail Gel, First Objects, And ... RepRap: Blog Shrinking the Factory: Meet RepRapMicron, the Open-Source ...</a></li>
<li><a href="https://github.com/VikOlliver/RepRapMicron">GitHub - VikOlliver/RepRapMicron: μRepRap - A 3D printer ...</a></li>
<li><a href="https://hackaday.com/tag/reprapmicron/">RepRapMicron – Hackaday</a></li>

</ul>
</details>

**社区讨论**: 评论者对该项目反应热烈，有人将其与 18 世纪 90 年代末相类比——当时 Ramsden、Maudslay 和 Wilkinson 把精密加工变成了可稳定量产的工艺；也有人打趣说 18 个月后就能自己造内存条了。不少人看重的，是让目前只存在于软件中的芯片设计得以低成本、可持续地制造出来；但也有一位质疑者反问，究竟凭什么指望这台机器能打印出自身千分之一尺寸的复制品。

**标签**: `#3d-printing`, `#reprap`, `#microfabrication`, `#hardware`, `#self-replication`

---

<a id="item-3"></a>
## [Linux 内核 CVE-2026-99999 漏洞可实现 KVM 访客逃逸](http://pwn.ai/) ⭐️ 8.0/10

PWN.AI 研究人员披露了 Linux 内核漏洞 CVE-2026-99999：该漏洞允许 KVM 访客改写已经通过校验的 IPv4 头，从而泄露 32 字节主机内存；研究团队还在自有 KVM 环境中演示了完整的访客到宿主机逃逸。相关修复已于 2026 年 10 月 14 日合并进 Linux 主线内核，随后被回迁到七个稳定版本分支。 KVM 是大多数公有云和多租户虚拟化平台的底层基础，因此一个能让不受信任的虚拟机突破访客/宿主机隔离边界的漏洞，直接动摇了这些平台赖以成立的核心安全假设，其 CVSS 评分为 9.3（严重）。任何运行不受信任或由客户控制的虚拟机的运营方——云服务商、VPS 提供商和 CI 系统——在打补丁之前都直接暴露在风险之中。 根本原因在于：当带有错误校验和元数据的数据包进入 IPv4 协议栈时，skb_checksum_help 会破坏网络头——在 virtio-net 场景下，不受信任的访客可以覆写宿主机上已经通过校验的 IPv4 头的两个字节。除 32 字节主机内存泄露外，研究人员还报告了宿主机崩溃以及在测试主机上以 root 身份执行代码；修复已随稳定内核 7.2.11、6.18.57、6.12.113、6.6.159、6.1.190、5.15.223 和 5.10.272 发布。

telegram · zaihuapd · 10月18日 09:47

**背景**: KVM 是内建于 Linux 内核的虚拟化层（hypervisor），让一台物理机可以运行多个相互隔离的虚拟机，而访客与宿主机之间的边界正是多租户云所依赖的安全保证。Linux 网络大量依赖校验和卸载（checksum offload）：网卡或 virtio-net 半虚拟化设备在硬件中计算数据包校验和，并在元数据中标记该包“已完成校验”，内核通常信任这一标记而跳过重新校验。当数据包的元数据不一致时，辅助函数 skb_checksum_help 会通过写入数据包头的方式在软件中重新计算校验和；如果记录的校验和偏移量从未被验证，这次写入就会落到错误的位置——这正是该 CVE 所利用的原语。所谓访客到宿主机逃逸，是指虚拟机内部运行的代码突破隔离、在物理宿主机上执行，且通常获得高权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cvefeed.io/vuln/detail/CVE-2026-99999">CVE-2026-99999 - ipv4: validate checksum_start before ...</a></li>
<li><a href="https://blog.cloudlinux.com/cve-2026-99999-guest-to-host-escape">CVE-2026-99999 Guest-to-Host Escape: mitigation and kernel ...</a></li>
<li><a href="https://thelinuxcamp.com/news/seven-linux-kernel-updates-fix-ipv4-checksum-metadata-corruption-mvauzk2s">Seven Linux kernel updates fix IPv4 checksum-metadata ...</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#KVM`, `#virtualization security`, `#CVE`, `#guest escape`

---

<a id="item-4"></a>
## [谷歌开源 Harness² 递归智能体优化框架](https://github.com/google-research/harness2) ⭐️ 8.0/10

谷歌研究（Google Research）开源了 Harness²，这是一个即插即用的框架，能够在完全不改动模型权重的前提下，递归地优化 LLM 智能体外围的 harness（提示词、代码、工具与脚手架）。该框架在 WorkBuddy-Bench 等基准测试中报告了最高 11.5 分的提升，并提供并行与顺序两种递归模式，同时集成了多款已有基准测试，以 Apache 2.0 协议开源。 这一发布表明，无需更强或经过微调的模型，也能显著提升智能体的表现，这既降低了构建高性能智能体的成本，也把关注点从模型规模转向了 harness 工程。由于它是即插即用且开源许可，生态中的智能体开发者可以直接将其用于现有流水线，而不必重新训练模型。 Harness² 连接了两层递归：任务级递归通过一个对比式的“Propose-Probe-Compose”步骤在当前任务上改进 harness，且无需真实标注验证器即可运行；第二层递归则可进一步扩展，以应对在 harness 设计阶段未曾见过的任务。值得注意的是，所有报告的提升都完全来自对冻结模型外围代码与文件的修改，因此收益上限受制于底层模型本身已具备的能力。

telegram · zaihuapd · 10月18日 11:24

**背景**: 所谓智能体的“harness”，指的是智能体系统中模型之外的一切：系统提示词、工具定义、控制循环、文件处理与错误恢复逻辑。传统上，想让智能体表现更好，要么换成更强的模型，要么微调模型权重，这既昂贵又需要训练基础设施。Harness² 则把 harness 本身当作优化对象，让系统在反复尝试中重写并改进它。文中所用的 WorkBuddy-Bench 是腾讯推出的多领域编码智能体基准，覆盖代码、Web、办公与安全四类工作任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google-research/harness2">google-research/harness2 - GitHub</a></li>
<li><a href="https://arxiv.org/abs/2610.14224">[2610.14224] Harness^2: Recursive Agent Harnessing for an ...</a></li>
<li><a href="https://www.marktechpost.com/2026/10/18/google-harness2-recursive-agent-harnessing-framework/">Google Open-Sources Harness2, a Recursive Agent Harnessing ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#recursive optimization`, `#Google Research`, `#open source`, `#AI frameworks`

---