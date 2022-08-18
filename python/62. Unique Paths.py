class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n==1:
            return 1
        list1 = []
        for i in range(m):
            list1.append([])
            for j in range(n):
                list1[i].append(0)
                if i == m-1 or j==(n-1):
                    list1[i][j] = 1
            
        list1[-1][-1] = 0
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                list1[i][j] = list1[i+1][j] + list1[i][j+1]
        return list1[0][0]

#         def dfs(i, j):
#             if i >= m or j >= n:      return 0
#             if i == m-1 and j == n-1: return 1
#             return dfs(i+1, j) + dfs(i, j+1)
#         return dfs(0, 0)
        
