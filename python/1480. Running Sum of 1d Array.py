class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        j = 0
        for i in nums:
            s += i
            nums[j] = s
            j += 1
        return nums
