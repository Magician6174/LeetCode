class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        d = {}
        for i in range(len(s)):
                d[s[i]] = i
        v = {}
        stack.append(s[0])
        v[s[0]] = 1
        for i in range(1,len(s)):
            if s[i] not in v:
                while stack and s[i] < stack[-1] and  d[stack[-1]] > i:
                    top = stack.pop()
                    v.pop(top)
            
                v[s[i]] = 1
                stack.append(s[i])

        return ''.join(stack)
            
