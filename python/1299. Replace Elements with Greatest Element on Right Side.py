class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
#         output = [-1]
        
#         # for i in range(len(arr)-1):
#         #     arr_ = sorted(arr[i+1:])
#         #     output.append(arr_[-1])
#         # output.append(-1)
#         # return output
        
#         # for i in range(len(arr)-1):
#         #     max_ = max(arr[i+1:])
#         #     output.append(max_)
#         # output.append(-1)
#         # return output
#         max = -1
#         for i in range(-1,-len(arr),-1):
#             if arr[i] > max:
#                 max = arr[i]
#             output.insert(0,max)
#         return output
        
        output = list(arr)
        max = -1
        output[-1] = max
        for i in range(-1,-len(arr),-1):
            # output[i] = max
            if arr[i] > max:
                max = arr[i]
            output[i-1] = max
            
        return output
        