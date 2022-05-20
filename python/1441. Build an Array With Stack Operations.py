class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        j=0
        for i in range(n):
                if j >= len(target):
                    return output
                if i+1 == target[j]:
                    output.append('Push')
                    j+=1
                else:
                    output.append('Push')
                    output.append('Pop')
                
        return output
