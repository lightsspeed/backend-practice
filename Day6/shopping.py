
def generate_receipt(items: list, discount_percentage: float = 10.0, discount_threshold: float = 10.0) -> dict:
    """
    Generate a receipt with subtotal, discount, and final total for a list of items.

    Args:
        items: List of tuples, each with (item_name: str, price: float/int).
        discount_percentage: Percentage discount to apply if subtotal > threshold (default 10.0).
        discount_threshold: Subtotal threshold for discount eligibility (default 10.0).

    Returns:
        Dictionary with:
            - items: List of input items
            - subtotal: Sum of prices (rounded to 2 decimals)
            - discount: Discount amount (rounded to 2 decimals)
            - total: Final total after discount (rounded to 2 decimals)

    Raises:
        ValueError: If inputs are invalid (e.g., non-string item names, negative prices).
    """
    # Validate inputs
    if not isinstance(items, list):
        raise ValueError("Items must be a list")
    if not isinstance(discount_percentage, (int, float)) or discount_percentage < 0:
        raise ValueError("Discount percentage must be a non-negative number")
    if not isinstance(discount_threshold, (int, float)) or discount_threshold < 0:
        raise ValueError("Discount threshold must be a non-negative number")

    # Validate each item
    for item in items:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Each item must be a tuple of (name, price)")
        name, price = item
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")

    # Calculate subtotal
    subtotal = sum(price for _, price in items)
    subtotal = round(subtotal, 2)

    # Calculate discount
    discount = 0.0
    if subtotal > discount_threshold:
        discount = round(subtotal * (discount_percentage / 100), 2)

    # Calculate final total
    total = round(subtotal - discount, 2)

    # Return receipt dictionary
    return {
        "items": items,
        "subtotal": subtotal,
        "discount": discount,
        "total": total
    }

# Example usage
if __name__ == "__main__":
    try:
        # Test case 1: Subtotal > $10, discount applies
        items1 = [("apple", 1.50), ("bread", 2.00), ("milk", 3.25), ("cheese", 4.50)]
        receipt1 = generate_receipt(items1)
        print("Receipt 1:")
        print(f"Items: {receipt1['items']}")
        print(f"Subtotal: ${receipt1['subtotal']:.2f}")
        print(f"Discount: ${receipt1['discount']:.2f}")
        print(f"Total: ${receipt1['total']:.2f}")

        # Test case 2: Subtotal <= $10, no discount
        items2 = [("apple", 8.50), ("bread", 2.00)]
        receipt2 = generate_receipt(items2)
        print("\nReceipt 2:")
        print(f"Items: {receipt2['items']}")
        print(f"Subtotal: ${receipt2['subtotal']:.2f}")
        print(f"Discount: ${receipt2['discount']:.2f}")
        print(f"Total: ${receipt2['total']:.2f}")

        # Test case 3: Empty list
        items3 = []
        receipt3 = generate_receipt(items3)
        print("\nReceipt 3:")
        print(f"Items: {receipt3['items']}")
        print(f"Subtotal: ${receipt3['subtotal']:.2f}")
        print(f"Discount: ${receipt3['discount']:.2f}")
        print(f"Total: ${receipt3['total']:.2f}")

        # Test error case
        # items4 = [("apple", -1.50)]  # Raises ValueError
        # receipt4 = generate_receipt(items4)
    except ValueError as e:
        print(f"Error: {e}")
