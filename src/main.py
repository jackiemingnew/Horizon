"""CLI entry point for Horizon."""

import argparse
import asyncio
from datetime import datetime, timezone
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from .storage.manager import ConfigError, StorageManager
from .orchestrator import HorizonOrchestrator, SourceQualityRunError
from .mcp.run_store import RunStore


console = Console()


def _persist_configuration_failure(
    artifact_store: RunStore | None,
    run_id: str | None,
) -> None:
    """Write the safe V2 failure envelope without echoing validation details."""
    if artifact_store is None or run_id is None:
        return
    manifest = {
        "schema_version": "1",
        "run_id": run_id,
        "status": "failed",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "healthy_source_ratio": 0.0,
        "source_counts": {
            "success": 0,
            "empty": 0,
            "partial": 0,
            "failed": 0,
            "skipped": 0,
        },
        "pipeline_counts": {},
        "failed_source_ids": [],
        "failed_stages": ["configuration"],
        "token_usage": None,
    }
    artifact_store.save_source_health(run_id, [])
    artifact_store.save_decisions(run_id, [])
    artifact_store.save_model_calls(run_id, [])
    artifact_store.save_manifest(run_id, manifest)
    artifact_store.update_meta(run_id, manifest)


def print_banner():
    """Print the application banner."""
    banner = r"""
[bold blue]
  _    _            _
 | |  | |          (_)
 | |__| | ___  _ __ _ ___  ___  _ __
 |  __  |/ _ \| '__| |_  / / _ \| '_ \
 | |  | | (_) | |  | |/ / | (_) | | | |
 |_|  |_|\___/|_|  |_/___| \___/|_| |_|
[/bold blue]
[cyan]  AI-Driven Information Aggregation System[/cyan]
    """
    console.print(banner)


def build_parser() -> argparse.ArgumentParser:
    """Build the backward-compatible CLI parser."""
    parser = argparse.ArgumentParser(description="Horizon - AI-Driven Information Aggregation System")
    parser.add_argument("--hours", type=int, help="Force fetch from last N hours")
    parser.add_argument(
        "--config", type=Path, help="Load a config file instead of data/config.json"
    )
    parser.add_argument(
        "--save-stages",
        action="store_true",
        help="Persist local pipeline stages and the V2 audit contract under data/runs/",
    )
    parser.add_argument(
        "--run-id", help="Use an explicit safe run ID for reproducible automation"
    )
    parser.add_argument(
        "--no-pages",
        action="store_true",
        help="Do not write docs/_posts; useful for local and CI shadow runs",
    )
    return parser


def main():
    """Main CLI entry point."""
    print_banner()

    args = build_parser().parse_args()

    try:
        # Load environment variables from .env file
        load_dotenv()

        # Ensure we're in the project directory or use data/ in current dir
        data_dir = Path("data")

        # Initialize storage manager
        storage = StorageManager(data_dir=str(data_dir))
        if args.config is not None:
            storage.config_path = args.config
        artifact_store = RunStore(data_dir / "runs") if args.save_stages else None
        run_id = args.run_id
        if artifact_store is not None:
            removed_runs = artifact_store.prune_runs(older_than_days=14)
            if removed_runs:
                console.print(
                    f"[dim]Pruned {len(removed_runs)} local run(s) older than 14 days.[/dim]"
                )
            run_id = artifact_store.create_run(run_id)
            console.print(
                f"[cyan]Local run artifacts:[/cyan] "
                f"{artifact_store.run_dir(run_id).resolve()}\n"
            )

        # Load configuration
        try:
            config = storage.load_config()
        except FileNotFoundError:
            _persist_configuration_failure(artifact_store, run_id)
            console.print("[bold red]❌ Configuration file not found![/bold red]\n")
            data_dir_path = data_dir if isinstance(data_dir, Path) else Path(data_dir)
            example_path = data_dir_path / "config.example.json"
            if example_path.exists():
                console.print(
                    f"Copy the example config and edit it:\n"
                    f"  [cyan]cp {example_path} {data_dir_path / 'config.json'}[/cyan]\n"
                )
            console.print(
                "Or run [bold cyan]uv run horizon-wizard[/bold cyan] to launch the interactive setup wizard.\n"
            )
            sys.exit(2 if artifact_store is not None else 1)
        except ConfigError as e:
            _persist_configuration_failure(artifact_store, run_id)
            console.print(f"[bold red]❌ Error loading configuration: {e}[/bold red]")
            sys.exit(2 if artifact_store is not None else 1)
        except Exception as e:
            _persist_configuration_failure(artifact_store, run_id)
            console.print(f"[bold red]❌ Error loading configuration: {e}[/bold red]")
            sys.exit(2 if artifact_store is not None else 1)

        # Create and run orchestrator
        orchestrator = HorizonOrchestrator(config, storage)
        outcome = asyncio.run(
            orchestrator.run(
                force_hours=args.hours,
                artifact_store=artifact_store,
                artifact_run_id=run_id,
                publish_pages=not args.no_pages,
            )
        )
        if outcome is not None and outcome.status == "partial":
            failed = [
                result.source_id
                for result in outcome.source_results
                if result.status.value in {"failed", "partial"}
            ]
            console.print(
                "[yellow]::warning::Horizon V2 completed partially; failed sources: "
                + ", ".join(failed)
                + "[/yellow]"
            )
        elif outcome is not None and outcome.status == "empty":
            console.print(
                "[yellow]::warning::Horizon V2 completed with an empty digest; "
                "all enabled sources were healthy.[/yellow]"
            )

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Interrupted by user[/yellow]")
        sys.exit(0)
    except SourceQualityRunError as e:
        console.print(f"\n[bold red]❌ {e}[/bold red]")
        sys.exit(e.exit_code)
    except Exception as e:
        console.print(f"\n[bold red]❌ Fatal error: {e}[/bold red]")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def print_config_template():
    """Print configuration template."""
    template = """
{
  "version": "1.0",
  "ai": {
    "provider": "anthropic",
    "model": "claude-sonnet-4.5-20250929",
    "api_key_env": "ANTHROPIC_API_KEY",
    "temperature": 0.3,
    "max_tokens": 4096
  },
  "sources": {
    "github": [
      {
        "type": "user_events",
        "username": "torvalds",
        "enabled": true
      }
    ],
    "hackernews": {
      "enabled": true,
      "fetch_top_stories": 30,
      "min_score": 100
    },
    "rss": [
      {
        "name": "Example Blog",
        "url": "https://example.com/feed.xml",
        "enabled": true,
        "category": "software-engineering"
      }
    ]
  },
  "filtering": {
    "ai_score_threshold": 7.0,
    "time_window_hours": 24,
    "max_items": null,
    "category_groups": {},
    "default_group": "other",
    "default_group_limit": null
  }
}

Also create a .env file with:
ANTHROPIC_API_KEY=your_api_key_here
GITHUB_TOKEN=your_github_token_here (optional but recommended)
"""
    console.print(template)


if __name__ == "__main__":
    main()
