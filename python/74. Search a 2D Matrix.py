class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low = 0
        m,n = len(matrix),len(matrix[0])
        high = (m*n)-1
        
        while low <= high:
            mid = (low+high)//2
            r = mid//n
            c = mid - (n*r)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
