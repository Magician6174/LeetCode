class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
#         output = []
#         for i in nums:
#             count = 0
#             for j in nums:
#                 if j < i:
#                     count += 1
#             output.append(count)
#         return output
        
#         nums_sorted = sorted(nums)
#         d={}
#         for i,j in enumerate(nums_sorted):
#             if j not in d.keys():
#                 d[j] = i
#             else:
#                 continue
#         output = []
#         for k in nums:
#             output.append(d[k])
            
#         return output

        # since in problem discription it is given that  0 <= nums[i] <= 100 so
        
        arr = [0] * 101
        
        for i in nums:
            arr[i] += 1
            
        # calculate prefix sum
        for i in range(1,101):
            arr[i] = arr[i-1] + arr[i]
        
        output = []
        for i in nums:
            if i == 0:
                output.append(0)
            else:
                output.append(arr[i-1])
        
        return output
        

        