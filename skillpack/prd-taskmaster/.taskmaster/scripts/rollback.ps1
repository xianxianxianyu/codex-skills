[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)][int]$TaskId
)

Continue = 'Stop'

$tag = "checkpoint-task-$TaskId"
$tags = git tag -l
if ($LASTEXITCODE -ne 0) { throw "git tag failed; is this a git repo?" }
if (-not ($tags -contains $tag)) {
  Write-Error "Checkpoint tag '$tag' not found. Available checkpoints:"
  git tag -l "checkpoint-task-*" | Sort-Object
  exit 1
}

Write-Host "Rolling back to $tag..." -ForegroundColor Yellow
Write-Host "This will discard all changes after Task $TaskId and preserve current work in a backup branch." -ForegroundColor Yellow
$confirm = Read-Host "Continue? (yes/no)"
if ($confirm -ne 'yes') { Write-Host "Rollback cancelled." -ForegroundColor DarkYellow; exit 0 }

$ts = Get-Date -Format 'yyyyMMdd-HHmmss'
$backupBranch = "rollback-backup-$ts"

git checkout -b $backupBranch | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Failed to create backup branch: $backupBranch" }

$null = git show-ref --verify --quiet refs/heads/main
$targetBranch = if ($LASTEXITCODE -eq 0) { 'main' } else { 'master' }
git checkout $targetBranch | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Failed to checkout $targetBranch" }

git reset --hard $tag | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Failed to reset to $tag" }

Write-Host "OK: rolled back to Task $TaskId ($tag)" -ForegroundColor Green
Write-Host "Backup branch: $backupBranch" -ForegroundColor Green

$progressPath = Join-Path (Join-Path '.taskmaster' 'docs') 'progress.md'
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $progressPath) | Out-Null

$log = @(
  '',
  '---',
  '## ROLLBACK PERFORMED',
  "**Timestamp**: $(Get-Date -AsUTC -Format \"yyyy-MM-dd HH:mm:ss 'UTC'\")",
  "**Rolled back to**: Task $TaskId ($tag)",
  "**Backup branch**: $backupBranch",
  '**Reason**: User-initiated rollback',
  '',
  "Tasks after $TaskId discarded. Ready to resume from Task $TaskId.",
  '---',
  ''
)
Add-Content -LiteralPath $progressPath -Value ($log -join "`r`n") -Encoding UTF8

Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1) Resume from Task $($TaskId + 1)" -ForegroundColor Cyan
Write-Host "  2) Review backup: git checkout $backupBranch" -ForegroundColor Cyan
