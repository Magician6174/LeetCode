class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # i = 1
        # nums.sort()
        # for j in nums:
        #     if j == i:
        #         i+=1
        # return i
        

        if 1 not in nums:
            return 1
        for i in range(len(nums)):
            if nums[i]<=0:
                nums[i]=1
            if nums[i]>len(nums):
                nums[i]=1
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1] *= -1
        print(nums)
        for i in range(1,len(nums)):
            if nums[i]>0:
                return i+1
        return i+2
                
