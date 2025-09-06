from collections import deque

def sliding_window_maximum(arr, k):
    dq = deque()
    result = []

    for i in range(len(arr)):
        # Remove elements out of current window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements (not useful)
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # Add current element index
        dq.append(i)

        # Append max for current window
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

# Test cases
print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(sliding_window_maximum([1, 5, 3, 2, 4, 6], 3))          # [5, 5, 4, 6]
print(sliding_window_maximum([1, 2, 3, 4], 2))                # [2, 3, 4]
print(sliding_window_maximum([7, 7, 7, 7], 1))                # [7, 7, 7, 7]
