#Requires -Version 5.1
<#
Get-CampfireRelayPaths - read-only relay path witness for Campfire Square.

Answers, from the installed source itself rather than from assumption:
  which relay path variables exist, what they resolve to, and which exist on disk.

WHY: 2026-08-20, the R29 local bootstrap refused with
     "expected exactly one WriteRelay\framework-relay\Ingress directory; found 0"
     because it assumed both apertures ingest the same way. They do not.

READ-ONLY. Parses text and tests paths. Never dot-sources, executes, or mutates
Campfire Square, and never creates a directory.

    SOURCE_TEXT != RUNNING_STATE
    PROSE_ABOUT_CODE != CODE
#>
[CmdletBinding()]
param(
    [string]$SourcePath = (Join-Path $env:USERPROFILE 'OneDrive\Documents\Campfire-Square\App\Campfire-Square.ps1'),
    [string]$Root       = (Join-Path $env:USERPROFILE 'OneDrive\Documents\Campfire-Square')
)

if (-not (Test-Path -LiteralPath $SourcePath)) { throw "Source not found: $SourcePath" }

$sha = (Get-FileHash -LiteralPath $SourcePath -Algorithm SHA256).Hash.ToLower()
Write-Output "SOURCE   $SourcePath"
Write-Output "SHA256   $sha"
Write-Output "ROOT     $Root  (exists: $(Test-Path -LiteralPath $Root))"
Write-Output ""

$lines = Get-Content -LiteralPath $SourcePath -Encoding UTF8
$assign = @{}
$order  = New-Object System.Collections.Generic.List[string]

for ($i = 0; $i -lt $lines.Count; $i++) {
    $m = [regex]::Match($lines[$i], '^\$((?:Cc)?(?:Read|Write)Relay[A-Za-z]*)\s*=\s*(.+)$')
    if (-not $m.Success) { continue }
    $name = $m.Groups[1].Value
    $expr = $m.Groups[2].Value.Trim()
    $assign[$name] = $expr
    $order.Add("$($i+1)`t$name`t$expr")
}

Write-Output "RELAY VARIABLE ASSIGNMENTS IN SOURCE  ($($assign.Count) found)"
foreach ($row in $order) {
    $p = $row -split "`t"
    Write-Output ("  {0,5}  {1,-34} {2}" -f $p[0], $p[1], $p[2])
}
Write-Output ""

# Resolve Join-Path chains textually. No invocation.
function Resolve-RelayExpr([string]$Name, [hashtable]$Table, [int]$Depth = 0) {
    if ($Depth -gt 12) { return $null }
    $expr = $Table[$Name]
    if (-not $expr) { return $null }
    $m = [regex]::Match($expr, "^Join-Path\s+\`$([A-Za-z]+)\s+'([^']+)'$")
    if ($m.Success) {
        $parentName = $m.Groups[1].Value
        $leaf = $m.Groups[2].Value
        if ($parentName -eq 'Root') { return (Join-Path $Root $leaf) }
        $parent = Resolve-RelayExpr $parentName $Table ($Depth + 1)
        if ($parent) { return (Join-Path $parent $leaf) }
        return $null
    }
    return $null
}

Write-Output "RESOLVED DIRECTORY PATHS AND WHETHER THEY EXIST"
$dirVars = $assign.Keys | Where-Object {
    $assign[$_] -match '^Join-Path' -and $_ -notmatch 'Path$'
} | Sort-Object
foreach ($v in $dirVars) {
    $path = Resolve-RelayExpr $v $assign
    if (-not $path) { Write-Output ("  {0,-34} UNRESOLVED  {1}" -f $v, $assign[$v]); continue }
    $exists = Test-Path -LiteralPath $path
    $mark = if ($exists) { 'EXISTS ' } else { 'MISSING' }
    Write-Output ("  {0,-34} {1}  {2}" -f $v, $mark, $path.Replace($Root, '<root>'))
}
Write-Output ""

Write-Output "INGRESS VARIABLES DEFINED (the R29 question)"
$ingress = $assign.Keys | Where-Object { $_ -match 'Ingress' } | Sort-Object
if (-not $ingress) { Write-Output "  none" }
foreach ($v in $ingress) { Write-Output ("  {0,-34} {1}" -f $v, $assign[$v]) }
Write-Output ""

Write-Output "REMOTE INGRESS SURFACES (issue-number constants)"
foreach ($v in ($assign.Keys | Where-Object { $_ -match 'IssueNumber' } | Sort-Object)) {
    Write-Output ("  {0,-34} {1}" -f $v, $assign[$v])
}
Write-Output ""
Write-Output "PER-APERTURE CONFIG (read-only)"
foreach ($ap in @('framework-relay', 'cc-relay')) {
    $cfg = Join-Path $Root "WriteRelay\$ap\config.json"
    if (-not (Test-Path -LiteralPath $cfg)) { Write-Output "  $ap : no config.json"; continue }
    $c = Get-Content -LiteralPath $cfg -Raw -Encoding UTF8 | ConvertFrom-Json
    Write-Output ("  {0,-16} enabled={1,-6} ops={2,-18} top_level_posts={3}" -f `
        $ap, $c.enabled, ($c.allowed_operations -join ','), $c.top_level_posts)
}
