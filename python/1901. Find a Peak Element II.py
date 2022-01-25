class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        # max = -1
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j] > max:
        #             max = mat[i][j]
        #             max_r, max_c = i,j
        # return [max_r, max_c]
        
        startcol = 0
        endcol = len(mat[0]) - 1
        
        while startcol <= endcol:
            # midcol = startcol + (endcol - startcol) // 2
            midcol = (startcol + endcol) // 2
            
            maxrowidx = 0
            for row in range(len(mat)):
                if mat[row][midcol] >= mat[maxrowidx][midcol]:
                    maxrowidx = row
            # print(startcol,midcol,endcol)
            if ((midcol-1) >= startcol) and (mat[maxrowidx][midcol-1] > mat[maxrowidx][midcol]):
                endcol = midcol - 1
            
            elif ((midcol+1) <= endcol) and (mat[maxrowidx][midcol+1] > mat[maxrowidx][midcol]):
                startcol = midcol + 1
            else:
                return [maxrowidx,midcol]
