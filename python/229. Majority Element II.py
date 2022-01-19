class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_n = n // 3
        a = []
        dict_ = {}
#         for i in nums:
#             if i not in dict_.keys():
#                 dict_[i] = 1
#             else:
#                 dict_[i] += 1
                
#         for i, j in dict_.items():
#             if j>max_n:
#                 a.append(i)
#         return a
        
        for i in nums:
            try:
                dict_[i] += 1
            except:
                dict_[i] = 1
        for i, j in dict_.items():
            if j>max_n:
                a.append(i)
        return a