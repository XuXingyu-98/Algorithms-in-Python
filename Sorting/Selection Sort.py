def selectionSort(array):
    currentId = 0
    while currentId < len(array) - 1:
        smallestId = currentId
        for i in range(currentId + 1, len(array)):
            if array[smallestId] > array[i]:
                smallestId = i
        swap(currentId, smallestId, array)
        currentId += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [8, 5, 2, 9, 5, 6, 3]
selectionSort(array)
print array