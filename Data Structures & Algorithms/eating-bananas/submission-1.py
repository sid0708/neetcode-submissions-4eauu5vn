class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        piles = sorted(piles)
        while L <=R:
            mid = (L+R)//2
            k = mid
            if self.canFinish(piles,k,h):
                R = mid - 1
            else:
                L = mid +1
        return L

    def canFinish(self, piles, k, h):
        total = 0
        for pile in piles:
            total += (pile + k - 1) // k
        if total <=h:
            return True
        return False
        