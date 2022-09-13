class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        from collections import Counter
        from heapq import nlargest
        d = Counter(nums)
        counts = d.items()
        ans = nlargest(k,counts,key=lambda x: x[1])
        return [i[0] for i in ans]
        
        
        """-------------------First Try-----------------"""
        # d = {}
        # for i in nums:
        #     if i not in d.keys():
        #         d[i] = 1
        #     else:
        #         d[i] += 1
        # return sorted(d,key=lambda k: d[k], reverse = True)[:k]
