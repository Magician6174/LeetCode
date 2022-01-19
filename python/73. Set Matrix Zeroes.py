from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = matrix
        row_flag = False
        coloumn_flag = False
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i ==0 and mat[i][j] ==0:
                    row_flag = True
                if j == 0 and mat[i][j] == 0:
                    coloumn_flag = True
                if mat[i][j] == 0:
                    mat[0][j] = 0
                    mat[i][0] = 0
        for i in range(1,len(mat)):
            for j in range(1,len(mat[0])):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        if row_flag:
            i = 0
            for j in range(len(mat[0])):
                mat[i][j] = 0
        if coloumn_flag:
            j = 0
            for i in range(len(mat)):
                mat[i][j] = 0
        print(mat)