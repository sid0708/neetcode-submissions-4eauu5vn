from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        print(m.most_common(k))
        return [keys for (keys,v) in m.most_common(k) ]



        