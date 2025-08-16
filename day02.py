def missing_number_sum(arr):
    n = len(arr) + 1              
    expected = n * (n + 1) // 2  
    return expected - sum(arr)

def missing_number_xor(arr):
    n = len(arr) + 1
    xor_all = 0
    # XOR 1..n
    for i in range(1, n + 1):
        xor_all ^= i
    
    for x in arr:
        xor_all ^= x
    return xor_all

# --- ---
tests = [
    ([1, 2, 4, 5], 3),            # Test Case 1
    ([2, 3, 4, 5], 1),            # Test Case 2
    ([1, 2, 3, 4], 5),            # Test Case 3
    ([1], 2),                     # Test Case 4
    (list(range(1, 1_000_000)), 1_000_000),  # Test Case 5 (conceptual; large)
]

for arr, expected in tests:
    a = missing_number_sum(arr)
    b = missing_number_xor(arr)
    assert a == expected and b == expected, f"Failed on {arr[:10]}... -> got {a},{b}, expected {expected}"
