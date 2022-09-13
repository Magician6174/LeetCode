class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        from heapq import nsmallest
        dist = []
        for i in points:
            d = (i[0]**2+i[1]**2)
            dist.append((d,i))
        ns = nsmallest(k,dist)
        
        return [i[1] for i in ns]
