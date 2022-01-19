class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        output = []
        n = len(nums)
        # Using Two pointer approach
        sorted_a = sorted(nums)
        closest = 999
        for i in range(n-1):
            l = i+1
            r = n-1
            while l < r:
                sum_3 = sorted_a[l]+sorted_a[r]+sorted_a[i]
                closest_n = min(closest,abs(target-sum_3))
                if closest_n < closest:
                    output = sum_3
                    closest = closest_n
                elif sum_3 < target:
                    l += 1
                else:
                    r -=1
        return output