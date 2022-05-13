class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n-1,-1,-1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                
                days += answer[curr_day + days]
                
            answer[curr_day] = days
        
        return answer
    
"""------------------------------------SOLUTION - 2-----------------------------"""


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0]*len(temperatures)
#         stack = []
#         for i, temp in enumerate(temperatures):
            
#             while stack and temperatures[stack[-1]] < temp:
#                 idx = stack.pop()
#                 answer[idx] = i - idx
#             stack.append(i)
        
#         return answer
