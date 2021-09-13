def quickSort(array):
    quickSortR(array, 0, len(array) - 1)
    return array

def quickSortR(array, start, end):
    if start >= end:
        return
    pivot = array[start]
    left = start + 1
    right = end
    while left <= right:
        if array[left] > pivot and array[right] < pivot:
            swap(left, right, array)
        if array[left] <= pivot:
            left += 1
        if array[right] >= pivot:
            right -= 1
    swap(start, right, array)
    quickSortR(array, start, right - 1)
    quickSortR(array, right + 1, end)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [8, 5, 2, 9, 5, 6, 3]
quickSort(array)
print array
