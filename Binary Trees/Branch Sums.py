class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    calculateHelper(root, 0, sums)
    return sums

def calculateHelper(node, current, sums):
    if node is None:
        return

    newCurrent = current + node.value
    if node.left is None and node.right is None:
        sums.append(newCurrent)
        return
    
    calculateHelper(node.left, newCurrent, sums)
    calculateHelper(node.right, newCurrent, sums)
    
