def factorial(n):
    """
    Compute the factorial of a number.
    
    Args:
        n (int): The number to compute factorial for (must be non-negative)
        
    Returns:
        int: The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [0, 1, 5, 10, 7]
    
    for num in test_cases:
        result = factorial(num)
        print(f"Factorial of {num} = {result}")
    
    # Example from request
    print(f"\nExample: Input: 5 → Output: {factorial(5)}")
