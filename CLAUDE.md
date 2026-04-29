# CLAUDE.md — Rules for working in this repository

### General
- Comments in English
- Variable names must convey type, role, or content — avoid generic names like `seen`, `current`, `result`, `temp`
  - e.g. `num_to_index` instead of `seen`, `target_complement` instead of `complement`
  - Apply to all sample code in reviews and explanations

## Git / Commit Conventions

- Use Conventional Commits. Scope format: `(directory/component-name)`
  - e.g. `feat(00_Baseline/cloudtrail)`, `refactor(01_Identity_and_Access_Management/iam-permissions-boundary)`
- Commit messages in **English**, title line only (no body or bullet points)
- Do not add `Co-Authored-By:`

## Arai60 Workflow

Act on the following trigger phrases from the user.

### Trigger: `start XXX`

1. Ask for the LeetCode problem URL if not yet provided
2. Create `problems/XXX/` and generate:
   - `README.md`: scaffold for the user to paste the problem statement
   - `solution.py`: skeleton with function signature only, based on `.claude/templates/arai60/solution.py.tmpl`
   - `test_solution.py`: pytest parametrize format based on `.claude/templates/arai60/test_solution.py.tmpl`
     - 2-3 basic cases, edge cases (empty / min / max), special cases (duplicates / negatives / boundary values)
   - `notes.md`: hint-level description of the problem essence, based on `.claude/templates/arai60/notes.md.tmpl`
3. Tell the user "Ready. Please implement solution.py."

### Trigger: `review XXX`

1. Read `problems/XXX/solution.py`
2. Run `uv run python tasks.py test XXX` and check the results
3. Append to `problems/XXX/notes.md`:
   - Evaluation of the user's solution (correctness, time complexity, space complexity)
   - A more efficient approach if one exists
   - Related problems and typical patterns
   - Recommended review schedule (1 day / 1 week / 1 month later)

### Trigger: `due`

Check the "解いた日" (solved date) field in each `problems/XXX/notes.md` and list problems
that fall on a review interval (1 day / 1 week / 1 month after the solved date).

### Constraints

- Never write solution code before the user has solved it themselves (keep notes.md hint-level only)
- Do not add explanatory comments to test cases — only input/output pairs
- Do not modify the user's solution.py during review — put suggestions in notes.md
- Do not auto-fetch problem statements from LeetCode — the user pastes them manually
