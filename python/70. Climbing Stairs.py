class Solution:
    def climbStairs(self, n: int) -> int:

        
        if n==1:
            return 1
        if n==2:
            return 2
        d = {1:1,2:2}
        ways = 0
        for i in range(3,n+1):
            ways = d[i-1] + d[i-2]
            d[i] = ways
        return ways
        # if n == 1:
        #     return 1 
        # if n == 2:
        #     return 2 
        # return self.climbStairs(n-1) +self.climbStairs(n-2)
        
        
