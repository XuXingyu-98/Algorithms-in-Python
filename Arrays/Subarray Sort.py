def subarraySort(array):
    minO = float("inf")
    maxO = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            maxO = max(num, maxO)
            minO = min(num, minO)
    if minO == float("inf"):
        return [-1, -1]
    leftId = 0
    while minO >= array[leftId]:
        leftId += 1
    rightId = len(array) - 1
    while maxO <= array[rightId]:
        rightId -= 1
    return [leftId, rightId]

def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num < array[i - 1] or num > array[i + 1]

array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print subarraySort(array)