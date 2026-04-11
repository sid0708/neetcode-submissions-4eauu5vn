
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for words in strs:
            groups["".join(sorted(words))].append(words)
        return list(groups.values())


        