def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.
    inputs: arr (list): A sorted list of elements.
    target: The value to search for in the list.
    If the target is found, return its index; otherwise, return None.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Found {arr[mid]} at index {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return None  # Target not found in the array

def main():
    # Example usage of binary_search function
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_value = int(input("Enter the target value: "))
    
    result = binary_search(sorted_array, target_value)

    print(result if result is not None else "Target not found in the array.")

if __name__ == "__main__":
    main()