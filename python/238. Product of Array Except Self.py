class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [1]
        p = 1
        for i in range(1,n):
            p *= nums[i-1]
            output.append(p)
        p = 1
        for i in range(0,n):
            output[n-1-i] *= p
            p *= nums[n-1-i]
        return output