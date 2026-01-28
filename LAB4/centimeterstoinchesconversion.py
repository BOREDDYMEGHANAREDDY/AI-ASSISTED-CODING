def cm_to_inches(centimeters):
    """
    Convert centimeters to inches.
    
    Formula: inches = centimeters / 2.54
    
    Args:
        centimeters (float): The length in centimeters
        
    Returns:
        float: The length converted to inches
    """
    inches = centimeters / 2.54
    return inches


# Test the function
if __name__ == "__main__":
    test_values = [10, 25, 50, 100, 5.5]
    
    for cm in test_values:
        result = cm_to_inches(cm)
        print(f"{cm} cm → {result:.2f} inches")
