---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 从 33 条内容中筛选出 3 条重要资讯。

---

1. [黑客攻破 Flock 安全摄像头，暴露硬编码凭证](#item-1) ⭐️ 8.0/10
2. [TMLR 约谈 10 篇被拒稿论文的作者，多数人无法解释自己的论文](#item-2) ⭐️ 8.0/10
3. [Cloudflare 推出设置：可屏蔽 AI 训练爬虫并保留搜索收录](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [黑客攻破 Flock 安全摄像头，暴露硬编码凭证](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

安全研究员 Micah Lee 与 404 Media 合作、由 Wired 刊发的报道披露，黑客利用硬编码凭证、以明文存储的密钥以及失效的安全启动机制，成功入侵了 Flock Safety 的车牌识别（ALPR）监控摄像头。此后 Distributed Denial of Secrets 公开了从这些摄像头中提取的分区镜像，而 Flock 的漏洞披露政策（VDP）也被指出明确排除了研究人员与设备交互或下载设备数据的场景。 Flock Safety 的车牌识别摄像头被美国各地警局和社区组织大规模部署，而此次发现这些设备可被物理入侵，直接动摇了这些机构对所采集数据的信任基础。由于 FBI 的 NCIC 热名单等联邦系统会与 Flock 采集的车牌进行比对，摄像头层面的失陷对任何被扫描车辆的车主都构成直接的隐私与公民自由风险。 泄露的并非管理员密码，而是一个 API key，但它可用于请求以明文方式存储、且看起来能够通过 Flock 服务器认证的凭证；攻击者以摄像头身份认证成功后究竟能做什么，目前仍不清楚。评论者还指出，Flock 的 VDP 仅在研究人员不与设备交互、也不下载设备数据的前提下才欢迎漏洞披露，批评者认为这套政策是为了营造负责任的安势头形象，而非真正收集漏洞信息。

hackernews · driverdan · 9月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**背景**: Flock Safety 生产自动车牌识别（ALPR）摄像头，拍摄过往车辆并允许执法机构检索车牌数据，其系统常与 FBI 的国家犯罪信息中心（NCIC）等热名单对接。硬编码凭证是众所周知的漏洞类型，被收录为 CWE-798，OWASP 也将其描述为“使用硬编码密码”，攻击者可提取并复用固件或源码中写死的密钥。漏洞披露政策（VDP）是厂商请安全研究人员上报缺陷的渠道，因此 VDP 排除哪些情形至关重要。这类摄像头通常安装在公共空间，其威胁模型必须考虑任何走近设备的人都能实施物理接触这一事实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/06/are-your-local-police-using-flock-safety-alprs-scan-immigrants">Are Your Local Police Using Flock Safety ALPRs to Scan for...</a></li>
<li><a href="https://owasp.org/www-community/vulnerabilities/Use_of_hard-coded_password">Use of hard-coded password - OWASP Foundation Hardcoded Credentials CWE-798: Fix Guide - Offensive360 CVE-2026-4832: SNMP Hard-coded Credentials Vulnerability Hardcoded Credentials Vulnerability: Why Immediate Action Matters DSA-2026-079: Security Update for RecoverPoint for Virtual ... CVE-2025-1393: Hard-Coded Credentials Auth Bypass Flaw</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论整体对 Flock 持批评态度，评论者称硬编码凭证是“完全无能”的表现，并将这些缺陷归因于“打着缩短上市时间旗号的纯粹偷懒”，而非真正的工程难题。多位评论者指出，Flock 的 VDP 似乎是为了劝退真实的漏洞上报；也有人提到，由于设备安装在无人看管的公共空间，使用现成的硬件与软件栈几乎必然让拥有本地物理接触能力的攻击者得手。

**标签**: `#security`, `#surveillance`, `#iot`, `#vulnerability-disclosure`, `#privacy`

---

<a id="item-2"></a>
## [TMLR 约谈 10 篇被拒稿论文的作者，多数人无法解释自己的论文](https://www.reddit.com/r/MachineLearning/comments/1wid67h/tmlr_reached_out_to_the_authors_of_10_papers/) ⭐️ 8.0/10

TMLR 的联合主编（Co-EiC）亲自联系了十篇已被列入“编辑直接拒稿”（desk rejection）名单的投稿作者，结果发布在 Medium 上并被 r/MachineLearning 转发总结，情况相当刺眼：有一篇的作者主动撤稿，一篇称因其他事务无法参加，一篇约好会议却未出席，三篇的作者无法回答关于论文的基础问题，三篇的作者只能谈高层思路、一涉及技术细节就卡壳，只有一篇完整回答了所有问题——而即便是这一篇，主编也发现了一个重大缺陷。 这一事件虽然只是个案，却提供了具体证据，说明相当一部分投稿可能出自那些根本无法为自己论文辩护的人——或者由大模型流水线代劳——这直接动摇了同行评审的前提假设：投稿人就是论文作者。若此类情况普遍存在，审稿人与编辑将承担越来越重的造假甄别负担，AI/ML 领域学术出版的可信度也将受到威胁。 该联合主编明确表示这并非系统性研究，只是小样本的个案调查，因此这十篇的统计结果不应被视为精确的造假比例；值得注意的是，即便是唯一一位能应对全部提问的作者，其论文也被发现存在重大缺陷，这说明“能讲清楚”并不等于“研究本身可靠”。

reddit · r/MachineLearning · /u/hihey54 · 9月16日 23:20

**背景**: TMLR（Transactions on Machine Learning Research）是一本机器学习领域的研究期刊，其 Co-EiC 即“联合主编”，属于对稿件作出最终决定的高级编辑。所谓 desk rejection（编辑直接拒稿），是指期刊在送外审之前就退稿，通常是因为编辑认为论文超出期刊范围、形式不符合要求，或者根本不是一篇真正的研究论文。正因如此，被标记为直接拒稿的论文是一组很特殊的访谈对象——按惯例，这类稿件根本不会经历详细的评审过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scientific-publishing.webshop.elsevier.com/publication-process/paper-rejection-common-reasons/">Paper Rejection: Common Reasons | Elsevier Language Services</a></li>
<li><a href="https://authorservices.taylorandfrancis.com/blog/get-published/5-reasons-for-desk-rejection-and-how-to-avoid-them/">5 top reasons for desk rejection – and how to avoid them - Author Services</a></li>
<li><a href="https://www.editage.com/insights/what-is-the-meaning-of-awaiting-eic-decision-in-manuscript-central">Meaning of 'Awaiting EiC Decision' | Editage Insights</a></li>

</ul>
</details>

**标签**: `#peer-review`, `#ML-research-ethics`, `#TMLR`, `#academic-publishing`, `#LLM-generated-content`

---

<a id="item-3"></a>
## [Cloudflare 推出设置：可屏蔽 AI 训练爬虫并保留搜索收录](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/) ⭐️ 8.0/10

9 月 15 日，Cloudflare 宣布推出新的“禁止 AI 训练”（Disallow AI Training）设置，允许网站继续被搜索引擎收录，同时拦截不符合其内容用于 AI 训练要求的爬虫。苹果、谷歌和微软已经符合或承诺符合相关要求。 Cloudflare 位于大量网站的前端，因此一个开关就能让内容方在不损失搜索流量的前提下，实际地把“搜索收录”和“AI 训练”区分开来。这标志着从 robots.txt 这类纯自愿信号，转向由基础设施层强制执行的内容治理，也迫使主要 AI 与搜索公司公开承诺遵守这些规则。 该设置按域名配置，若选择“阻止”，所有受 AI 训练策略约束的爬虫都会被拦截——包括既做搜索收录、又为 AI 训练提供数据的混合爬虫——因此搜索收录也可能受到影响。Cloudflare 还表示计划于明年初让网站控制其内容可被 AI 摘要引用的比例；另据相关报道，Bing 目前尚不支持该 robots.txt 退出信号。

telegram · zaihuapd · 9月16日 05:46

**背景**: 网站传统上通过 robots.txt 文件告知爬虫可以访问哪些内容，但这种约定依赖爬虫方自愿遵守，而且它无法区分“搜索引擎为收录而抓取”与“AI 公司为训练数据而抓取”这两种用途。Cloudflare 是为互联网相当大一部分流量提供服务的反向代理和 CDN，因此可以代表客户在网络边缘强制执行此类规则。所谓“混合爬虫”指 Googlebot、Applebot、Bingbot 这类既做搜索收录、其运营方又可能将抓取内容用于 AI 目的的机器人，这正是两种用途难以被分开处理的技术与商业原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/1/003/108.htm">Cloudflare 推出新设置：可允许搜索引擎爬取，同时拒绝 AI 训练 - IT之家</a></li>
<li><a href="https://developers.cloudflare.com/ai-crawl-control/">Overview · Cloudflare AI Crawl Control docs</a></li>
<li><a href="https://www.bingdada.com/blog/cloudflare-disallow-ai-training-search-crawlers">Cloudflare 新设置：拒绝 AI 训练不伤搜索收录 | Bingdada 技术博客</a></li>

</ul>
</details>

**标签**: `#AI Crawlers`, `#Cloudflare`, `#AI Training Data`, `#Web Scraping`, `#Content Rights`

---