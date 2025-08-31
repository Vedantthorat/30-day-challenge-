def prime_factorization(N):
    factors = []
    
    # Step 1: Divide by 2
    while N % 2 == 0:
        factors.append(2)
        N //= 2
    
    # Step 2: Divide by odd numbers
    i = 3
    while i * i <= N:
        while N % i == 0:
            factors.append(i)
            N //= i
        i += 2  # check only odd numbers
    
    # Step 3: If N is still > 1, it's a prime
    if N > 1:
        factors.append(N)
    
    return factors
print(prime_factorization(18))      # [2, 3, 3]
print(prime_factorization(30))      # [2, 3, 5]
print(prime_factorization(49))      # [7, 7]
print(prime_factorization(19))      # [19]
print(prime_factorization(64))      # [2, 2, 2, 2, 2, 2]
print(prime_factorization(123456))  # [2, 2, 2, 2, 2, 3, 643]
