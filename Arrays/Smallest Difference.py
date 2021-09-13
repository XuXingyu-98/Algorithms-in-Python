def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idOne = 0
    idTwo = 0
    smallest = float("inf")
    smallestPair = []
    while idOne < len(arrayOne) and idTwo < len(arrayTwo):
        first = arrayOne[idOne]
        second = arrayTwo[idTwo]
        if first < second:
            current = second - first
            idOne += 1
        elif second < first:
            current = first - second
            idTwo += 1
        else:
            return [first, second]
        if smallest > current:
            smallest = current
            smallestPair = [first, second]
    return smallestPair

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
print smallestDifference(arrayOne, arrayTwo)

