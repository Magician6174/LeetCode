class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char,1])
        return ''.join([stack[i][0]*stack[i][1] for i in range(len(stack))])
        
        
        """---------------------------Second Attempt ----------------------------"""
        # stack = []
        # for i in range(len(s)):
        #     stack.append(s[i])
        #     while len(stack) >= k and stack[-k:] == [s[i] for j in range(k)]:
        #         for i in range(k):
        #             stack.pop()
        # return ''.join(stack)
        
        """-------------------------------First Attempt------------------------"""
        # temp = 1
        # for i in range(1,len(s)):
        #     if s[i] == s[i-1]:
        #         temp += 1
        #     else:
        #         temp = 1
        #     if temp == k:
        #         new_s = s[:i-k+1] + s[i+1:]
        #         return self.removeDuplicates(new_s,k)
        # return s
