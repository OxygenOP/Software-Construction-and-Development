"""
Week 2 - Task 1 - Guided lab: refactor the student result program

Start from the single process_student function in the Week 2 deck. Paste it in first as the
'before' version, list every responsibility it mixes, then split it into the functions below.
This file name is the required deliverable.

Skeleton only: the signatures and the questions come from the assignment. The logic is not
written here - implement it, then get it reviewed.
"""


# BEFORE: paste the original process_student function from the deck here, unchanged, so the
# refactor has a baseline you can run and compare against.
# Responsibilities I found in it: (list them)


def calculate_total(marks) -> float:
    raise NotImplementedError


def calculate_average(marks) -> float:
    raise NotImplementedError


def determine_grade(average: float) -> str:
    # Grade bands exactly as in the original program. TODO
    raise NotImplementedError


def display_result(name: str, total: float, average: float, grade: str) -> None:
    raise NotImplementedError


def save_result(name: str, grade: str, path: str = "results.txt") -> None:
    # The original appended to a file. Keep that behaviour, but keep it out of the
    # calculation functions - that separation is the point of the exercise. TODO
    raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
