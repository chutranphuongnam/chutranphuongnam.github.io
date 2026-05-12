# Clears cached GitHub HTTPS credentials and sets origin to the Pages repo.
# Run from repo root: powershell -ExecutionPolicy Bypass -File scripts\refresh-github-auth.ps1

$ErrorActionPreference = "Continue"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $repoRoot

Write-Host "=== Git Credential Manager: erase github.com ===" -ForegroundColor Cyan
@"
protocol=https
host=github.com
"@ | & git credential-manager erase

Write-Host "`n=== GCM: GitHub accounts ===" -ForegroundColor Cyan
& git credential-manager github list 2>&1

Write-Host "`n=== cmdkey entries (git / github) ===" -ForegroundColor Cyan
cmdkey /list 2>&1 | Select-String -Pattern "git|GitHub|github" -CaseSensitive:$false

Write-Host "`n=== Set remote origin (chutranphuongnam Pages) ===" -ForegroundColor Cyan
$pagesUrl = "https://github.com/chutranphuongnam/chutranphuongnam.github.io.git"
git remote set-url origin $pagesUrl
git remote -v

Write-Host "`nDone. Next `git push` will prompt login — use account chutranphuongnam (browser or PAT)." -ForegroundColor Green
Write-Host "Then run: git push -u origin main`n" -ForegroundColor Yellow
