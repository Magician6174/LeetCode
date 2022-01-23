class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums))
        
        max = -2**31
        # max_index = 0
        # for i in range(len(nums)):
        #     if nums[i] > max:
        #         max = nums[i]
        #         max_index = i
        # return max_index
        
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        if nums[0] > nums[len(nums)-1]:
            return 0
        else:
            return len(nums)-1
        
