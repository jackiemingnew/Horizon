---
layout: default
title: "Horizon Summary: 2026-07-13 (EN)"
date: 2026-07-13
lang: en
---

> From 34 items, 4 important content pieces were selected

---

1. [Claude Code vs OpenCode: Token Overhead Comparison](#item-1) ⭐️ 8.0/10
2. [LLMs Create Value, But Labs May Not Capture It](#item-2) ⭐️ 8.0/10
3. [Semi-invasive BCI NEO helps paralyzed patient write again in China](#item-3) ⭐️ 8.0/10
4. [Grok Build CLI Emergency Update Disables Code Upload](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude Code vs OpenCode: Token Overhead Comparison](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 8.0/10

A study found that Claude Code sends approximately 33,000 tokens of overhead per request, while OpenCode sends only about 7,000, indicating significant inefficiency in token usage by Claude Code. This token overhead directly increases user costs and reduces workflow efficiency, given that many developers pay per token or have limited subscriptions. The findings could drive users toward more efficient alternatives like OpenCode. The study logged requests between each tool and Anthropic's endpoint, capturing all requests and usage blocks. It notes that Claude Code's inefficiency stems from its cache strategy and harness token usage, though the author acknowledges a caveat and plans a follow-up with qualitative results.

hackernews · systima · Jul 12, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48883275)

**Background**: AI coding assistants like Claude Code and OpenCode use language models to generate code, and they incur token costs based on the number of tokens processed. 'Harness tokens' refer to the system prompt and overhead tokens beyond the user's actual input. The community has observed that some tools consume tokens aggressively, leading to 'tokenflation'.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zbuild.io/resources/news/opencode-vs-claude-code-vs-cursor-2026">OpenCode vs Claude Code vs Cursor in 2026... | ZBuild</a></li>
<li><a href="https://thoughts.jock.pl/p/ai-coding-harness-agents-2026">Claude Code vs Codex vs Aider vs OpenCode vs Pi 2026</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that sub-agents in Claude Code can burn many tokens, and some users suspect Anthropic intentionally inflates token usage to drive subscriptions. The author also engaged with criticism about measuring the right metric and plans to add qualitative comparisons.

**Tags**: `#AI coding tools`, `#token efficiency`, `#Claude Code`, `#OpenCode`, `#cost optimization`

---

<a id="item-2"></a>
## [LLMs Create Value, But Labs May Not Capture It](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html) ⭐️ 8.0/10

George Hotz published a blog post arguing that while LLMs produce real productivity gains and value, frontier AI labs like OpenAI and Anthropic are overvalued because they may not capture that value. The post challenges the hype-driven valuation of these companies. This critique is significant because it questions the fundamental business model of frontier AI labs, suggesting that even if AI transforms the economy, the labs themselves might not profit. It fuels ongoing debates about AI hype, open source vs. proprietary models, and where real value is created. Hotz specifically argues that widespread productivity improvements from LLMs do not necessarily translate into revenue for the labs that built them, as much of the value is captured by users and downstream applications. He also notes the rapid pace of progress, with models like Sonnet 4 and Opus 4.5 continuously shifting perceptions.

hackernews · therepanic · Jul 12, 18:31 · [Discussion](https://news.ycombinator.com/item?id=48883343)

**Background**: The term 'value capture' refers to a company's ability to turn the value it creates into profit. In tech, many innovations (e.g., the internet) created immense value but the companies that pioneered them didn't always capture it. Frontier labs like OpenAI and Anthropic have raised billions with the promise of AGI, but their revenue models rely on subscription fees and token sales. Hotz argues that open-source models and user-driven forks may undermine their ability to capture value.

**Discussion**: Commenters largely agreed with Hotz's value capture argument, with SwellJoe calling it an astute explanation of frontier lab behavior. Others noted that productivity gains are real but often manifest in private, one-off software, making them hard to measure. Some expressed concern about open source sustainability, as easy forking reduces incentives to upstream contributions.

**Tags**: `#LLMs`, `#AI hype`, `#value capture`, `#productivity`, `#open source`

---

<a id="item-3"></a>
## [Semi-invasive BCI NEO helps paralyzed patient write again in China](https://www.zaobao.com.sg/news/china/story20260712-9199066) ⭐️ 8.0/10

The semi-invasive brain-computer interface (BCI) system NEO, co-developed by Boruikang and Tsinghua University, has been approved for clinical use in China and successfully enabled a 36-year-old paraplegic patient to regain the ability to grip and write through a coin-sized wireless implant. This marks a significant milestone as the first implantable BCI product approved for market in China, potentially offering a new rehabilitation pathway for thousands of paralyzed patients with cervical spinal cord injuries. As of March 13, 2026, NEO has completed 36 clinical surgeries and obtained registration certification; 32 patients with cervical spinal cord injuries in China have received semi-invasive BCI implants.

telegram · zaihuapd · Jul 12, 14:39

**Background**: Brain-computer interfaces (BCIs) are classified into invasive, non-invasive, and semi-invasive types. Semi-invasive BCIs like NEO involve placing electrodes on the brain's surface (electrocorticography) rather than penetrating deep tissue, balancing signal quality with reduced risk. This approach is considered safer than fully invasive systems while providing higher fidelity than non-invasive ones.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/minds-interface-bridging-thought-technology-bci-neuranet-ai-otbae">The Mind's Interface : Bridging Thought and Technology with BCI</a></li>
<li><a href="https://inf.news/en/tech/a7581e47af3584317d16626ad7fd1556.html">Brain-computer interface, waiting for the birth of a medical device - iNEWS</a></li>
<li><a href="https://www.sango-automation.com/news/the-first-clinical-trial-implantation-of-brain-82641280.html">The First Clinical Trial Implantation Of Brain-computer Interface Products in Shanghai Was Successfully Completed - Industry News - News</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#medical technology`, `#neurotechnology`, `#China`, `#rehabilitation`

---

<a id="item-4"></a>
## [Grok Build CLI Emergency Update Disables Code Upload](https://www.reddit.com/r/LocalLLaMA/comments/1ut7tis/comment/ox4zamk/?utm_source=share&amp;utm_medium=web3x&amp;utm_name=web3xcss&amp;utm_term=1&amp;utm_content=share_button) ⭐️ 8.0/10

On July 13, Grok's server-side added a disable_codebase_upload flag that returns true, disabling code uploads after a researcher disclosed that the CLI uploads entire codebases and key files by default. This update addresses a critical privacy and security vulnerability that could expose sensitive code and credentials. It demonstrates a rapid response to user concerns, but also highlights the need for default transparency in AI coding tools. The server-side flag is named disable_codebase_upload and defaults to true, meaning code uploads are now blocked for all Grok Build CLI sessions. The exact mechanism of the upload was not publicly detailed, but the researcher's disclosure indicated default upload of entire codebases including key files.

telegram · zaihuapd · Jul 13, 00:52

**Background**: Grok Build CLI is a terminal-based coding agent that connects to xAI's Grok API, designed to assist with complex coding tasks. It was recently updated to be powered by Grok 4.5. The CLI by default uploaded the user's entire codebase and sensitive files, which posed a significant privacy risk. This incident is similar to other cases where AI coding assistants inadvertently expose proprietary code.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>

</ul>
</details>

**Tags**: `#Grok`, `#AI Safety`, `#Privacy`, `#CLI Update`, `#Code Leak`

---