class Solution:
    def interpret(self, command: str) -> str:
        
        ans = ''
        j = 0
        while j < len(command):
            if command[j] == 'G':
                ans += 'G'
                j += 1
            elif command[j] == '(' and command[j+1] == ')':
                ans += 'o'
                j += 2
            else:# command[j] == '(' and command[j+1] == 'a':
                ans += 'al'
                j += 4
        return ans
