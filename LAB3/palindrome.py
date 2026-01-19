def is_palindrome(num):
    """
    Check whether a given number is a palindrome.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Convert number to string and remove the negative sign if present
    num_str = str(abs(num))
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]


# Test cases
if __name__ == "__main__":
    test_numbers = [121, 123, 1001, 12321, 100, -121, 0, 7]
    
    for num in test_numbers:
        result = is_palindrome(num)
        print(f"{num} is a palindrome: {result}")
