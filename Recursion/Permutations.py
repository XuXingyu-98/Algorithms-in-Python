def getPermutations(array):
    permutations = []
    permutationsRecursive(array, [], permutations)
    return permutations

def permutationsRecursive(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
        return
        
    for i in range(len(array)):
        newArray = array[:i] + array[i + 1:]
        newPermutation = currentPermutation + [array[i]]
        permutationsRecursive(newArray, newPermutation, permutations)
    return

array = [1, 2, 3]
print getPermutations(array)
