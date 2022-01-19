class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        arr = []
        # for i in nums:
        #     if i not in d.keys():
        #         d[i] = 1
        #         arr.append(i)
        #     else:
        #         d[i] += 1
        #         arr.remove(i)
        # return arr
        
        for i in nums:
            if i not in arr:
                arr.append(i)
            else:
                arr.remove(i)
        return arr
        