class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        self.m = len(image)
        self.n = len(image[0])
        
        self.temp = image[sr][sc]
        if image[sr][sc] == color:
            return image
        self.dfs(image,sr,sc,color)
        return image
        
    def dfs(self,image,sr,sc,color):
        if self.temp == color:
            return image
        else:
            image[sr][sc] = color
        if sr+1 < self.m and image[sr+1][sc] == self.temp:
            self.dfs(image,sr+1,sc,color)
        if sr-1 >=0 and image[sr-1][sc] == self.temp:
            self.dfs(image,sr-1,sc,color)
        if sc+1 <self.n and image[sr][sc+1] == self.temp:
            self.dfs(image,sr,sc+1,color)
        if sc-1>=0 and image[sr][sc-1] == self.temp:
            self.dfs(image,sr,sc-1,color)
        
