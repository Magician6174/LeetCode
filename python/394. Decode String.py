class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            
            if s[i] == "]":
                st = ""
                while stack[-1] != "[":
                    top = stack.pop()
                    st += top

                stack.pop()
                n = ''
                while stack and stack[-1].isnumeric():
                    n += stack.pop()
                n = n[::-1]
                st = int(n) * st
                stack.append(st)
            
            else:
                stack.append(s[i])
        ans = ''
        for i in stack:
            ans += i[::-1]
        return ans
