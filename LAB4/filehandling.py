def count_lines(filename):
    """
    Count the number of lines in a text file.
    
    Args:
        filename (str): The path to the text file
        
    Returns:
        int: The number of lines in the file
        
    Raises:
        FileNotFoundError: If the file does not exist
    """
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1


# Alternative method
def count_lines_v2(filename):
    """Count lines by reading all lines and getting the length."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1


# Test the function
if __name__ == "__main__":
    # Create test files
    with open('test_file_3lines.txt', 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")
    
    with open('test_file_10lines.txt', 'w') as f:
        for i in range(1, 11):
            f.write(f"Line {i}\n")
    
    # Test counting lines
    result1 = count_lines('test_file_3lines.txt')
    print(f"test_file_3lines.txt has {result1} lines")
    
    result2 = count_lines('test_file_10lines.txt')
    print(f"test_file_10lines.txt has {result2} lines")
    
    # Test with non-existent file
    result3 = count_lines('non_existent.txt')
