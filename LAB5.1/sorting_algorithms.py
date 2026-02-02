"""
Sorting Algorithms: Bubble Sort vs Quick Sort
Comprehensive implementation with detailed comments and analysis
"""


# ============================================================================
# BUBBLE SORT IMPLEMENTATION
# ============================================================================

def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    
    How it works:
    - Compares adjacent elements and swaps them if they're in wrong order
    - Repeats until no more swaps needed
    - Smallest elements "bubble up" to the beginning
    - Simpler but slower for large datasets
    
    Args:
        arr (list): List of numbers to sort
        
    Returns:
        list: Sorted list in ascending order
        
    Time Complexity: O(n²) in all cases (worst, average, best)
    Space Complexity: O(1) - sorts in place
    """
    
    # Get the length of the array
    n = len(arr)
    
    # Outer loop: number of passes through the array
    # We need at most n-1 passes to sort n elements
    for i in range(n):
        
        # Flag to optimize: if no swaps occur, array is already sorted
        # We can break early instead of continuing all passes
        swapped = False
        
        # Inner loop: compare adjacent elements
        # In each pass, the largest unsorted element moves to the end
        # So we reduce the range each time (n - i - 1)
        for j in range(0, n - i - 1):
            
            # Compare current element with next element
            if arr[j] > arr[j + 1]:
                
                # Swap if current is greater than next
                # This moves larger elements toward the end
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                # Mark that a swap occurred
                swapped = True
        
        # If no swaps occurred in this pass, array is sorted
        # Early termination optimization
        if not swapped:
            break
    
    # Return the sorted array
    return arr


def bubble_sort_verbose(arr):
    """
    Bubble Sort with step-by-step visualization.
    Shows each swap and pass for educational purposes.
    
    Args:
        arr (list): List of numbers to sort
        
    Returns:
        list: Sorted list
    """
    
    n = len(arr)
    print(f"Starting Bubble Sort: {arr}")
    print("=" * 60)
    
    # Outer loop for passes
    for i in range(n):
        swapped = False
        print(f"\nPass {i + 1}:")
        
        # Inner loop for comparisons
        for j in range(0, n - i - 1):
            print(f"  Comparing {arr[j]} and {arr[j + 1]}", end="")
            
            # Swap if needed
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f" → Swap → {arr}")
                swapped = True
            else:
                print(" → No swap")
        
        print(f"  After pass {i + 1}: {arr}")
        
        if not swapped:
            print(f"\n✓ No swaps in pass {i + 1}, array is sorted!")
            break
    
    print("=" * 60)
    return arr


# ============================================================================
# QUICK SORT IMPLEMENTATION
# ============================================================================

def quick_sort(arr):
    """
    Quick Sort Algorithm
    
    How it works:
    - Divide and conquer approach
    - Selects a 'pivot' element
    - Partitions array into: smaller than pivot | pivot | larger than pivot
    - Recursively sorts left and right partitions
    - Much faster than bubble sort for large datasets
    
    Args:
        arr (list): List of numbers to sort
        
    Returns:
        list: Sorted list in ascending order
        
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) for recursion stack
    """
    
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose pivot: we use middle element for better average performance
    # (Random or first element could also work)
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    
    # Initialize three lists for partitioning
    left = []      # Elements smaller than pivot
    middle = []    # Elements equal to pivot (handles duplicates)
    right = []     # Elements larger than pivot
    
    # Partition: distribute elements into three lists
    for num in arr:
        if num < pivot:
            left.append(num)      # Add to left if smaller
        elif num == pivot:
            middle.append(num)    # Add to middle if equal
        else:
            right.append(num)     # Add to right if larger
    
    # Recursively sort left and right partitions, then combine
    # left (sorted) + middle (equals) + right (sorted)
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    Quick Sort with in-place partitioning (more efficient).
    
    This version modifies the array in place instead of creating new lists,
    using much less extra memory.
    
    Args:
        arr (list): List to sort
        low (int): Starting index
        high (int): Ending index
        
    Returns:
        list: Same array, now sorted
    """
    
    # Initialize high on first call
    if high is None:
        high = len(arr) - 1
    
    # Base case: if low >= high, partition is sorted
    if low < high:
        
        # Partition the array and get pivot position
        pivot_index = _partition(arr, low, high)
        
        # Recursively sort left partition
        quick_sort_inplace(arr, low, pivot_index - 1)
        
        # Recursively sort right partition
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr


def _partition(arr, low, high):
    """
    Partition helper function for in-place quick sort.
    Rearranges array so all elements smaller than pivot are on left,
    and all larger are on right.
    
    Args:
        arr (list): Array to partition
        low (int): Start index
        high (int): End index
        
    Returns:
        int: Final position of pivot
    """
    
    # Choose rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element - indicates right end of left partition
    i = low - 1
    
    # Traverse through all elements
    # Compare each element with pivot
    for j in range(low, high):
        if arr[j] < pivot:
            # If element is smaller, move it to left partition
            i += 1
            # Swap to move smaller element left
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    # Swap pivot with element at position i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return pivot's final position
    return i + 1


def quick_sort_verbose(arr, low=0, high=None, depth=0):
    """
    Quick Sort with step-by-step visualization.
    Shows partitioning and recursive calls for educational purposes.
    
    Args:
        arr (list): Array to sort
        low (int): Starting index
        high (int): Ending index
        depth (int): Recursion depth for indentation
        
    Returns:
        list: Sorted array
    """
    
    if high is None:
        high = len(arr) - 1
        print(f"Starting Quick Sort: {arr}")
        print("=" * 60)
    
    if low < high:
        indent = "  " * depth
        print(f"{indent}Sorting arr[{low}:{high + 1}] = {arr[low:high + 1]}")
        
        # Partition and get pivot position
        pivot_index = _partition_verbose(arr, low, high, depth)
        
        print(f"{indent}After partition, pivot at index {pivot_index}")
        print(f"{indent}Array: {arr}\n")
        
        # Recursively sort left partition
        quick_sort_verbose(arr, low, pivot_index - 1, depth + 1)
        
        # Recursively sort right partition
        quick_sort_verbose(arr, pivot_index + 1, high, depth + 1)
    
    # Print final result on last return
    if depth == 0:
        print("=" * 60)
        print(f"Final sorted array: {arr}\n")
    
    return arr


def _partition_verbose(arr, low, high, depth=0):
    """
    Partition helper with visualization.
    
    Args:
        arr (list): Array to partition
        low (int): Start index
        high (int): End index
        depth (int): Recursion depth
        
    Returns:
        int: Pivot position
    """
    
    indent = "  " * depth
    pivot = arr[high]
    print(f"{indent}  Pivot: {pivot}")
    
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"{indent}  Swapped {arr[j]} and {arr[i]}")
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def print_comparison():
    """Print detailed comparison of both algorithms."""
    
    comparison = """
╔════════════════════════════════════════════════════════════════════════════╗
║                    BUBBLE SORT vs QUICK SORT COMPARISON                   ║
╚════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────┐
│ ALGORITHM LOGIC                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BUBBLE SORT:                          │ QUICK SORT:                        │
│ • Simple and straightforward           │ • Divide and conquer strategy     │
│ • Compares adjacent elements           │ • Selects a pivot element        │
│ • Swaps if in wrong order              │ • Partitions around pivot        │
│ • Repeats until sorted                 │ • Recursively sorts partitions   │
│ • "Bubbles" largest to end each pass   │ • Efficient for large datasets   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ TIME COMPLEXITY                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BUBBLE SORT:                          │ QUICK SORT:                        │
│ • Best Case: O(n)                     │ • Best Case: O(n log n)          │
│   - Already sorted array              │   - Balanced partitions          │
│   - Early termination possible        │   - Pivot divides array evenly   │
│                                       │                                  │
│ • Average Case: O(n²)                 │ • Average Case: O(n log n)       │
│   - Random array                      │   - Random array                 │
│   - Most comparisons needed           │   - Logarithmic depth            │
│                                       │                                  │
│ • Worst Case: O(n²)                   │ • Worst Case: O(n²)              │
│   - Reverse sorted array              │   - Poor pivot selection         │
│   - Maximum comparisons               │   - Example: pivoting on min/max │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ SPACE COMPLEXITY                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BUBBLE SORT:                          │ QUICK SORT:                        │
│ • O(1) - In-place sorting             │ • O(log n) - Recursion stack     │
│ • Only swaps elements                 │ • In-place variant: O(log n)     │
│ • No extra arrays needed              │ • Simple variant: O(n) extra     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ EFFICIENCY & PERFORMANCE                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Input Size    │ Bubble Sort       │ Quick Sort        │ Winner            │
│ ──────────────┼───────────────────┼───────────────────┼──────────────────│
│ n = 10        │ ~100 operations   │ ~50 operations    │ Quick Sort        │
│ n = 100       │ ~10,000 ops       │ ~700 operations   │ Quick Sort (↑↑)   │
│ n = 1,000     │ ~1,000,000 ops    │ ~10,000 ops       │ Quick Sort (↑↑↑)  │
│ n = 10,000    │ ~100,000,000 ops  │ ~130,000 ops      │ Quick Sort        │
│                                                                             │
│ For n = 10,000:                                                             │
│ • Bubble Sort: ~770x slower than Quick Sort                                │
│ • Quick Sort is clearly superior for any reasonably large dataset          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ STABILITY                                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BUBBLE SORT:                          │ QUICK SORT:                        │
│ • STABLE sort                         │ • NOT stable (basic version)     │
│ • Preserves relative order of         │ • Order of equal elements may   │
│   equal elements                      │   change during partitioning    │
│ • Important for complex objects       │ • Can be made stable with       │
│                                       │   additional logic              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ USE CASES & RECOMMENDATIONS                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BUBBLE SORT:                          │ QUICK SORT:                        │
│ ✓ Educational purposes                │ ✓ Real-world production code     │
│ ✓ Very small arrays (<20 elements)    │ ✓ Large datasets                 │
│ ✓ Nearly sorted data                  │ ✓ General-purpose sorting       │
│ ✓ When simplicity is priority         │ ✓ When performance matters      │
│ ✗ Avoid for any serious application   │ ✗ Avoid when stability crucial  │
│                                       │   (use merge sort instead)      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ IMPLEMENTATION COMPLEXITY                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BUBBLE SORT:                          │ QUICK SORT:                        │
│ • Very easy to understand             │ • More complex logic             │
│ • ~20 lines of code                   │ • ~30-40 lines of code           │
│ • No recursive calls needed           │ • Recursive implementation       │
│ • Beginner-friendly                   │ • Intermediate level             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ WHEN TO USE EACH                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ USE BUBBLE SORT IF:                   │ USE QUICK SORT IF:                 │
│ • Learning algorithms (educational)   │ • Performance is important       │
│ • Dataset is tiny (< 20 items)        │ • Dataset is large (> 50 items) │
│ • Data is nearly sorted already       │ • Average performance sufficient │
│ • Memory is extremely limited         │ • Stability not required         │
│ • Need a stable sort (with flag)      │ • Want industry-standard choice  │
│                                       │ • Recursion is acceptable       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ REAL-WORLD COMPARISON                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Sorting 1 MILLION numbers:                                                  │
│                                                                             │
│ Bubble Sort:                                                                │
│ • Estimated operations: 10¹² (1 trillion)                                  │
│ • Estimated time: ~100 hours on modern CPU                                 │
│ • Status: IMPRACTICAL ✗                                                    │
│                                                                             │
│ Quick Sort:                                                                 │
│ • Estimated operations: 2×10⁷ (20 million)                                 │
│ • Estimated time: ~200 milliseconds on modern CPU                          │
│ • Status: PRACTICAL ✓                                                      │
│                                                                             │
│ DIFFERENCE: Quick Sort is 180,000x FASTER! 🚀                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

CONCLUSION:
═══════════════════════════════════════════════════════════════════════════════

Quick Sort is almost always the better choice for real-world applications.

Bubble Sort's only advantages are:
  • Simplicity for learning
  • Stability property
  • O(n) for nearly-sorted data

Quick Sort's advantages outweigh these by far:
  • O(n log n) for most practical cases
  • Much faster even for small datasets
  • Industry standard (used in most language libraries)
  • In-place sorting possible

For production code: ALWAYS use Quick Sort or other O(n log n) algorithms.
For learning/education: Bubble Sort is excellent for understanding basics.
    """
    
    print(comparison)


# ============================================================================
# TESTING & DEMONSTRATION
# ============================================================================

def test_sorting_algorithms():
    """Test both algorithms with various datasets."""
    
    print("\n" + "="*70)
    print("SORTING ALGORITHMS TESTING")
    print("="*70)
    
    # Test case 1: Random array
    print("\n1. RANDOM ARRAY TEST")
    print("-" * 70)
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr1}")
    print(f"Bubble Sort Result: {bubble_sort(arr1.copy())}")
    print(f"Quick Sort Result: {quick_sort(arr1.copy())}")
    
    # Test case 2: Already sorted
    print("\n2. ALREADY SORTED ARRAY TEST")
    print("-" * 70)
    arr2 = [1, 2, 3, 4, 5]
    print(f"Original: {arr2}")
    print(f"Bubble Sort Result: {bubble_sort(arr2.copy())}")
    print(f"Quick Sort Result: {quick_sort(arr2.copy())}")
    
    # Test case 3: Reverse sorted
    print("\n3. REVERSE SORTED ARRAY TEST")
    print("-" * 70)
    arr3 = [5, 4, 3, 2, 1]
    print(f"Original: {arr3}")
    print(f"Bubble Sort Result: {bubble_sort(arr3.copy())}")
    print(f"Quick Sort Result: {quick_sort(arr3.copy())}")
    
    # Test case 4: Duplicates
    print("\n4. ARRAY WITH DUPLICATES TEST")
    print("-" * 70)
    arr4 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"Original: {arr4}")
    print(f"Bubble Sort Result: {bubble_sort(arr4.copy())}")
    print(f"Quick Sort Result: {quick_sort(arr4.copy())}")
    
    # Test case 5: Single element
    print("\n5. SINGLE ELEMENT TEST")
    print("-" * 70)
    arr5 = [42]
    print(f"Original: {arr5}")
    print(f"Bubble Sort Result: {bubble_sort(arr5.copy())}")
    print(f"Quick Sort Result: {quick_sort(arr5.copy())}")
    
    # Test case 6: Empty array
    print("\n6. EMPTY ARRAY TEST")
    print("-" * 70)
    arr6 = []
    print(f"Original: {arr6}")
    print(f"Bubble Sort Result: {bubble_sort(arr6.copy())}")
    print(f"Quick Sort Result: {quick_sort(arr6.copy())}")


def demonstrate_verbose():
    """Show step-by-step visualization."""
    
    test_array = [38, 27, 43, 3, 9]
    
    print("\n" + "="*70)
    print("BUBBLE SORT STEP-BY-STEP VISUALIZATION")
    print("="*70)
    bubble_sort_verbose(test_array.copy())
    
    print("\n" + "="*70)
    print("QUICK SORT STEP-BY-STEP VISUALIZATION")
    print("="*70)
    quick_sort_verbose(test_array.copy())


# ============================================================================
# MAIN PROGRAM
# ============================================================================

if __name__ == "__main__":
    
    # Test both algorithms
    test_sorting_algorithms()
    
    # Show step-by-step visualization
    demonstrate_verbose()
    
    # Print detailed comparison
    print_comparison()
    
    print("\nProgram completed successfully!")
