class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        lst = []
        for i in l:
            if len(i) != 0:
                lst.append(i)
        lst.reverse()
        return ' '.join(lst)
        
