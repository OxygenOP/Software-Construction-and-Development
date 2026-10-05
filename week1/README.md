# Week 1 — Introduction to Software Construction

**Focus:** What makes software good: correct, readable, maintainable, testable, robust.

## What this week asks for

### 1. Guided lab — Simple Billing System (`billing_system.py`)
Input: product name, price, quantity. Then subtotal = price × quantity, discount = 10% of subtotal,
final amount = subtotal − discount.

Required output shape, for the worked example:

```
Product: Keyboard
Price: 2500
Quantity: 2
Subtotal: 5000
Discount: 500
Final Amount: 4500
```

Then review your own code against: meaningful variable names, readability, duplicated logic,
calculations separated from input/output, clear output, and what happens when price is negative,
quantity is zero, or the user types something that is not a number.

### 2. Independent challenge — Employee Salary Calculator (`employee_salary_calculator.py`)
Input: employee name, basic salary, allowance.
- gross salary = basic salary + allowance
- tax = 5% of gross salary
- net salary = gross salary − tax

Construction requirements: meaningful names, readable code, no unnecessary duplication, functions
used where appropriate, clear output, invalid input considered, logical organisation.

Note the assessment wording: **you are marked on how the solution is constructed, not only on whether
the final numbers are correct.**

### 3. Git
Repository, commit, history — `git init`, `git add`, `git commit`. Branching and merging come later
in the semester.

### 4. Semester project
Library Management System introduced. Nothing to build yet; it evolves every week.
