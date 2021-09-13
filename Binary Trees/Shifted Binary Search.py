def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    leftNum = array[left]
    rightNum = array[right]
    if target == potentialMatch:
        return middle
    elif leftNum <= potentialMatch:
        if target >= leftNum and target < potentialMatch:
            return shiftedBinarySearchHelper(array, target, left, middle - 1)
        else:
            return shiftedBinarySearchHelper(array, target, middle + 1, right)
    else:
        if target > potentialMatch and target <= rightNum:
            return shiftedBinarySearchHelper(array, target, middle + 1, right)
        else:
            return shiftedBinarySearchHelper(array, target, left, middle - 1)

array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
print shiftedBinarySearch(array, target)