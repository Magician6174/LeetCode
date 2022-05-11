class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def match(s1,s2):
            if s1 == '(' and s2 ==')':
                return True
            if s1 == '[' and s2 ==']':
                return True
            if s1 == '{' and s2 =='}':
                return True
            return False
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            if i == ')' or i == ']' or i == '}': 
                if len(stack) == 0:
                    return False
                else:
                    m = match(stack[-1], i)
                    if not m:
                        return False
                    else:
                        stack = stack[:-1]
        if len(stack) == 0:
            return True
        return False
