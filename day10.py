from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    return list(anagram_map.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)
