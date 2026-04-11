class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            mat = []
            for sublist in matrix:
                for items in sublist:
                    mat.append(items)
            L = 0
            R = len(mat) -1
    
            while L <=R:
                mid = (L+R)//2
                if target==mat[mid]:
                    return True
                elif target > mat[mid]:
                    L = mid +1
                elif target < mat[mid]:
                    R = mid -1
            return False
        