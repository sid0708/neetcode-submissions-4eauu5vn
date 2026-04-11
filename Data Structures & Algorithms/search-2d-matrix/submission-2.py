class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = [item for sub  in matrix for item in sub]
        L = 0
        R= len(lst) -1
        while L <=R:
            mid = (L +R)//2
            if lst[mid] > target:
                 R = mid -1
            elif lst[mid] < target:
                L = mid +1       
            else:
                return True
        return False
        