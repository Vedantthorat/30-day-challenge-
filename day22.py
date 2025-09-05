def first_element_to_repeat_k_times(arr, k):

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:
        if freq[num] == k:
            return num

    return -1


# Test Cases
print(first_element_to_repeat_k_times([3, 1, 4, 4, 5, 2, 6, 1, 4], 2))  # Output: 1
print(first_element_to_repeat_k_times([2, 3, 4, 2, 2, 5, 5], 2))        # Output: 5
print(first_element_to_repeat_k_times([1, 1, 1, 1], 1))                  # Output: -1
print(first_element_to_repeat_k_times([10], 1))                          # Output: 10
print(first_element_to_repeat_k_times([6, 6, 6, 6, 7, 7, 8, 8, 8], 3))   # Output: 8
