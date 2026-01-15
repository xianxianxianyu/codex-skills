#!/bin/bash
# Setup taskmaster directory structure (Codex-friendly)
# Creates .taskmaster/ scaffold and optionally copies helper scripts.

set -e

COPY_HELPERS=1
FORCE_COPY=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-copy-helpers) COPY_HELPERS=0; shift ;;
    --force-copy) FORCE_COPY=1; shift ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

echo "Setting up taskmaster directory structure..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUNDLE_SCRIPTS_DIR="$SCRIPT_DIR/../.taskmaster/scripts"

mkdir -p .taskmaster/docs .taskmaster/tasks .taskmaster/reports .taskmaster/scripts .taskmaster/state
echo "OK: created .taskmaster/{docs,tasks,reports,scripts,state}"

# Update .gitignore to exclude taskmaster state files
GITIGNORE_FILE=".gitignore"

ensure_gitignore() {
  if [ -f "$GITIGNORE_FILE" ]; then
    if ! grep -q ".taskmaster/state.json" "$GITIGNORE_FILE" 2>/dev/null; then
      {
        echo ""
        echo "# Taskmaster AI state files"
        echo ".taskmaster/state.json"
        echo ".taskmaster/tasks/"
        echo ".taskmaster/reports/"
      } >> "$GITIGNORE_FILE"
      echo "OK: updated .gitignore"
    else
      echo "OK: .gitignore already configured"
    fi
  else
    {
      echo "# Taskmaster AI state files"
      echo ".taskmaster/state.json"
      echo ".taskmaster/tasks/"
      echo ".taskmaster/reports/"
    } > "$GITIGNORE_FILE"
    echo "OK: created .gitignore"
  fi
}

ensure_gitignore

# Create placeholder README in docs/
if [ ! -f ".taskmaster/docs/README.md" ]; then
  cat > .taskmaster/docs/README.md <<'EOF'
# Taskmaster Documentation

This directory contains project documentation for Taskmaster.

## Files

- `prd.md` - Product Requirements Document (generated)
- `task-hints.md` - Task breakdown suggestions (optional)
- `progress.md` - Execution log (optional)

## Usage

1. Ensure `prd.md` exists with comprehensive requirements
2. Run `taskmaster init` to initialize project
3. Run `taskmaster generate` to generate tasks from PRD

See https://www.task-master.dev/ for documentation.
EOF
  echo "OK: created .taskmaster/docs/README.md"
fi

# Create placeholder config if taskmaster CLI not initialized
if [ ! -f ".taskmaster/config.json" ]; then
  cat > .taskmaster/config.json <<'EOF'
{
  "version": "2.0",
  "project": {
    "name": "Project Name",
    "description": "Project description"
  },
  "ai": {
    "provider": "anthropic",
    "model": "claude-sonnet-4"
  },
  "workflow": {
    "autoGenerate": false,
    "taskFormat": "json"
  }
}
EOF
  echo "OK: created placeholder .taskmaster/config.json"
fi

copy_helpers() {
  if [ "$COPY_HELPERS" -ne 1 ]; then
    return 0
  fi
  if [ ! -d "$BUNDLE_SCRIPTS_DIR" ]; then
    echo "WARN: bundle scripts dir not found: $BUNDLE_SCRIPTS_DIR"
    return 0
  fi
  for f in "$BUNDLE_SCRIPTS_DIR"/*; do
    [ -f "$f" ] || continue
    dest=".taskmaster/scripts/$(basename "$f")"
    if [ -f "$dest" ] && [ "$FORCE_COPY" -ne 1 ]; then
      continue
    fi
    cp -f "$f" "$dest"
  done
  echo "OK: copied helper scripts to .taskmaster/scripts (use --force-copy to overwrite)"
}

copy_helpers

echo ""
echo "Taskmaster directory structure ready!"
echo "Next steps:"
echo "1. Create/update PRD at .taskmaster/docs/prd.md"
echo "2. Run: taskmaster init"
echo "3. Run: taskmaster generate"

