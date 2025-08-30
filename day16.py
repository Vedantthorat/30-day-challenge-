import math

def lcm(n, m):
    return (n * m) // math.gcd(n, m)

# Example test cases
print(lcm(4, 6))         # 12
print(lcm(5, 10))        # 10
print(lcm(7, 3))         # 21
print(lcm(1, 987654321)) # 987654321
print(lcm(123456, 789012)) # 8117355456
