
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for each in strs:
            sorted_str = ''.join(sorted(each))
            if sorted_str not in group:
                group[sorted_str] = []
            group[sorted_str].append(each)
        return group.values()

        