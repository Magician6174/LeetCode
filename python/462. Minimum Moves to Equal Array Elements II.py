import numpy as np
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums_sor = sorted(nums)
        if len(nums_sor) % 2 != 0:
            cmp = nums_sor[len(nums)//2]
        else:
            cmp = (nums_sor[len(nums)//2] + nums_sor[len(nums)//2 - 1])/2
        moves = 0
        for i in range(len(nums)):
            moves += abs((cmp - nums[i]))
            
        return int(moves)
                
        """--------------------Using Numpy-------------------"""
#         cmp = np.median(nums)
#         moves = 0
#         for i in range(len(nums)):
#             moves += abs((cmp - nums[i]))
            
#         return int(moves)
        
        """---------------------Brute Force-----------------------"""
        # answer = 99999999999
        # for i in range(len(nums)):
        #     moves = 0
        #     cmp = nums[i]
        #     for j in range(len(nums)):
        #         moves += abs((cmp -nums[j]))
        #     if moves < answer:
        #         answer = moves
        # return answer
