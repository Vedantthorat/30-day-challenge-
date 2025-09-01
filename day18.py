import math

def count_divisors(N):
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i == N // i:
                count += 1  # perfect square divisor
            else:
                count += 2  # pair of divisors
    return count
print(count_divisors(12))   # 6
print(count_divisors(18))   # 6
print(count_divisors(29))   # 2
print(count_divisors(100))  # 9
print(count_divisors(1))    # 1
print(count_divisors(997))  # 2
