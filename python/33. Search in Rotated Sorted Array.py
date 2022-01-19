class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if target in nums:
            return nums.index(target)
        else:
            return -1