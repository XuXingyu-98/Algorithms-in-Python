def invertBinaryTree(tree):
    if tree is None:
        return
    swap(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree

def swap(node):
    node.left, node.right = node.right, node.left

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None