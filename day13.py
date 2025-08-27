def longest_palindrome(s: str) -> str:
    if not s or len(s) == 1:
        return s
    
    start, max_len = 0, 0
    
    def expand_from_center(left: int, right: int) -> None:
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
    
    for i in range(len(s)):
        # Odd length palindrome
        expand_from_center(i, i)
        # Even length palindrome
        expand_from_center(i, i + 1)
    
    return s[start:start + max_len]
