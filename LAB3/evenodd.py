def check_even_odd(num):
    """
    Check whether a number is even or odd.
    
    Args:
        num (int): The number to check
        
    Returns:
        str: "Even" if the number is even, "Odd" if odd
        
    Raises:
        ValueError: If input is not an integer
    """
    if not isinstance(num, int) or isinstance(num, bool):
        raise ValueError("Input must be an integer")
    
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Test cases
if __name__ == "__main__":
    test_cases = [8, 15, 0, -5, -8, 100, 1, 2, 999]
    
    print("Even/Odd Checker Program")
    print("=" * 40)
    
    for num in test_cases:
        result = check_even_odd(num)
        print(f"Input: {num:>4} → {result}")
    
    print("\n" + "=" * 40)
    print("Examples from request:")
    print(f"Input: 8 → {check_even_odd(8)}")
    print(f"Input: 15 → {check_even_odd(15)}")
    print(f"Input: 0 → {check_even_odd(0)}")
    
    print("\n" + "=" * 40)
    print("Interactive mode:")
    
    while True:
        try:
            user_input = input("\nEnter a number to check (or 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                print("Thank you for using the checker!")
                break
            
            num = int(user_input)
            result = check_even_odd(num)
            print(f"Input: {num} → {result}")
            
        except ValueError as e:
            print(f"Invalid input. Please enter a valid integer.")
