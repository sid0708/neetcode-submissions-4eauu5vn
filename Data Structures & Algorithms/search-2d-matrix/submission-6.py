class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        abc = []
        for sub in matrix:
            for ele in sub:
                abc.append(ele)
        L = 0
        R = len(abc) -1
        while L <=R:
            mid = (L +R)//2
            if abc[mid] == target:
                return True
            elif target > abc[mid]:
                L = mid+1
            else:
                R = mid-1
        return False
