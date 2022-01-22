class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        return sorted(sorted(d),key=lambda k: d[k], reverse=True)[:k]
        
