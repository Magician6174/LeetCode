class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        i = 0
        while i < len(heights):
            if (not stack) or (heights[i] >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                top_ = stack.pop()
                area = heights[top_] * ((i-stack[-1] - 1) if stack else i)
                if area > max_area:
                    max_area = area
        while stack:
            top_ = stack.pop()
            area = heights[top_] * ((i-stack[-1] - 1) if stack else i)
            if area > max_area:
                max_area = area
        return max_area
        """--------------------Brute Force-----------------------"""
#         max_area = 0
#         for i, current in enumerate(heights):
#             left_index = i-1
#             right_index = i+1
#             while left_index >= 0:
#                 if heights[left_index] >= current:
#                     left_index -= 1
#                 else:
#                     left_index += 1
#                     break
#             if left_index < 0:
#                 left_index = 0
#             while right_index < len(heights):
#                 if heights[right_index] >= current:
#                     right_index += 1
#                 else:
#                     break
#             area = current * (right_index - left_index)
#             if area > max_area:
#                 max_area = area
        
#         return max_area
