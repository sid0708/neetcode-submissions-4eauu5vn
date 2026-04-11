
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for each in nums:
            freq[each] = 1 + freq.get(each, 0)
        return sorted(freq, key=freq.get, reverse=True)[:k]



        