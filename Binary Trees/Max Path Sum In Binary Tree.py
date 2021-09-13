def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
    return maxSum

def findMaxSum(tree):
    if tree is None:
        return (0, float("-inf"))
    
    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChilSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    maxSumAsBranch = max(maxChilSumAsBranch + tree.value, tree.value)
    maxSumAsRootNode = max(maxSumAsBranch, tree.value + leftMaxSumAsBranch + rightMaxSumAsBranch)
    maxPathSum = max(maxSumAsRootNode, leftMaxPathSum, rightMaxPathSum)
    return (maxSumAsBranch, maxPathSum)