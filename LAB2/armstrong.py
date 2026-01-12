# Armstrong number checker

# An Armstrong (narcissistic) number is an integer such that the sum of its digits
# each raised to the power of the number of digits equals the number itself.
# Example: 153 -> 1^3 + 5^3 + 3^3 = 153

def is_armstrong(n: int) -> bool:
    """Return True if `n` is an Armstrong number (n >= 0).

    Args:
        n: non-negative integer to check

    Returns:
        True if n is an Armstrong number, False otherwise
    """
    if n < 0:
        return False

    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n


if __name__ == '__main__':
    # Simple CLI: read a number and report whether it is Armstrong.
    try:
        value = int(input("Enter a non-negative integer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        if value < 0:
            print("Please enter a non-negative integer.")
        else:
            if is_armstrong(value):
                print(f"{value} is an Armstrong number.")
            else:
                print(f"{value} is not an Armstrong number.")

            # Optionally show all Armstrong numbers up to the entered value
            if value <= 100000:  # keep it bounded to avoid long runs
                armstrong_list = [i for i in range(value + 1) if is_armstrong(i)]
                print("Armstrong numbers up to", value, ":", " ".join(map(str, armstrong_list)))