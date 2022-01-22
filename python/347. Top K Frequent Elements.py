class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        return sorted(d,key=lambda k: d[k], reverse = True)[:k]
