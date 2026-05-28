"""Copy bundled Cursor rules into a target project directory."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from importlib import resources
from pathlib import Path


@dataclass(frozen=True)
class ApplyResult:
    """Summary of files written by ``crs apply``."""

    target: Path
    cursorrules_path: Path
    rule_files: tuple[Path, ...]


def bundled_root() -> Path:
    """Return the directory containing shipped rule templates."""
    with resources.as_file(resources.files("crs") / "bundled") as bundled:
        return Path(bundled)


def apply_rules(target_dir: Path, *, dry_run: bool = False) -> ApplyResult:
    """
    Install ``.cursorrules`` and ``.cursor/rules/*.mdc`` into ``target_dir``.

    Existing files with the same names are overwritten.
    """
    target = target_dir.resolve()
    if not target.is_dir():
        raise NotADirectoryError(f"Target is not a directory: {target}")

    bundled = bundled_root()
    rules_src = bundled / "rules"
    rules_dst = target / ".cursor" / "rules"
    cursorrules_src = bundled / ".cursorrules"
    cursorrules_dst = target / ".cursorrules"

    if not cursorrules_src.is_file():
        raise FileNotFoundError(f"Missing bundled entrypoint: {cursorrules_src}")

    rule_sources = sorted(rules_src.glob("*.mdc"))
    if not rule_sources:
        raise FileNotFoundError(f"No rule files found in: {rules_src}")

    if dry_run:
        return ApplyResult(
            target=target,
            cursorrules_path=cursorrules_dst,
            rule_files=tuple(rules_dst / src.name for src in rule_sources),
        )

    rules_dst.mkdir(parents=True, exist_ok=True)
    shutil.copy2(cursorrules_src, cursorrules_dst)

    written: list[Path] = []
    for src in rule_sources:
        dst = rules_dst / src.name
        shutil.copy2(src, dst)
        written.append(dst)

    return ApplyResult(
        target=target,
        cursorrules_path=cursorrules_dst,
        rule_files=tuple(written),
    )
