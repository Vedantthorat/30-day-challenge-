def permuteUnique(s):
    res = []
    s = sorted(s)
    used = [False] * len(s)day11

    def backtrack(path):
        if len(path) == len(s):
            res.append("".join(path))
            return
        for i in range(len(s)):
            if used[i] or (i > 0 and s[i] == s[i-1] and not used[i-1]):
                continue
            used[i] = True
            backtrack(path + [s[i]])
            used[i] = False

    backtrack([])
    return res
