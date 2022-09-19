class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.heights = heights
        self.pacific = set()
        self.atlantic = set()
        self.directions = [(1,0),(-1,0),(0,-1),(0,1)]
        rows,cols = len(heights), len(heights[0])
        
        for i in range(len(heights)):
            self.dfs(i,0,rows,cols,self.pacific)
            self.dfs(i,cols-1,rows,cols,self.atlantic)
        for j in range(len(heights[0])):
            self.dfs(0,j,rows,cols,self.pacific)
            self.dfs(rows-1,j,rows,cols,self.atlantic)
        return (self.pacific & self.atlantic)
        
        
    def dfs(self,i,j,rows,cols,visited):
        if (i,j) in visited:
            return
        visited.add((i,j))
        for x,y in self.directions:
            new_i,new_j = i+x, j+y
            if 0 <= new_i < rows and 0 <= new_j < cols and self.heights[new_i][new_j] >= self.heights[i][j]:
                self.dfs(new_i,new_j,rows,cols,visited)
