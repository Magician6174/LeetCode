# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # def update_n(x):
        #     if isBadVersion(x):
        #         return x
        #     else:
        #         return x
        start = 1
        end = n
        while start<end:
            z = start + ((end - start) // 2) 
            if isBadVersion(z):
                end = z
            else:
                start = z + 1
                # if isBadVersion(start+1):
                #     return(start+1)
        
        return start