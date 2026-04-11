class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valueMap = {}
        for each in nums:
            if each not in valueMap:
                valueMap[each] = 1
            valueMap[each] += 1
        sorted_elements = sorted(valueMap, key=valueMap.get, reverse=True)
        return sorted_elements[:k]


        