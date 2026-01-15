[CmdletBinding()]
param(
  [switch]$CopyHelperScripts = $true,
  [switch]$ForceCopy
)

Continue = 'Stop'

Write-Host "Setting up Taskmaster directory structure..." -ForegroundColor Cyan

$projectRoot = (Get-Location).Path
$taskmasterDir = Join-Path $projectRoot '.taskmaster'
$docsDir = Join-Path $taskmasterDir 'docs'
$tasksDir = Join-Path $taskmasterDir 'tasks'
$reportsDir = Join-Path $taskmasterDir 'reports'
$scriptsDir = Join-Path $taskmasterDir 'scripts'
$stateDir = Join-Path $taskmasterDir 'state'

New-Item -ItemType Directory -Force -Path $docsDir, $tasksDir, $reportsDir, $scriptsDir, $stateDir | Out-Null
Write-Host "OK: .taskmaster/ docs/ tasks/ reports/ scripts/ state/" -ForegroundColor Green

# Update .gitignore
$gitignorePath = Join-Path $projectRoot '.gitignore'
$entries = @(
  '# Taskmaster AI state files',
  '.taskmaster/state.json',
  '.taskmaster/tasks/',
  '.taskmaster/reports/'
)

if (Test-Path $gitignorePath) {
  $existing = Get-Content -Raw -LiteralPath $gitignorePath
  if ($existing -notmatch [regex]::Escape('.taskmaster/state.json')) {
    Add-Content -LiteralPath $gitignorePath -Value "" -Encoding UTF8
    Add-Content -LiteralPath $gitignorePath -Value ($entries -join "`r`n") -Encoding UTF8
    Write-Host "OK: updated .gitignore" -ForegroundColor Green
  } else {
    Write-Host "OK: .gitignore already configured" -ForegroundColor DarkGreen
  }
} else {
  Set-Content -LiteralPath $gitignorePath -Value ($entries -join "`r`n") -Encoding UTF8
  Write-Host "OK: created .gitignore" -ForegroundColor Green
}

# Create docs/README.md
$docsReadme = Join-Path $docsDir 'README.md'
if (-not (Test-Path $docsReadme)) {
  $readme = @(
    '# Taskmaster Documentation',
    '',
    'This directory contains project documentation for Taskmaster.',
    '',
    '## Files',
    '',
    '- `prd.md` - Product Requirements Document (generated)',
    '- `task-hints.md` - Task breakdown suggestions (optional)',
    '- `progress.md` - Execution log (optional)',
    '',
    '## Usage',
    '',
    '1. Ensure `prd.md` exists with comprehensive requirements',
    '2. Run `taskmaster init` to initialize project',
    '3. Run `taskmaster generate` to generate tasks from PRD',
    '',
    'See https://www.task-master.dev/ for documentation.'
  )
  Set-Content -LiteralPath $docsReadme -Value $readme -Encoding UTF8
  Write-Host "OK: created .taskmaster/docs/README.md" -ForegroundColor Green
}

# Create placeholder config
$configPath = Join-Path $taskmasterDir 'config.json'
if (-not (Test-Path $configPath)) {
  $config = @(
    '{',
    '  "version": "2.0",',
    '  "project": {',
    '    "name": "Project Name",',
    '    "description": "Project description"',
    '  },',
    '  "ai": {',
    '    "provider": "anthropic",',
    '    "model": "claude-sonnet-4"',
    '  },',
    '  "workflow": {',
    '    "autoGenerate": false,',
    '    "taskFormat": "json"',
    '  }',
    '}'
  )
  Set-Content -LiteralPath $configPath -Value ($config -join "`r`n") -Encoding UTF8
  Write-Host "OK: created placeholder .taskmaster/config.json" -ForegroundColor Green
}

if ($CopyHelperScripts) {
  $bundleScripts = Join-Path $PSScriptRoot '..\.taskmaster\scripts'
  if (Test-Path $bundleScripts) {
    Get-ChildItem -File -LiteralPath $bundleScripts | ForEach-Object {
      $dest = Join-Path $scriptsDir $_.Name
      if ((Test-Path $dest) -and (-not $ForceCopy)) { return }
      Copy-Item -LiteralPath $_.FullName -Destination $dest -Force
    }
    Write-Host "OK: copied helper scripts to .taskmaster/scripts (use -ForceCopy to overwrite)" -ForegroundColor Green
  } else {
    Write-Host "WARN: bundle scripts not found at $bundleScripts" -ForegroundColor Yellow
  }
}

Write-Host ""
Write-Host "Taskmaster scaffolding ready." -ForegroundColor Cyan
Write-Host "Next: create/update .taskmaster/docs/prd.md, then run taskmaster init + taskmaster generate." -ForegroundColor Cyan
