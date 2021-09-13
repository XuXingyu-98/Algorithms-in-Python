def minHeightBst(array):
    return constructMinHeightBst(array, 0, len(array) - 1)

def constructMinHeightBst(array, startId, endId):
    if endId < startId:
        return None
    midId = (startId + endId) // 2
    bst = BST(array[midId])
    bst.left = constructMinHeightBst(array, startId, midId)
    bst.right = constructMinHeightBst(array, midId + 1, endId)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self