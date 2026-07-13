(function () {
  "use strict";

  const root = document.getElementById("source-configurator");
  if (!root) return;

  const elements = {
    catalog: document.getElementById("source-catalog"),
    search: document.getElementById("source-search"),
    category: document.getElementById("source-category-filter"),
    level: document.getElementById("source-level-filter"),
    resetFilters: document.getElementById("source-reset-filters"),
    resultCount: document.getElementById("source-result-count"),
    emptyFilter: document.getElementById("source-empty-filter"),
    loadError: document.getElementById("source-load-error"),
    clearSelection: document.getElementById("source-clear-selection"),
    selectedCount: document.getElementById("source-selected-count"),
    selectedSummary: document.getElementById("source-selected-summary"),
    configOutput: document.getElementById("source-config-output"),
    copyConfig: document.getElementById("source-copy-config"),
    downloadConfig: document.getElementById("source-download-config"),
    actionStatus: document.getElementById("source-action-status"),
    hubCount: document.getElementById("hub-record-count"),
    catalogCount: document.getElementById("catalog-source-count"),
    forkCount: document.getElementById("fork-sample-count"),
    verifiedDate: document.getElementById("catalog-verified-date")
  };

  const typeLabels = {
    rss: "RSS",
    github_repo: "GitHub Release",
    github_user: "GitHub User",
    hackernews: "Hacker News",
    reddit_subreddit: "Reddit",
    telegram: "Telegram"
  };

  const levelLabels = {
    L1: "L1 直接源",
    L2: "L2 分析源",
    L3: "L3 发现源"
  };

  let sources = [];
  const selectedIds = new Set();

  function normalize(value) {
    return String(value || "").trim().toLocaleLowerCase();
  }

  function appendTextElement(parent, tag, className, text) {
    const element = document.createElement(tag);
    if (className) element.className = className;
    element.textContent = text;
    parent.appendChild(element);
    return element;
  }

  function makeChip(text, className) {
    const chip = document.createElement("span");
    chip.className = className;
    chip.textContent = text;
    return chip;
  }

  function createSourceCard(source) {
    const card = document.createElement("article");
    card.className = "source-card";
    card.dataset.sourceId = source.id;

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.id = `source-${source.id}`;
    checkbox.checked = selectedIds.has(source.id);
    checkbox.setAttribute("aria-describedby", `source-description-${source.id}`);

    const label = document.createElement("label");
    label.className = "source-card-body";
    label.htmlFor = checkbox.id;

    const content = document.createElement("div");
    content.className = "source-card-content";

    const topLine = document.createElement("div");
    topLine.className = "source-card-topline";
    appendTextElement(topLine, "h3", "source-card-title", source.name);
    topLine.appendChild(makeChip(levelLabels[source.source_level], `source-level source-level-${source.source_level.toLowerCase()}`));
    content.appendChild(topLine);

    const description = appendTextElement(content, "p", "source-card-description", source.description);
    description.id = `source-description-${source.id}`;

    const meta = document.createElement("div");
    meta.className = "source-card-meta";
    meta.appendChild(makeChip(typeLabels[source.type] || source.type, "source-meta-chip"));
    meta.appendChild(makeChip(source.language, "source-meta-chip"));
    meta.appendChild(makeChip(source.category, "source-meta-chip"));
    meta.appendChild(makeChip(`出处：${source.origin}`, "source-origin-chip"));
    content.appendChild(meta);

    if (source.caveat) {
      appendTextElement(content, "p", "source-card-caveat", `注意：${source.caveat}`);
    }

    label.appendChild(content);

    const link = document.createElement("a");
    link.className = "source-card-link";
    link.href = source.homepage;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.textContent = "查看原始站点";
    link.setAttribute("aria-label", `查看 ${source.name} 原始站点（新窗口）`);

    checkbox.addEventListener("change", function () {
      if (checkbox.checked) selectedIds.add(source.id);
      else selectedIds.delete(source.id);
      updateConfiguration();
    });

    card.append(checkbox, label, link);
    return card;
  }

  function getFilteredSources() {
    const query = normalize(elements.search.value);
    const category = elements.category.value;
    const level = elements.level.value;

    return sources.filter(function (source) {
      const searchable = normalize([
        source.name,
        source.description,
        source.category,
        source.origin,
        source.language,
        typeLabels[source.type] || source.type
      ].join(" "));
      return (!query || searchable.includes(query)) &&
        (!category || source.category === category) &&
        (!level || source.source_level === level);
    });
  }

  function renderCatalog() {
    const filtered = getFilteredSources();
    const fragment = document.createDocumentFragment();
    filtered.forEach(function (source) {
      fragment.appendChild(createSourceCard(source));
    });

    elements.catalog.replaceChildren(fragment);
    elements.catalog.setAttribute("aria-busy", "false");
    elements.emptyFilter.hidden = filtered.length > 0;
    elements.resultCount.textContent = `显示 ${filtered.length} / ${sources.length} 个`;
    elements.resetFilters.hidden = !(
      elements.search.value || elements.category.value || elements.level.value
    );
  }

  function selectedSources() {
    return sources.filter(function (source) {
      return selectedIds.has(source.id);
    });
  }

  function buildSourcesConfig(items) {
    if (!items.length) return { sources: {} };

    const result = {};
    const github = [];
    const rss = [];
    const reddit = [];
    const telegram = [];
    let hackernews = null;

    items.forEach(function (source) {
      const config = source.config;
      if (source.type === "rss") {
        rss.push({
          name: config.name,
          url: config.url,
          enabled: true,
          category: config.category
        });
      } else if (source.type === "github_repo") {
        github.push({
          type: "repo_releases",
          owner: config.owner,
          repo: config.repo,
          enabled: true,
          category: config.category
        });
      } else if (source.type === "github_user") {
        github.push({
          type: "user_events",
          username: config.username,
          enabled: true,
          category: config.category
        });
      } else if (source.type === "hackernews") {
        hackernews = {
          enabled: true,
          fetch_top_stories: config.fetch_top_stories,
          min_score: config.min_score,
          category: config.category
        };
      } else if (source.type === "reddit_subreddit") {
        reddit.push({
          subreddit: config.subreddit,
          enabled: true,
          sort: config.sort,
          time_filter: config.time_filter,
          fetch_limit: config.fetch_limit,
          min_score: config.min_score,
          category: config.category
        });
      } else if (source.type === "telegram") {
        telegram.push({
          channel: config.channel,
          enabled: true,
          fetch_limit: config.fetch_limit,
          category: config.category
        });
      }
    });

    if (github.length) result.github = github;
    if (hackernews) result.hackernews = hackernews;
    if (rss.length) result.rss = rss;
    if (reddit.length) {
      result.reddit = {
        enabled: true,
        subreddits: reddit,
        users: [],
        fetch_comments: 10
      };
    }
    if (telegram.length) {
      result.telegram = {
        enabled: true,
        channels: telegram
      };
    }

    return { sources: result };
  }

  function updateSelectedSummary(items) {
    if (!items.length) {
      elements.selectedSummary.replaceChildren();
      appendTextElement(
        elements.selectedSummary,
        "p",
        "",
        "勾选左侧数据源后，这里会生成 Horizon 可识别的 sources 配置。"
      );
      return;
    }

    const counts = items.reduce(function (accumulator, source) {
      const label = typeLabels[source.type] || source.type;
      accumulator[label] = (accumulator[label] || 0) + 1;
      return accumulator;
    }, {});

    const list = document.createElement("ul");
    list.className = "source-selected-groups";
    Object.keys(counts).sort().forEach(function (label) {
      appendTextElement(list, "li", "", `${label} × ${counts[label]}`);
    });
    elements.selectedSummary.replaceChildren(list);
  }

  function updateConfiguration() {
    const items = selectedSources();
    const config = buildSourcesConfig(items);
    const configText = JSON.stringify(config, null, 2);
    const hasSelection = items.length > 0;

    elements.selectedCount.textContent = String(items.length);
    elements.configOutput.textContent = configText;
    elements.copyConfig.disabled = !hasSelection;
    elements.downloadConfig.disabled = !hasSelection;
    elements.clearSelection.disabled = !hasSelection;
    elements.actionStatus.textContent = "";
    updateSelectedSummary(items);
  }

  async function copyConfiguration() {
    const text = elements.configOutput.textContent;
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(text);
      } else {
        const temporary = document.createElement("textarea");
        temporary.value = text;
        temporary.setAttribute("readonly", "");
        temporary.style.position = "fixed";
        temporary.style.opacity = "0";
        document.body.appendChild(temporary);
        temporary.select();
        const copied = document.execCommand("copy");
        temporary.remove();
        if (!copied) throw new Error("copy command failed");
      }
      elements.actionStatus.textContent = "配置已复制。";
    } catch (_error) {
      elements.actionStatus.textContent = "复制失败，请从上方预览中手动复制。";
    }
  }

  function downloadConfiguration() {
    const blob = new Blob([elements.configOutput.textContent + "\n"], {
      type: "application/json;charset=utf-8"
    });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "horizon-sources.json";
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
    elements.actionStatus.textContent = "配置已生成并下载。";
  }

  function populateCategoryFilter() {
    const categories = Array.from(new Set(sources.map(function (source) {
      return source.category;
    }))).sort(function (left, right) {
      return left.localeCompare(right, "zh-CN");
    });

    categories.forEach(function (category) {
      const option = document.createElement("option");
      option.value = category;
      option.textContent = category;
      elements.category.appendChild(option);
    });
  }

  function bindEvents() {
    elements.search.addEventListener("input", renderCatalog);
    elements.category.addEventListener("change", renderCatalog);
    elements.level.addEventListener("change", renderCatalog);
    elements.resetFilters.addEventListener("click", function () {
      elements.search.value = "";
      elements.category.value = "";
      elements.level.value = "";
      renderCatalog();
      elements.search.focus();
    });
    elements.clearSelection.addEventListener("click", function () {
      selectedIds.clear();
      renderCatalog();
      updateConfiguration();
    });
    elements.copyConfig.addEventListener("click", copyConfiguration);
    elements.downloadConfig.addEventListener("click", downloadConfiguration);
  }

  async function initialize() {
    try {
      const response = await fetch(root.dataset.catalogUrl, { credentials: "same-origin" });
      if (!response.ok) throw new Error(`catalog request failed: ${response.status}`);
      const catalog = await response.json();
      if (!catalog || !Array.isArray(catalog.sources)) throw new Error("invalid catalog format");

      sources = catalog.sources;
      elements.hubCount.textContent = String(catalog.meta.horizon_hub_records);
      elements.catalogCount.textContent = String(sources.length);
      elements.forkCount.textContent = String(catalog.meta.forks_sampled);
      elements.verifiedDate.textContent = catalog.meta.last_verified;

      populateCategoryFilter();
      bindEvents();
      renderCatalog();
      updateConfiguration();
    } catch (_error) {
      elements.catalog.setAttribute("aria-busy", "false");
      elements.resultCount.textContent = "目录不可用";
      elements.loadError.hidden = false;
      elements.catalog.hidden = true;
    }
  }

  initialize();
})();
