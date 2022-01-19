class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        # Using Two pointer approach
        sorted_a = sorted(nums)

        for i in range(n-2):
            l = i+1
            r = n-1
            while l < r:
                if sorted_a[l]+sorted_a[r]+sorted_a[i] == 0:
                    output.append([sorted_a[l],sorted_a[r],sorted_a[i]])
                    l+=1
                    r-=1
                elif sorted_a[l]+sorted_a[r]+sorted_a[i] > 0:
                    r-=1
                else:
                    l+=1
        return set([tuple(x) for x in output])
