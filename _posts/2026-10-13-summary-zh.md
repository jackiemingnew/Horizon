---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 38 条内容中筛选出 6 条重要资讯。

---

1. [网络攻击迫使欧洲超市冷柜进入除霜模式](#item-1) ⭐️ 8.0/10
2. [WiFi 7 路由器被改造成 320 Msps 软件无线电接收机](#item-2) ⭐️ 8.0/10
3. [Codex CLI 默认静默安装常驻自更新后台守护进程](#item-3) ⭐️ 8.0/10
4. [Show HN：PS2 游戏被静态重编译为 WebAssembly](#item-4) ⭐️ 8.0/10
5. [Python 3.15 发布，PEP 810 显式惰性导入正式落地](#item-5) ⭐️ 8.0/10
6. [learnc：直接调优未经修改的 C 代码常量以拟合数据](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [网络攻击迫使欧洲超市冷柜进入除霜模式](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

一场网络攻击导致欧洲多家连锁超市的制冷控制器失灵，其中包括法国零售商 Intermarché，约 150 家门店在 10 月 12 日前后被攻击，冷柜被强制进入自动除霜循环。据路透社、BBC 和《世界报》报道，该事件还波及门店定价系统和配送环节。 这是一起少见的、公开可见的针对运营技术（OT）而非 IT 系统的攻击，说明零售业中联网的老旧制冷控制器可被武器化，并直接造成食品变质、供应中断等物理后果。它还暗示攻击者可能在不同地区复用同一类制冷设备漏洞，包括 2026 年 8 月发生在美国军事设施冷柜上的事件。 疑似入口是已停止支持的 Danfoss 控制器，例如 SM800（2021 年终止支持）和 SC355（2016 年终止支持），Claroty 的 Team82 团队曾在一份题为《冻结控制器，解冻食物》的研究中分析过相关漏洞。值得注意的是，这类设备联网往往有正当理由——远程设定除霜时间、故障诊断以及跨门店能效对比——因此对运营方来说“干脆不联网”通常并不可行。

hackernews · Zeekaas · 10月12日 12:16 · [社区讨论](https://news.ycombinator.com/item?id=50055304)

**背景**: 商用制冷系统由电子柜体控制器管理，它决定压缩机何时运转、系统何时执行除霜循环（短暂加热蒸发器盘管以融化积冰）。近年来厂商推动这类控制器联网，以便维修工程师远程排障、零售商对比数百家门店的能耗表现。但由于许多控制器设计于 15 至 20 年前，当时 OT 安全尚未受到重视，它们常常存在认证薄弱、无固件升级途径、早已超出支持期限等问题，这正是棕地工业环境中典型的“老旧物联网”难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.danfoss.com/en/products/dcs/electronic-controls/">Electronic controls - Danfoss</a></li>
<li><a href="https://iotdigitaltwinplm.com/brownfield-iot-legacy-machine-connectivity-playbook-2026/">Brownfield IoT : Legacy Machine Connectivity... - IoT Digital Twin PLM</a></li>
<li><a href="https://www.linkedin.com/advice/3/dealing-legacy-iot-devices-your-network-you-uekff">Secure Legacy IoT : Mitigate Network Risks</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者普遍认为，根本原因是经济压力而非无知：Danfoss SM800、SC355 等控制器虽有已知 CVE，但门店利润微薄，轮班制 IT 人员既无安全审查预算，也无硬件更新周期。不少人反驳了“为什么要把冷柜联网”这种条件反射式的质疑，指出订阅制锁定的实验室与工业设备本身就强制联网；也有人推测此次攻击与 2026 年 8 月美军 commissary（军人服务社）冷柜事件存在关联，或是模仿作案。

**标签**: `#cybersecurity`, `#iot`, `#industrial-control-systems`, `#supply-chain`, `#legacy-systems`

---

<a id="item-2"></a>
## [WiFi 7 路由器被改造成 320 Msps 软件无线电接收机](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 8.0/10

一个名为 w1700k-sdr 的 GitHub 项目（github.com/h0m3us3r/w1700k-sdr）展示了如何把 WiFi 7 路由器内部的芯片组改造成软件无线电接收机，能够在 5 GHz 频段以 320 Msps 的速率采样。同一位开发者此前还做过 eSpDR，即用 ESP32 Wi-Fi 微控制器搭建的软件无线电。 这说明廉价大批量生产的消费级网络硬件可以充当高采样率的软件无线电前端，其成本远低于能达到同等速率的专用 SDR 设备。如果该技术能推广到其他 Wi-Fi 网卡，普通笔记本电脑和路由器就有可能成为低成本的射频实验、频谱监测与研究工具。 由于 320 Msps 约为目标频段宽度的两倍，这意味着它能提供很宽的瞬时捕获带宽；不过该项目只是接收机，并未宣称具备发射能力。有评论者指出 Banana Pi R4 使用的是同一款芯片组，因此该方法可能同样适用于那块开发板。

hackernews · djfergus · 10月12日 12:41 · [社区讨论](https://news.ycombinator.com/item?id=50055593)

**背景**: 软件定义无线电（SDR）是指把传统上由模拟硬件实现的功能——混频器、滤波器、放大器、调制器和解调器——改由通用计算机或嵌入式系统上的软件来完成，通常在射频前端和模数转换器之后进行。这样一台设备只需更换软件就能接收多种不同的无线电协议。WiFi 7（即 IEEE 802.11be）是第七代 Wi-Fi，为超高吞吐量而设计，其芯片组内置在 5 GHz 和 6 GHz 频段工作的高速模拟前端与数字化器，而这些正是软件无线电所需的部件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software-defined radio</a></li>
<li><a href="https://www.tp-link.com/in/wifi7/">What is WiFi 7 ? What does WiFi 7 offer? | TP-Link WiFi 7 Router</a></li>

</ul>
</details>

**社区讨论**: 评论者反响热烈，认为这可能是获得 5 GHz、320 Msps 接收机最便宜的方式，并提到该开发者早前的 ESP32 项目 eSpDR，期待更多 Wi-Fi 网卡被改造成软件无线电。也有人指出 Banana Pi R4 很可能使用同一款芯片组，追问手机厂商限制第三方使用 FM 收音机是否正是因为现代手机射频是软件定义的，还有人设想为这样的接收机配上衰减器、滤波器和混频器，做出廉价的服务监测仪替代品。

**标签**: `#SDR`, `#WiFi 7`, `#hardware hacking`, `#RF`, `#embedded systems`

---

<a id="item-3"></a>
## [Codex CLI 默认静默安装常驻自更新后台守护进程](https://github.com/openai/codex/issues/48195) ⭐️ 8.0/10

一个 GitHub issue（openai/codex#48195）指出，OpenAI 的 Codex CLI 默认启用了常驻后台守护进程，并且会自动自我更新，而官方文档中并没有提供关闭它的方法。该报告迅速在 Hacker News 上引发热议（480 分、244 条评论），开发者们描述了具体的负面影响，例如数 GB 的旧版本缓存，以及自动更新破坏代码仓库权限等问题。 这对任何在终端中使用 AI 编程代理的人都很重要，因为一个隐藏且常驻、还会静默下载并替换二进制文件的后台进程，会扩大攻击面，并增加这个工具在开发者个人机器和企业代码仓库中的软件供应链足迹。这也反映出开发者工具正整体转向沉重、可自我管理的后台服务，由此引发对用户知情同意、透明度和企业合规政策的质疑。 用户反映该守护进程累积的旧版本占用了约 12 GB 磁盘空间，而且自动更新会莫名其妙地把 .git 变成只读，从而阻塞正在进行的工作。社区找到了一种变通方法但官方并未记录：在 `~/.codex/config.toml` 的 `[features]` 段中设置 `daemon_auto_start = false`；对于写入 `~/.codex` 的 PID 文件和锁文件，可以删除并用指向 `/dev/null` 的符号链接替代，再用 `chattr +i` 将其标记为不可写。

hackernews · whimblepop · 10月12日 18:29 · [社区讨论](https://news.ycombinator.com/item?id=50060694)

**背景**: Codex CLI 是 OpenAI 推出的轻量级编程代理，在终端本地运行，于 2025 年 4 月 16 日与 o3、o4-mini 推理模型一同发布；它与此前 2021 年驱动 GitHub Copilot 的旧版 Codex 语言模型并非同一事物。后台守护进程是指主程序退出后仍在运行的长驻进程，通常用于处理更新、会话或远程任务；一旦与自动自我更新结合，就意味着无需用户显式操作即可拉取并执行代码，这也是此类行为通常被放在软件供应链安全语境下讨论的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Codex_CLI">Codex CLI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model)</a></li>
<li><a href="https://grokipedia.com/page/supply_chain_security">Supply chain security</a></li>

</ul>
</details>

**社区讨论**: 整体情绪以负面为主但仍具建设性：用户认为这个守护进程臃肿且问题多，有人称 Codex 在各项指标上都比 Claude Code 更差，也有人指出 Claude Code 采用的是同样的版本化二进制加后台任务的运行模式。另一些人分享了实用的缓解办法（利用 feature flag、把锁文件软链到 /dev/null 并用 `chattr +i` 锁定），还有人表示已改用刻意保持精简的 harness，例如主要依赖纯 bash 的 hax，而不是过度工程化的代理。

**标签**: `#ai-coding-agents`, `#codex-cli`, `#developer-tools`, `#privacy`, `#software-supply-chain`

---

<a id="item-4"></a>
## [Show HN：PS2 游戏被静态重编译为 WebAssembly](https://github.com/snuri00/ps2-web-recomp) ⭐️ 8.0/10

一位开发者发布了名为 ps2-web-recomp（github.com/snuri00/ps2-web-recomp）的 Show HN 项目，该项目将 PlayStation 2 游戏静态重编译为 WebAssembly，使其可以直接在网页浏览器中运行。该帖子获得了热烈反响，在 Hacker News 上拿到 277 分和 145 条评论。 这表明静态重编译这一迅速成熟的技术正被用于 PS2 这样的复杂主机平台，并通过 WebAssembly 交付，可能让游戏保存与浏览器端游玩变得更容易普及。讨论中还出现了类似的其他项目，说明一个面向 WebAssembly 的重编译工具生态正在初步形成。 评论者提到了一个平行项目 cretz/vitaslop：它不是针对单个游戏，而是在 WASM 中“构建”了一个面向 PS Vita 的 ARM 到 WASM 转译器，还包含 WebGPU 着色器与音频的转码。还有人建议把重编译器本身也编译成 WebAssembly，从而完全在浏览器中完成转换；同时有评论者提出警示，认为反编译/重编译项目缺乏成熟模拟器社区那样的信任度与审核机制。

hackernews · deadxwarrior · 10月12日 06:46 · [社区讨论](https://news.ycombinator.com/item?id=50052251)

**背景**: 静态重编译是二进制翻译的一种形式，它在运行之前就把某一指令集架构的机器码翻译成另一种目标架构的代码，而不是像模拟器那样在运行时逐条解释指令；广为人知的例子包括用于 Nintendo 64 二进制的 N64Recomp。WebAssembly（Wasm）是一种可移植、由 W3C 标准化的二进制格式，能在浏览器等宿主环境中以接近原生的速度运行，因此很自然地成为这类翻译代码的目标平台。二者结合后，主机游戏的二进制可以被一次性转换，然后在任何存在 Wasm 运行时的环境中执行，比如网页。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Static_recompilation">Static recompilation</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://github.com/N64Recomp/N64Recomp">GitHub - N64Recomp/N64Recomp: Tool to statically recompile ...</a></li>

</ul>
</details>

**社区讨论**: 整体氛围是对这项工程的热烈赞赏，但也夹杂着明显的信任与安全担忧：反编译/重编译项目不像模拟器社区那样经过严格审核，可能暗藏恶意软件。讨论的增量价值体现在一个可直接类比的 PS Vita ARM 到 WASM 项目、把重编译器本身搬到浏览器中运行的建议，以及一句关于《GT 赛车》漫长读盘时间的调侃。

**标签**: `#WebAssembly`, `#Static Recompilation`, `#Game Emulation`, `#Reverse Engineering`, `#Show HN`

---

<a id="item-5"></a>
## [Python 3.15 发布，PEP 810 显式惰性导入正式落地](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 正式发布，Simon Willison 重点介绍了两个新特性：PEP 810 显式惰性导入（写作 `lazy import json` 或 `lazy from pathlib import Path`），以及 PEP 798 推导式中的解包语法（如 `[*L for L in lists]`）。他还提到，随着 Python 3.10 结束支持，他终于可以在自己的项目中放弃 3.10，转而使用早在 Python 3.11 就已引入的特性。 惰性导入直击一个长期痛点：Python 会在文件顶部立即导入模块，因此安装一个依赖沉重的插件，可能让每条命令的启动都多花好几秒。相关基准测试显示，应用启动时间可从普通导入的约 104 毫秒降到全惰性导入的约 36 毫秒，接近 3 倍提速；而 Python 支撑着大量工具与基础设施，因此每个大版本的发布几乎影响整个生态。 PEP 810 是 CPython 中惰性导入的第二次尝试：PEP 690 曾在 2022 年提出全局隐式惰性导入，但因复杂性和不可预测性而在 2023 年被撤回，正是这种显式、可选择启用的设计让它最终获得通过，模块只会在其符号第一次被真正使用时才被导入。PEP 798 扩展了源自 PEP 448、在 Python 3.5 中落地的解包语法；而 Willison 此前不得不在 LLM 的插件文档中建议作者手动实现惰性导入，以避免 `sentence_transformers` 这类重型依赖拖慢 `llm` 命令。

rss · Simon Willison · 10月12日 18:15

**背景**: Python 每年十月发布一个新的特性版本，每个版本大约支持五年，先经过缺陷修复阶段，再进入仅安全修复阶段，这正是 3.10 生命周期结束促使 Willison 放弃它的原因。PEP（Python Enhancement Proposal，Python 增强提案）是用于提出和讨论语言改动的文档格式；PEP 810 定义了显式惰性导入的语法与语义，与 Python 常规的即时导入形成对照——后者在 import 语句执行的瞬间就会加载模块。惰性导入把加载推迟到被导入的名字第一次被使用之时，以极小的间接开销换取更快的启动速度和更低的内存占用，尤其适合那些导入了远超单次运行实际所需模块的程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0810/">PEP 810 – Explicit lazy imports | peps . python .org</a></li>
<li><a href="https://socket.dev/blog/pep-810-proposes-explicit-lazy-imports-for-python-3-15">PEP 810 Proposes Explicit Lazy Imports for Python 3.15 - Soc...</a></li>
<li><a href="https://realpython.com/python315-lazy-imports/">Python 3.15 Preview: Lazy Imports – Real Python</a></li>

</ul>
</details>

**标签**: `#python`, `#python-3.15`, `#pep-810`, `#lazy-imports`, `#programming-languages`

---

<a id="item-6"></a>
## [learnc：直接调优未经修改的 C 代码常量以拟合数据](https://www.reddit.com/r/MachineLearning/comments/1x4dlbm/learnc_fit_the_constants_in_existing_c_code_to/) ⭐️ 8.0/10

一个名为 learnc 的 MIT 许可新工具，能够针对用户自己编写的评分函数，自动调优未经修改的 C 源码中的具名常量，并把更新后的值写回同一个文件。在留出数据上，它让 stb_image_write.h 中 128 个 JPEG 量化表条目在相同 SSIM 下取得 9.1% 的 BD-rate 提升（mozjpeg 的量化表仅为 2.7%），并把 Google WebRTC VAD 在 LibriParty 评测集上的 F1 从 0.810 提升到 0.859。 这提供了一种通用的、与代码无关的优化闭环：任何拥有可调常量和可度量目标的 C 代码库，都可以在不重写算法、不引入新依赖的情况下获得改进。它对手工调参启发式规则的系统与信号处理工程师尤其有价值，而 JPEG 量化表上的结果说明它能够重新发现甚至超越 mozjpeg 这类成熟专家调优项目所做的设计选择。 JPEG 实验在 12 张 Kodak 图像上调优了 128 个量化表常量，并在另外 12 张上测试，结果用 scikit-image 在 libjpeg 中独立复核；VAD 实验则调优了 vad_core.c 中的每一个常量，在 LibriParty dev 集上训练、在 eval 集上报告结果。作者也说明了局限：在低于 1 bpp 时 JPEG 没有增益，且该方法最适合数十到数百个常量，而非大规模权重集合。

reddit · r/MachineLearning · /u/keep_up_sharma · 10月12日 20:51

**背景**: BD-rate 是一种标准压缩指标，表示在相同质量下平均节省的码率，因此 9.1% 意味着调优后的量化表在同等 SSIM 下少用 9.1% 的比特。量化表是 JPEG 编码器内部的固定整数表，决定每个频率系数被丢弃的激进程度，历来由专家手工调校。WebRTC VAD 是一种轻量、低延迟的语音活动检测器，用于实时通信中把音频帧判为语音或静音，其行为由硬编码的阈值和常量决定；LibriParty 则是一个带背景噪声和音乐的语音数据集，常被用来评测这类检测器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/wiseman/py-webrtcvad/5.3-webrtc-vad-algorithm">WebRTC VAD Algorithm | wiseman/py-webrtcvad | DeepWiki</a></li>
<li><a href="https://huggingface.co/speechbrain/vad-crdnn-libriparty">speechbrain/vad-crdnn- libriparty · Hugging Face</a></li>
<li><a href="https://arxiv.org/html/2601.10373">Towards Efficient Low- rate Image Compression with...</a></li>

</ul>
</details>

**标签**: `#optimization`, `#C`, `#tooling`, `#JPEG`, `#WebRTC-VAD`

---