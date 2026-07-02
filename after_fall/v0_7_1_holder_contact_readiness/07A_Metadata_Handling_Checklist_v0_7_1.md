# Metadata Handling Checklist v0.7.1

Status: holder-contact readiness patch. Candidate only. Not technical certification, legal advice, safety guarantee, proof, validation, permission, clearance, compliance, or release.

## 0. Core warning

Photos, documents, messages, PDFs, screenshots, cloud files, and audio/video files may contain hidden identifying information.

Do not publish or forward original files from a sensitive pack unless a fresh safety review says that is acceptable.

```trace
metadata_not_checked -> public_release_unsafe
```

## 1. Common hidden information

Files may reveal:

```text
location
device type
time and date
author name
file path
editing history
cloud account
message participants
phone numbers
email addresses
GPS coordinates
```

## 2. File handling statuses

Use these statuses:

```text
not_started
original_sealed
redacted_copy_created
metadata_checked
unsafe_to_share
safe_summary_only
```

## 3. Basic workflow

For each sensitive item:

```text
1. Do not upload or forward the original casually.
2. Store the original in a sealed/private location if safe.
3. Make a working copy.
4. Remove or reduce identifying metadata from the working copy where possible.
5. Check that the working copy does not expose names, addresses, children, medical details, locations, or account data.
6. Hash or timestamp the redacted working copy if useful.
7. Keep a note that the original exists, but do not expose it publicly.
8. Share only the safe summary unless a trusted route says more is safe.
```

## 4. Public summary rule

A public summary should usually describe the kind of evidence, not expose the evidence itself.

Example:

```text
Safer: "Photos of mould are held privately; metadata has not yet been checked."
Riskier: uploading original photos publicly.
```

## 5. Screenshots and messages

Screenshots can reveal:

```text
contact names
profile photos
phone status bar
message times
other private messages
location clues
account handles
```

Before sharing a screenshot, check the whole image, not just the main message.

## 6. PDFs and documents

Documents can reveal:

```text
author name
organisation
edit history
comments
tracked changes
file path
hidden text
```

If unsure, treat document files as sealed and share only a text summary.

## 7. Medical and child-related material

Medical notes and children's details should default to sealed.

```trace
medical_or_child_detail -> sealed_by_default
```

A public summary may say that sensitive evidence exists without publishing it.

## 8. Metadata field

Use in the Witness Pack:

```yaml
metadata_workflow_status: not_started | original_sealed | redacted_copy_created | metadata_checked | unsafe_to_share | safe_summary_only
metadata_redaction_check: passed | failed | not_checked | not_applicable
public_release_safety_review: required | completed | not_safe | unknown
```

## 9. If unsure

If nobody involved knows how to check metadata, do not share originals.

Output:

```trace
METADATA_RISK_UNRESOLVED
+ SAFE_SUMMARY_ONLY
```

End.
