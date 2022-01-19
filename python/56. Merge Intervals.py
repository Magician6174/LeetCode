class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack_ = []
        # Let T = [0,2] then si = 0 and ei = 2
        # Make sure that the start of every time interval is smaller than the next one so sort
        a = sorted(intervals,key=lambda k: k[0])
        # print(a) 
        for T in a:
            if len(stack_) == 0:
                stack_.append(T)
            else:
                prev_T = stack_.pop()
                if prev_T[-1] >= T[0]:
                    # since start of every time interval is already sorted so just append prev_T[0]
                    stack_.append([prev_T[0],max(prev_T[-1],T[-1])])
                else:
                    stack_.append(prev_T)
                    stack_.append(T)
        return stack_