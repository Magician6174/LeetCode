class Solution:
    def reorganizeString(self, s: str) -> str:
        
        from collections import Counter
        from heapq import heappop, heappush
        d = Counter(s)
        maxheap = [(-v,k) for k,v in d.items()]
        
        prev_v,prev_k = 0, ""
        ans = ''
        heapify(maxheap)
        while maxheap:
            
            v,k = heappop(maxheap)
            ans += k
            if prev_v < 0:
                heappush(maxheap,(prev_v,prev_k))
            
            v += 1 # adding because stored as negatives
            prev_v,prev_k = v,k
        if len(ans) != len(s): 
            return ""
        return ans
