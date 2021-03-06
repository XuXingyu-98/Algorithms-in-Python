def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest
    
def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftUpdate(threeLargest,  num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftUpdate(threeLargest, num, 0)

def shiftUpdate(array, num, id):
    for i in range(id + 1):
        if i == id:
            array[i] = num
        else:
            array[i] = array[i + 1]

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print findThreeLargestNumbers(array)
