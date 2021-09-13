def isValidSubsequence(array, sequence):
    arrayId = 0
    seqId = 0
    while seqId < len(sequence) and arrayId < len(array):
        if sequence[seqId] == array[arrayId]:
            seqId += 1
        arrayId += 1
    return seqId == len(sequence)

array=[5, 1, 22, 25, 6, -1, 8, 10]
sequence=[1, 6, -1, 10]
print isValidSubsequence(array, sequence)