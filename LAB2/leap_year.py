def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 400, OR
    - It is divisible by 4 but NOT by 100
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if the year is a leap year, False otherwise
        
    Examples:
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2024)
        True
    """
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def main():
    """Main function to test the leap year checker."""
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year (integer).")


if __name__ == "__main__":
    main()
