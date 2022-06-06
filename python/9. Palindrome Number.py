class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_num = 0
        while reversed_num < x:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x = x // 10
        if x == reversed_num or( x == reversed_num // 10):
            return True
        return False
        """---------------with string--------------"""
        # s = x.__repr__()
        # n = len(s)
        # for f in range(n):
        #     l = n - 1 - f
        #     if s[f] != s[l]:
        #         return False
        # return True
