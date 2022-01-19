class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+2,len(nums)):
#                 if nums[i] > nums[j]:
#                     return False
#         return True
        
        # cmax = 0
        # for i in range(len(nums) - 2):
        #     cmax = max(cmax, nums[i])
        #     if cmax > nums[i + 2]:
        #         return False
        # return True
        
        
        # Explanation at :https://leetcode.com/problems/global-and-local-inversions/discuss/1143422/JS-Python-Java-C%2B%2B-or-Simple-           # 3-Line-Solutions-w-Explanation
        for i in range(len(nums)):
            if i - nums[i] > 1 or i - nums[i] < -1: return False
        return True
        