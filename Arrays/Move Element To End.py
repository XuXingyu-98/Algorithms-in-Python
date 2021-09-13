def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        while left < right and array[right] == toMove:
            right -= 1 
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1
    return array
    
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
print moveElementToEnd(array, toMove)
