class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        answer = [-1] * len(nums)
        for i, current_num in enumerate(nums):
            while stack and nums[stack[-1]] < current_num:
                idx = stack.pop()
                answer[idx] = current_num
            stack.append(i)
        for i, current_num in enumerate(nums):
            while stack and nums[stack[-1]] < current_num:
                idx = stack.pop()
                answer[idx] = current_num
            stack.append(i)   
        return answer
