# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TODO: add missing code
    for x in range(len(arr)):
        if target == arr[x]:
            return x

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    # TODO: add missing code
    while arr[(low+high)//2] != target:
        if target > arr[(low+high)//2]:
            low = (low+high)//2
        else:
            high = (low+high)//2
    if arr[(low+high)//2] == target:
        return (low+high)//2
    else:
        return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    # TODO: add missing if/else statements, recursive calls
    if len(arr) == 0:
        return -1  # array empty
    elif arr[middle] == target:
        return middle
    elif target > arr[middle]:
        return binary_search_recursive(arr, target, middle, high)
    elif target < arr[middle]:
        return binary_search_recursive(arr, target, low, middle)
    else:
        return -1
