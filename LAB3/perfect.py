def is_perfect(num):
    """
    Check whether a given number is a perfect number.
    A perfect number is equal to the sum of its proper positive divisors (excluding itself).
    
    Args:
        num (int): The number to check (must be positive)
        
    Returns:
        bool: True if the number is perfect, False otherwise
    """
    # Perfect numbers must be positive
    if num <= 0:
        return False
    
    # 1 is not a perfect number (no proper divisors)
    if num == 1:
        return False
    
    # Find sum of proper divisors
    divisor_sum = 0
    
    # Check divisors up to num/2
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisor_sum += i
    
    # Check if sum equals the number
    return divisor_sum == num


def is_perfect_optimized(num):
    """
    Optimized version using √n approach.
    More efficient for larger numbers.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is perfect, False otherwise
    """
    if num <= 0 or num == 1:
        return False
    
    divisor_sum = 1  # 1 is always a divisor for num > 1
    
    # Check divisors up to sqrt(num)
    i = 2
    while i * i <= num:
        if num % i == 0:
            divisor_sum += i
            # Add complementary divisor if different
            if i != num // i:
                divisor_sum += num // i
        i += 1
    
    return divisor_sum == num


# Test cases
if __name__ == "__main__":
    test_numbers = [6, 28, 496, 8128, 10, 15, 100, 1, 2, 0, -6]
    
    print("Perfect Number Checker")
    print("=" * 50)
    print(f"{'Number':<10} {'Result':<20} {'Divisors'}")
    print("=" * 50)
    
    for num in test_numbers:
        result = is_perfect(num)
        
        # Calculate divisors for display
        if num > 1:
            divisors = [i for i in range(1, num) if num % i == 0]
            divisor_str = f"{divisors} = {sum(divisors)}"
        else:
            divisor_str = "N/A"
        
        status = "Perfect" if result else "Not Perfect"
        print(f"{num:<10} {status:<20} {divisor_str}")
    
    print("\n" + "=" * 50)
    print("Examples:")
    print(f"6 is perfect: {is_perfect(6)} (1 + 2 + 3 = 6)")
    print(f"28 is perfect: {is_perfect(28)} (1 + 2 + 4 + 7 + 14 = 28)")
    print(f"496 is perfect: {is_perfect(496)}")
    print(f"8128 is perfect: {is_perfect(8128)}")
