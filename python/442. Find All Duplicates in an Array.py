class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        nums_sorted = sorted(nums)
        output = []
        
        for i in range(1,len(nums)):
            
            if nums_sorted[i-1] == nums_sorted[i]:
                output.append(nums_sorted[i])
        
        return output
    
        """Very Nice Solution Below"""

        # res = []
        # for x in nums:
        #     if nums[abs(x)-1] < 0:
        #         res.append(abs(x))
        #     else:
        #         nums[abs(x)-1] *= -1
        # return res