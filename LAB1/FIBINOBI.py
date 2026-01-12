# Fibonacci series generator with comments

# generate_fibonacci returns the first n Fibonacci numbers as a list.
# - n: number of terms (expected to be an integer >= 0)
# Example: generate_fibonacci(5) -> [0, 1, 1, 2, 3]
def generate_fibonacci(n):
    """Generate a list containing the first n Fibonacci numbers.

    Uses an iterative approach with O(n) time and O(n) space.
    """
    if n <= 0:
        return []  # return empty list for non-positive input

    sequence = []        # list to collect Fibonacci numbers
    a, b = 0, 1          # 'a' is the current term, 'b' is the next term
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # advance the two-term window
    return sequence


if __name__ == '__main__':
    # CLI: read number of terms and print the series
    try:
        term_count = int(input("Enter the number of terms: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    else:
        if term_count <= 0:
            print("Please enter a positive integer.")
        else:
            series = generate_fibonacci(term_count)
            print("Fibonacci series:", " ".join(map(str, series)))