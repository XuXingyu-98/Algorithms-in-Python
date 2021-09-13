def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binarySearchHelper(array, target, mid + 1, end)
    else:
        return binarySearchHelper(array, target, start, mid - 1)

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print binarySearch(array, target)
