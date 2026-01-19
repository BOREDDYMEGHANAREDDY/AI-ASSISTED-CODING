def is_armstrong(num):
    """
    Check whether a number is an Armstrong number (narcissistic number).
    An Armstrong number is equal to the sum of its own digits each raised 
    to the power of the number of digits.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is an Armstrong number, False otherwise
    """
    # Convert to string to get number of digits
    num_str = str(abs(num))
    num_digits = len(num_str)
    
    # Calculate sum of each digit raised to the power of number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Compare with the original number
    return sum_of_powers == abs(num)


# Test cases
if __name__ == "__main__":
    test_cases = [
        (153, True),
        (370, True),
        (123, False),
        (9474, True),
        (1634, True),
        (100, False),
        (0, True),
        (9, True)
    ]
    
    for num, expected in test_cases:
        result = is_armstrong(num)
        status = "Armstrong Number" if result else "Not an Armstrong Number"
        print(f"Input: {num} → {status}")
    
    # Examples from request
    print("\n--- Examples from request ---")
    print(f"Input: 153 → {'Armstrong Number' if is_armstrong(153) else 'Not an Armstrong Number'}")
    print(f"Input: 370 → {'Armstrong Number' if is_armstrong(370) else 'Not an Armstrong Number'}")
    print(f"Input: 123 → {'Armstrong Number' if is_armstrong(123) else 'Not an Armstrong Number'}")
