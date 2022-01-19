class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = sorted(nums)
        for i in range(len(nums)):
            diff = target -nums[i]
            if diff in nums:
                if i == nums.index(diff):
                    continue
                return [i,nums.index(diff)]
                
    
