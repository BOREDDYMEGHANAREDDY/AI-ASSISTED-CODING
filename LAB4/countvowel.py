def count_vowels(text):
    """
    Count the number of vowels in a given string.
    
    Vowels are: a, e, i, o, u (case-insensitive)
    
    Args:
        text (str): The string to check for vowels
        
    Returns:
        int: The count of vowels in the string
    """
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count


# Alternative one-liner version
def count_vowels_v2(text):
    """Count vowels using a more concise approach."""
    return sum(1 for char in text if char.lower() in "aeiou")


# Test the function
if __name__ == "__main__":
    test_strings = ["Hello World", "Python", "aEiOu", "xyz", "Anita Rao"]
    
    for string in test_strings:
        vowel_count = count_vowels(string)
        print(f'"{string}" has {vowel_count} vowels')
