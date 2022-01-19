class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 1
        n = len(s)
        max = 0
        l=[]
        while start < end and end < n+1:
            
            w = list(s[start:end])
            if w[-1] not in l:
                end +=1
                l = w
                
            else:
                start += 1
                l = list(s[start:end-1]) 
                
            if len(l)>max:
                max = len(l)
            
        return max