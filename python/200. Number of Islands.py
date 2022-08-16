class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.visited = {}
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.visited.keys():
                    self.visited[(i,j)] = 1
                    if grid[i][j] == "1":
                        island += 1
                        self.dfs(grid,i,j)
        return island
    
    def dfs(self,m,i,j):

        if i+1 < len(m) and (i+1,j) not in self.visited.keys():
            self.visited[(i+1,j)]=1
            if m[i+1][j] == "1":
                self.dfs(m,i+1,j)
        if i-1 >= 0 and (i-1,j) not in self.visited.keys():
            self.visited[(i-1,j)]=1
            if m[i-1][j] == "1":
                self.dfs(m,i-1,j)
        if j+1 < len(m[0]) and (i,j+1) not in self.visited.keys():
            self.visited[(i,j+1)] = 1
            if m[i][j+1] == "1":
                self.dfs(m,i,j+1)
        if j-1 >= 0 and (i,j-1) not in self.visited.keys():
            self.visited[(i,j-1)] = 1
            if m[i][j-1] == "1":
                self.dfs(m,i,j-1)

