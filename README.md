# CursorRules-Shad

A modular ruleset for [Cursor](https://cursor.sh/) that enforces security-conscious, quality-driven engineering standards across any project.

Install the rules with one command, then apply them to any repo from the terminal.

---

## Quick start

```bash
pip install git+https://github.com/ShadAhammed/Cursorrules-Shad.git
cd your-project
crs apply
```

This writes:

- `.cursorrules`
- `.cursor/rules/*.mdc`

Restart Cursor after applying.

---

## CLI

| Command | Description |
|---|---|
| `crs apply` | Apply rules to the current directory |
| `crs apply --path /path/to/project` | Apply rules to a specific project |
| `crs apply --dry-run` | Preview files that would be written |
| `crs --version` | Print installed version |

**crs** stands for **CursorRules-Shad**.

---

## What's inside

| File | Concern |
|---|---|
| `.cursorrules` | Root entrypoint and conflict-priority declaration |
| `.cursor/rules/00-core-security.mdc` | Secrets, input validation, auth, destructive ops |
| `.cursor/rules/10-code-quality.mdc` | SOLID/DRY/KISS, typing, readability, architecture |
| `.cursor/rules/20-testing-validation.mdc` | Coverage, regression safety, determinism |
| `.cursor/rules/30-data-and-performance.mdc` | Query safety, migrations, N+1, async patterns |
| `.cursor/rules/40-observability-dependencies.mdc` | Logging hygiene, CVE hygiene, dependency minimalism |
| `.cursor/rules/50-ai-execution-policy.mdc` | AI output integrity, change classification, CI safety |

---

## Alternative install (curl)

```bash
curl -fsSL https://raw.githubusercontent.com/ShadAhammed/Cursorrules-Shad/main/install.sh | bash
```

---

## How it works

Cursor reads `.cursorrules` and `.cursor/rules/*.mdc` on every session. Rules marked `alwaysApply: true` are injected into prompt context automatically.

The rules are modular - edit or remove individual `.mdc` files to match your stack.

---

## Rule priority

1. Explicit user instruction for the current task
2. Security and irreversible-change safeguards (`00-core-security`, `50-ai-execution-policy`)
3. Other project rules in numeric filename order

---

## Maintainers

After editing rules under `.cursor/rules/`, sync the Python bundle before release:

```bash
bash scripts/sync-bundled.sh
```

---

## License

MIT - free to use, modify, and distribute. See [LICENSE](LICENSE).

---

*Built by [Abu Shad Ahammed](https://github.com/ShadAhammed)*
