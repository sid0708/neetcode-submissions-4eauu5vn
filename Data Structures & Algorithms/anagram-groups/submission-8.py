from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for each in strs:
            key = "".join(sorted(each))
            cache[key].append(each)
        return list(cache.values())
            
        

        