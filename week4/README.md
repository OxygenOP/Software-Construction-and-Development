# Week 4 — Modularity and Separation of Concerns

**Focus:** From a monolithic program to cohesive Python modules: responsibilities, coupling, dependencies.

## The assignment

A working monolithic Student Marks program (name, three subject marks, validation, total, average,
grade, display — all inside one function) must be restructured into meaningful modules. The marks are
for modularity, separation of concerns, cohesion, coupling and change isolation — **not** merely for
making imports work.

## Required artefacts

| Part | Artefact | Location |
|---|---|---|
| A | Code archaeology: annotate the given code INPUT / VALIDATION / CALCULATION / GRADING / DISPLAY | `CODE_ARCHAEOLOGY.md` |
| B | Responsibility map: for each concern, what it does and where it should live | `RESPONSIBILITY_MAP.md` |
| C | Module design: justify the structure and answer the design questions | `MODULE_DESIGN.md` |
| D | Implementation | `student_marks/` package |
| E | Dependency mapping: diagram plus the coupling questions | `DEPENDENCY_DIAGRAM.md` |
| F | Change request test: which module changes for each of four changes | `CHANGE_REQUEST_TEST.md` |
| G | Verification runs | recorded in `VERIFICATION.md` |
| — | Reflection: five questions | `REFLECTION.md` |

### Part D — required module and function names
```
student_marks/
├── main.py          # coordinates the application
├── validation.py    # validate_mark(mark)
├── calculations.py  # calculate_total(marks), calculate_average(marks), calculate_grade(average)
└── display.py       # display_result(name, total, average, grade)
```
Behaviour must remain unchanged from the original program.

### Part F — the four change requests
1. Grading changes to A ≥ 85, B ≥ 75, C ≥ 65, D ≥ 55 — which module changes?
2. The result format changes — which module changes?
3. The validation message changes — which module changes?
4. Results will later be displayed through a GUI — what must be replaceable without touching
   calculation logic?

### Part G — verification inputs
- Normal marks: 75, 82, 68
- Boundary marks: 50, 60, 70, 80
- Invalid marks: −5 and 105
- A second student with a different result

### Semester project connection
Sketch the semester project's major responsibilities, possible modules and main dependencies. Do not
copy the Student Marks structure mechanically — use the same reasoning.

### Reading
McConnell, *Code Complete* 2e, Chapter 5 (Design in Construction: information hiding, areas likely to
change, loose coupling, cohesion); Chapter 7 as supporting reading.
