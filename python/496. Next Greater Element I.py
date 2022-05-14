class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        answer2 = [-1] * len(nums2)
        stack2 = []
        answer1 = []
        for i, current_num in enumerate(nums2):
            while stack2 and current_num > nums2[stack2[-1]]:
                idx = stack2.pop()
                answer2[idx] = current_num
            stack2.append(i)
        for i in nums1:
            idx1 = nums2.index(i)
            answer1.append(answer2[idx1])
        
        return answer1
                
