# Week 2 — Writing Good Functions

**Focus:** One function, one responsibility: cohesion, names, parameters, returns, side effects.

## What this week asks for

### 1. Guided lab — refactor a student result program (`student_result.py`)
Starting point is the supplied single function that calculates a total, an average, decides a grade,
prints the result and appends to a file.

1. List every responsibility inside that function
2. Propose better names for each responsibility
3. Extract the calculation and decision logic into their own functions
4. Move presentation/output into a separate responsibility
5. Run the program after each change and verify the result is unchanged
6. Commit the improved version

**Deliverable:** `student_result.py` containing clearly named, cohesive functions — the file name and
the function names are part of the mark.

### 2. Independent challenge — Employee Salary Calculator (`salary_calculator.py`)
Inputs: employee name, basic salary, allowance, tax rate.

Required functions, by name:
- `calculate_gross_salary()`
- `calculate_tax()`
- `calculate_net_salary()`

Plus a written justification of why those responsibilities and function boundaries were chosen.

### 3. Semester project
Finalise the group and the project, and prepare a short proposal (`PROJECT_PROPOSAL.md`):
title, problem, users, 4–6 core features, group members.

### Self-check before submitting
Clear meaningful purpose · name describes the purpose · one primary responsibility · strong cohesion ·
meaningful and necessary parameters · appropriate return value · no unnecessary or hidden side effects ·
length justified by design · easy to understand and reuse · easy to test independently.
