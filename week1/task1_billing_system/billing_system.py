"""
Week 1 - Task 1 - Guided lab: Simple Billing System

Input product name, price and quantity. Subtotal = price x quantity,
discount = 10% of subtotal, final amount = subtotal - discount.
Expected output for Keyboard / 2500 / 2: subtotal 5000, discount 500, final 4500.

Skeleton only: the signatures and the questions come from the assignment. The logic is not
written here - implement it, then get it reviewed.
"""


def get_product_name() -> str:
    # Return the product name typed by the user. TODO
    raise NotImplementedError


def get_price() -> float:
    # Return the price. Decide what happens for a negative price or a non-numeric entry,
    # and write that decision down - it is part of the mark. TODO
    raise NotImplementedError


def get_quantity() -> int:
    # Return the quantity. Consider zero and negative values. TODO
    raise NotImplementedError


def calculate_subtotal(price: float, quantity: int) -> float:
    raise NotImplementedError


def calculate_discount(subtotal: float, rate: float = 0.10) -> float:
    raise NotImplementedError


def calculate_final_amount(subtotal: float, discount: float) -> float:
    raise NotImplementedError


def display_receipt(product, price, quantity, subtotal, discount, final_amount) -> None:
    # Print in exactly the shape the lab sheet shows. TODO
    raise NotImplementedError


def main() -> None:
    # Coordinate the steps above. No calculations of its own. TODO
    raise NotImplementedError


if __name__ == "__main__":
    main()
