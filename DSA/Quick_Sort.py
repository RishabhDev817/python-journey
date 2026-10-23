def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choosing the middle element as the pivot
    pivot = arr[len(arr) // 2]

    # Partition array into three parts:
    # 1. Elements smaller than pivot
    # 2. Elements equal to pivot
    # 3. Elements greater than pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right sublists, then combine
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
mylist = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted list:", mylist)
print("Sorted list:", quick_sort(mylist))
