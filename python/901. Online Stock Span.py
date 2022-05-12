class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []
        self.count = 0
        

    def next(self, price: int) -> int:
        self.prices.append(price)
        if len(self.prices) == 1:
            self.stack.append(self.count)
            self.count += 1
            return 1
        else:
            while len(self.stack) and self.prices[self.stack[-1]] <= price:
                indx = self.stack.pop()
            if len(self.stack):
                span = self.count - self.stack[-1]
            else:
                span = self.count+1
            self.stack.append(self.count)
            self.count += 1
            return span
            
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
"""--------------------------------BRUTE FORCE-------------------------------------"""
# class StockSpanner:

#     def __init__(self):
#         self.stack = []
        

#     def next(self, price: int) -> int:
#         span = 1
#         i = -1
#         if len(self.stack) == 0:
#             self.stack.append(price)
#             return span
#         else:
#             while abs(i) <= len(self.stack) and price >= self.stack[i]:
#                 span += 1
#                 i -= 1
#             self.stack.append(price)
#             return span


# # Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# # p = [100,80,60,70,60,75,85]
# p = [31,41,48,59,79]
# for price in p:
#     param_1 = obj.next(price)
#     print(param_1)