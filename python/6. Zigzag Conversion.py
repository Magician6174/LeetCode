class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        list_ = [[] for i in range(numRows)]
        count = 0
        # breakpoint()
        n = True
        for i, l in enumerate(s,1):
            # print(i%numRows)
            # print(count)
            list_[count].append(l)
            # print(n)
            if numRows == 1:
                if count == 0:
                    n = not n
                if n:
                    count -=1
                if count == numRows-1:
                    n = not n
                
                if not n:
                    count +=1
            else:
                if count == 0:
                    n = not n
                if count == numRows-1:
                    n = not n
                
                if n:
                    count -=1
                if not n:
                    count +=1
            


            # count += 1
        # print(list_)
        # breakpoint()
        llll = ''
        for i in range(numRows):
            llll += ''.join(list_[i])
        # llll = [''.join(list_[i] for i in range(numRows))]
        return llll
        