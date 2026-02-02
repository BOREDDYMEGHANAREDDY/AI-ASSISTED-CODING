# Armstrong Number Checker - Line-by-Line Explanation

## What is an Armstrong Number?

An **Armstrong number** (also called a **narcissistic number**) is a number that equals the sum of its own digits each raised to the power of the number of digits.

### Examples

**153 is an Armstrong number:**
```
153 has 3 digits
1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓
```

**9474 is an Armstrong number:**
```
9474 has 4 digits
9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474 ✓
```

**123 is NOT an Armstrong number:**
```
123 has 3 digits
1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123 ✗
```

---

## Main Function: `is_armstrong_number(number)`

### Line-by-Line Breakdown

#### Step 1: Handle Negative Numbers
```python
if number < 0:
    return False
```

**Explanation:**
- Armstrong numbers are defined only for non-negative integers
- If the input is negative, we immediately return `False`
- This prevents errors and follows mathematical definition

**Example:** `is_armstrong_number(-153)` → `False`

---

#### Step 2: Convert Number to String
```python
number_str = str(number)
```

**Explanation:**
- We convert the integer to a string to easily access individual digits
- This allows us to loop through each digit separately
- Strings can be indexed like a list

**Example:**
```python
number = 153
number_str = str(153)  # "153"
number_str[0]  # '1'
number_str[1]  # '5'
number_str[2]  # '3'
```

---

#### Step 3: Count the Number of Digits
```python
num_digits = len(number_str)
```

**Explanation:**
- We get the length of the string, which equals the number of digits
- This is needed because each digit is raised to the power of total digits

**Example:**
```python
number_str = "153"
num_digits = len("153")  # 3
```

---

#### Step 4: Initialize Sum Variable
```python
sum_of_powers = 0
```

**Explanation:**
- We create a variable to store the cumulative sum
- We start at 0 and will add each powered digit to it
- This accumulates the total that we'll compare with the original number

---

#### Step 5: Loop Through Each Digit
```python
for digit_char in number_str:
```

**Explanation:**
- This loop goes through each digit character in the string
- One iteration for each digit in the number
- `digit_char` gets each character one by one

**Example for 153:**
```
Iteration 1: digit_char = '1'
Iteration 2: digit_char = '5'
Iteration 3: digit_char = '3'
```

---

#### Step 6: Convert Digit Character to Integer
```python
digit = int(digit_char)
```

**Explanation:**
- We convert the character '1' back to the integer 1
- This is necessary because we need to do math operations on it
- Strings cannot be raised to powers; only numbers can

**Example:**
```python
digit_char = '5'
digit = int('5')  # 5 (now it's an integer)
```

---

#### Step 7: Calculate Power and Add to Sum
```python
sum_of_powers += digit ** num_digits
```

**Explanation:**
- `digit ** num_digits` raises the digit to the power of total digits
- `+=` adds this value to our running sum
- This builds up the total we need to compare

**Example for 153:**
```
Iteration 1: sum_of_powers += 1**3  → sum_of_powers = 0 + 1 = 1
Iteration 2: sum_of_powers += 5**3  → sum_of_powers = 1 + 125 = 126
Iteration 3: sum_of_powers += 3**3  → sum_of_powers = 126 + 27 = 153
```

---

#### Step 8: Compare and Return Result
```python
return sum_of_powers == number
```

**Explanation:**
- We compare the calculated sum with the original number
- If they're equal, the `==` operator returns `True`
- If they're not equal, it returns `False`
- This is what we return to the caller

**Example for 153:**
```python
sum_of_powers = 153
number = 153
153 == 153  # True ✓
```

**Example for 123:**
```python
sum_of_powers = 36
number = 123
36 == 123  # False ✗
```

---

## Complete Function Trace

### Tracing `is_armstrong_number(153)`

```
Step 1: Check if 153 < 0?
        No, continue

Step 2: Convert to string
        number_str = "153"

Step 3: Count digits
        num_digits = 3

Step 4: Initialize sum
        sum_of_powers = 0

Step 5-7: Loop through digits
        Iteration 1:
            digit_char = '1'
            digit = 1
            sum_of_powers += 1**3  →  sum_of_powers = 1
        
        Iteration 2:
            digit_char = '5'
            digit = 5
            sum_of_powers += 5**3  →  sum_of_powers = 126
        
        Iteration 3:
            digit_char = '3'
            digit = 3
            sum_of_powers += 3**3  →  sum_of_powers = 153

Step 8: Return result
        153 == 153?  →  True ✓
```

### Tracing `is_armstrong_number(123)`

```
Step 1: Check if 123 < 0?
        No, continue

Step 2: Convert to string
        number_str = "123"

Step 3: Count digits
        num_digits = 3

Step 4: Initialize sum
        sum_of_powers = 0

Step 5-7: Loop through digits
        Iteration 1:
            digit_char = '1'
            digit = 1
            sum_of_powers += 1**3  →  sum_of_powers = 1
        
        Iteration 2:
            digit_char = '2'
            digit = 2
            sum_of_powers += 2**3  →  sum_of_powers = 9
        
        Iteration 3:
            digit_char = '3'
            digit = 3
            sum_of_powers += 3**3  →  sum_of_powers = 36

Step 8: Return result
        36 == 123?  →  False ✗
```

---

## Helper Functions

### `check_armstrong_in_range(start, end)`

**Purpose:** Find all Armstrong numbers between two values

**Line-by-line:**
```python
armstrong_numbers = []           # Create empty list to store results

for num in range(start, end + 1): # Loop from start to end (inclusive)
    if is_armstrong_number(num):  # Check each number
        armstrong_numbers.append(num)  # Add if it's Armstrong

return armstrong_numbers         # Return all found numbers
```

**Example:** `check_armstrong_in_range(1, 1000)` → `[1, 153, 370, 371, 407]`

---

### `print_armstrong_analysis(number)`

**Purpose:** Show detailed breakdown of calculation

**Key operations:**
```python
result = is_armstrong_number(number)  # Check if Armstrong
number_str = str(number)              # Get digits
num_digits = len(number_str)          # Count digits

# Loop to show each digit's power
for digit_char in number_str:
    digit = int(digit_char)
    powered = digit ** num_digits
    print(f"  {digit}^{num_digits} = {powered}")
```

**Output example for 153:**
```
Number of digits: 3

Breakdown:
  1^3 = 1
  5^3 = 125
  3^3 = 27

Sum: 1 + 125 + 27 = 153

✓ 153 is an Armstrong number!
```

---

## Key Programming Concepts Used

| Concept | Usage |
|---------|-------|
| **Type Conversion** | `str()`, `int()` to convert between types |
| **String Indexing** | Access individual characters in string |
| **Loop** | `for` loop to process each digit |
| **Accumulation** | `+=` to build running sum |
| **Power Operator** | `**` to raise digit to power |
| **Comparison** | `==` to check equality |
| **Function Return** | Return boolean result |

---

## Common Armstrong Numbers

```
1-digit:   1, 2, 3, 4, 5, 6, 7, 8, 9
2-digit:   None (there are no 2-digit Armstrong numbers)
3-digit:   153, 370, 371, 407
4-digit:   1634, 8208, 9474
5-digit:   54748, 92727, 93084
6-digit:   None
7-digit:   548834, 1741725, 4210818, 9800817, 9926315
```

---

## Time Complexity Analysis

**For `is_armstrong_number(number)`:**
- Converting to string: **O(d)** where d = number of digits
- Loop through digits: **O(d)**
- Total: **O(d)** or essentially **O(log n)** where n = the number

**For `check_armstrong_in_range(start, end)`:**
- Range size: **O(end - start)**
- Each check: **O(d)**
- Total: **O((end - start) × log n)**

---

## Usage Examples

```python
# Single number check
is_armstrong_number(153)     # True
is_armstrong_number(9474)    # True
is_armstrong_number(123)     # False

# Find in range
check_armstrong_in_range(1, 1000)  # [1, 153, 370, 371, 407]

# Detailed analysis
print_armstrong_analysis(153)
```

---

## Why This Implementation is Good

✓ **Clear variable names** - `sum_of_powers`, `num_digits` explain what they do
✓ **Comments explain logic** - Every important line has explanation
✓ **Handles edge cases** - Negative numbers, single digits
✓ **Efficient** - Doesn't recalculate unnecessarily
✓ **Readable** - Easy to understand and follow
✓ **Well-documented** - Docstrings explain parameters and returns
