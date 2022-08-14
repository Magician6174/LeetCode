class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack_s = []
        for i in range(len(s)):
            if s[i] == '#':
                if stack_s:
                    stack_s.pop()

            else:
                stack_s.append(s[i])
        stack_t = []
        for i in range(len(t)):
            if t[i] == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(t[i])
        return stack_s == stack_t
