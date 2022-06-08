class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f = 0
        l = 1
        k = 1
        for i in range(1,len(nums)):
            if nums[f] == nums[l]:
                l += 1
            else:
                f += 1
                nums[f] = nums[l]
                l += 1
                k += 1
        return k
            
