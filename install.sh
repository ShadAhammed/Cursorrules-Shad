#!/usr/bin/env bash
# Installs cursor-engineering-rules into the current directory.
set -e

REPO="https://raw.githubusercontent.com/ShadAhammed/cursor-engineering-rules/main"
RULES_DIR=".cursor/rules"

mkdir -p "$RULES_DIR"

echo "Downloading .cursorrules..."
curl -fsSL "$REPO/.cursorrules" -o .cursorrules

for file in \
  00-core-security.mdc \
  10-code-quality.mdc \
  20-testing-validation.mdc \
  30-data-and-performance.mdc \
  40-observability-dependencies.mdc \
  50-ai-execution-policy.mdc
do
  echo "Downloading $file..."
  curl -fsSL "$REPO/.cursor/rules/$file" -o "$RULES_DIR/$file"
done

echo ""
echo "Done. Cursor engineering rules installed into $(pwd)"
echo "Restart Cursor to activate."
