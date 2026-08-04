---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
---

> 从 41 条内容中筛选出 14 条重要资讯。

---

1. [活跃 Shai-Hulud 供应链攻击攻陷 Keyv 等 npm 包](#item-1) ⭐️ 9.0/10
2. [我国首部 L3/L4 自动驾驶强制性国标发布，2027 年 7 月实施](#item-2) ⭐️ 9.0/10
3. [Mistral 发布 Shieldstral：3B 开源权重多模态审核模型](#item-3) ⭐️ 8.0/10
4. [生成多样化肤色的新色彩空间与算法](#item-4) ⭐️ 8.0/10
5. [真实的联邦快递与谷歌邮件酷似钓鱼邮件，削弱用户信任](#item-5) ⭐️ 8.0/10
6. [DeepSeek V4 Flash 在单个 AMD MI300X 上高效运行](#item-6) ⭐️ 8.0/10
7. [Xbox 宕机导致光盘游戏无法游玩，引发 DRM 与数字所有权热议](#item-7) ⭐️ 8.0/10
8. [AI 智能体迭代优化自身的 Harness 工程](#item-8) ⭐️ 8.0/10
9. [MiniMax-H3 全模态模型已移植到 Apple Silicon 上的 MLX](#item-9) ⭐️ 8.0/10
10. [华为首席科学家警告英伟达芯片扩展将触及物理极限](#item-10) ⭐️ 8.0/10
11. [Cloudflare 用 58 美元/月 AI 取代第三方安全工具，称他人勿效仿](#item-11) ⭐️ 8.0/10
12. [谷歌为 Anthropic 搭建 2000 亿美元华尔街融资机器](#item-12) ⭐️ 8.0/10
13. [特朗普政府拟起草禁令 禁止进口中国数据中心光模块](#item-13) ⭐️ 8.0/10
14. [白宫开源 AI 监管急转弯，硅谷分歧加剧](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [活跃 Shai-Hulud 供应链攻击攻陷 Keyv 等 npm 包](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 9.0/10

新一轮 Shai-Hulud 供应链攻击正在活跃地破坏 npm 生态，最初涉及 Keyv 和 cacheable 包。该攻击已影响 400 多个包，窃取凭据并自我传播到可写的 npm 包。 这很重要，因为 Keyv 是一个被超过 1700 个项目依赖的广泛使用的键值存储库，此次攻击对许多下游应用构成严重风险。同时它也暴露了 npm 依赖系统的持续脆弱性，并重新引发了关于安装钩子安全性的争论。 Shai-Hulud 蠕虫会窃取开发者凭据，将自己发布到可写的 npm 包，并在 GitHub 仓库中植入执行钩子。Keyv 的最新版本 6.0.0 在一小时前刚刚发布，表明攻击仍在持续。

hackernews · cimi_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**背景**: npm 包可以通过 pre-install 和 post-install 钩子在安装时执行任意脚本，这一功能已成为供应链攻击的主要载体。Shai-Hulud 是一个自我传播的蠕虫家族，已多次针对 npm 生态系统，此前曾攻陷数百个包并窃取开发者凭据。Keyv 是一个支持多种后端的简单键值存储库，因其广泛使用而成为有吸引力的攻击目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.npmjs.com/package/keyv">keyv - npm</a></li>
<li><a href="https://research.jfrog.com/post/shai-hulud-is-back-august/">Major Shai Hulud campaign strikes npm again, affecting keyv and 400+ packages - JFrog Security Research</a></li>
<li><a href="https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack">Shai - Hulud npm Supply Chain Attack | Wiz Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了紧迫感和不满，有人提议暂停新增 pre-install/post-install 钩子，还有人呼吁彻底取消这些钩子。其他人则建议在 .npmrc 中设置 'min-release-age=5' 作为缓解措施，并请求能够扫描 node_modules 以检测受感染的检查工具，还有人分享了关于 npm 供应链攻击技术的最新文档。

**标签**: `#security`, `#supply-chain`, `#npm`, `#open-source`, `#dependency-management`

---

<a id="item-2"></a>
## [我国首部 L3/L4 自动驾驶强制性国标发布，2027 年 7 月实施](https://wap.miit.gov.cn/jgsj/zbys/qcgy/art/2026/art_a1d2072374884287b67048a77560014e.html) ⭐️ 9.0/10

2026 年 7 月 30 日，工业和信息化部组织制定并归口的强制性国家标准《智能网联汽车 自动驾驶系统安全要求》（GB 44721—2026）正式发布，拟于 2027 年 7 月 1 日起实施。这是我国首部针对 L3 级有条件自动驾驶和 L4 级高度自动驾驶系统的强制性国标。 作为强制性标准，它把 L3/L4 系统的安全要求从推荐性建议转变为具有法律约束力的合规义务，直接影响车企和供应商的产品开发、测试与市场准入。该标准明确了安全基线和人机责任边界，有助于推动高级别自动驾驶在中国的商业化落地。 该标准适用于搭载 L3、L4 级系统的 M 类（载客）和 N 类（载货）车辆，但不适用于自动泊车系统。它是对 2024 年推荐性国标的系统性升级，从推荐性转为强制性，并从企业全生命周期安全保障、系统动态驾驶能力、人机交互与用户告知、多维度检验检测四个维度构建安全要求体系，要求自动驾驶系统安全水平至少达到合格且专注驾驶人的水平。

telegram · zaihuapd · 8月4日 13:06

**背景**: L3 和 L4 是国际自动机工程师学会（SAE）自动驾驶分级中的两个等级：L3 为有条件自动驾驶，车辆在特定条件下可自行行驶，但驾驶人必须随时准备接管；L4 为高度自动驾驶，在限定场景内无需驾驶人干预即可完成全部驾驶任务。在中国车辆分类中，M 类指载客车辆，N 类指载货车辆。此前我国 L3/L4 安全要求仅为推荐性标准，此次转为强制性，标志着高级别自动驾驶监管进入有明确合规要求的阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.autohome.com.cn/news/202608/1316205.html">autohome.com.cn/news/202608/1316205.html</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/21796837458">自动驾驶级别L1、L2、L3、L4、L5的定义区别 - 知乎</a></li>
<li><a href="https://www.shangyici.com/vehicle_778784">数乘 车 辆 _机动 车 的 准 乘人数_商易赐汽 车</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#L3/L4`, `#regulation`, `#safety standards`, `#China`

---

<a id="item-3"></a>
## [Mistral 发布 Shieldstral：3B 开源权重多模态审核模型](https://mistral.ai/news/shieldstral/) ⭐️ 8.0/10

Mistral 发布了 Shieldstral，一个 3B 参数的开源权重（open-weights）多模态审核模型，以 Apache 2.0 协议在 Hugging Face 上提供。它支持对提示词与回复进行审核、提示-回复对分类、拒答检测，以及文本和图像的安全过滤，据称性能超过比自己大 7 倍的模型。 Shieldstral 为开发者提供了一种实用且成本较低的本地替代方案，可用于用户生成内容平台的审核，而不必依赖专有的审核 API。它也体现了 Mistral 转向更小、更专用的微调模型，而不是直接与前沿大模型竞争。 该模型通过用“是/否”回答自然语言政策问题来工作，从而实现灵活的安全过滤。它仅 3B 参数，据称能超过 20B 参数的安全模型；Apache 2.0 许可证允许广泛的商业使用和微调。

hackernews · riadsila · 8月4日 16:36 · [社区讨论](https://news.ycombinator.com/item?id=49171268)

**背景**: 开源权重（open-weights）模型会发布最终训练好的参数，任何人都能下载并在本地运行，但不像完全开源那样一定包含训练代码或数据集。多模态内容审核会结合文本、图像、音频和视频等线索，来发现单一模态系统可能漏掉的违规内容，例如梗图或视频。Shieldstral 是该领域中的一个轻量级模型，专为本地部署而非托管的审核 API 设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/shieldstral/">Introducing Shieldstral. | Mistral AI</a></li>
<li><a href="https://docs.mistral.ai/models/model-cards/shieldstral-1-0">Shieldstral 1.0 - docs.mistral.ai</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: 有评论者问 Shieldstral 能否针对任意审核规则进行调节，还是只能复现大型科技平台那种“只要措辞温和就允许恶意内容”的审核风格，并将其与 OpenAI 的 omni-moderation API 比较。一些人认为它是人工复核前现实且经济的初筛方案，另一些人则赞赏 Mistral 打造更小、更专用微调模型的策略。

**标签**: `#AI`, `#content moderation`, `#Mistral`, `#open-weights`, `#model release`

---

<a id="item-4"></a>
## [生成多样化肤色的新色彩空间与算法](https://toneyalexander.github.io/inclusive-color-space/) ⭐️ 8.0/10

作者发布了一个交互式页面，介绍了一种专门构建的色彩空间和程序化生成算法，可让数字艺术和游戏中轻松生成逼真且多样化的肤色。 这为数字艺术家和游戏开发者提供了一个简单实用的工具，避免使用刻板或有限的肤色配色。同时也引发了关于色彩科学和数字媒体中包容性表现的讨论。 该色彩空间通过少量线性代数和曲线拟合运算定义，页面包含交互式取色器、程序化生成以及多个 JavaScript 演示。作者承认方法上有些临时拼凑，并列出未来改进方向。

hackernews · automatoney · 8月4日 15:16 · [社区讨论](https://news.ycombinator.com/item?id=49170165)

**背景**: 色彩空间是一种将颜色表示为数字的有组织系统，通常具有三维或四维，并定义可显示颜色的色域。程序化生成是算法自动创建内容而不是手动创建，常用于生成游戏中的纹理和模型。人类肤色在色彩空间中只占据相对狭窄的区域，而由于照明和感知的影响，准确建模肤色是一个挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Color_space">Color space - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Color_space">Color space - Glossary - MDN Web Docs - Mozilla</a></li>
<li><a href="https://en.wikipedia.org/wiki/Procedural_generation">Procedural generation - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这项作品美丽且巧妙，指出拟合的椭圆很好地捕捉了真实粉底色号在 Oklab 色彩空间中的聚集情况。有人提到 Pantone SkinTones 等现有参考，并分享皮肤在高饱和度下偏橙色的观察；也有人质疑部分生成的肤色看起来偏绿或偏紫。

**标签**: `#color space`, `#skin tones`, `#procedural generation`, `#digital art`, `#algorithm`

---

<a id="item-5"></a>
## [真实的联邦快递与谷歌邮件酷似钓鱼邮件，削弱用户信任](https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/) ⭐️ 8.0/10

Troy Hunt 在其 2024 年的文章《Thanks FedEx, This Is Why We Keep Getting Phished》中指出，联邦快递（FedEx）和谷歌（Google）发出的合法邮件与钓鱼攻击极为相似，这说明用户为何仍然容易受骗。他认为，当真实公司发送看起来像诈骗的邮件时，反而会训练用户点击危险的链接。 这动摇了“留意钓鱼特征”的常见建议：如果正规品牌的邮件也具有同样的警示信号，用户就无法可靠地区分安全邮件和恶意邮件。同时，它也说明需要更强的邮件认证标准，以及企业应采用更清晰一致的发送方式。 社区评论中的例子包括：一封由个人发送并附带 PDF 的联邦快递海关通知，以及一封使用短域名 c.gle 的 Google 存储空间提醒，该域名最初无法通过 WHOIS 查询验证。其他例子还提到 IRS 电话树使用与诈骗者相同的商用文本转语音系统，以及澳大利亚 ACMA 屏蔽了 3.36 亿条诈骗短信。

hackernews · stymaar · 8月4日 21:09 · [社区讨论](https://news.ycombinator.com/item?id=49175192)

**背景**: 钓鱼攻击会利用视觉上相似域名和同形异义词（homograph）手法，采用与可信品牌名称外观相似的字符。SPF、DKIM 和 DMARC 等邮件认证协议有助于防止域名伪造，但正规公司仍会发送带有通用问候语、未经请求的附件和短链接的邮件——这些正是识别钓鱼邮件时的警示特征。这使用户缺乏可靠线索来区分真实企业邮件和诈骗邮件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/">What are DMARC, DKIM, and SPF? - Cloudflare SPF, DKIM, and DMARC Explained: Email Authentication Guide How email authentication works in Microsoft 365 - Microsoft ... Email Authentication Explained: SPF, DKIM, and DMARC SPF, DKIM, and DMARC Explained: The Complete Email ...</a></li>
<li><a href="https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams">How To Recognize and Avoid Phishing Scams | Consumer Advice</a></li>
<li><a href="https://www.hexnode.com/blogs/explained/what-is-homograph-attack/">What is Homograph attack ? - Hexnode Blogs</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了与文章论点一致的个人经历：有人收到过由“某个人”发送的真实 FedEx 海关通知并附带 PDF，有人发现 Google 的 c.gle 链接难以验证，还有人指出 gTLD 数量激增使钓鱼邮件更难识别。总体情绪是，即使是技术熟练的用户也很难分辨，这再次说明企业和协议都需要改进。

**标签**: `#phishing`, `#security`, `#email`, `#domain names`, `#user education`

---

<a id="item-6"></a>
## [DeepSeek V4 Flash 在单个 AMD MI300X 上高效运行](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

一个来自 ryanzhou 的 GitHub 项目展示了 DeepSeek V4 Flash 在单个 AMD MI300X 上通过量化权重高效运行。该方案每秒可处理超过 150 个 token，但上下文窗口从原始的 1M 缩减到 256K。 这一演示表明，大型混合专家（MoE）模型可以在单个加速器上运行，显著降低了部署前沿大模型的硬件门槛。同时，它也证明了 AMD MI300X 是 NVIDIA 硬件在 LLM 推理方面的可行替代方案，有望拓宽整个生态系统。 量化是实现这一成果的核心，使总参数量 284B（激活 13B）的模型能够装入 MI300X 的 192GB HBM3 显存中。代价是上下文长度缩减到 256K，但仍大于许多生产级模型。此外，MI300X 是 OAM 模块，通常作为约 25 万欧元的 8 卡整机销售，而非单个购买。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是 DeepSeek V4 系列的预览版模型，属于混合专家（MoE）架构，总参数量 284B、激活参数量 13B，原生支持 100 万 token 的上下文。AMD MI300X 是 Instinct 系列加速器，配备 192GB HBM3 显存，常用于数据中心的 AI 推理。量化可将高精度权重转换为低精度表示，从而减少内存占用和计算开销，但有时会带来精度损失。MoE 架构每个 token 只激活部分参数，使大模型推理更加高效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V4 Flash 0423 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了硬件可获取性问题：MI300X 是 OAM 模块，通常只随 8 卡整机出售，而基于 PCIe 的 MI350P 更容易获得，但显存只有 144GB。也有人提到此前已有 DwarfStar 等方法能以更少内存运行相同模型。整体态度积极，认为将上下文缩减到 256K 是一个实用且可接受的权衡。

**标签**: `#DeepSeek`, `#AMD MI300X`, `#LLM inference`, `#quantization`, `#hardware`

---

<a id="item-7"></a>
## [Xbox 宕机导致光盘游戏无法游玩，引发 DRM 与数字所有权热议](https://birchtree.me/blog/xbox-goes-down-you-cant-play-games-you-own-on-disc/) ⭐️ 8.0/10

一次大范围的 Xbox 网络宕机导致用户无法游玩即使是光盘版的游戏，因为 Xbox 需要通过 Xbox Live 在线验证游戏许可。该事件将一次例行服务中断变成了“实体媒体仍依赖云服务”的生动演示。 这件事很重要，因为它暴露了在线 DRM 之下“拥有”实体游戏的脆弱性，影响了消费者信任和游戏保存。它加剧了业界关于离线可用性、数字所有权和消费者权益的持续争论。 Xbox 的 DRM 系统要求主机通过联系 Xbox 服务器来验证特定光盘游戏，因此即使插入光盘，网络宕机也可能导致无法运行。微软此前曾改进离线体验，例如 2022 年的更新让向下兼容游戏可以离线运行，但对在线验证的依赖依然存在。

hackernews · surprisetalk · 8月4日 12:01 · [社区讨论](https://news.ycombinator.com/item?id=49167448)

**背景**: 数字版权管理（DRM）是限制数字内容访问和复制方式的技术。与许多现代主机类似，Xbox Series X/S 采用常时在线 DRM 模式，游戏许可通过 Xbox 网络管理，这意味着在初始设置和运行某些光盘游戏时通常需要联网。这种设计有助于反盗版，但也造成了云服务依赖，引发了对服务停止后游戏保存问题的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Always-on_DRM">Always-on DRM - Wikipedia</a></li>
<li><a href="https://techraptor.net/gaming/features/microsofts-xbox-drm-and-what-it-might-mean-for-preservation">Understanding The Online Xbox DRM That Disrupted Gaming</a></li>
<li><a href="https://www.windowscentral.com/xbox-drm-explained">Xbox DRM explained: Setting a home console... | Windows Central</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对游戏所有权的现状表示惋惜，认为现代主机不如 GameCube 等可以离线运行的老主机。有用户认为真正的问题在于“所有权”本身，并列出了永久持有、离线使用、转售、传给子女等权利。还有人指出，较早世代的主机通过自建匹配服务器处理在线功能，从而避免了这种锁定问题。

**标签**: `#DRM`, `#gaming`, `#digital ownership`, `#cloud dependency`, `#consumer rights`

---

<a id="item-8"></a>
## [AI 智能体迭代优化自身的 Harness 工程](https://lilianweng.github.io/posts/2026-07-04-harness/) ⭐️ 8.0/10

Lilian Weng 的博客文章《Harness engineering for self-improvement》提出了一种方法：AI 智能体通过反馈循环迭代优化自身的工程 harness——包括工具、提示词和上下文管理。这将优化重点从模型权重转向智能体外围基础设施。 这一点很重要，因为它指向了一种无需重新训练模型即可提升 AI 智能体性能的新范式，转而聚焦于引导智能体的 harness。如果成功，它可能使智能体在大型代码库和复杂现实任务中变得更高效、更经济、更可靠，使开发者和企业同时受益。 该概念建立在“harness engineering”之上，这一术语由 OpenAI 的 Codex 团队推广，强调让缺失的能力对智能体清晰可见且可强制执行。社区讨论强调了实际需求：为代码库建立通用可靠的适应度函数、让智能体编写自己的工具（例如将上下文加载从 15 次调用的 2 万 token 减少到一次调用的 800 token），以及使用带训练/测试集划分的评估来避免奖励作弊。

hackernews · tosh · 8月4日 06:17 · [社区讨论](https://news.ycombinator.com/item?id=49164896)

**背景**: Harness 工程是构建 AI 模型外部脚手架（提示词、工具、上下文和反馈循环）以控制和引导其行为的学科。自我改进的 AI 智能体通过诊断反馈不断迭代和提升，通常使用 LLM-as-a-judge 或自动化评估。这种方法与传统模型微调形成对比，更强调提示词和工具优化。Lilian Weng 是知名的 AI 研究者和博客作者，其深度技术文章被广泛关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/harness-engineering/">Harness engineering: leveraging Codex in an agent-first world | OpenAI</a></li>
<li><a href="https://martinfowler.com/articles/harness-engineering.html">Harness engineering for coding agent users</a></li>
<li><a href="https://datagrid.com/blog/7-tips-build-self-improving-ai-agents-feedback-loops">How to Build Self-Improving AI Agents through Feedback Loops | Datagrid Blog | Datagrid</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了实践经验和建议：有人强调为大型代码库构建通用适应度函数，有人报告了自动研究 harness 的成功体验（读取生产轨迹、让智能体自写工具），还有人以“Torment Nexus”调侃，并推测未来 harness 会生成自己的 RLHF/DPO 训练集用于 LoRA 微调。整体氛围务实且乐观，聚焦于实现策略和未来方向。

**标签**: `#AI agents`, `#self-improvement`, `#LLM engineering`, `#harness optimization`, `#agent tools`

---

<a id="item-9"></a>
## [MiniMax-H3 全模态模型已移植到 Apple Silicon 上的 MLX](https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything) ⭐️ 8.0/10

MiniMax 发布了 MiniMax-H3，一个通用的全模态生成系统，可接受文本、图像、音频和视频输入，并生成最长 15 秒、含音频的视频。新的 Python 包 PipeNetwork/minimax-h3-mlx 将该模型移植到 MLX，可在 Apple Silicon 上运行；Simon Willison 在 M5 Max MacBook Pro 上演示了运行过程，下载约 115 GB 模型文件，视频生成耗时不到 45 分钟。 这一进展意义重大，因为开放权重的全模态模型现在可以在 Apple Silicon 上本地运行，降低了视频生成研究和实验的门槛。同时，它也体现了通过 MLX 将前沿多模态模型移植到消费级硬件的日益增长的生态系统趋势。 该包需要下载 MiniMaxAI/MiniMax-H3 的 FL2VA 权重和 pipenetwork/MiniMax-H3-MLX-8bit，再运行 scripts/generate.py 并输入文本提示。输出质量高度依赖提示词指导；没有针对音频的提示时，生成的音频可能变成奇怪的类语音噪声。底层 MiniMax-H3 模型支持最高 2K 分辨率、15 秒时长的视频，并带有原生立体声音频。

rss · Simon Willison · 8月4日 19:10

**背景**: MLX 是苹果推出的用于 Apple silicon 上机器学习的数组框架，其 Python API 与 NumPy 非常相似。MiniMax-H3 是一个开放权重的全模态生成模型，可以在统一架构中联合理解并生成文本、图像、视频和音频。这个 MLX 移植让这样的大型多模态模型能够在消费级 Mac 上运行，但仍需要大量的存储空间和计算资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://github.com/ml-explore/mlx">GitHub - ml-explore/ mlx : MLX : An array framework for Apple silicon</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/omni-model/">What’s an Omni-Model? Definition, Uses, and Benefits | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#AI`, `#MLX`, `#MiniMax-H3`, `#omni-modal`, `#video generation`

---

<a id="item-10"></a>
## [华为首席科学家警告英伟达芯片扩展将触及物理极限](https://www.bloomberg.com/news/articles/2026-08-04/huawei-s-top-scientist-warns-of-chip-limit-nvidia-will-soon-face) ⭐️ 8.0/10

在 7 月底一场罕见的四小时公开采访中，华为首席半导体科学家廖恒警告，英伟达通过持续增加计算芯片和高带宽内存来扩展规模的做法将很快触及物理极限，一旦越过该极限将出现“雪崩”。他还表示，首款采用华为 LogicFolding 技术框架的手机芯片将于今年晚些时候亮相。 这一警告意义重大，因为它挑战了当前 AI 硬件领域主流的扩展策略，并可能在中美形成独立半导体生态系统的背景下重塑全球芯片竞争格局。如果华为的替代路径取得成功，它可能为没有 EUV 光刻机的情况下制造先进芯片提供一条可行道路。 LogicFolding 通过将电路布局从一层扩展到两层来缩短芯片内部布线，从而减少信号传输时间并提高晶体管密度。廖恒强调，在中美分化的格局下，各方必须建立完整的制造与供应能力才能生存。

telegram · zaihuapd · 8月4日 08:04

**背景**: 传统半导体扩展遵循摩尔定律，主要依靠缩小晶体管尺寸以及增加计算芯片和内存芯片来提升性能。然而，这些方法正逼近根本性的物理极限。华为的 LogicFolding 是一项芯片设计技术，旨在通过将电路布局垂直堆叠而不是进一步缩小特征尺寸来延续性能提升。更大的背景是，美国出口管制限制了中国获取 EUV 光刻机等先进芯片制造设备，加速了半导体产业分化为两个独立生态系统的进程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.yahoo.com/computing/articles/huawei-logicfolding-chip-design-aims-133711716.html">Huawei LogicFolding chip design aims to match 1.4nm by 2031</a></li>
<li><a href="https://www.phonearena.com/news/huawei-plan-to-make-advanced-node-chips-without-euv-is-legit-says-scientist_id180999">U.S. chip scientist says Huawei's plan to make... - PhoneArena</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#Huawei`, `#Nvidia`, `#chip design`, `#AI hardware`

---

<a id="item-11"></a>
## [Cloudflare 用 58 美元/月 AI 取代第三方安全工具，称他人勿效仿](https://www.theregister.com/security/2026/08/04/cloudflare-has-mostly-ditched-third-party-security-tools-suggests-not-trying-that-at-home/5282600) ⭐️ 8.0/10

Cloudflare 首席安全官 Grant Bourzikas 在悉尼透露，公司已用内部构建的 200 多个自主安全代理基本取代第三方安全工具，并用 Anthropic 的 Claude Sonnet 模型以每月仅 58 美元的成本处理漏洞赏金报告；若改用 Anthropic 的 Mythos 安全模型，同样工作每月约需 20 万美元。 这一案例展示了将物美价廉的通用 AI 用于安全运营的实用方式，可能重塑漏洞管理的成本结构。但 Bourzikas 明确警告其他企业不要效仿，强调在推进此类自动化之前必须拥有深厚的内部安全工程能力。 58 美元这一数字对应 Claude Sonnet 模型，而 Anthropic 的 Mythos——具备自主攻击性安全能力的前沿模型——处理相同分类工作负载要昂贵得多。Cloudflare 还构建了 200 多个自主安全代理，并开发了部分由 AI 辅助编写的自研应用；首席战略官 Stephanie Cohen 将公司裁员 1100 人与 AI 驱动的自动化变革联系起来。

telegram · zaihuapd · 8月4日 09:24

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，Sonnet 是其中以强大 agentic 编码能力著称的中端型号。Mythos（正式名称为 Claude Mythos Preview）是 Anthropic 截至 2026 年 4 月能力最强的前沿模型，专长于长时间自主推理和攻击性安全任务。自主安全代理是独立运行、几乎无需人工干预的 AI 驱动网络防御系统，与传统的基于规则的扫描器形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model)</a></li>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet \ Anthropic</a></li>
<li><a href="https://www.illumio.com/cybersecurity-101/what-is-mythos">Cybersecurity 101: What Is Mythos AI ? Complete Technical... | Illumio</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#Cloudflare`, `#automation`, `#vulnerability management`

---

<a id="item-12"></a>
## [谷歌为 Anthropic 搭建 2000 亿美元华尔街融资机器](https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c) ⭐️ 8.0/10

《金融时报》调查发现，谷歌已悄然搭建史上最大规模的基础设施融资架构之一，用于支持向 Anthropic 交付超 1500 亿美元 AI 芯片，相关合同总额约 2000 亿美元。今年 6 月，特殊目的载体 Compute SPV 完成首批交易，购入约 350 亿美元硬件，约合 1 吉瓦算力、100 万颗 TPU。 这一创新融资模式将数千亿美元的 AI 硬件移出企业资产负债表，使没有信用评级的 Anthropic 也能获得庞大的算力资源。它同时标志着 AI 基础设施的资本运作方式正在被深刻重构，科技巨头与华尔街机构正在 AI 竞赛中共同分担风险。 相关合同中约八成与芯片直接挂钩，参与方包括博通、阿波罗、黑石、摩根士丹利及多家加密矿企。风险分担机制为：谷歌担保数据中心，博通购买并协助融资芯片，阿波罗与黑石出资购买硬件后回租给 Anthropic，这一模式借鉴了波音和 GE 推销飞机、发动机的厂商融资玩法。

telegram · zaihuapd · 8月4日 10:52

**背景**: 特殊目的载体（SPV）是为特定目的设立的独立法律实体，通常用于持有单笔投资并将金融风险与母公司隔离，Compute SPV 就是这样的载体。厂商融资（vendor financing）指卖方借钱给买方、让买方购买卖方自家产品的融资方式，波音和 GE 长期用此模式销售飞机和发动机。谷歌的 TPU 是为机器学习任务定制的专用集成电路（ASIC）加速器。这些结构使各方都能将巨额硬件成本移出资产负债表，同时转移所有权和风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.angelschool.vc/blog/spv-special-purpose-vehicles-and-their-role-in-business-and-finance">What Is an SPV ? Special Purpose Vehicles Explained (2026)</a></li>
<li><a href="https://www.investopedia.com/terms/v/vendorfinancing.asp">What is Vendor Financing? Definition, Types, and Advantages</a></li>
<li><a href="https://jonathan-hui.medium.com/ai-chips-tpu-3fa0b2451a2d">AI Chips: Google TPU . Google ’s chip designers argue that the | Medium</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Google`, `#Anthropic`, `#financing`, `#cloud computing`

---

<a id="item-13"></a>
## [特朗普政府拟起草禁令 禁止进口中国数据中心光模块](https://www.reuters.com/world/trump-administration-drafting-ban-chinese-data-center-devices-sources-say-2026-08-04/) ⭐️ 8.0/10

据报道，特朗普政府正在起草一项禁令，拟禁止进口新型中国数据中心光模块，美国联邦通信委员会（FCC）正推进此事，并希望年内发布生效。消息人士提醒，该禁令仍可能修改或搁置。 这一监管举措可能扰乱全球数据中心供应链和 AI 基础设施，直接影响中际旭创等主要厂商，后者约占光模块市场 27%的份额。这也表明美国对关键基础设施中中国技术的限制正进一步收紧。 据报道，该禁令旨在防止数据窃取、植入恶意软件或中断服务，此前 FCC 已对中国无人机、路由器、机器人和逆变器实施类似限制。中国驻美使馆表示，将对损害中国利益的行为采取一切必要措施。

telegram · zaihuapd · 8月4日 11:29

**背景**: 光模块又称光收发器，负责将电信号转换为光信号并进行反向转换，从而实现数据中心内部及之间的高速数据传输。随着 AI 工作负载增长，数据中心互联越来越依赖更快的光模块（如 200G 和 400G 等型号），Marvell、Lumentum 等主要供应商为云和超大规模数据中心生产这些组件。该禁令草案反映了美国对供应链安全及 AI 相关基础设施保护的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marvell.com/products/optical-modules.html">DCI Optical Modules | Delivering high bandwidth over distance - Marvell</a></li>
<li><a href="https://www.versitron.com/blogs/post/optical-transceivers-in-data-centers-challenges-and-market-trends">Optical Transceivers in Data Centers: Challenges and Market Trends | Versitron</a></li>
<li><a href="https://www.lumentum.com/en/optical-communications/applications/optical-transport-and-data-center-interconnects">Optical Transport and Data Center Interconnects | Lumentum</a></li>

</ul>
</details>

**标签**: `#technology policy`, `#AI infrastructure`, `#data centers`, `#supply chain`, `#trade restrictions`

---

<a id="item-14"></a>
## [白宫开源 AI 监管急转弯，硅谷分歧加剧](https://www.nytimes.com/2026/08/04/technology/ai-washington-regulation-whiplash.html) ⭐️ 8.0/10

特朗普政府在硅谷强烈反对后，放弃了制裁或拉黑中国开源 AI 模型的计划，转而聚焦提升美国竞争力并对 AI 模型进行发布前安全审查。8 月 4 日，白宫召集科技公司商讨新框架，拟在高级 AI 模型公开发布前进行网络安全审查。 这一政策反转标志着美国 AI 监管的重大转变，国家安全考量与开源生态之间形成冲突。它影响到推动限制的 OpenAI、Anthropic，以及捍卫开放生态的 Nvidia、Meta，并可能重塑全球 AI 创新与安全之间的平衡。 白宫幕僚长 Susie Wiles 和财长 Scott Bessent 曾考虑动用制裁、贸易黑名单甚至禁止美企与中国公司合作，但在业界反对后放弃。黄仁勋上月首次在 X 上发帖为开源 AI 辩护，并参与组建了拥有逾 230 家成员的安全联盟。

telegram · zaihuapd · 8月4日 15:22

**背景**: 开源 AI 模型（如 Moonshot AI 的 Kimi 系列）公开其权重，任何人都能对其进行定制和部署，这引发担忧——美国对手可能借此加速自身 AI 能力。Kimi K2 于 2025 年 7 月以开放权重形式发布，后续的 Kimi K2.5 是开源多模态模型。包括 Anthropic 和 OpenAI 在内的美国主要 AI 实验室已同意自愿进行发布前安全审查，2026 年 6 月的行政令进一步确立了政府与产业在 AI 安全方面的合作框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(AI)">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://www.kimi.com/ai-models/kimi-k2-5">Kimi K2.5 | Open Visual Agentic Model for Real Work</a></li>
<li><a href="https://www.cio.com/article/4166828/white-house-weighs-pre-release-reviews-for-high-risk-ai-models.html">White House weighs pre-release reviews for high-risk AI ...</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#open source`, `#Silicon Valley`, `#national security`, `#technology policy`

---