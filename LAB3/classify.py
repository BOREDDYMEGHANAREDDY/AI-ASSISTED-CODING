import math


def classify_number(num):
    """
    Classify a number as prime, composite, or neither.
    
    Args:
        num: The number to classify (should be an integer)
        
    Returns:
        str: Classification of the number
        
    Raises:
        ValueError: If input is invalid or not an integer
    """
    # Input validation
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    
    # Handle numbers <= 1
    if num <= 1:
        return f"{num} is neither prime nor composite"
    
    # Handle 2 (only even prime)
    if num == 2:
        return f"{num} is a prime number"
    
    # Even numbers (except 2) are composite
    if num % 2 == 0:
        return f"{num} is a composite number"
    
    # Optimize using √n approach
    # Only check divisors up to sqrt(n)
    sqrt_num = int(math.sqrt(num))
    
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return f"{num} is a composite number"
    
    return f"{num} is a prime number"


def main():
    """
    Main function to demonstrate the classifier.
    """
    test_cases = [
        0, 1, 2, 3, 4, 5, 10, 15, 17, 20, 29, 49, 97, 100, -5
    ]
    
    print("Number Classification Program")
    print("=" * 50)
    
    for num in test_cases:
        try:
            result = classify_number(num)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")
    
    print("\n" + "=" * 50)
    print("\nTesting with user input:")
    
    while True:
        try:
            user_input = input("\nEnter a number to classify (or 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                print("Thank you for using the classifier!")
                break
            
            num = int(user_input)
            result = classify_number(num)
            print(result)
            
        except ValueError as e:
            print(f"Invalid input. Please enter a valid integer. Error: {e}")


if __name__ == "__main__":
    main()
