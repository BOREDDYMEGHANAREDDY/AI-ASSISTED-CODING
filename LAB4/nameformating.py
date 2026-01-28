def format_name(full_name):
    """
    Format a full name from "First Last" to "Last, First" format.
    
    Args:
        full_name (str): The full name in "First Last" format
        
    Returns:
        str: The name formatted as "Last, First"
    """
    parts = full_name.split()
    
    if len(parts) >= 2:
        first_name = parts[0]
        last_name = parts[-1]
        return f"{last_name}, {first_name}"
    else:
        # If only one name provided, return as is
        return full_name


# Test the function
if __name__ == "__main__":
    names = ["John Smith", "Anita Rao", "Mary Jane Watson", "Alice"]
    
    for name in names:
        formatted = format_name(name)
        print(f'"{name}" → "{formatted}"')
