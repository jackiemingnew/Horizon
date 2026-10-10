---
layout: default
title: "Horizon Summary: 2026-10-10 (EN)"
date: 2026-10-10
lang: en
---

> From 39 items, 2 important content pieces were selected

---

1. [Cloudflare Acquires Deno; Runtime Development to End After One Year](#item-1) ⭐️ 9.0/10
2. [Telegram Desktop Flaw Lets Malicious tg:// Links Steal Arbitrary Files](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cloudflare Acquires Deno; Runtime Development to End After One Year](https://deno.com/blog/cloudflare) ⭐️ 9.0/10

Cloudflare has acquired Deno, and according to the announcement on Deno's blog, the company will support the Deno runtime for only one more year with monthly releases containing bug fixes and security updates, after which Cloudflare will end its development of the runtime entirely. Deno will remain open source, and Cloudflare says it welcomes others who want to continue its development. Deno was the highest-profile attempt to rebuild a JavaScript runtime from first principles, so its discontinuation removes the main counterweight to Node.js and forces teams running Deno or Deno Deploy in production to plan migrations back to Node.js or to Bun. It also cements a broader wave of consolidation in JavaScript tooling, where independent projects increasingly end up absorbed by platform companies such as Cloudflare, Vercel, Anthropic, and OpenAI. Deno was created in 2018 by Ryan Dahl, the original author of Node.js, and its compiler/runtime is written in Rust and built on the V8 engine. Under the acquisition terms, users get monthly bug fix and security releases for one year, after which the project is effectively unsupported unless an outside maintainer steps up; some community members hope Cloudflare's workerd runtime absorbs Deno's permission-based sandboxing.

hackernews · ilreb · Oct 9, 13:03 · [Discussion](https://news.ycombinator.com/item?id=50019911)

**Background**: Deno is a JavaScript and TypeScript runtime released in 2018 as Ryan Dahl's answer to design regrets he had about Node.js, which he originally created in 2009. Deno supports TypeScript natively without configuration files, runs code inside a permission system that blocks file, network, and environment access by default, and ships built-in tooling such as a formatter, linter, and test runner. To ease migration and adoption, the project later made npm compatibility a priority, which some users felt bloated it and moved it away from its original minimalist vision.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.logrocket.com/dev/what-is-deno/">What is Deno , and how is it different from Node.js? - LogRocket Blog</a></li>
<li><a href="https://javascript.plainenglish.io/deno-vs-node-js-which-javascript-runtime-should-you-use-in-2025-466011af9f74">Deno vs . Node . js : Which JavaScript Runtime Should You Use in...</a></li>

</ul>
</details>

**Discussion**: The discussion mixes grief with post-mortem analysis: commenters quote the blog's one-year maintenance window as confirmation that Deno will die unless someone else takes over, while others say they stopped investing once npm compatibility became a priority, attributing the shift to pressure from VC funding. Several users hope Cloudflare's workerd adopts Deno's security mechanisms, one argues the headline should read 'acquihire' rather than 'acquisition,' and another lists a long chain of similar tooling buy-ups (Astral/uv to OpenAI, Bun to Anthropic, Astro.js and VoidZero to Cloudflare).

**Tags**: `#deno`, `#cloudflare`, `#javascript`, `#runtime`, `#acquisition`

---

<a id="item-2"></a>
## [Telegram Desktop Flaw Lets Malicious tg:// Links Steal Arbitrary Files](https://t.me/zaihuapd/44307) ⭐️ 8.0/10

Telegram Desktop versions below 7.2.9 contain a critical vulnerability tracked as CVE-2026-107181, which allows an attacker to silently exfiltrate arbitrary local files (SSH keys, browser sessions, crypto wallets, documents) when a user merely clicks a crafted tg:// link, with no confirmation prompt. The flaw has been patched in version 7.2.9, and users are urged to upgrade immediately. Telegram Desktop is used by hundreds of millions of people, and this is a one-click, no-confirmation attack that can lead to full account takeover and theft of highly sensitive secrets such as SSH keys and crypto wallet data. Because the exploit class appears to be actively exploited grade, any user running an unpatched build is exposed until they upgrade. The root cause is an unescaped semicolon in a tg:// link that gets treated as a separate IPC record separator inside Core::Sandbox, letting attackers inject OPEN: records; combined with the interpret: handler, this reads arbitrary files off disk and sends them to the attacker, including the account's own session files. The official fix is version 7.2.9, and users should also watch for suspicious tg:// links and enable a local passcode as defense in depth.

telegram · zaihuapd · Oct 9, 09:51

**Background**: Telegram Desktop uses a single-instance IPC mechanism so that clicking a tg:// link hands off the request to the already-running client rather than launching a new process. That IPC protocol uses delimiters to separate records, so if a delimiter character such as a semicolon is not properly escaped when parsing a link, an attacker can smuggle in extra commands. The interpret: handler, which normally lets the client act on a file or path passed by a link, then becomes the vehicle for reading and transmitting local files.

<details><summary>References</summary>
<ul>
<li><a href="https://beaksec.github.io/posts/telegram-desktop-one-click-account-takeover/">Telegram Desktop: one-click account takeover via IPC... | beaksec</a></li>
<li><a href="https://packages.altlinux.org/ru/vuln/CVE-2026-107181">ALT Linux - Все ветки - Vulnerability CVE-2026-107181 - Information</a></li>
<li><a href="https://dbu.gs/vulnerability/CVE-2026-107181">CVE-2026-107181 — Telegram Telegram Desktop | dbugs</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#CVE`, `#Telegram`, `#IPC`

---