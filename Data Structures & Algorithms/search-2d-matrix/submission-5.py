class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix = [val for sub in matrix for val in sub]
        L = 0
        R = len(matrix) -1
        while L <=R:
            mid = (L+R) //2
            if matrix[mid] < target:
                L = mid +1
            elif matrix[mid] > target:
                R = mid -1
            else:
                return True
        return False 


