---
layout: default
title: "Horizon Summary: 2026-10-30 (ZH)"
date: 2026-10-30
lang: zh
---

> 从 39 条内容中筛选出 6 条重要资讯。

---

1. [据报道币安被盗 56 亿美元，引发稳定币冻结与 SAFU 讨论](#item-1) ⭐️ 9.0/10
2. [开放问题 van der Waerden 数 w(2;3,21)=416 获 Lean 4 内核检验证明](#item-2) ⭐️ 9.0/10
3. [Mistral 开放 Mistral Large 4 权重，许可证限制引争议](#item-3) ⭐️ 8.0/10
4. [DoorDash 宣布收购 Instacart，餐饮与杂货配送巨头合流](#item-4) ⭐️ 8.0/10
5. [PHP2Shell 与 Linux XFRM 内核漏洞连锁利用，攻陷 25 台服务器（含美国政府系统）](#item-5) ⭐️ 8.0/10
6. [Anthropic 借助 Claude 用 Rust 重写 Messages API，CPU 用量降低 40%至 50%](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [据报道币安被盗 56 亿美元，引发稳定币冻结与 SAFU 讨论](https://arkm.com/explorer/entity/21a94755-f604-45e5-9501-6542e23005e8) ⭐️ 9.0/10

一起据称涉及币安的 56 亿美元黑客事件正在引发讨论，社区成员引用链上交易称，Tether 和 Circle 已冻结约 24 亿美元的 USDT 和 USDC。 若得到证实，这将是史上规模最大的加密安全事件之一，将考验市场对中心化交易所的信心，并凸显稳定币发行方能在以太坊和波场上迅速冻结资金的能力。 社区成员指出，币安的 SAFU 保险基金据称仅有约 10 亿美元的 BTC，远不足以覆盖损失；而被冻结的稳定币交易则展示了发行方的黑名单冻结能力。

hackernews · Tiberium · 10月29日 21:38 · [社区讨论](https://news.ycombinator.com/item?id=50296470)

**背景**: 币安的“用户安全资产基金”（SAFU）是由交易所自行出资设立的自保险储备，用于在特定情况下补偿用户损失，并非受监管的存款保险。Tether 和 Circle 等稳定币发行方可以将地址列入黑名单，并在支持的区块链上冻结 USDT 或 USDC，因此被盗资金能否追回部分取决于这些中心化控制点。中心化交易所仍是加密生态中的主要瓶颈，持有大量用户资产并充当法币出入金通道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stablecoininsider.org/can-stablecoins-be-frozen/">Can Stablecoins Be Frozen? Blacklisting Explained (2026)</a></li>
<li><a href="https://cryptodaily.co.uk/2026/07/crypto-exchange-insurance-funds-coverage">Crypto Exchange Insurance Funds: What They Actually Cover</a></li>
<li><a href="https://coinmarketcap.com/academy/article/centralization-risk-in-crypto">Centralization Risk in Crypto: How Decentralized Is Crypto?</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了震惊与怀疑：一些人认为该事件证明加密生态的中心化瓶颈背离了其最初承诺，另一些人则关注实际应对，指出 Circle 和 Tether 已冻结约 24 亿美元，并质疑 SAFU 约 10 亿美元的储备能否覆盖损失。

**标签**: `#cryptocurrency`, `#security`, `#Binance`, `#hacking`, `#stablecoins`

---

<a id="item-2"></a>
## [开放问题 van der Waerden 数 w(2;3,21)=416 获 Lean 4 内核检验证明](https://www.reddit.com/r/MachineLearning/comments/1xivpue/w2321_416_a_van_der_waerden_number_conjectured_by/) ⭐️ 9.0/10

van der Waerden 数 w(2;3,21) 由 Oliver Kullmann 于 2010 年猜测为 416，并且今年仍被列在 DeepMind 的 Formal Conjectures 开放问题清单中，如今这一数值已被证明：对 {1,…,416} 的任意红蓝染色必定包含红色 3 项等差数列或蓝色 21 项等差数列，而 {1,…,415} 存在某种染色两者皆无。该结果是经 Lean 4 内核检验的定理，并附有预印本论文与 13.6 GB 的可独立核验证据包。 这是一个长期悬而未决的具体组合数学数值，凭借可机器检验的证明而非单纯的计算机搜索结果得以确定，从而提高了 Ramsey 型组合数学中“已验证结果”的门槛。这也表明神经-符号 AI 系统能够驱动生成端到端通过 Lean 内核与经形式化验证的 LRAT 检查器的证明，是 AI 用于数学这一方向上的重要例证。 该 Lean 定理按 209 个案例、38,661,140 条叶公式组织，每条反驳都由 cake_pr（在 CakeML 中经形式化验证的 LRAT 检查器）核验，并通过摘要值与对应的 Lean 项绑定，因此只有被 Lean 内核或 cake_pr 接受的内容才会计入。证明由 Hupyy 的神经-符号系统 LPM（Large Proof Model）生成，证据包内附 Lean 源码、检查器记录和重放工具，可通过 'shasum -a 256 -c SHA256SUMS' 校验完整性。

reddit · r/MachineLearning · /u/Rodriguez909 · 10月29日 20:46

**背景**: van der Waerden 定理指出：对任意正整数 r 和 k，都存在一个 N，使得用 r 种颜色对 {1,…,N} 染色时必定出现某个颜色下的 k 项等差数列；van der Waerden 数 w(r;k1,k2,…) 就是在给定各颜色对应长度下最小的这样的 N。因此 w(2;3,21)=416 是关于二染色的精确命题，即避免红色 3 项等差数列与蓝色 21 项等差数列，这一情形正是 Kullmann 猜测的出处——Ahmed、Kullmann 与 Snevily 2011 年的论文《On the van der Waerden numbers w(2;3,t)》。DeepMind 的 Formal Conjectures 是用 Lean 形式化的开放数学命题集合，而 LRAT 是一种紧凑、可检验的不可满足性反驳证明格式，正是它让如此庞大的案例分析可以被独立核验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Van_der_Waerden_number">Van der Waerden number - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/1102.5433">[1102.5433] On the van der Waerden numbers w ( 2 ; 3 , t)</a></li>
<li><a href="https://cakeml.org/checkers.html">Verified Proof Checking - ML</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#Lean 4`, `#automated theorem proving`, `#combinatorics`, `#AI for mathematics`

---

<a id="item-3"></a>
## [Mistral 开放 Mistral Large 4 权重，许可证限制引争议](https://mistral.ai/news/mistral-large-4-oss/) ⭐️ 8.0/10

Mistral 已发布 Mistral Large 4（又称 Le Chonk）的可下载权重，这是一个总参数约 1.05T、激活参数 52B、带 1.6B 视觉编码器的多模态混合专家（MoE）模型，同时将 API 价格降至每百万输入/输出 token 0.70/2.10 美元。 此次发布为企业与开发者提供了一个可自托管、可微调的大型欧洲开放权重模型，加剧了与其他开放权重 LLM 系列的竞争，但许可证限制了商业模型服务业务。大幅降价也使 Mistral Large 4 在基于 API 的生产负载中更具竞争力。 权重体积约 1.06 TB，许可证为带“模型即服务”（MaaS）条款的修改版 MIT 许可证；经营模型服务业务的公司需与 Mistral 另行签订商业协议。模型可在 Hugging Face 上获取，但其体积意味着自托管需要可观的 GPU 显存和存储资源。

hackernews · kuberwastaken · 10月29日 14:13 · [社区讨论](https://news.ycombinator.com/item?id=50289418)

**背景**: 开放权重模型会公开训练后的参数，允许他人下载、运行并通常可微调，但这不等同于开源：许可证仍可能限制商业使用或再分发。Mistral Large 4 采用混合专家（MoE）架构，每个 token 只激活约 1 万亿总参数中的一部分，从而降低推理成本。Mistral 是一家法国 AI 公司，将其模型定位为面向企业的欧洲替代方案，而其“模型即服务”条款主要针对转售托管推理服务的供应商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.mistral.ai/models/mistral-large-4-0">Mistral Large 4 - Mistral AI | Mistral Docs</a></li>
<li><a href="https://www.orcarouter.ai/blog/mistral-large-4-open-weights-licence">Mistral Large 4 Open Weights: 1.06 TB, No Gate, One Catch</a></li>
<li><a href="https://mistral.ai/news/mistral-large-4-oss/">Mistral Large 4 (Le Chonk) is now open weight | Mistral</a></li>

</ul>
</details>

**社区讨论**: 评论者对面向欧盟部署的发布和近乎减半的 API 定价表示欢迎，有用户称新价格使其值得重新评估该模型与替代方案。另一些人批评“开放权重”标签具有误导性，因为 MaaS 条款要求另行签订商业许可证；还有人质疑安全基准只强调恶意请求拒绝率，却未报告对良性请求的过度拒绝情况。

**标签**: `#Mistral`, `#open weights`, `#model licensing`, `#LLMs`, `#AI pricing`

---

<a id="item-4"></a>
## [DoorDash 宣布收购 Instacart，餐饮与杂货配送巨头合流](https://about.doordash.com/en-us/news/doordash-to-acquire-instacart) ⭐️ 8.0/10

DoorDash 宣布将收购杂货配送公司 Instacart，这将成为两家 Y Combinator 校友企业之间规模最大的一次合并（DoorDash 出自 YC S13，Instacart 出自 YC S12）。DoorDash 将该交易定位为帮助本地商家提升竞争力的举措。 该交易将把零工经济消费配送领域两个最知名的品牌纳入同一家公司，从而重塑按需配送市场与 Walmart、Amazon 等规模更大的杂货巨头之间的竞争格局。由于它把领先的餐饮外卖平台与领先的独立杂货配送平台合为一体，也很可能招致监管机构的反垄断审查。 评论者指出，两家公司的产品重叠度出人意料地低：DoorDash 在杂货配送领域几乎空白，而 Instacart 的非杂货配送业务又是由 Uber Eats 履约的。这种有限的重叠很可能成为反垄断论证的核心，但也让人质疑合并后的公司究竟能实现多少真正的整合。

hackernews · WalterSobchak · 10月29日 12:33 · [社区讨论](https://news.ycombinator.com/item?id=50287919)

**背景**: DoorDash 最为人熟知的是餐饮外卖业务，而 Instacart 则开创了基于应用的杂货代购配送模式——由零工人员在门店替顾客采购商品。两家公司都出自知名创业孵化器 Y Combinator，且属于相邻批次（Instacart 为 S12，DoorDash 为 S13）。与餐饮外卖相比，杂货配送利润率更低、运营更复杂，目前由 Walmart 和 Amazon 主导，因此中小玩家之间的整合被视为与这些巨头竞争的一种方式。

**社区讨论**: Hacker News 的评论者对条件反射式的反垄断担忧提出了反驳，指出两家公司的产品实际上重叠极少，并认为这笔交易或许反而是合并后公司在杂货领域与 Walmart、Amazon 竞争的手段。也有人对 DoorDash "帮助本地商家取胜"的说辞持怀疑态度，称其是本地商户不得不忍受的"必要之恶"，并对它的抽成比例、配送员的行为以及暗黑设计模式提出批评。还有评论者强调了这是"Y Combinator 企业之间规模最大的合并"这一角度。

**标签**: `#mergers-acquisitions`, `#antitrust`, `#grocery-delivery`, `#gig-economy`, `#startups`

---

<a id="item-5"></a>
## [PHP2Shell 与 Linux XFRM 内核漏洞连锁利用，攻陷 25 台服务器（含美国政府系统）](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers) ⭐️ 8.0/10

Dream 的研究人员披露了一起入侵事件：攻击者先利用 PHP2Shell 攻击链，滥用 PHP 的 session.upload_progress 处理机制触发内存耗尽型释放后重用（use-after-free），从而实现远程代码执行，随后又串联了 Linux 内核 XFRM ESP-in-TCP 子系统中的本地提权漏洞以获取 root 权限。此次攻击共攻陷了分布在美国、日本、台湾和韩国的 25 台服务器，其中包括 3 台属于美国政府相关环境的系统，其请求流量与公开的概念验证（PoC）利用代码高度吻合。 这是一个典型的漏洞串联案例：一个面向 Web 的 PHP 缺陷被逐步放大为完整的 root 权限沦陷，而受害者中包含政府相关系统，更凸显出公开 PoC 被武器化的速度之快。此事也再次引发争论：为何 XFRM ESP-in-TCP、MPTCP 这类功能会在根本用不到它们的系统上默认开启，从而为每台服务器扩大了内核攻击面。 面向 Web 的阶段使用了四步 HTTP 请求链：前几步请求耗尽 PHP 内存并泄露内存内容，最后一步执行 shell 命令；内核阶段则被编号为 CVE-2026-46300（代号“Fragnesia”），是一个 CVSS 评分 7.8 的“任意地址写”（write-what-where）漏洞，一旦启用 ESP-in-TCP 处理，就会通过操纵 AES-GCM 密钥流破坏底层页缓存。有评论者指出，内存耗尽那一步大约 383MB、手法相对粗糙，而且公开的 PoC 仓库（StealMyBitcoin-PoC）已经展示了借助大语言模型对该利用进行迭代改进的过程。

hackernews · 882542F3884314B · 10月29日 10:42 · [社区讨论](https://news.ycombinator.com/item?id=50286987)

**背景**: PHP2Shell 指的是直接利用 PHP 自身的缺陷（此处是会话上传进度跟踪机制）在 Web 服务器上实现代码执行，而 Web 服务通常以低权限用户身份运行。从这个低权限用户提升到 root 还需要一个独立的本地提权漏洞，本例中它来自 XFRM——Linux 内核的 IPsec 变换框架；ESP-in-TCP（RFC 8229）允许 IPsec 的 ESP 数据包封装在 TCP 中传输，以便穿越那些会阻断基于 UDP 的 IKE 协商的中间盒，而 Fragnesia 漏洞正位于这条代码路径上。将初始入侵漏洞与本地提权漏洞串联是攻击者的常规做法，因为这能把一次受限的 Web 沦陷升级为对主机的完全控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/php2shell-gained-root-access-on-25-servers/">Hackers Chain PHP 2 Shell and Linux Kernel Exploits to Gain Root...</a></li>
<li><a href="https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp">Fragnesia: Linux Kernel Local Privilege Escalation via ESP - in - TCP</a></li>
<li><a href="https://www.securityweek.com/php2shell-exploitation-moves-from-probes-to-working-shells/">PHP 2 Shell Exploitation Moves From Probes to... - SecurityWeek</a></li>

</ul>
</details>

**社区讨论**: 评论者的焦点集中在不必要默认开启的攻击面上，有人表示自己早已在系统中禁用 MPTCP，并质疑这类功能为何默认启用、XFRM 是否也能关闭。另一位自称业余爱好者的用户讲述了自己用 DeepSeek 编写并尝试精简 PHP2Shell 利用代码的经历，并对原始攻击手法不够精细感到意外；还有读者根据报告中逐字出现的 PAN-OS 配置项以及吻合的 SELinux 配置，推断涉事防火墙厂商是 Palo Alto Networks。也有人提到 Dream 由奥地利前总理塞巴斯蒂安·库尔茨领导。

**标签**: `#security`, `#exploits`, `#linux-kernel`, `#vulnerability-research`, `#incident-response`

---

<a id="item-6"></a>
## [Anthropic 借助 Claude 用 Rust 重写 Messages API，CPU 用量降低 40%至 50%](https://latent.space/p/opus55/) ⭐️ 8.0/10

Anthropic 将原本部署在单一 GCP 区域的 Python 单体 Messages API 整体迁移到 Rust，由工程师负责系统设计与验证、Claude 负责代码实现。迁移后 CPU 用量下降约 40% 至 50%，首个 token 的响应时间缩短约 10% 至 20%。 这是一个来自生产环境的具体案例，说明在几乎没有 Rust 经验的团队里，AI 辅助重写也能让语言迁移变得经济可行。由于当时的瓶颈是 CPU 而不是 GPU，这部分节省会直接转化为行业中最繁忙的 LLM API 之一的服务成本下降与容量提升。 值得注意的是，项目启动时团队里 reportedly 没有 Rust 开发者，因此他们依靠对比新旧系统输出的差分测试来验证正确性。约 10% 至 20% 的首 token 延迟改善来自 API 侧请求处理变快，而非模型推理本身变快。

telegram · zaihuapd · 10月29日 03:13

**背景**: Messages API 是开发者调用 Claude 模型的主要接口，因此它处在所有基于 Anthropic 模型构建的应用的请求路径上。Python 便于快速搭建服务，但在高并发下相对较慢且内存开销大，这正是基础设施团队有时会用 Rust 重写热点路径的原因。首 token 延迟（TTFT）衡量的是从请求到达至第一个输出 token 出现之间的时间，涵盖排队、路由和 prompt 处理，在流式对话应用中它主导着用户的响应体感。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.generalcompute.com/blog/what-is-time-to-first-token-ttft">What Is Time to First Token ( TTFT )? The LLM Latency Metric That...</a></li>
<li><a href="https://www.rustpython.com/guides/python-to-rust-performance">Python → Rust Performance: A Practical Decision Guide</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Rust`, `#Claude`, `#AI-assisted coding`, `#API infrastructure`

---