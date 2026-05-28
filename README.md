# Cursor Engineering Rules

A modular, opinionated ruleset for [Cursor](https://cursor.sh/) that turns your AI
assistant into a senior software engineer - security-conscious, quality-driven, and
disciplined about risky changes.

Drop these files into any project and Cursor will consistently enforce the same
engineering standards across your entire codebase.

---

## What's Inside

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

## Quick Install

### Option A - Copy into an existing project

```bash
# from your project root
curl -fsSL https://raw.githubusercontent.com/ShadAhammed/cursor-engineering-rules/main/install.sh | bash
```

### Option B - Manual copy

```
.cursorrules
.cursor/
  rules/
    00-core-security.mdc
    10-code-quality.mdc
    20-testing-validation.mdc
    30-data-and-performance.mdc
    40-observability-dependencies.mdc
    50-ai-execution-policy.mdc
```

Copy the above structure into the root of any project and open it in Cursor.

### Option C - Clone and symlink (monorepo / shared setup)

```bash
git clone https://github.com/ShadAhammed/cursor-engineering-rules.git ~/.cursor-rules
# then symlink into each project:
ln -s ~/.cursor-rules/.cursorrules /path/to/your/project/.cursorrules
ln -s ~/.cursor-rules/.cursor      /path/to/your/project/.cursor
```

---

## How It Works

Cursor reads `.cursorrules` and `.cursor/rules/*.mdc` automatically on every session.
Rules marked `alwaysApply: true` are injected into every prompt context regardless of
which file you have open.

The rules are modular by design - you can edit or delete individual `.mdc` files to
match your stack without touching the rest.

---

## Rule Priority

When instructions conflict, this order applies:

1. **Explicit user instruction** for the current task
2. **Security and irreversible-change safeguards** (`00-core-security`, `50-ai-execution-policy`)
3. **Other project rules** in numeric filename order

---

## Change Classification

The execution policy (`50-ai-execution-policy.mdc`) requires the AI to classify every
task before acting:

| Class | Examples | AI Behavior |
|---|---|---|
| **Lightweight** | Small fixes, refactors, Q&A | Implement directly |
| **Standard** | Feature additions, multi-file changes | Staged implementation with lint/type/test |
| **Critical** | Architecture, security, schema, infra, cost | Plan → risks → rollback → wait for approval |

---

## Customization

These rules are designed to be a starting point, not a straitjacket.

- **Add a language-specific rule:** create a new `.mdc` with a `globs` pattern, e.g.
  `globs: **/*.py` for Python-only guidance.
- **Relax a rule:** edit the relevant `.mdc` file and add a project-specific exception.
- **Disable a rule entirely:** delete the `.mdc` file or set `alwaysApply: false`.

---

## Contributing

Issues and PRs are welcome. If you have a rule that has saved you from a bad deploy or
a security incident, consider sharing it here.

---

## License

MIT - free to use, modify, and distribute. See [LICENSE](LICENSE).

---

*Built by [Abu Shad Ahammed](https://github.com/ShadAhammed)*
