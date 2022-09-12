class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        from collections import Counter
        d = Counter(words)
        ans = 0
        fdiff = False
        for i in d.keys():
            if i[::-1] in d.keys() and i[0] != i[1]:
                ans += min(d[i],d[i[::-1]])*4
                fdiff = True
                d[i] = 0
                d[i[::-1]] = 0
        
        ans2 = 0
        fdiff2 = False
        for i in d.keys():
            if i[0] == i[1]:
                if d[i]%2 != 0 and not fdiff2:
                    ans2 += (d[i]-1)*2+2
                    fdiff2 = True
                else:
                    if d[i]%2==0:
                        ans2+= d[i]*2
                    else:
                        ans2 += (d[i]-1)*2
            
        return ans+ans2
                
            
