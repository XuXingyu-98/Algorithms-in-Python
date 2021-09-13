def rightSmallerThan(array):
    if len(array) == 0:
        return []
    lastId = len(array) - 1
    rightSmallerCounts = array[:]
    bst = SpecialBST(array[lastId])
    rightSmallerCounts[lastId] = 0
    for i in reversed(range(len(array) - 1)):
        bst.insert(array, i, rightSmallerCounts)
    return rightSmallerCounts

class SpecialBST:
    def __init__(self, value):
        self.value = value
        self.leftTreeSize = 0
        self.left = None
        self.right = None 

    def insert(self, value, id, rightSmallerCounts, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftTreeSize += 1
            if self.left is None:
                self.left = SpecialBST(value)
                rightSmallerCounts[id] = numSmallerAtInsertTime
            else:
                self.left.insert(value, id, rightSmallerCounts, numSmallerAtInsertTime)
        else:
            numSmallerAtInsertTime += self.leftTreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
            if self.right is None:
                self.right = SpecialBST(value)
                rightSmallerCounts[id] = numSmallerAtInsertTime
            else:
                self.right.insert(value, id, rightSmallerCounts, numSmallerAtInsertTime)

