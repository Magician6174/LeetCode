class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
# """-------------------------TC - O(n) SC - O(1)-------------------------------"""        

        i = -1
        for j in range(len(asteroids)):
            while i >= 0 and asteroids[i] > 0 and asteroids[j] < 0:
                if asteroids[i] < abs(asteroids[j]):
                    i-=1
                    continue
                elif asteroids[i] == abs(asteroids[j]):
                    i-=1
                break
            else:
                asteroids[i + 1] = asteroids[j] # inserting the asteroid
                i += 1
        return asteroids[:i+1]

"""-------------------------TC - O(n) SC - O(n)-------------------------------"""
#         result = []
#         for new in asteroids:
            
#             while result and new < 0 < result[-1]:
#                 if result[-1] < abs(new):
#                     result.pop()
#                     continue
#                 elif result[-1] == abs(new):
#                     result.pop()
#                 break
#             else:
#                 result.append(new)
        
        
#         return result
        
        
"""------------------------------------Misinterpreted question----------------------------"""
        # stack = []
        # n = len(asteroids)
        # for i in range(n):
        #     check = 0
        #     while stack:
        #         if stack[-1] > 0 and asteroids[i] < 0:
        #             if stack[-1] < abs(asteroids[i]):
        #                 stack.pop()
        #             elif stack[-1] == abs(asteroids[i]):
        #                 check = 1
        #                 stack.pop()
        #                 break
        #             else:
        #                 check = 1
        #                 break
        #         elif stack[-1] < 0 and asteroids[i] > 0:
        #             if abs(stack[-1]) < asteroids[i]:
        #                 stack.pop()
        #             elif abs(stack[-1]) == asteroids[i]:
        #                 check = 1
        #                 stack.pop()
        #                 break
        #             else:
        #                 check = 1
        #                 break
        #         else:
        #             break
        #     if check != 1:
        #         stack.append(asteroids[i])
        # return stack
