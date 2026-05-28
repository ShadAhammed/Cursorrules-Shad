#!/usr/bin/env bash
# Sync repo rule files into the crs Python package bundle.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUNDLED="$ROOT/crs/bundled"

mkdir -p "$BUNDLED/rules"
cp "$ROOT/.cursorrules" "$BUNDLED/.cursorrules"
cp "$ROOT/.cursor/rules/"*.mdc "$BUNDLED/rules/"

echo "Synced rules into $BUNDLED"
