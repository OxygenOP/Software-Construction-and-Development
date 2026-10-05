"""
Week 1 - Task 2 - Independent challenge: Employee Salary Calculator

Input employee name, basic salary and allowance.
gross = basic + allowance; tax = 5% of gross; net = gross - tax.
Marked on construction quality: names, structure, clarity, invalid input.

Skeleton only: the signatures and the questions come from the assignment. The logic is not
written here - implement it, then get it reviewed.
"""


TAX_RATE = 0.05


def read_employee_details():
    # Return (name, basic_salary, allowance). TODO
    raise NotImplementedError


def calculate_gross_salary(basic_salary: float, allowance: float) -> float:
    raise NotImplementedError


def calculate_tax(gross_salary: float, tax_rate: float = TAX_RATE) -> float:
    raise NotImplementedError


def calculate_net_salary(gross_salary: float, tax: float) -> float:
    raise NotImplementedError


def display_salary_slip(name: str, gross: float, tax: float, net: float) -> None:
    raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
