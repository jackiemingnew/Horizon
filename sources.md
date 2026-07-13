---
layout: default
title: 数据源配置器
permalink: /sources/
---

<link rel="stylesheet" href="{{ '/assets/css/source-configurator.css' | relative_url }}">

<div class="source-page-intro">
  <p class="source-page-eyebrow">SOURCE WORKBENCH</p>
  <h1>数据源配置器</h1>
  <p class="source-page-lead">从已核对的官方源、专业分析和社区入口中组合自己的 Horizon 信息流。所有选择只在当前浏览器中处理，不会上传配置或凭据。</p>
</div>

<div
  id="source-configurator"
  class="source-configurator"
  data-catalog-url="{{ '/data/source-catalog.json' | relative_url }}"
>
  <section class="source-research-note" aria-labelledby="source-research-title">
    <div>
      <p class="source-section-kicker">调研快照</p>
      <h2 id="source-research-title">先看出处，再决定是否采集</h2>
      <p>本目录综合了 Horizon Hub、公开 fork 的真实配置和社区常用信息流。L1 / L2 / L3 表示离原始事件的距离，不是准确率评分。</p>
    </div>
    <dl class="source-research-stats" aria-label="数据源调研统计">
      <div><dt>Hub 记录</dt><dd id="hub-record-count">—</dd></div>
      <div><dt>已整理</dt><dd id="catalog-source-count">—</dd></div>
      <div><dt>抽样 forks</dt><dd id="fork-sample-count">—</dd></div>
      <div><dt>核对日期</dt><dd id="catalog-verified-date">—</dd></div>
    </dl>
  </section>

  <section class="source-level-guide" aria-label="信息源层级说明">
    <div><span class="source-level source-level-l1">L1 直接源</span><p>官方项目、公司、维护者、研究机构或期刊的直接发布。</p></div>
    <div><span class="source-level source-level-l2">L2 分析源</span><p>专业作者或媒体对一手材料的报道、解释与判断。</p></div>
    <div><span class="source-level source-level-l3">L3 发现源</span><p>社区、排行、讨论和聚合，用来发现线索并回溯原文。</p></div>
  </section>

  <section class="source-filter-bar" aria-labelledby="source-filter-title">
    <h2 id="source-filter-title" class="source-visually-hidden">筛选数据源</h2>
    <label class="source-search-field">
      <span>搜索</span>
      <input id="source-search" type="search" placeholder="名称、说明或出处" autocomplete="off">
    </label>
    <label>
      <span>分类</span>
      <select id="source-category-filter"><option value="">全部分类</option></select>
    </label>
    <label>
      <span>层级</span>
      <select id="source-level-filter">
        <option value="">全部层级</option>
        <option value="L1">L1 直接源</option>
        <option value="L2">L2 分析源</option>
        <option value="L3">L3 发现源</option>
      </select>
    </label>
    <div class="source-filter-status">
      <span id="source-result-count" role="status" aria-live="polite">正在载入…</span>
      <button id="source-reset-filters" class="source-button source-button-quiet" type="button" hidden>重置筛选</button>
    </div>
  </section>

  <div id="source-load-error" class="source-error" role="alert" hidden>
    <h2>数据源目录载入失败</h2>
    <p>请确认页面通过本地服务器或 GitHub Pages 打开，并检查目录 JSON 是否可访问。</p>
  </div>

  <div class="source-workbench">
    <main aria-labelledby="source-catalog-title">
      <div class="source-catalog-heading">
        <div>
          <p class="source-section-kicker">候选目录</p>
          <h2 id="source-catalog-title">选择要采集的数据源</h2>
        </div>
        <button id="source-clear-selection" class="source-button source-button-quiet" type="button" disabled>清空选择</button>
      </div>
      <div id="source-catalog" class="source-catalog" aria-busy="true"></div>
      <div id="source-empty-filter" class="source-empty" role="status" hidden>
        <h3>没有匹配的数据源</h3>
        <p>换一个关键词或重置筛选条件。</p>
      </div>
    </main>

    <aside class="source-config-panel" aria-labelledby="source-config-title">
      <div class="source-config-heading">
        <div>
          <p class="source-section-kicker">导出配置</p>
          <h2 id="source-config-title">已选 <span id="source-selected-count">0</span> 个</h2>
        </div>
        <span class="source-local-only">仅本地</span>
      </div>
      <div id="source-selected-summary" class="source-selected-summary">
        <p>勾选左侧数据源后，这里会生成 Horizon 可识别的 <code>sources</code> 配置。</p>
      </div>
      <div class="source-code-header">
        <span>config.sources.json</span>
        <span>JSON</span>
      </div>
      <pre class="source-config-preview" tabindex="0"><code id="source-config-output">{
  "sources": {}
}</code></pre>
      <p class="source-config-help">这是局部配置。请审阅后，将 <code>sources</code> 合并到现有 <code>data/config.json</code>；页面不会直接修改仓库。</p>
      <div class="source-config-actions">
        <button id="source-copy-config" class="source-button source-button-secondary" type="button" disabled>复制 JSON</button>
        <button id="source-download-config" class="source-button source-button-primary" type="button" disabled>下载配置</button>
      </div>
      <p id="source-action-status" class="source-action-status" role="status" aria-live="polite"></p>
    </aside>
  </div>
</div>

<script src="{{ '/assets/js/source-configurator.js' | relative_url }}" defer></script>
