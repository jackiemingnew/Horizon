---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> 从 37 条内容中筛选出 9 条重要资讯。

---

1. [OpenAI 声称攻克 Navier-Stokes 千禧年难题，尚待验证](#item-1) ⭐️ 10.0/10
2. [巴克马斯特声明指控 OpenAI 侵占纳维-斯托克斯成果](#item-2) ⭐️ 8.0/10
3. [Qwen3.8 27B 量化基准测试：4 位性能坚挺，1 位严重崩坏](#item-3) ⭐️ 8.0/10
4. [OpenAI 推出 ChatGPT Images 2.5，新增双 API 模型](#item-4) ⭐️ 8.0/10
5. [NeurIPS 使用有缺陷的 AI 检测器直接拒稿 178 篇论文，引发强烈争议](#item-5) ⭐️ 8.0/10
6. [马来西亚拟用华为 Ascend 910C 芯片建设主权 AI 项目](#item-6) ⭐️ 8.0/10
7. [张一鸣亲自督导字节跳动开发空间视频模型](#item-7) ⭐️ 8.0/10
8. [ASML 与台积电合作推进 High NA EUV 采用 12 英寸光掩模](#item-8) ⭐️ 8.0/10
9. [中国计划到 2030 年将智能算力提升至 9800 EFLOPS](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 声称攻克 Navier-Stokes 千禧年难题，尚待验证](https://www.reddit.com/r/MachineLearning/comments/1wavdi7/openal_says_it_has_cracked_one_of_maths/) ⭐️ 10.0/10

2026 年 9 月 8 日，OpenAI 宣布其未发布的内部模型产出了一个证明，表明在光滑外力作用下，光滑且有限能量的三维不可压缩流动可能在有限时间内形成奇点，并已在 Lean 证明助手中完成形式化。该公司称这证实了 Fefferman 官方问题表述中的陈述 C 和 D。 如果得到验证，这将是第二个被解决的千禧年难题，也是数学、物理学和流体力学领域的重大突破。它可能深刻改变人们对湍流的理解，并证明 AI 能够为前沿数学研究作出贡献，但仍需独立验证。 截至 2026 年 9 月，这一声称的证明尚未得到数学界的独立验证，也未经过 Clay 数学研究所评估，据报道 OpenAI 表示即使被授予千禧年奖也会拒绝。该公告还伴随着与研究 Euler 方程相关爆破结果的数学家的优先权争议，其方法建立在 Diego Córdoba 和 Luis Martínez Zoroa 于 2023 年工作的基础上。

reddit · r/MachineLearning · /u/Shizuka_Kuze · 9月8日 17:42

**背景**: Navier-Stokes 方程是描述流体运动的偏微分方程，其解广泛应用于科学和工程领域。2000 年，Clay 数学研究所将 Navier-Stokes 存在性与光滑性问题列为七大千禧年难题之一，每个问题设 100 万美元奖金。该问题要求数学家证明三维方程的光滑全局解总是存在，或给出反例；OpenAI 通过声称有限时间奇点，提出了一个反例。截至 2026 年，唯一被官方解决的千禧年难题是 Poincaré猜想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Navier-Stokes`, `#mathematics`, `#AI research`, `#Millennium Problem`

---

<a id="item-2"></a>
## [巴克马斯特声明指控 OpenAI 侵占纳维-斯托克斯成果](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 8.0/10

特里斯坦·巴克马斯特发表公开声明（PDF），指控 OpenAI 在 2026 年 9 月发布 AI 发现证明的公告中，未经许可或署名地使用了他与莱文特·阿尔珀格未发表的数学工作——包括一个接近千禧年大奖问题的纳维-斯托克斯奇异性结果。声明描述了围绕该结果的提议、威胁和试图抢先发表的经过。 这一争议使学术界的开放署名研究规范与大型 AI 实验室的封闭开发方式形成对立。若指控成立，将是严重的研究伦理失范，会对分享草稿或使用 AI 工具的数学家产生寒蝉效应。 巴克马斯特与阿尔珀格表示，他们证明了光滑外力下 3D 不可压缩欧拉方程、多孔介质方程和 Boussinesq 方程等的有限时间爆破，但并没有证明完整的克莱千禧年纳维-斯托克斯问题。OpenAI 在评论中承认“不能排除”去标识化的用户数据帮助改进了其模型。

hackernews · procedurecall · 9月8日 05:42 · [社区讨论](https://news.ycombinator.com/item?id=49605915)

**背景**: 纳维-斯托克斯方程描述粘性流体的运动，而三维情况下光滑全局解是否总是存在正是克莱数学研究所的千禧年大奖问题之一，悬赏 100 万美元。OpenAI 在 2026 年 9 月的公告中声称，其内部模型产生了形式化证明，表明受光滑外力的不可压缩流动可在有限时间内形成奇性，从而确立了费弗曼表述中的“C”和“D”两项陈述，但该说法尚未被独立验证。巴克马斯特与阿尔珀格的相关工作并非千禧年问题的完整解答，但可能是通向完整证明的阶梯。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_equations">Navier-Stokes equations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>

</ul>
</details>

**社区讨论**: 评论者对 OpenAI 提出尖锐批评，指责其查看用户数据、窃取世界级研究者的成果，并威胁研究者以维护企业利润。也有评论者指出，除非 OpenAI 确实使用了这两位数学家的数据，否则此事可能只是被 AI 放大的普通学术优先权之争；但 OpenAI 自己在数据使用问题上的含糊态度使疑问仍然存在。

**标签**: `#Navier-Stokes`, `#OpenAI`, `#academic integrity`, `#research ethics`, `#mathematics`

---

<a id="item-3"></a>
## [Qwen3.8 27B 量化基准测试：4 位性能坚挺，1 位严重崩坏](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) ⭐️ 8.0/10

Quesma 的一项基准测试对 Qwen3.8-27B 的量化版本进行了评测，结果显示 4 位量化基本保持质量，2 位量化得分下降，1 位量化则严重崩坏。这些结果说明，该模型的实用质量阈值大概在 4 位。 这为开发者提供了实用指引，说明在本地推理时能把 Qwen3.8-27B 压缩到什么程度，因为更低的位数能降低显存占用与内存带宽。特别是“4 位仍是安全选择”的结论，对在 24GB 显卡上运行 27B 模型的场景很有帮助。 该基准用 Wilson 95%置信区间来反映运行噪声；在该区间内，模型质量直到 4 位都保持稳定，2 位的得分则明显更低。1 位量化会造成灾难性的质量损失。文章没有直接涉及 KV cache 量化，而评论区提到这对于长上下文使用很重要。

hackernews · stared · 9月8日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49611128)

**背景**: 量化（quantization）通过用更低精度的数字来表示 LLM 的权重，从而压缩模型体积，用少量输出质量换取大幅降低的显存占用和更快的推理速度。Qwen3.8-27B 是阿里巴巴发布的开源权重模型，参数约 277.8 亿，采用 Apache 2.0 许可，并能在 24GB 显存上以 4 位量化运行。这类基准测试能帮助本地部署用户选择合适的量化档位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.techpillow.co/blog/qwen3-8-27b-alibaba-open-weight-multimodal-model">Qwen 3 .8- 27 B Open-Weight AI Model Benchmarks | TechPillow Blog</a></li>

</ul>
</details>

**社区讨论**: 评论区对置信区间提出质疑：有人认为 Wilson 区间很难说明逐次运行噪声，也有人提出 Qwen3.8-27B 会通过更高思考等级“想得更久”来补偿量化带来的质量损失。还有用户希望看到 KV cache 量化的类似测试，并指出缺少 Q3 档位会影响 16GB 以下显卡用户的判断。

**标签**: `#quantization`, `#LLM`, `#benchmarking`, `#Qwen`, `#machine learning`

---

<a id="item-4"></a>
## [OpenAI 推出 ChatGPT Images 2.5，新增双 API 模型](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 8.0/10

2026 年 9 月 8 日，OpenAI 发布了 ChatGPT Images 2.5，增强了多轮指令遵循能力，提升了响应速度，并更好地保留参考照片中的主体。该版本新增两个 API 模型 ID：gpt-image-2.5-sunburst 面向精细编辑，gpt-image-2.5-flare 面向快速日常生成。 这一发布意义重大，因为它为开发者提供了两个各有侧重的图像生成模型，让他们可以在精度与速度之间进行取舍，也表明 OpenAI 正转向按工作负载提供专用 API。由于 ChatGPT Images 和 GPT-Image API 模型已生成超过 30 亿张图片，即使指令遵循和主体保留方面的渐进式改进，也会对创意工具与开发者工具产生广泛影响。 OpenAI 文档指出，Sunburst 适用于最注重编辑精度的场景，Flare 则用于快速、高质量的日常生成。两个模型均支持文本和图像输入；Simon Willison 也已更新 openai_image.py CLI 工具，使其支持传入一张或多张参考图片。

rss · Simon Willison · 9月8日 22:46

**背景**: ChatGPT Images 是 OpenAI 基于 API 中的 GPT-Image 模型推出的图像生成产品，这些模型迄今已生成超过 30 亿张图片。与以往只推出单一旗舰模型不同，2.5 版本拆分为 Sunburst 和 Flare 两个兄弟模型，分别面向不同的工作负载。本次改进的关键之一是增强多轮指令遵循能力，这对于用户上传参考图片并通过多轮提示逐步调整输出结果的迭代式编辑工作流尤其重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-images-2-5/">Introducing ChatGPT Images 2 . 5 | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-image-2.5-flare">GPT - Image - 2 . 5 Flare Model | OpenAI API</a></li>
<li><a href="https://www.orcarouter.ai/blog/gpt-image-2-5-flare-sunburst">GPT - Image - 2 . 5 Flare vs Sunburst: New OpenAI Image APIs</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#image generation`, `#ChatGPT`, `#API`, `#AI models`

---

<a id="item-5"></a>
## [NeurIPS 使用有缺陷的 AI 检测器直接拒稿 178 篇论文，引发强烈争议](https://www.reddit.com/r/MachineLearning/comments/1wakf62/neurips_deskrejected_178_papers_for_being/) ⭐️ 8.0/10

NeurIPS 的 Position Paper Track 使用专有 AI 检测器 Pangram 直接拒稿了 178 篇论文，占所有投稿的 18.4%，且没有人工审查或申诉程序。测试显示，该检测器将三位主席近期的论文标记为 24%–69%的 AI 生成概率，按同样规则他们自己也有被拒风险。 这次争议凸显了在学术等高风险决策中使用黑盒 AI 检测器的危险，它可能不公平地影响非英语母语研究者，并削弱对同行评审的信任。同时，它也引发了关于程序公正性、算法偏见以及 NeurIPS 等顶级会议问责制的紧迫质疑。 该帖子指出，Pangram 的默认设置最初将整个赛道 42.7%的投稿标记为 90%–100%由 AI 生成，组织者不得不缩小检测文本窗口，才将标记率降至 12.7%。此外，有 22 篇被拒论文是因为检测得分超过 0.5、而作者否认使用 AI 而被直接拒绝；同时引用的一项斯坦福研究表明，61.22%的人类写的 TOEFL 作文会被错误标记为 AI 生成。

reddit · r/MachineLearning · /u/tughanbulut · 9月8日 10:19

**背景**: Desk rejection（桌面拒稿）是学术出版中在同行评审之前进行行政筛选的步骤，通常因不符合范围或投稿规则而拒稿。Pangram 由 Pangram Labs 开发，是一种用于识别大语言模型生成文本的 AI 检测工具，曾因助长对 AI 写作的‘猎巫’行为而受到批评。NeurIPS（神经信息处理系统大会）是最负盛名的机器学习会议之一，其 2026 年 Position Paper Track 引入自动化 AI 筛查，引发了社区激烈讨论。帖子作者还透露自己开发了 StrictCite（一种确定性的零 AI 引用检查器），这可能会使其观点带有一定倾向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pangram_(AI_detector)">Pangram (AI detector)</a></li>
<li><a href="https://www.pangram.com/">AI Detector : Free AI Checker for ChatGPT, Claude & Gemini | Pangram</a></li>

</ul>
</details>

**标签**: `#NeurIPS`, `#AI detection`, `#ethics`, `#academic publishing`, `#algorithmic bias`

---

<a id="item-6"></a>
## [马来西亚拟用华为 Ascend 910C 芯片建设主权 AI 项目](https://www.businesstimes.com.sg/international/malaysia-eyes-huawei-chips-ai-project-despite-us-warning) ⭐️ 8.0/10

据报道，马来西亚正在评估将华为 Ascend 910C 芯片用于其主权 AI 项目，该项目规模达 20 亿林吉特（约 4.94 亿美元）。若最终落地，马来西亚将成为首个正式选择中国 AI 加速器而非美国产品的政府。 这一决定可能重塑 AI 硬件供应链和地缘政治技术联盟，因为它无视了美国的出口警告。这标志着中国 AI 芯片在国际市场上的接受度不断提高，可能影响美国的出口管制政策。 采购芯片的具体数量尚不清楚。美国特朗普政府曾警告，使用华为 AI 加速器芯片可能违反美国出口规定，但马来西亚认为该决定纯属商业考量。

telegram · zaihuapd · 9月8日 03:35

**背景**: 华为 Ascend 910C 是华为开发的高性能 AI 加速芯片，是美国出口管制背景下中国构建本土 AI 计算能力的一部分。主权 AI 是指一个国家利用自己的基础设施、数据和模型来开发、部署和管理 AI 的能力，以确保符合本国法律和战略利益。马来西亚考虑采用华为芯片，反映了各国寻求 AI 自主的更广泛趋势，即便美国试图限制中国在先进技术上的影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.redhat.com/en/topics/ai/sovereign-ai">What is sovereign AI?</a></li>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#AI chips`, `#Malaysia`, `#geopolitics`, `#sovereign AI`

---

<a id="item-7"></a>
## [张一鸣亲自督导字节跳动开发空间视频模型](https://www.bloomberg.com/news/articles/2026-09-07/bytedance-founder-joins-ai-elite-in-race-to-perfect-world-models) ⭐️ 8.0/10

字节跳动创始人张一鸣正亲自督导一款实时空间视频生成模型的开发，最快可能于 2026 年 10 月发布。该模型基于 Seedance，可为 Pico 头显生成响应语音或动作的互动虚拟世界。 这标志着字节跳动将生成式 AI 与空间计算相结合，通过云托管计算降低 VR 硬件门槛。若成功，可能通过实时对话式世界生成加速消费者对 VR 的采用。 该模型据称以约 0.05 秒延迟、每秒 20 帧生成视频，并将高强度计算转移至云端。尽管目标定在 2026 年 10 月，发布时间仍可能调整。

telegram · zaihuapd · 9月8日 04:05

**背景**: 字节跳动的 Seedance 是其基于豆包多模态技术构建的 AI 视频生成模型系列，支持文生视频、图生视频以及参考引导创建。空间视频生成在传统 AI 视频的基础上，在跨视角时保持物体一致性，这对 Pico 头显等沉浸式 VR 体验至关重要。随着与 OpenAI、Meta 等对手竞争加剧，字节跳动创始人张一鸣重新直接参与高风险 AI 项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seeddance.ai/seedance-2-5">Seedance 2.5 — 30s One-Take AI Video with Multimodal... | SeedDance</a></li>
<li><a href="https://www.seedancepro.net/seedance">Seedance AI Video Models</a></li>

</ul>
</details>

**标签**: `#AI`, `#Video Generation`, `#VR`, `#ByteDance`, `#Spatial Computing`

---

<a id="item-8"></a>
## [ASML 与台积电合作推进 High NA EUV 采用 12 英寸光掩模](https://www.nrc.nl/nieuws/2026/09/08/asml-gaat-samenwerken-met-taiwanese-chipgigant-tsmc-om-zijn-nieuwste-chipmachines-te-upgraden-a4936073) ⭐️ 8.0/10

ASML 与台积电于 9 月 7 日发起产业合作，推动 High NA EUV 光刻从 6 英寸光掩模转向 12 英寸规格。双方计划在 2031 年建成 12 英寸掩模试产线，2033 年将相关系统用于先进制程量产；台积电拟从 2030 年起在先进节点大规模制造中使用 High NA EUV。 更大的光掩模有望提高设备生产率、降低芯片制造成本，并减少限制超大尺寸先进制程芯片的拼接约束。这一合作也使台积电成为 ASML High NA EUV 路线图的重要塑造者，将影响整个前沿半导体生态。 现有的 High NA EUV 设备使用 6 英寸掩模，其有限视场可能导致大芯片需要拼接或降低生产效率。2031 年试产线和 2033 年量产目标仍属规划阶段，向 12 英寸掩模转变还将涉及掩模制造、防护膜和工件台设计等多方面的变革。

telegram · zaihuapd · 9月8日 06:55

**背景**: High NA EUV 是新一代极紫外光刻技术，通过 0.55 的数值孔径实现比早期 EUV 更精细的图形。数值孔径越高，单次曝光的视场越小，因此业界需要探索更大的光掩模规格或拼接方案。光掩模是将电路图案转移到硅片上的模板，改为 12 英寸规格会影响整个掩模制造体系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/极紫外光刻">极紫外光刻 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#半导体`, `#EUV`, `#光刻`, `#ASML`, `#台积电`

---

<a id="item-9"></a>
## [中国计划到 2030 年将智能算力提升至 9800 EFLOPS](https://www.scmp.com/tech/policy/article/3366733/china-targets-fourfold-boost-ai-computing-capacity-2030-major-tech-push) ⭐️ 8.0/10

中国工信部发布了新的五年规划，提出到 2030 年将智能算力提升至 9800 EFLOPS，约为当前水平的四倍。规划还提出 2026 年至 2030 年累计投入 3.8 万亿元用于信息基础设施建设。 这是一项旨在扩展人工智能基础设施的重大政府举措，可能重塑国家间 AI 竞争格局，因为中国正寻求降低对进口芯片的依赖。该规划表明各国政府正将算力视为人工智能发展的战略性基础设施。 截至 6 月底，中国智能算力为 2185 EFLOPS，同比增长 177%，因此 2030 年目标意味着要在该基数上增长至 4 倍以上。规划还提出“有序部署”万卡级及 10 万卡以上的智能计算集群，并加强基础设施与国产算力芯片的适配。

telegram · zaihuapd · 9月8日 11:23

**背景**: EFLOPS（exaflops，百亿亿次浮点运算）是衡量计算性能的单位，1 EFLOPS 等于每秒 10^18 次浮点运算，常用于衡量超级计算机和国家计算能力。“智能算力”指面向人工智能训练与推理等任务的计算资源。在先进 GPU 出口管制背景下，华为、寒武纪等中国企业已成为国产 AI 加速器的主要供应商，政府也在鼓励采用国产芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theworldofai.org/ai-glossary/eflops/">What is EFLOPS ( exaFLOPS )? — AI Glossary</a></li>
<li><a href="https://biztechmagazine.com/article/2023/08/what-flops-and-how-does-it-help-supercomputer-performance-perfcon">What Is FLOPS (Floating Point Performance)... | BizTech Magazine</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd">China's homegrown AI accelerators to supply 90% of the country's domestic market, analysts suggest — Cambricon and Huawei expected to be the biggest winners in the shift away from Nvidia and AMD | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#China`, `#AI infrastructure`, `#policy`, `#computing capacity`, `#EFLOPS`

---