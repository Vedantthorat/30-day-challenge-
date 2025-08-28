def count_substrings_exactly_k(s, k):
    def at_most_k(s, k):
        n = len(s)
        count = {}
        left = 0
        result = 0

        for right in range(n):
            count[s[right]] = count.get(s[right], 0) + 1

            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            result += (right - left + 1)

        return result

    return at_most_k(s, k) - at_most_k(s, k - 1)


# Test Cases
print(count_substrings_exactly_k("pqpqs", 2))      # 7
print(count_substrings_exactly_k("aabacbebebe", 3)) # 10
print(count_substrings_exactly_k("a", 1))           # 1
print(count_substrings_exactly_k("abc", 3))         # 1
print(count_substrings_exactly_k("abc", 2))         # 2
