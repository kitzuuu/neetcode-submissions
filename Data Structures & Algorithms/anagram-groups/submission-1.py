class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        if len(strs)<=1:
            return [strs]
        for word in strs:
            key = "".join(sorted(word))
            anagram_map[key].append(word)
        return list(anagram_map.values())

