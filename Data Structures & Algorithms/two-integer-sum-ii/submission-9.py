class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        # 0 index
        res = []
        L = 0
        R = len(n) -1
        while L <R:
            if n[L] + n[R] > target:
                R -=1
            elif n[L] + n[R] < target:
                L += 1
            else:
                return [L+1, R+1]



            
        