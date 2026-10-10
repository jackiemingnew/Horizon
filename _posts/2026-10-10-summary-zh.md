---
layout: default
title: "Horizon Summary: 2026-10-10 (ZH)"
date: 2026-10-10
lang: zh
---

> 从 39 条内容中筛选出 2 条重要资讯。

---

1. [Cloudflare 收购 Deno，运行时开发将在一年后终止](#item-1) ⭐️ 9.0/10
2. [Telegram Desktop 漏洞：恶意 tg:// 链接可静默窃取任意文件](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare 收购 Deno，运行时开发将在一年后终止](https://deno.com/blog/cloudflare) ⭐️ 9.0/10

Cloudflare 已收购 Deno。根据 Deno 官方博客的公告，Cloudflare 只会再为 Deno 运行时提供一年支持，期间以月度发布的形式提供缺陷修复和安全更新，此后将彻底停止对 Deno 运行时的开发。Deno 仍将保持开源，Cloudflare 表示欢迎其他人接手继续开发。 Deno 是试图从第一性原理重建 JavaScript 运行时的最受关注的项目，因此它的停摆消除了 Node.js 的主要竞争制衡，并迫使在生产环境使用 Deno 或 Deno Deploy 的团队规划迁移回 Node.js 或转向 Bun。这也进一步印证了 JavaScript 工具链领域正在经历的整合浪潮——独立项目越来越多地被 Cloudflare、Vercel、Anthropic、OpenAI 等平台型公司收编。 Deno 由 Node.js 的原作者 Ryan Dahl 于 2018 年创建，其运行时用 Rust 编写并基于 V8 引擎。按照收购条款，用户可在一年内获得每月的缺陷修复与安全版本，此后除非有外部维护者接手，否则该项目实际上将失去支持；部分社区成员希望 Cloudflare 的 workerd 运行时能吸收 Deno 基于权限的沙箱机制。

hackernews · ilreb · 10月9日 13:03 · [社区讨论](https://news.ycombinator.com/item?id=50019911)

**背景**: Deno 是一个 JavaScript 与 TypeScript 运行时，于 2018 年发布，是 Ryan Dahl 为弥补他当初在 2009 年创建 Node.js 时留下的设计遗憾而推出的作品。Deno 无需配置文件即可原生支持 TypeScript，代码默认运行在权限系统之下，禁止访问文件、网络和环境变量，并内置格式化器、linter 和测试运行器等工具。为便于迁移和推广，该项目后来把 npm 兼容性列为优先事项，一些用户认为这使 Deno 变得臃肿，偏离了最初的极简理念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.logrocket.com/dev/what-is-deno/">What is Deno , and how is it different from Node.js? - LogRocket Blog</a></li>
<li><a href="https://javascript.plainenglish.io/deno-vs-node-js-which-javascript-runtime-should-you-use-in-2025-466011af9f74">Deno vs . Node . js : Which JavaScript Runtime Should You Use in...</a></li>

</ul>
</details>

**社区讨论**: 讨论中既有惋惜也有事后复盘：有评论者引用博客中“再支持一年”的表述，确认除非有人接手，否则 Deno 将走向终结；也有人表示自从 npm 兼容性成为优先事项后就停止投入，并把这一转向归因于风险投资带来的压力。一些用户希望 Cloudflare 的 workerd 能采纳 Deno 的安全机制，有人认为更准确的标题应是“收购式人才吸纳（acquihire）”而非“收购”，还有人列举了一连串类似的工具链收购案（Astral/uv 归 OpenAI、Bun 归 Anthropic、Astro.js 与 VoidZero 归 Cloudflare 等）。

**标签**: `#deno`, `#cloudflare`, `#javascript`, `#runtime`, `#acquisition`

---

<a id="item-2"></a>
## [Telegram Desktop 漏洞：恶意 tg:// 链接可静默窃取任意文件](https://t.me/zaihuapd/44307) ⭐️ 8.0/10

Telegram Desktop 7.2.9 以下版本存在一个编号为 CVE-2026-107181 的严重漏洞，攻击者只需诱导用户点击一个精心构造的 tg:// 链接，即可在没有任何确认提示的情况下静默窃取本地任意文件，包括 SSH 密钥、浏览器会话、加密钱包和文档。该漏洞已在 7.2.9 版本中修复，官方建议用户立即升级。 Telegram Desktop 拥有数亿用户，而这是一个只需一次点击、无需任何确认的攻击，可能导致账户被完全接管，并泄露 SSH 密钥、加密钱包数据等高度敏感的信息。由于该漏洞被归类为已被实际利用的高危级别，任何仍在使用未修补版本的用户在升级前都处于风险之中。 漏洞根源在于 tg:// 链接中的分号未被转义，被 Core::Sandbox 当作独立的 IPC 记录分隔符处理，使攻击者能够注入 OPEN: 记录；再配合 interpret: 处理器，即可读取磁盘上的任意文件并发送给攻击者，其中也包括账户自身的会话文件。官方修复版本为 7.2.9，同时建议警惕异常 tg:// 链接并启用本地密码作为纵深防御。

telegram · zaihuapd · 10月9日 09:51

**背景**: Telegram Desktop 采用单实例 IPC 机制，因此点击 tg:// 链接时请求会被交给已在运行的客户端，而不是启动新进程。该 IPC 协议使用分隔符来区分不同记录，如果解析链接时像分号这样的分隔符没有被正确转义，攻击者就能夹带额外的命令。而 interpret: 处理器本意是让客户端对链接传入的文件或路径执行操作，在这个漏洞中却成了读取并外传本地文件的工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://beaksec.github.io/posts/telegram-desktop-one-click-account-takeover/">Telegram Desktop: one-click account takeover via IPC... | beaksec</a></li>
<li><a href="https://packages.altlinux.org/ru/vuln/CVE-2026-107181">ALT Linux - Все ветки - Vulnerability CVE-2026-107181 - Information</a></li>
<li><a href="https://dbu.gs/vulnerability/CVE-2026-107181">CVE-2026-107181 — Telegram Telegram Desktop | dbugs</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#CVE`, `#Telegram`, `#IPC`

---