"""
Armstrong Number Checker
An Armstrong number (narcissistic number) is a number that equals 
the sum of its own digits each raised to the power of the number of digits.

Examples:
- 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓
- 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474 ✓
- 123 = 1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ✗
"""


def is_armstrong_number(number):
    """
    Check whether a given number is an Armstrong number.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if number is Armstrong number, False otherwise
    """
    
    # Handle negative numbers - Armstrong numbers are positive only
    if number < 0:
        return False
    
    # Convert the number to a string to easily access individual digits
    # Example: 153 becomes "153"
    number_str = str(number)
    
    # Count how many digits are in the number
    # Example: "153" has 3 digits, so num_digits = 3
    num_digits = len(number_str)
    
    # Initialize a variable to store the sum of powered digits
    # This will accumulate the sum as we process each digit
    sum_of_powers = 0
    
    # Loop through each digit in the number
    # Example: For 153, we process '1', '5', '3' one at a time
    for digit_char in number_str:
        
        # Convert the digit character back to an integer
        # Example: '1' becomes 1 (integer), '5' becomes 5, '3' becomes 3
        digit = int(digit_char)
        
        # Raise the digit to the power of total number of digits
        # and add it to the sum
        # Example: 1³ + 5³ + 3³
        sum_of_powers += digit ** num_digits
    
    # Compare the sum with the original number
    # If they're equal, it's an Armstrong number
    return sum_of_powers == number


def check_armstrong_in_range(start, end):
    """
    Find all Armstrong numbers in a given range.
    
    Args:
        start (int): Starting number of the range (inclusive)
        end (int): Ending number of the range (inclusive)
        
    Returns:
        list: List of Armstrong numbers found in the range
    """
    
    # Create an empty list to store Armstrong numbers
    armstrong_numbers = []
    
    # Loop through each number in the given range
    for num in range(start, end + 1):
        
        # Check if the current number is an Armstrong number
        if is_armstrong_number(num):
            
            # If yes, add it to the list
            armstrong_numbers.append(num)
    
    # Return the list of all Armstrong numbers found
    return armstrong_numbers


def print_armstrong_analysis(number):
    """
    Print detailed analysis of whether a number is Armstrong or not.
    
    Args:
        number (int): The number to analyze
    """
    
    # Check if the number is Armstrong
    result = is_armstrong_number(number)
    
    # Convert number to string to get digits
    number_str = str(number)
    
    # Get the number of digits
    num_digits = len(number_str)
    
    # Print header
    print(f"\n{'='*50}")
    print(f"Armstrong Number Analysis: {number}")
    print(f"{'='*50}")
    
    # Print number of digits
    print(f"Number of digits: {num_digits}")
    print(f"\nBreakdown:")
    
    # Initialize sum for calculation display
    calculation_sum = 0
    
    # Display each digit raised to the power
    for digit_char in number_str:
        digit = int(digit_char)
        powered = digit ** num_digits
        calculation_sum += powered
        print(f"  {digit}^{num_digits} = {powered}")
    
    # Display the sum
    print(f"\nSum: {' + '.join([str(int(d)**num_digits) for d in number_str])} = {calculation_sum}")
    
    # Display result
    print(f"\nOriginal number: {number}")
    print(f"Sum of powered digits: {calculation_sum}")
    
    if result:
        print(f"\n✓ {number} is an Armstrong number!")
    else:
        print(f"\n✗ {number} is NOT an Armstrong number.")
    
    print(f"{'='*50}\n")


# Main program
if __name__ == "__main__":
    
    print("Armstrong Number Checker")
    print("=" * 50)
    
    # Example 1: Check single numbers
    print("\n1. Checking individual numbers:")
    test_numbers = [153, 370, 371, 407, 1634, 8208, 9474, 123, 456]
    
    for num in test_numbers:
        result = is_armstrong_number(num)
        status = "✓ Armstrong" if result else "✗ Not Armstrong"
        print(f"  {num}: {status}")
    
    # Example 2: Detailed analysis
    print("\n2. Detailed analysis for 153:")
    print_armstrong_analysis(153)
    
    print("3. Detailed analysis for 9474:")
    print_armstrong_analysis(9474)
    
    print("4. Detailed analysis for 123:")
    print_armstrong_analysis(123)
    
    # Example 3: Find all Armstrong numbers in a range
    print("\n5. Armstrong numbers from 1 to 10000:")
    armstrong_list = check_armstrong_in_range(1, 10000)
    print(f"  Found {len(armstrong_list)} Armstrong numbers:")
    print(f"  {armstrong_list}")
    
    # Example 4: Interactive mode
    print("\n6. Interactive Mode:")
    while True:
        try:
            user_input = input("\nEnter a number to check (or 'quit' to exit): ").strip()
            
            # Allow user to exit
            if user_input.lower() == 'quit':
                print("Thank you for using Armstrong Number Checker!")
                break
            
            # Convert input to integer
            number = int(user_input)
            
            # Analyze the number
            print_armstrong_analysis(number)
            
        except ValueError:
            # Handle invalid input
            print("Error: Please enter a valid integer or 'quit' to exit.")
