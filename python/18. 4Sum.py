class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for i in range(n):
            for j in range(i+1,n):
                l = j+1
                r = n-1
                while l < r:
                    sum4 = nums[i]+nums[j]+nums[l]+nums[r]
                    if sum4 == target:
                        output.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1
                    elif sum4 > target:
                        r -=1
                    else:
                        l+=1
        return set([tuple(x) for x in output])