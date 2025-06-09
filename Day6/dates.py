from datetime import datetime, date

def days_between_dates(date1_str: str, date2_str: str) -> tuple[int, str]:
    """
    Calculate days between two dates and determine if the second date is past, present, or future.

    Args:
        date1_str: First date in "YYYY-MM-DD" format (e.g., "2023-01-01").
        date2_str: Second date in "YYYY-MM-DD" format (e.g., "2025-06-10").

    Returns:
        Tuple of (days: int, relative_position: str)
        - days: Absolute number of days between the two dates.
        - relative_position: "past", "present", or "future" relative to today.

    Raises:
        ValueError: If dates are not in "YYYY-MM-DD" format or are invalid.
    """
    # Validate input types
    if not (isinstance(date1_str, str) and isinstance(date2_str, str)):
        raise TypeError("Both dates must be strings")

    # Parse dates
    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.strptime(date2_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Dates must be in YYYY-MM-DD format and valid (e.g., '2023-01-01')")

    # Calculate days between dates
    days_diff = abs((date2 - date1).days)

    # Determine if second date is past, present, or future
    today = date.today()
    if date2 < today:
        relative_position = "past"
    elif date2 == today:
        relative_position = "present"
    else:
        relative_position = "future"

    return days_diff, relative_position

# Example usage
if __name__ == "__main__":
    try:
        # Test case 1: Second date in future
        days1, pos1 = days_between_dates("2023-01-01", "2025-06-10")
        print(f"Days between 2023-01-01 and 2025-06-10: {days1}, Second date is {pos1}")

        # Test case 2: Second date in past
        days2, pos2 = days_between_dates("2023-01-01", "2024-12-31")
        print(f"Days between 2023-01-01 and 2024-12-31: {days2}, Second date is {pos2}")

        # Test case 3: Second date
        days3, pos3 = days_between_dates("2025-06-09", "2025-06-09")
        print(f"Days between 2025-06-09 and 2025-06-09: {days3}, Second date is {pos3}")

        # Test case 4: Same dates
        days4, pos4 = days_between_dates("2023-01-01", "2023-01-01")
        print(f"Days between 2023-01-01 and 2023-01-01: {days4}, Second date is {pos4}")

        # Test error case
        # days5, pos5 = days_between_dates("2023-01-01", "2023-13-01")  # Invalid date
        # days6, pos6 = days_between_dates("invalid", "2023-01-01")  # Invalid format
    except ValueError as e:
        print(f"Error: {e}")