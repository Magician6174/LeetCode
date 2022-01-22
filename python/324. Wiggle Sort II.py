class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        h = len(nums[::2])
        nums1 = nums[:h][::-1]
        nums2 = nums[h:][::-1]
        print(nums1,nums2)
        j,k = 0,0
        for i in range(0,len(nums),2):
            nums[i] = nums1[j]
            j+=1
        for i in range(1,len(nums),2):
            nums[i] = nums2[k]
            k += 1

