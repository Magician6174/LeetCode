class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0,cost[-1]]
        for i in range(len(cost)-2,-1,-1):
            c = cost[i] + min(dp[-1],dp[-2])
            dp.append(c)
        if dp[-1] < dp[-2]:
            return dp[-1]
        else:
            return dp[-2]
