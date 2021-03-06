class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        neighbors = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for n in neighbors:
                    r = row+n[0]
                    c = col+n[1]
                    if (r<rows and r>=0) and (c < cols and c>=0) and abs(board[r][c])==1:
                        live_neighbors+=1
                if (board[row][col] == 1) and (live_neighbors>3 or live_neighbors<2):
                        board[row][col] = -1
                if (board[row][col] == 0) and (live_neighbors==3):
                        board[row][col] = 2
        
        print(board)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
