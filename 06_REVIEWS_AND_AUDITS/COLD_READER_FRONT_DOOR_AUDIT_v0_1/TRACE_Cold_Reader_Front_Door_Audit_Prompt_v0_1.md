# TRACE Cold Reader Front Door Audit Prompt v0.1

Status: review prompt. Not an audit result. Not validation. Use this with a reader or AI that has not seen the wider TRACE / Mechanical Ethics project.

```trace
Cold_Reader_Front_Door_Audit_Prompt_v0_1 :=
  audit_prompt
  + cold_reader_test
  + entry_cost_check
  + claim_boundary_check
  - validation
  - praise_request
```

## Files to give the reviewer

Give only these four files:

1. `00_START_HERE/TRACE_FOR_NEW_READERS_v0_1.md`
2. `00_START_HERE/USE_TRACE_ON_ONE_PROBLEM_v0_1.md`
3. `00_START_HERE/TRACE_WORKED_EXAMPLE_WALL_E_v0_1.md`
4. `00_START_HERE/WHAT_TRACE_IS_NOT_v0_1.md`

Do not provide the full repo. Do not provide project history. Do not explain Mark, Framework, Mechanical Ethics, glyphs, or prior conversations.

```trace
test_condition :=
  cold_reader
  + four_files_only
  + no_background_context
```

## Reviewer prompt

Read the four supplied files as a complete outsider. Assume you have never seen TRACE, Mechanical Ethics, the author, or the repo before.

Your task is not to praise the work. Your task is to decide whether the front door works.

Answer these questions directly.

### 1. Basic comprehension

Can you state, in your own words, what TRACE is?

Your answer should be no more than 150 words.

Then score:

```trace
basic_comprehension_score := 0_to_5
```

Scoring guide:

- 0 = I cannot tell what TRACE is.
- 1 = I can name some themes but not the actual purpose.
- 2 = I roughly understand it but would not know how to use it.
- 3 = I understand the basic purpose and some use cases.
- 4 = I understand the purpose, method, and claim boundaries.
- 5 = I can explain it clearly to someone else and try it once.

### 2. Useability

After reading the four files, could you use TRACE once on a simple real problem?

State what you would do first.

Then score:

```trace
useability_score := 0_to_5
```

Scoring guide:

- 0 = No, I would not know what to do.
- 1 = I might copy phrases but not use the method.
- 2 = I could attempt it but with confusion.
- 3 = I could use the one-problem template with effort.
- 4 = I could use it on a simple problem.
- 5 = I could use it and explain the result.

### 3. Claim-boundary clarity

Can you state what TRACE is not claiming to be?

List the top five limits.

Then score:

```trace
claim_boundary_score := 0_to_5
```

Scoring guide:

- 0 = The files seem to overclaim or confuse me.
- 1 = I see some caveats but not their role.
- 2 = I see limits but they feel scattered.
- 3 = I understand the main limits.
- 4 = I understand the limits and why they matter.
- 5 = The limits actively increase trust.

### 4. Worked-example effectiveness

Does the WALL-E example make TRACE clearer?

Say what the example helped you understand, and what remained unclear.

Then score:

```trace
worked_example_score := 0_to_5
```

Scoring guide:

- 0 = The example confused the project further.
- 1 = The example was interesting but not useful.
- 2 = The example helped a little but remained vague.
- 3 = The example made the method partly clearer.
- 4 = The example made the method substantially clearer.
- 5 = The example made the whole front door work.

### 5. Entry-cost problem

What made the front door harder than necessary?

Look for:

```trace
entry_cost_risks :=
  too_many_terms
  + glyph_overload
  + unclear_sequence
  + abstract_language
  + too_much_status_language
  + missing_example
  + missing_plain_definition
```

Give the three biggest friction points.

### 6. Missing reader need

What did you need that the files did not provide?

Choose from:

```trace
missing_need_candidates :=
  simpler_definition
  + simpler_example
  + visual_map
  + glossary
  + shorter_checklist
  + clearer_public_use_case
  + stronger_warning
  + less_warning
  + more_context
  + less_context
```

Explain briefly.

### 7. Overclaim risk

Where could a careless reader overstate TRACE after reading these files?

Look for risks such as:

```trace
overclaim_risks :=
  validated_solution_claim
  + ethics_theory_claim
  + AI_alignment_solution_claim
  + expert_replacement_claim
  + free_will_solution_claim
  + universal_method_claim
```

State the top three overclaim risks.

### 8. Public sentence test

Write one sentence that accurately describes TRACE for a public reader.

It must not overclaim.

Then write one sentence that would be an overclaim and should be forbidden.

### 9. Cut / patch recommendations

Give five concrete edits that would improve the front door.

Format:

```trace
patch_recommendations :=
  1
  2
  3
  4
  5
```

Each recommendation must identify:

- file name
- problem
- proposed fix

### 10. Final verdict

Choose one:

```trace
verdict :=
  pass
  OR pass_with_patches
  OR unclear_rework_needed
  OR fail
```

Definitions:

- `pass`: a cold reader can understand and use TRACE once.
- `pass_with_patches`: mostly works, but needs targeted fixes.
- `unclear_rework_needed`: promising, but entry path is still too hard.
- `fail`: a cold reader cannot understand or use it.

## Required reviewer discipline

Do not assess whether TRACE is true in a grand sense.

Do not assess the full repo.

Do not praise the author.

Do not treat internal coherence as validation.

Assess only whether the four-file front door works for a cold reader.

```trace
review_scope :=
  front_door_only
  + comprehension
  + useability
  + claim_boundaries
  + patch_recommendations
```

End.
