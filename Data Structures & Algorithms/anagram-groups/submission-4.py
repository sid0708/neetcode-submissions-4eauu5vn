from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordCounter = defaultdict(list)
        for each in strs:
            m = "".join(sorted(each))
            wordCounter[m].append(each)
        return list(wordCounter.values())

            
        



  
            
     


        