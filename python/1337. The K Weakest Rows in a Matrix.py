class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         sum_ = [sum(i) for i in mat]
#         # print(sum_)

#         index_ = [i for i in range(len(sum_))]
#         output = sorted(index_,key=lambda k: sum_[k])
#         return output[:k]
        sum_ = []
        for i in range(len(mat)):
            l = 0
            r = len(mat[0])
            while l < r:
                mid = l+(r-l) // 2
                if mat[i][mid] == 0:
                    r = mid 
                else:
                    l = mid + 1
            sum_.append(l)
        print(sum_)
        index_ = [i for i in range(len(sum_))]
        output = sorted(index_,key=lambda k: sum_[k])
        return output[:k]