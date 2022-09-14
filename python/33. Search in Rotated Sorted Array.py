class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low+high)//2
            
            if (nums[mid] >= nums[0] and target >= nums[0]) or (nums[mid] < nums[0] and target < nums[0]): # same side
                comp = nums[mid]
            else:
                if target >= nums[0]:
                    comp = float('inf')
                else:
                    comp = -float('inf')
            
            if comp == target:
                return mid
            elif comp < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
          
        
        
        
        
        """----------------First try----------------------"""
        if len(nums) == 0:
            return -1
        if target in nums:
            return nums.index(target)
        else:
            return -1
