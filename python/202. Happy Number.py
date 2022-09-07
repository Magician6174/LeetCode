class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_sod(d):
            digits = d
            sod = 0
            while digits !=0 or digits%10 != 0:
                sod += (digits%10)**2
                digits = digits // 10
            return sod
        d = {}
        sod = get_sod(n)
        while sod != 1:
            n = sod
            if sod not in d.keys():
                d[sod] = 1
                sod = get_sod(n)
            else:
                return False
        return True
        
