class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate90(matrix):
            matrix.reverse()
            # Calculat transpose
            for i in range(len(matrix)):
                for j in range(i+1,len(matrix[0])):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        if mat == target:
            return True
        for i in range(3):
            rotate90(mat)
            if mat == target:
                return True
        return False