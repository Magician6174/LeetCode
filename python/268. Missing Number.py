class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # s = sum(nums)
        n = len(nums)
        # ts = n*(n+1)/2
        # return int(ts - s)
        ans = 0
        for i in range(n):
            ans = ans ^ i ^ nums[i]
        return ans ^ i+1
