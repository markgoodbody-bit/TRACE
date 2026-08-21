#Requires -Version 5.1
<#
Test-ReviewedPostNormalizer - regression cases for the reviewed-POST deadlock.

FW/R29-POST-PATH-UNREACHABLE-20260820-001 established, by two live refusals,
that a reviewed remote POST cannot reach /api/post. CC/111 extended the scope:
the same deadlock exists on the CC lane. FW's condition for a third attempt is
that the normalizer is repaired AND both refusal cases are regression-tested.
These are those cases, for BOTH lanes.

STATIC CONTRACT TEST. It reads the exact installed source as text and asserts
the composition. It does not dot-source or execute Campfire Square.

    SOURCE_CONTRACT_TEST != RUNTIME_TEST

T1/T2 assert today's deadlock and MUST PASS now - they prove the harness fires.
T3/T4 assert the repaired contract and MUST FAIL now - they are the regression.
A run where T3/T4 pass before any repair means this file is broken, not fixed.
#>
[CmdletBinding()]
param(
    [string]$SourcePath = (Join-Path $env:USERPROFILE 'OneDrive\Documents\Campfire-Square\App\Campfire-Square.ps1'),
    [string]$ExpectedSha256 = '97f4905b53973d625cfd254db74775cb372b90aa46bb4a91eae019d8964bd9e2'
)

$src  = Get-Content -LiteralPath $SourcePath -Raw -Encoding UTF8
$sha  = (Get-FileHash -LiteralPath $SourcePath -Algorithm SHA256).Hash.ToLower()
$results = New-Object System.Collections.Generic.List[object]

function Add-Case([string]$Id, [string]$Name, [bool]$Ok, [string]$Detail, [string]$ExpectNow) {
    $results.Add([pscustomobject]@{
        Id = $Id; Name = $Name; Result = if ($Ok) { 'PASS' } else { 'FAIL' }
        ExpectedNow = $ExpectNow; Detail = $Detail
    })
}

Write-Output "SOURCE  $SourcePath"
Write-Output "SHA256  $sha"
Write-Output "PINNED  $ExpectedSha256"
if ($sha -ne $ExpectedSha256) {
    Write-Output "NOTE: source has moved from the pinned head; results describe the CURRENT file."
}
Write-Output ""

# --- the validator predicate that both lanes must satisfy -------------------
$validatorRequires = $src -match [regex]::Escape("Plan must explicitly require a local execution trigger")
Add-Case 'T1' 'Validate-PlanShape still demands a local execution trigger' `
    $validatorRequires 'the gate that refuses; must not be weakened by any repair' 'PASS'

# --- each lane's virtual-plan builder ---------------------------------------
foreach ($lane in @(
    @{ Id='FW'; Fn='New-RemoteRoutineVirtualPlan';   Boundary=7526 },
    @{ Id='CC'; Fn='New-CcRemoteRoutineVirtualPlan'; Boundary=8487 }
)) {
    $pattern = "(?s)function\s+$([regex]::Escape($lane.Fn))\b.*?\n\}"
    $m = [regex]::Match($src, $pattern)
    if (-not $m.Success) {
        Add-Case "T2-$($lane.Id)" "$($lane.Fn) located" $false 'function not found' 'PASS'
        continue
    }
    $body = $m.Value
    $setsFalse = $body -match 'requires_operator_trigger\s*=\s*\$false'
    $setsTrue  = $body -match 'requires_operator_trigger\s*=\s*\$true'

    Add-Case "T2-$($lane.Id)" "$($lane.Fn) currently hardcodes `$false (the deadlock)" `
        $setsFalse 'documents the defect; flips to FAIL once repaired' 'PASS'

    Add-Case "T3-$($lane.Id)" "REPAIRED: $($lane.Fn) installs the local trigger requirement" `
        $setsTrue 'normalizer must install it; caller must never assert it' 'FAIL'
}

# --- the caller must not be able to assert the local-only field --------------
$envelopeRejects = $src -match 'unknown field' -or $src -match 'REQUEST_REFUSED'
Add-Case 'T4a' 'Request envelope still refuses unknown fields' $envelopeRejects `
    'remote caller must not gain authority over a local-only field' 'PASS'

$schemaLeak = $src -match "'requires_operator_trigger'\s*,|,\s*'requires_operator_trigger'"
Add-Case 'T4b' 'requires_operator_trigger absent from any public request schema' (-not $schemaLeak) `
    'adding it to the schema would make the path pass for the wrong reason' 'PASS'

# --- the contradiction CC/114 found -----------------------------------------
$declaresNoTrigger = ([regex]::Matches($src,'human_operator_trigger_required_for_post\s*=\s*\$false')).Count
Add-Case 'T5' 'lanes declaring human_operator_trigger_required_for_post=$false' `
    ($declaresNoTrigger -eq 0) `
    "found $declaresNoTrigger; while Validate-PlanShape demands a trigger. If the repair sets `$true, these must change or the response contradicts its own plan." `
    'FAIL'

# --- report ------------------------------------------------------------------
$fmt = "{0,-7} {1,-6} {2,-9} {3}"
Write-Output ($fmt -f 'CASE','RESULT','EXPECTED','NAME')
foreach ($r in $results) {
    $flag = if ($r.Result -eq $r.ExpectedNow) { '' } else { '   <-- UNEXPECTED' }
    Write-Output ($fmt -f $r.Id, $r.Result, $r.ExpectedNow, ($r.Name + $flag))
    if ($r.Detail) { Write-Output ("        " + $r.Detail) }
}
Write-Output ""
$unexpected = @($results | Where-Object { $_.Result -ne $_.ExpectedNow })
if ($unexpected.Count -eq 0) {
    Write-Output "HARNESS_CONSISTENT: every case matched its pre-repair expectation."
    Write-Output "The T3 cases are the regression. They must flip to PASS when the"
    Write-Output "normalizer is repaired, and T1/T4 must stay PASS."
    exit 0
}
Write-Output "HARNESS_INCONSISTENT: $($unexpected.Count) case(s) did not match expectation."
exit 1
