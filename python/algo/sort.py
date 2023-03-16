#BUBBLE SORT 

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


#SELECTON SORT 
def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

#QUICK SORT 


def quick_sort(arr):
    n = len(arr)

    # Base case: array with 0 or 1 element is already sorted
    if n <= 1:
        return arr

    # Choose the rightmost element as the pivot
    pivot = arr[-1]

    # Partition the array into smaller and larger elements
    smaller, larger, equal = [], [], []
    for element in arr:
        if element < pivot:
            smaller.append(element)
        elif element > pivot:
            larger.append(element)
        else:
            equal.append(element)

    # Recursively apply quick sort to the smaller and larger subarrays
    return quick_sort(smaller) + equal + quick_sort(larger)

#MERGE SORT 
#RECURSIVE 

def merge_sort(arr):
    n = len(arr)

    # Base case: array with 0 or 1 element is already sorted
    if n <= 1:
        return arr

    # Divide the array into two halves and recursively apply merge sort to each half
    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves into a single sorted array
    sorted_arr = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1
    sorted_arr += left_half[i:]
    sorted_arr += right_half[j:]

    return sorted_arr  


#MERGRE SORT 
#ITERATIVE

def merge_sort(arr):
    n = len(arr)
    width = 1

    # Loop over the array with increasing width until the entire array is sorted
    while width < n:
        for i in range(0, n, width * 2):
            left = i
            mid = min(i + width, n)
            right = min(i + width * 2, n)
            merged = merge(arr[left:mid], arr[mid:right])
            arr[left:right] = merged
        width *= 2

    return arr

def merge(left_half, right_half):
    i = j = 0
    merged = []
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
    merged += left_half[i:]
    merged += right_half[j:]
    return merged
