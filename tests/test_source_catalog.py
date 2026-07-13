import json
from pathlib import Path

from src.models import SourcesConfig


CATALOG_PATH = Path(__file__).parents[1] / "docs" / "data" / "source-catalog.json"


def load_catalog() -> dict:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def build_sources_config(catalog_sources: list[dict]) -> dict:
    result: dict = {}
    github = []
    rss = []
    reddit = []
    telegram = []

    for source in catalog_sources:
        config = source["config"]
        if source["type"] == "rss":
            rss.append(
                {
                    "name": config["name"],
                    "url": config["url"],
                    "enabled": True,
                    "category": config.get("category"),
                }
            )
        elif source["type"] == "github_repo":
            github.append(
                {
                    "type": "repo_releases",
                    "owner": config["owner"],
                    "repo": config["repo"],
                    "enabled": True,
                    "category": config.get("category"),
                }
            )
        elif source["type"] == "hackernews":
            result["hackernews"] = config
        elif source["type"] == "reddit_subreddit":
            reddit.append({**config, "enabled": True})
        elif source["type"] == "telegram":
            telegram.append({**config, "enabled": True})

    if github:
        result["github"] = github
    if rss:
        result["rss"] = rss
    if reddit:
        result["reddit"] = {
            "enabled": True,
            "subreddits": reddit,
            "users": [],
            "fetch_comments": 10,
        }
    if telegram:
        result["telegram"] = {"enabled": True, "channels": telegram}

    return result


def test_source_catalog_has_unique_ids_and_known_levels():
    sources = load_catalog()["sources"]
    source_ids = [source["id"] for source in sources]

    assert len(source_ids) == len(set(source_ids))
    assert {source["source_level"] for source in sources} <= {"L1", "L2", "L3"}
    assert all(source["homepage"].startswith("https://") for source in sources)


def test_source_catalog_exports_valid_horizon_sources_config():
    sources = load_catalog()["sources"]

    parsed = SourcesConfig.model_validate(build_sources_config(sources))

    assert any(source.name == "Linux.DO Top" for source in parsed.rss)
    assert parsed.hackernews.enabled is True
    assert {source.repo for source in parsed.github} >= {"vllm", "sglang"}
    assert {source.subreddit for source in parsed.reddit.subreddits} >= {
        "MachineLearning",
        "LocalLLaMA",
    }
