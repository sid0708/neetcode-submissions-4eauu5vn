from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        freq = defaultdict(list)
        for w in strs:
            key = "".join(sorted(w))
            freq[key].append(w)
        return list(freq.values())


        