# Week 3 — Writing Understandable Code

**Focus:** Boolean clarity, deep nesting, guard clauses, control-flow complexity, refactoring safely.

## What this week asks for

### 1. Practical exercise — refactor deep nesting (`refactor_nesting.py`)
Given a working program with 4–5 levels of nesting: refactor it using guard clauses and/or meaningful
helper functions, **without changing required behaviour**.

Run the original and the refactored version with the same inputs, then record in a comment block or
companion note: what changed, why it is clearer, and how you verified behaviour is preserved.

### 2. Practical exercise — simplify a business rule (`bonus_eligibility.py`)
Implement an employee bonus eligibility rule. Conditions: active employee, at least 12 months of
service, performance rating ≥ 4, no disciplinary action, attendance ≥ 90%.

1. Write a working version first
2. Refactor the Boolean logic for readability
3. Extract a function if that makes the rule easier to understand
4. Test normal, boundary and failing cases

### 3. Independent challenge — refactor access control (`check_access_refactor.py`)
The supplied `check_access(user, resource)` is deeply nested. Refactor it without changing behaviour,
and be ready to explain the design decisions.

### 4. Semester project
Proposal and group submission.

### 5. Reading
McConnell, *Code Complete* 2e, Chapter 19 (19.1 Boolean Expressions, 19.2 Compound Statements,
19.4 Taming Dangerously Deep Nesting, 19.5 Structured Programming, 19.6 Control Structures and
Complexity), plus Chapter 11 on names and a review of Chapter 7.

Be prepared to explain one example from the reading that made code easier to understand.

### Useful reminder
Refactoring changes internal structure without intentionally changing observable behaviour. Understand
the code first, change it second, compare results third.
