import math

def merge_inplace(arr1, arr2):
    m, n = len(arr1), len(arr2)
    total = m + n

    def next_gap(gap):
        if gap <= 1:
            return 0
        return math.ceil(gap / 2)

    gap = next_gap(total)
    while gap > 0:
        i, j = 0, gap
        while j < total:
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]
            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]
            i += 1
            j += 1
        gap = next_gap(gap)
    return arr1, arr2
