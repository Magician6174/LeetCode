class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        TS = sum(nums)
        sum_left = 0
        for i in range(len(nums)):
            if sum_left == TS - sum_left - nums[i]:
                return i
            sum_left += nums[i]
        return -1
        
        
        # sum_left = 0
        # for i in range(len(nums)):
        #     if sum_left == sum(nums[i+1:]):
        #         return i
        #     sum_left += nums[i]
        # return -1
