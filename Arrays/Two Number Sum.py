def twoNumberSum(array, targetSum):
    nums=[]
    for i in range(len(array)):
        n=targetSum-array[i]
        if n in nums:
            return [n, array[i]]
        nums.append(array[i])
    return []

array=[3, 5, -4, 8, 11, 1, -1, 6]
targetSum=10
nums=twoNumberSum(array, targetSum)
print nums