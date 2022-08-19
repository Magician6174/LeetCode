class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        from collections import Counter
        pd = Counter(p)
        pl = len(p)
        sl = len(s)
        
        if pl > sl:
            return []
        for i in range(pl-1):
            if s[i] in pd:
                pd[s[i]] -= 1
        
        ans = []
        for i in range(-1,sl-pl+1):
            
            if i > -1 and s[i] in pd:
                pd[s[i]] += 1

            if i+pl < sl and s[i+pl] in pd:
                pd[s[i+pl]] -= 1
            
            if all(j==0 for j in pd.values()):
                ans.append(i+1)
        return ans
        
        

#         from collections import Counter
#         pd = Counter(p)
#         ans = []
#         l = len(p)
#         for i in range(len(s)-l+1):
#             temp_s = s[i:i+l]
#             if pd == Counter(temp_s):
#                 ans.append(i)
#         return ans
            
            
            
