def is_leap_year(year):
    """
    Check whether a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4 AND not divisible by 100, OR
    - It is divisible by 400
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Test the function
if __name__ == "__main__":
    test_years = [2000, 2004, 2023, 2024, 1900, 2100]
    
    for year in test_years:
        if is_leap_year(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
