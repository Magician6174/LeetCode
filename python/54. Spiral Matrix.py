class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        IR,IC,DR,DC = False, True, False, False
        SR,SC,ER,EC = 0,0,len(matrix)-1, len(matrix[0])-1
        n_ele = len(matrix)*len(matrix[0])
        i,j = 0,0
        ans = []
        def get_next_ind(i,j,IR,IC,DR,DC):
            if IR:
                i+=1
            if IC:
                j+=1
            if DR:
                i-=1
            if DC:
                j-=1
            return i,j
        
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                ans.append(matrix[i][0])
            return ans
            
        while n_ele>=1:
            ans.append(matrix[i][j])
            n_ele -= 1
            if j == EC and IC:
                IC,IR = False, True
                EC-=1
            if i == ER and IR:
                IR,DC = False, True
                ER-=1
            if j == SC and DC:
                DC,DR = False, True
                SC += 1
            if i == SR+1 and DR:
                DR,IC = False, True
                SR += 1
            i,j = get_next_ind(i,j,IR,IC,DR,DC)
        return ans
        
