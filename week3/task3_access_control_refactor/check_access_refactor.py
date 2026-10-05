"""
Week 3 - Task 3 - Independent challenge: refactor access control

The supplied check_access(user, resource) is deeply nested. Refactor it without changing
behaviour, and be ready to explain the design decisions.

Skeleton only: the signatures and the questions come from the assignment. The logic is not
written here - implement it, then get it reviewed.
"""


# ORIGINAL: paste the supplied nested version here as the baseline.


def check_access(user, resource) -> bool:
    # Rules to preserve exactly: an admin is allowed; otherwise the owner is allowed;
    # otherwise a public resource is allowed; a missing user or resource is denied. TODO
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: build the truth table for the original, then show the refactor matches it.
    pass
