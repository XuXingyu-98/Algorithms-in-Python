def LongestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        left = i - 1
        while left >= 1 and array[left] > array[left - 1]:
            left -= 1
        right = i + 1
        while right <= len(array) - 2 and array[right] > array[right + 1]:
            right += 1

        currentLength = right - left + 1
        longestPeakLength = max(longestPeakLength, currentLength)
        i = right

    return longestPeakLength

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print LongestPeak(array)
