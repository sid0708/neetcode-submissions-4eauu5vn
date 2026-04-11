from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        freq = defaultdict(list)
        for each in strs:
            key = " ".join(sorted(each))
            freq[key].append(each)
        return list(freq.values())

        