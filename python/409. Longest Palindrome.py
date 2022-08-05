class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        max_len = 0
        n = len(s)
        for i in d.values():
            max_len += (i // 2)*2
            n -= (i//2) * 2
        if n>0:
            return max_len + 1
        return max_len
                
