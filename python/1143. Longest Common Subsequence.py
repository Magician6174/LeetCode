class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        L = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i][j-1],L[i-1][j])
        return L[len(text1)][len(text2)]
        

        """----------------------Using Recursion-------------------------------"""
        # if text1 == '' or text2 == '':
        #     return 0
        # if text1[-1] == text2[-1]:
        #     return self.longestCommonSubsequence(text1[:-1],text2[:-1]) + 1
        # else:
        #     return max(self.longestCommonSubsequence(text1,text2[:-1]),self.longestCommonSubsequence(text1[:-1],text2))
