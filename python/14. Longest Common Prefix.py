class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def get_common(s1,s2):
            s=""
            n = min(len(s1),len(s2))
            for i in range(n):
                if s1[i] == s2[i]:
                    s+= s1[i]
                else:
                    break
            return s
        if len(strs)==1:
            return strs[0]
        cs = get_common(strs[0],strs[1])
        for i in range(1,len(strs)):
            cs = get_common(cs,strs[i])
        return cs
            
