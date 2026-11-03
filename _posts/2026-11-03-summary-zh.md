---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 42 条内容中筛选出 6 条重要资讯。

---

1. [Astra 可直接读写神经网络权重，将 Qwen 数学能力提升约五倍](#item-1) ⭐️ 9.0/10
2. [YC 创业公司 Subvocal 发布 RF 智能眼镜，可将无声口型转为文字](#item-2) ⭐️ 8.0/10
3. [近三周仍未修复：Ubuntu LTS 内核严重 0day 远程代码执行漏洞持续裸露](#item-3) ⭐️ 8.0/10
4. [WIRED 调查：400 多款 AI 应用暗藏色情深伪功能](#item-4) ⭐️ 8.0/10
5. [瑞典连锁超市 ICA 遭网络攻击，冷柜被远程调至 50°C](#item-5) ⭐️ 8.0/10
6. [Anthropic 招股书披露：前三季度营收 332 亿美元，净亏损 1040 亿美元](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Astra 可直接读写神经网络权重，将 Qwen 数学能力提升约五倍](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 9.0/10

一篇关于“权重空间编程”（weight-space programming）的新博客文章报告称，名为 Astra 的前沿模型（报道中称为 GPT-6 Astra，来自 MIT CSAIL）能够在没有优化器、也没有训练过程的情况下，原生地读取并编辑另一个网络的权重。在其第八个实验中，Astra 手工编辑了 Qwen3.5-0.8B，改动了 131,072 个权重条目——约占该模型 8 亿参数中的 0.016%——使 MATH-500 准确率从 7.9% 提升至 48.1%。 如果结果可以复现，这将是一个范式级别的成果：模型行为将不再只能通过重训练、微调或提示工程来调整，而是可以直接在权重空间中被检视和“打补丁”。它还触及递归自我改进（recursive self-improvement）问题——一个能可靠编辑其他模型权重的模型，原则上可以在没有常规训练循环的情况下改进 AI 系统。 Astra 将 Qwen 的“循环”故障（其前 96 个练习答案中有 85 个一路跑到 32,768 token 上限）定位到由第 15 层和第 19 层 MLP 写出的某一个方向，并从这两层各自的 64 个输出列中减去该方向；它先用 Python 计算出替换数值，再提交编辑后的张量进行测试，而这一修复还顺带改善了指令遵循能力。需要保留的限定是：这只是一个 8 亿参数的小模型、单一基准测试，而且 Sean Goedecke 等质疑者认为 LLM 在读写权重方面并非真正超人。

hackernews · dbreunig · 11月2日 18:21 · [社区讨论](https://news.ycombinator.com/item?id=50341174)

**背景**: 神经网络的权重通常由 Adam、Muon 之类的优化器产生，或者由一个“写网络的网络”生成，抑或由把形式化程序编译成权重的编译器产出。作者所定义的“权重空间编程”与此不同：由一个通用大模型直接读写某个网络的权重，而不经过优化器。Qwen 是阿里云推出的开放权重大模型系列，Qwen3.5-0.8B 是其中最小的成员之一，因此很适合作为权重层面实验的试验台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight -Space Programming: LLMs can natively read & write...</a></li>
<li><a href="https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/">LLMs are not superhuman at reading and writing neural network ...</a></li>
<li><a href="https://kingy.ai/blog/weight-space-programming-ai-agent-model-weights/">Weight-Space Programming: GPT-6 Astra Edits Qwen - kingy.ai</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（2,059 分、669 条评论）异常扎实：vessenes 表示自己“被震住了”，并说若在今天早上被问到，他会认为 LLM 对自身权重的理解不比人类对神经元内部机制的理解更强；xg15 则认为这一结果并非完全出乎意料，因为当代 LLM 反复展现出快速掌握庞大复杂系统的能力。vanyle 的反驳最有力，认为这不是涌现能力，而很可能是刻意用神经网络权重数据训练 Astra、以追求递归自我改进的产物。

**标签**: `#AI/ML`, `#interpretability`, `#weight-space editing`, `#LLM`, `#recursive self-improvement`

---

<a id="item-2"></a>
## [YC 创业公司 Subvocal 发布 RF 智能眼镜，可将无声口型转为文字](https://news.ycombinator.com/item?id=50340088) ⭐️ 8.0/10

YC F26 批次的创业公司 The Subvocal Company 由佐治亚理工学院的 Aarush 和 Arnav 创立，他们展示了用射频传感把无声口型——甚至闭着嘴的“内部言语”——解码成文字的智能眼镜。团队称该系统识别速度超过每分钟 200 词，已融资约 130 万美元，目前正在接受预订。 无声语音输入能让人们在图书馆、办公室和公共场所向 AI 工具和电脑口述，而在这些场景中使用 Wispr Flow 这类语音输入很不方便，同时对有言语或运动障碍的用户可能带来变革性帮助。如果它能稳定地跨用户工作，还意味着一种无需麦克风和摄像头的、随时可用的免手 AI 输入方式。 眼镜发射类似蓝牙的低功率无线电波穿透面部，电波会被舌头、嘴唇和软腭调制，团队再用在此数据上训练的基础模型把扰动解码为文字。创始人放弃了早期在 TreeHacks 用 36 小时搭出的 EMG 电极方案，原因是出汗、电气干扰、电极位置不稳定以及佩戴舒适度问题；他们表示最难解决的仍是跨用户泛化，因为每个人的面部解剖结构会产生不同的射频特征。

hackernews · aarushyadav · 11月2日 17:16

**背景**: 无声语音识别（SSR）是学界长期研究的声学语音识别替代方案，它不依赖可听声音，而是通过肌电信号（EMG）、雷达、深度传感或耳机声学传感等方式捕捉言语。MIT 媒体实验室的 AlterEgo 项目让通过面部电极进行“亚言语”输入的思路广为人知，而此前 RFTattoo 等射频方案需要在面部贴 RFID 标签。Subvocal 的主张是：把天线嵌入外观普通的眼镜框，可以让传感变得无感且适合日常使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eesel.ai/blog/subvocal">Subvocal glasses: silent speech to text, price and what's ...</a></li>
<li><a href="https://www.indiatoday.in/technology/news/story/subvocal-founded-by-arnav-and-aarush-makes-ai-glasses-that-turn-silent-words-into-text-3029418-2026-10-31">Subvocal, founded by Arnav and Aarush, makes AI glasses that ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Subvocal_recognition">Subvocal recognition - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的反应相当热烈，不少人称其有科幻感，并认为这对无障碍使用和免手计算是重大利好；但评论者也不断追问实用性：一位鼻梁较高的预订者希望团队保留可调节金属鼻托，另一位则希望推出可夹在现有近视镜框上的模块，因为现成镜框尺寸偏小。还有人询问 Subvocal 与 LipFlow、HushKey、Chaplin、LipNet 等开源无声输入项目相比如何，并就隐私提出担忧——推理是在设备端还是离线运行，担心常开的传感会被用于用户画像和广告定向。

**标签**: `#silent speech recognition`, `#smart glasses`, `#human-computer interaction`, `#accessibility`, `#privacy`, `#RF sensing`

---

<a id="item-3"></a>
## [近三周仍未修复：Ubuntu LTS 内核严重 0day 远程代码执行漏洞持续裸露](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) ⭐️ 8.0/10

Ubuntu 的 LTS 内核在近三周时间里仍未修复一个被编号为 CVE-2026-98432 的 Linux 内核 0day 远程代码执行漏洞，并且在此期间没有发布任何缓解措施说明。由于 Canonical 既未提供官方补丁也未给出临时方案，社区成员自行传播了应急防御手段，并质疑补丁为何迟迟不来。 一个可远程利用且厂商尚未提供补丁的内核漏洞，会让所有受影响的 Ubuntu LTS 服务器和桌面系统处于暴露状态，而 LTS 版本被大量用于生产和云基础设施，内核层被攻破往往意味着整台主机失守。同时，这种沉默也损害了人们对 Ubuntu 安全响应流程的信任，已有用户表示今后新服务器将不再选择 Ubuntu。 由于内核在补丁落地前就可能被利用，有评论者提出在 raw 表的 PREROUTING 链上用 iptables 的 u32 匹配提前丢弃恶意数据包（`iptables -t raw -I PREROUTING -p tcp -m u32 ! --u32 "0>>24&0x0F=5" -j DROP`）。相比之下，RHEL 已发布缓解方案，但承认它“只能降低暴露面、无法完全阻止该漏洞利用”，却没有解释这一限制的含义，其他评论者表示从未见任何来源证实这一说法。

hackernews · majorchord · 11月2日 18:39 · [社区讨论](https://news.ycombinator.com/item?id=50341462)

**背景**: 0day（零日）漏洞是指在厂商发布修复之前就已被知晓甚至已被利用的安全缺陷，防御方只能依靠临时绕过手段。远程代码执行（RCE）指攻击者无需用户交互即可通过网络执行任意命令的一类漏洞，若发生在内核中，则意味着攻击者可完全控制整台机器。Ubuntu LTS（长期支持）版本会被维护多年，是服务器的默认选择之一，因此内核补丁拖延所波及的范围远大于短生命周期的发行版。内核补丁通常只是例行更新，正因如此，社区才要求 Canonical 给出拖延的具体原因，而不只是再发一个新内核。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/remote-code-execution/">What is Remote Code Execution (RCE)? | CrowdStrike</a></li>
<li><a href="https://en.wikipedia.org/wiki/Arbitrary_code_execution">Arbitrary code execution - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论整体偏批评：有人指出公众讨论中几乎没人提到可以用 iptables/nftables 的 u32 规则在 PREROUTING 链上丢弃相关数据包来阻止利用；也有人要求官方给出拖延的真实原因，指出 RHEL 至少公布了（ albeit 含糊的）缓解方案，并提醒运行 Linux 的消费级路由器根本收不到内核安全更新。多位评论者认为大语言模型正在把国家级水平的攻击工具交到脚本小子手里，使未修补的已知漏洞更危险，至少一位长期用户表示这一事件动摇了他对 Ubuntu 的信心。

**标签**: `#linux-kernel`, `#security-vulnerability`, `#ubuntu`, `#0day`, `#mitigation`

---

<a id="item-4"></a>
## [WIRED 调查：400 多款 AI 应用暗藏色情深伪功能](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 8.0/10

WIRED 于 11 月 2 日发布调查，揭露一个由 400 多个相互关联的应用与网站组成的网络：它们对外表现为宠物画像、语言学习、AI 健身教练等普通工具，却在特定条件下加载隐藏的色情深度伪造界面。在收到 WIRED 提供的线索后，苹果下架了 19 款应用；截至 9 月仍在 Google Play 上架、累计下载超过 35 万次的 27 款应用中，多数已被谷歌在媒体联系前移除；Meta 则阻止了 209 款相关应用投放广告。 这一事件表明，应用商店审核与广告审核流程可以被大规模、系统性地绕过，使得制造未经同意的私密影像的工具能够触达普通用户，其中不少应用还被标为适合所有年龄段，未成年人同样暴露在风险中。这也给苹果、谷歌和 Meta 施加压力：它们需要针对同一运营网络协同治理，而不是等到媒体曝光后才逐一处理。 据报道，这些应用以正常功能通过审核，上架后再由服务器切换远程网页内容，从而在不提交新原生二进制包的情况下改变用户所见。研究人员通过共享代码、托管信息、中文源代码及域名等线索把这些应用串联起来，并将其与中文开发者及一家香港注册公司关联；报道方强调这属于媒体与研究人员的调查判断，相关运营方未回应置评请求。

telegram · zaihuapd · 11月2日 12:45

**背景**: 所谓“nudify”类服务利用生成式图像模型，从一张上传照片中去除衣物或合成露骨图像，常被用于制作未经同意的私密影像。由于苹果 App Store 与 Google Play 禁止此类内容，运营者便把应用伪装成普通 AI 工具，并借助远程网页视图在用户安装后才提供违规功能。调查人员通常通过比对共享代码特征、托管基础设施、域名注册信息以及广告追踪标识，把表面上互不相关的应用关联成同一网络。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openai-hub.com/news/2645/">苹果下架19款伪装App：深度伪造如何靠审核后换壳绕过App Store治理 - ...</a></li>
<li><a href="https://www.shuzhipunk.com/articles/CqvTLA0p2tX">400余款伪装AI应用暗藏深度伪造违规功能，科技巨头审核机制遭系统性绕...</a></li>
<li><a href="https://nudify.im/ai-clothes-remover/">AI Clothes Remover - Remove Clothing from Any Photo | Nudify .im</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#deepfakes`, `#app store moderation`, `#privacy`, `#content moderation`

---

<a id="item-5"></a>
## [瑞典连锁超市 ICA 遭网络攻击，冷柜被远程调至 50°C](https://x.com/InsiderGeo/status/2117164877701595165) ⭐️ 8.0/10

瑞典连锁超市 ICA 表示，多家门店夜间遭到网络攻击，冷藏柜和冷冻柜被远程设定为 50°C，受影响的门店包括斯约博（Sjöbo）和托梅利拉（Tomelilla）等地。相关门店上午暂停营业，预计当地时间 9 点左右重新开门，ICA 已向顾客致歉。 这是一次典型的网络物理攻击：纯数字层面的入侵直接造成了物理与经济损失——食品变质、门店停业和营收流失，而非数据被窃。近几周法国、爱尔兰、比利时和美国的零售商也接连出现针对制冷系统的类似攻击，这应促使零售业的 OT/IoT 运营方把制冷与楼宇控制系统当作安全关键资产来对待。 ICA 并未披露攻击者是如何触达制冷控制系统的，也没有给出入侵途径的技术细节、受影响门店数量或食品变质的总体损失。安全研究者多次警告，暴露在互联网上的制冷与楼宇自动化控制器可被滥用——攻击者只需调用正常的设定值功能，无需破坏性恶意软件即可造成损害。

telegram · zaihuapd · 11月2日 13:52

**背景**: 现代超市的制冷与暖通空调设备运行在联网控制系统之上，属于运营技术（OT）和物联网（IoT）范畴，通常由员工或第三方承包商远程监控和调优以节能。当这些控制器可从互联网直接访问、或仅有弱口令保护时，攻击者就能像授权技师一样修改温度设定值，系统会将其视为合法指令执行。由于食品变质与食品安全风险迫在眉睫，零售商在此类事件后通常会将冷藏和冷冻商品下架，爱尔兰 SuperValu 门店以及法国 Intermarché 与 Coopérative U 门店此前都采取了类似措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/">Cold Chain, Open Control: Exposed Refrigeration Systems Reveal...</a></li>
<li><a href="https://www.euronews.com/2026/11/02/cyberattack-hits-belgian-supermarket-fridges-and-freezers">Cyberattacks hit supermarket fridges and freezers in... | Euronews</a></li>
<li><a href="https://www.rte.ie/news/world/2026/1102/1597622-cyber-attacks-appliances/">Explainer: Is my fridge vulnerable to a cyber attack ?</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#IoT/OT security`, `#cyber-physical attack`, `#critical infrastructure`, `#retail`

---

<a id="item-6"></a>
## [Anthropic 招股书披露：前三季度营收 332 亿美元，净亏损 1040 亿美元](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) ⭐️ 8.0/10

Anthropic 周一更新了其 IPO 招股书，披露截至 2026 年 9 月 30 日的前三季度营收达到 332.4 亿美元，同比增长约 1200%，其中仅第三季度营收就约为 170 亿美元。同一份文件显示，该期间净亏损达到 1040 亿美元，远高于去年同期的 251 亿美元。 这份披露为外界提供了一个难得的机会，得以在上市前审视一家头部 AI 实验室的经济状况：营收以惊人的速度增长，但亏损扩张得更快。约 8954 亿美元的算力与基础设施承诺也表明公司已锁定巨额未来支出，这对投资者、云服务商以及整个 AI 供应链上的芯片供应商都具有重要意义。 Anthropic 表示，上半年净亏损主要受可转换债券及衍生负债的公允价值变动影响，因此并不完全代表实际经营现金消耗。约 8954 亿美元的累计采购与租赁承诺几乎全部用于算力和基础设施。

telegram · zaihuapd · 11月2日 15:12

**背景**: Anthropic 是 Claude 系列模型背后的 AI 公司，而 IPO 招股书是公司在公开发行股票前提交的注册文件，需要披露营收、亏损和重大债务义务。根据会计准则，可转换债券和衍生负债每个报告期都要按公允价值计量，当公司估值飙升时，这些计量会产生大额非现金亏损，并与真实经营业绩并列呈现。算力承诺则是购买 GPU 算力和云基础设施的多年期合同，本质上是在押注未来的模型训练与推理需求足以支撑这些支出。

**标签**: `#Anthropic`, `#AI industry`, `#IPO`, `#financials`, `#compute infrastructure`

---