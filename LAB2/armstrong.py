# armstrong_check.py
# Check whether a number is an Armstrong (narcissistic) number.

s = input("Enter an integer: ")
try:
    n = int(s)
except ValueError:
    print("Invalid input. Please enter an integer.")
    raise SystemExit(1)

if n < 0:
    print("Negative numbers are not Armstrong numbers.")
else:
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    if total == n:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")