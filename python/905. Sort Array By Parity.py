class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         even=[]
#         odd=[]
        
#         for i in nums:
#             if i%2 ==0:
#                 even.append(i)
#             else:
#                 odd.append(i)
        
#         return even + odd
        
#         output = []
#         for i in nums:
#             if i%2 ==0:
#                 output.insert(0,i)
#             else:
#                 output.append(i)
#         return output
        n = len(nums)
        i = 0
        j = n-1
        while i < j:
            if nums[i] % 2 != 0:
                nums[i],nums[j] = nums[j], nums[i]
                j -= 1
            else: 
                i += 1
        return nums