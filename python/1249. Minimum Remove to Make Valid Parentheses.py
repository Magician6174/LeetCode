class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = list(s)
        stack = []
        for i,w in enumerate(s):
            if w == '(':
                stack.append(i)
            elif w == ')':
                if len(stack):
                    stack.pop()
                else:
                    l[i] = ''
        for j in stack:
            l[j] = ''
        return ''.join(l)
        
        """---------------------------SOLUTION 1------------------------------------------"""
        # stack = []
        # answer = ''
        # for i,w in enumerate(s):
        #     if w == '(':
        #         stack.append(i)
        #     elif w == ')':
        #         if len(stack) > 0 and s[stack[-1]] == '(':
        #             stack.pop()
        #         else:
        #             stack.append(i)
        # print(stack)
        # for i,w in enumerate(s):
        #     if i in stack:
        #         continue
        #     answer += w
        # return answer
