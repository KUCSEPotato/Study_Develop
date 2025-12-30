# selsection_sort.py
# This code implements the selection sort algorithm.
# The selection sort algorithm sorts an array by repeatedly finding the smallest element
# from the unsorted part and moving it to the sorted part.
# time complexity: O(n^2)

def smallest_element_index(arr):
    """
    Find the smallest element in an array.
    input: arr (list): A list of elements.
    return: The smallest element index in the list.
    """
    if not arr:
        return f"empty array"
    
    smallest = arr[0]
    smallest_index = 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):
    """
    Sort an array using the selection sort algorithm.
    input: arr (list): A list of elements to be sorted.
    return: The sorted list.
    """
    sorted_arr = []
    copied_arr = list(arr) # Copy the original array to avoid modifying it

    for i in range(len(copied_arr)):
        smallest = smallest_element_index(copied_arr)
        sorted_arr.append(copied_arr[smallest])
        copied_arr.pop(smallest)

    return sorted_arr

def main():
    # Example usage of selection_sort function
    unsorted_array = [64, 25, 12, 22, 11]
    
    sorted_array = selection_sort(unsorted_array)
    
    print(f"Unsorted array: {unsorted_array}")
    print(f"Sorted array: {sorted_array}")

if __name__ == "__main__":
    main()