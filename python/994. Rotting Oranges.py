class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        queue = []
        minutes = 0
        fresh_oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        while queue and fresh_oranges > 0:
            
            minutes += 1
            for _ in range(len(queue)):
                r,c = queue.pop(0)
                for dr,dc in [[-1,0],[0,-1],[1,0],[0,1]]:

                    rr = r + dr
                    cc = c + dc

                    if rr < 0 or rr >= rows or cc <0 or cc >= cols:
                        continue
                    if grid[rr][cc] == 0 or grid[rr][cc] == 2:
                        continue

                    fresh_oranges -= 1
                    grid[rr][cc] = 2
                    queue.append((rr,cc))
        if fresh_oranges == 0:
            return minutes
        else:
            return -1
