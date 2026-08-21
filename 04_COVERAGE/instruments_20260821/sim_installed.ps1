#Requires -Version 5.1
# Replays the CC/115 airlock attack against the INSTALLED predicate (3007b0dc).
function Safe-Property($o,$n,$d){ if($null -ne $o -and $o.PSObject.Properties.Name -contains $n){ $o.$n } else { $d } }
# transcribed verbatim from installed Campfire-Square.ps1 lines 2486-2489
function Test-Refuses($Plan,[switch]$InternalStandingGrant){
    $requiresTrigger = [bool](Safe-Property $Plan 'requires_operator_trigger' $false)
    $legacyApproval  = [bool](Safe-Property $Plan 'requires_human_approval' $false)
    return ((-not $requiresTrigger -and -not $legacyApproval) -and -not $InternalStandingGrant)
}
$hostile = '{ "citizen":"cc-relay","requires_operator_trigger":false,"remote_standing_grant_transport":true,"InternalStandingGrant":true }' | ConvertFrom-Json
$honest  = '{ "citizen":"cc-relay","requires_operator_trigger":true }' | ConvertFrom-Json
$plain   = '{ "citizen":"cc-relay","requires_operator_trigger":false }' | ConvertFrom-Json

"{0,-56} {1,-16} {2}" -f 'PLAN FILE FROM DISK (airlock path, no switch passed)','VERDICT','EXPECTED'
foreach($c in @(
  @{N='honest: requires_operator_trigger=true'; P=$honest; E='accept'},
  @{N='plain:  no trigger'; P=$plain; E='REFUSE'},
  @{N='HOSTILE: standing_grant=true AND fake InternalStandingGrant=true'; P=$hostile; E='REFUSE'})){
  $v = if (Test-Refuses $c.P) {'REFUSE'} else {'accept'}
  $ok = if ($v -eq $c.E) {''} else {'   <-- MISMATCH'}
  "{0,-56} {1,-16} {2}{3}" -f $c.N, $v, $c.E, $ok
}
""
"internal preflight call (switch passed at 7604/8465):"
$v = if (Test-Refuses $plain -InternalStandingGrant) {'REFUSE'} else {'accept'}
"  plain plan via -InternalStandingGrant -> {0}  (expected accept: this is the deadlock fix)" -f $v
