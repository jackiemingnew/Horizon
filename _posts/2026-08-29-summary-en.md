---
layout: default
title: "Horizon Summary: 2026-08-29 (EN)"
date: 2026-08-29
lang: en
---

> From 23 items, 3 important content pieces were selected

---

1. [Simple 100-Year-Old SPC Algorithm Outperforms SOTA Time Series Anomaly Detection](#item-1) ⭐️ 9.0/10
2. [Analysis of 31,352 Hourly LLM Benchmark Scores Reveals 3x Between-Day vs Within-Day Variation](#item-2) ⭐️ 8.0/10
3. [OpenAI Cuts Cursor Model Access by 2026 After SpaceX Acquisition](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Simple 100-Year-Old SPC Algorithm Outperforms SOTA Time Series Anomaly Detection](https://www.reddit.com/r/MachineLearning/comments/1w1wt1s/you_can_beat_sota_time_series_anomaly_detection/) ⭐️ 9.0/10

Eamonn Keogh, a prominent researcher, demonstrated that a simple 100-year-old Statistical Process Control (SPC) algorithm beats state-of-the-art time series anomaly detection methods on the TSB-AD-M benchmark. He called for community introspection on whether recent progress is real or an artifact of trivial benchmarks. This challenges the validity of one of the most widely used benchmarks in the field, affecting how future papers are evaluated and compared. If a century-old method can win, many published results may reflect benchmark flaws rather than algorithmic novelty. SPC achieves perfect results on the shown ECG trace, and Keogh notes that dozens of 'TAO' traces are even easier for SPC to solve. He does not claim his critique applies to every proposed algorithm, but asserts the TSB-AD-M benchmark is too trivial to support strong claims.

reddit · r/MachineLearning · /u/eamonnkeogh · Aug 29, 20:16

**Background**: Statistical Process Control (SPC) is a classic quality-control method that monitors process stability using control charts and control limits, and has existed for about a century. TSB-AD-M is a popular time series anomaly detection benchmark introduced by Paparrizos et al., built from real-world datasets with labeled anomaly ranges. Keogh argues that many TSAD papers evaluate on this benchmark, making its triviality a field-wide issue.

<details><summary>References</summary>
<ul>
<li><a href="https://in.mathworks.com/help/predmaint/ug/industrial-process-anomaly-detection-using-statistical-process-control.html">Industrial Process Anomaly Detection using Statistical ...</a></li>
<li><a href="https://thedatumorg.github.io/TSB-AD/">TSB-AD</a></li>
<li><a href="https://www.emergentmind.com/topics/tsb-ad-m-benchmark">TSB-AD-M: Time Series Anomaly Detection Benchmark</a></li>

</ul>
</details>

**Tags**: `#time-series`, `#anomaly-detection`, `#benchmarks`, `#research-critique`, `#SPC`

---

<a id="item-2"></a>
## [Analysis of 31,352 Hourly LLM Benchmark Scores Reveals 3x Between-Day vs Within-Day Variation](https://www.reddit.com/r/MachineLearning/comments/1w1jp1j/i_analyzed_31352_hourly_llm_benchmark_scores/) ⭐️ 8.0/10

A new analysis of 31,352 hourly LLM benchmark scores across 49 model identifiers found within-day variation of 2.8 points and between-day variation of 8.4 points — roughly three times greater. The study was conducted using AIStupidLevel, a continuous evaluation pipeline that repeatedly tests models on coding, reasoning, tool calling, and canary tasks. This matters because most LLM evaluations are single-point snapshots, and this large-scale empirical analysis shows that day-to-day variation is a much stronger signal for detecting real performance drift than short-term noise. It provides a practical methodology and open-source tooling for continuous model monitoring, which is increasingly important for production LLM systems. The evaluation executes coding responses rather than relying only on model-based judgment, runs tool-calling tests inside isolated Docker environments, and aggregates five repetitions per task to reduce stochastic noise. The detection pipeline uses daily medians and sequential change-point detection, with incidents required to persist beyond historical variance and pass statistical and minimum-effect thresholds before being flagged.

reddit · r/MachineLearning · /u/ionutvi · Aug 29, 11:08

**Background**: LLM benchmarks are typically administered once per model, but recent research (e.g., the 'LLM Stability' paper) shows models can be non-deterministic even at temperature 0, so a single score can be misleading. AIStupidLevel is a MIT-licensed, open-source continuous monitoring platform that repeatedly evaluates models on coding, reasoning, tool use and 'canary' tasks, and tracks drift over time. It currently reports 169,858 benchmark runs, 104,458 measured scores, and 88M+ processed tokens, and also powers an OpenAI-compatible model router.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2408.04667v2">LLM Stability: A detailed analysis with some surprises</a></li>
<li><a href="https://israynotarray.com/en/ai/2026/06/16/aistupidlevel-llm-degradation-monitor/">Is AI Getting Quietly Dumber? AIStupidLevel: A 24-Hour Watchdog for LLM Degradation | Is Ray, Not Array</a></li>
<li><a href="https://huggingface.co/AIStupidLevel">AIStupidLevel (AI Stupid Level)</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#benchmark stability`, `#time series analysis`, `#model monitoring`, `#open-source`

---

<a id="item-3"></a>
## [OpenAI Cuts Cursor Model Access by 2026 After SpaceX Acquisition](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 8.0/10

OpenAI announced it will terminate its agreement to provide OpenAI models to Cursor, with a recommended service discontinuation date of November 12, 2026. The termination follows SpaceX's acquisition of Cursor and OpenAI's stated lack of confidence that SpaceX will comply with the terms of service. This decision directly impacts the AI coding tool ecosystem, as Cursor is a widely used AI-first code editor and relies on OpenAI's models. It also highlights how corporate policy decisions and contract disputes can reshape developer tools and partnerships in the rapidly evolving AI industry. OpenAI's custom agreement with Cursor allows for a time-limited cancellation after a change of control, and the company is using the maximum notice period permitted by the contract. OpenAI cited a history of breaches by Musk's companies, including Twitter's contract violations after its acquisition and xAI's admission earlier this year of violating OpenAI's terms of service.

telegram · zaihuapd · Aug 29, 02:24

**Background**: Cursor is an AI-first code editor built on the VS Code platform, offering features like multi-line edits and AI-assisted code rewriting through models such as OpenAI's. OpenAI is a leading AI research organization that provides API access to its models to third-party developers. The acquisition of Cursor by SpaceX—part of Elon Musk's group of companies—triggers a change-of-control clause in the agreement between OpenAI and Cursor.

<details><summary>References</summary>
<ul>
<li><a href="https://cursor.com/">AI Coding Agent for Building Ambitious Software | Cursor</a></li>
<li><a href="https://www.cursor.com/features">Features | Cursor - The AI -first Code Editor</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Cursor`, `#SpaceX`, `#AI policy`, `#contracts`

---