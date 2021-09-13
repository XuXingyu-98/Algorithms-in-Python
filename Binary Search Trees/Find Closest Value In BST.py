def findClosestValueInBST(tree, target):
    return findClosestValueInBSTR(tree, target, tree.value)

def findClosestValueInBSTR(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTR(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTR(tree.right, target, closest)
    else:
        return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None