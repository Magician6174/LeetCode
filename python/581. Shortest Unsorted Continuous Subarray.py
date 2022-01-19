class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
#         start = len(nums)
#         end = 0
        
#         for i in range(len(nums)):
            
#             for j in range(i+1,len(nums)):
                
#                 if nums[i] > nums[j]:
#                     start = min(i,start)
#                     end = max(j,end)
#         ans = end -start+1
#         if ans<0:
#             return 0
#         return ans
        
#         start = len(nums)
#         end = 0
#         nums_sorted = sorted(nums)
        
#         for i in range(len(nums)):
#             if nums[i] == nums_sorted[i]:
#                 continue
#             else:
#                 start = min(start,i)
#                 end = max(end,i)
            
#         ans = end -start+1
#         if ans<0:
#             return 0
#         return ans

        start = len(nums)
        end = 0
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start,stack.pop())
            stack.append(i)
        stack =[]
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end,stack.pop())
            stack.append(i)
        
        ans = end -start+1
        if ans<0:
            return 0
        return ans
        