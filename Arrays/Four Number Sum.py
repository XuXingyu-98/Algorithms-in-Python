def fourNumberSum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            current = array[i] + array[j]
            diff = targetSum - current
            if diff in allPairSums:
                for pair in allPairSums[diff]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            current = array[i] + array[k]
            if current in allPairSums:
                allPairSums[current].append([array[k], array[i]])
            else:
                allPairSums[current] = [[array[k], array[i]]]
    return quadruplets

array = [7, 6, 4, -1, 1, 2]
target = 16
print fourNumberSum(array, target)