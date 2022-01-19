class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        output = [-1,-1]
        
        
        for i,j in enumerate(nums):
            if j == target:
                output[0] = i
                break


        if len(nums)!=0:
            for i in range(output[0],len(nums)):
                if nums[i] == target:
                    output[1] = i
                else:
                    break
        return output
                
        