import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        piles = sorted(piles)
        while L <=R:
            mid = (L+R)//2
            if self.totaltime(piles, mid, h):
                R = mid -1
            else:
                L = mid+1
        return L


    def totaltime(self, piles, k, h):
        total = 0
        for each in piles:
            total += math.ceil(each/k)
        if total <= h:
            return True
        return False

