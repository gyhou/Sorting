def insertion_sort(arr):
    """
    Avg Time Complexity: Θ(n^2)
    """
    # 1. Separate the first element from the rest of the array
    # Think about it as a sorted list of one element.
    # 2. For all other indices, beginning with [1]:
    for i in range(1, len(arr)):
        # a. Copy the item at that index into a temp variable
        current_value = arr[i]
        index = i
        # b. Iterate to the left until you find the correct index
        # in the "sorted" part of the array at which this element
        # should be inserted
        # - Shift items over to the right as you iterate
        while index > 0 and arr[index-1] > current_value:
            arr[index] = arr[index-1]
            index -= 1
        # c. When the correct index is found, copy temp into this position
        arr[index] = current_value
    return arr


# TODO: Complete the selection_sort function below
def selection_sort(arr):
    """
    Avg Time Complexity: Θ(n^2)
    """
    # loop through n-1 elements
    for i in range(len(arr)-1):
        smallest_index = i
        # TODO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(i, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
        # TODO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TODO:  implement the bubble_sort function below
def bubble_sort(arr):
    """
    Avg Time Complexity: Θ(n^2)
    """
    n = len(arr)
    swaps = True
    while n > 0 and swaps:
        swaps = False
        for x in range(n-1):
            # Compare each element to its neighbor
            if arr[x] > arr[x+1]:
                # If elements in wrong position
                # (relative to each other, swap them)
                arr[x], arr[x+1] = arr[x+1], arr[x]
                # If no swaps performed, stop the while loop
                swaps = True
        n -= 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    """
    Avg Time Complexity: Θ(n+k)
    """
    # Return empty list if arr is empty
    if len(arr) < 1:
        return []
    # Create count list with length equal to the max of arr
    count = [0]*(max(arr)+1)
    # Count each element in arr and add count to the index
    for i in range(len(arr)):
        if arr[i] > -1:
            count[arr[i]] += 1
        # Count sort does not work with negative numbers
        else:
            return "Error, negative numbers not allowed in Count Sort"
    # Create new list base on counts values
    new_arr = []
    for i in range(len(count)):
        new_arr += [i]*count[i]
    return new_arr
