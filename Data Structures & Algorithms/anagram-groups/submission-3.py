from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        z = defaultdict(list)
        for each in strs:
            m = "".join(sorted(each)) 
            z[m].append(each)
        return list(z.values())
            
     


        