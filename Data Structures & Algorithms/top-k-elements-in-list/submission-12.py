from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict(Counter(nums))
        return sorted(freq, key=freq.get, reverse=True)[:k]



        