def partition(arr):
    # Select a pivot
    # Often times this is the first or last element in a set
    # It can also be the middle
    left = []
    pivot = arr[0]
    right = []

    for v in arr[1:]:
        if v <= pivot:
            # Move all elements smaller than the pivot to the left
            left.append(v)
        else:
            # Move all elements greater than the pivot to the right
            right.append(v)

    return left, [pivot], right


def quicksort(arr):
    # While LHS and RHS are greater than 1, repeat steps 1-3 on each side
    if len(arr) > 1:
        left, pivot, right = partition(arr)
        return quicksort(left) + pivot + quicksort(right)
    else:
        return arr


# TODO: complete the Merge help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    """
    Start merging your single lists of one 
    element together into larger, sorted sets
    """
    merged_arr = []
    # TODO
    while arrA != [] and arrB != []:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
        else:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
    if arrA != []:
        merged_arr += arrA
        return merged_arr
    if arrB != []:
        merged_arr += arrB
        return merged_arr


# TODO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TODO
    # While your data set contains more than one item, split it in half
    if len(arr) > 1:
        h = len(arr)//2
        return merge(merge_sort(arr[:h]), merge_sort(arr[h:]))
    else:
        return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TODO

    return arr


def merge_sort_in_place(arr, l, r):
    # TODO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
