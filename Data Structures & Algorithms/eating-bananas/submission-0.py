from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        while L < R:
            mid = (L+R) //2
            if h >= self.getTime(piles, mid):  # so mid works
                R = mid
            elif h < self.getTime(piles, mid): # mid doesnt work
                L = mid +1
        return L
            





    def getTime(self, piles, k):
        time = 0
        for each in piles:
            if each!=0:
                time += (each + k-1) // k
        return time