"""Command-line interface for CursorRules-Shad."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from crs import __version__
from crs.apply import apply_rules


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="crs",
        description="CursorRules-Shad - apply engineering rules to a project.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"crs {__version__}",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    apply_cmd = sub.add_parser(
        "apply",
        help="Copy .cursorrules and .cursor/rules into a project.",
    )
    apply_cmd.add_argument(
        "--path",
        type=Path,
        default=Path.cwd(),
        help="Project directory to update (default: current directory).",
    )
    apply_cmd.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be written without modifying files.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the ``crs`` CLI and return an exit code."""
    args = _build_parser().parse_args(argv)

    if args.command == "apply":
        try:
            result = apply_rules(args.path, dry_run=args.dry_run)
        except (FileNotFoundError, NotADirectoryError, OSError) as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1

        if args.dry_run:
            print(f"Dry run - would write to: {result.target}")
            print(f"  {result.cursorrules_path}")
            for path in result.rule_files:
                print(f"  {path}")
            return 0

        print(f"Applied CursorRules-Shad to: {result.target}")
        print(f"  {result.cursorrules_path.name}")
        for path in result.rule_files:
            print(f"  .cursor/rules/{path.name}")
        print("Restart Cursor to activate the new rules.")
        return 0

    print(f"Unknown command: {args.command}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
