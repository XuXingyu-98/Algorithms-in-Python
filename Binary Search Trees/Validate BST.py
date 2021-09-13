class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    return validateBstR(tree, float("-inf"), float("inf"))

def validateBstR(tree, min, max):
    if tree is None:
        return True
    if tree.value > max and tree.value < min:
        return False
    return validateBstR(tree.left, min, tree.value) and validateBstR(tree.right, tree.value, max)

