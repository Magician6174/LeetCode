class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d = {}
        for i,j in zip(s,t):
            
            if i not in d.keys() and j not in d.values():
                d[i] = j

        for i in range(len(s)):
            if s[i] not in d.keys():
                return False
            if t[i] != d[s[i]]:
                return False
        return True
