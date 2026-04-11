
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for each in nums:
            freq[each] = freq.get(each, 0) + 1
        return sorted(freq, key=freq.get, reverse=True)[:k]


        