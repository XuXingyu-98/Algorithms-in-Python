def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for n in array:
        nums[n] = True
    for n in array:
        if not nums[n]:
            continue
        nums[n] = False
        currentLength = 1
        left = n - 1
        right = n + 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print largestRange(array)