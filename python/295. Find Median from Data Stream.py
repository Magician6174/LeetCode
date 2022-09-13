class MedianFinder:

    def __init__(self):
        self.nums = []
    def addNum(self, num: int) -> None:
        
        if len(self.nums)==0 or len(self.nums)==1:
            self.nums.append(num)
            self.nums.sort()
        else:
            l, r = 0 , len(self.nums)-1
            while l <= r:
                mid = (l+r)//2
                if self.nums[mid] < num:
                    l = mid+1
                else:
                    r = mid-1
            self.nums.insert(l,num)

    def findMedian(self) -> float:
        # print(self.nums)
        n = len(self.nums)
        if n %2 ==0:
            i = n//2
            median = (self.nums[i-1] + self.nums[i])/2
            return median
        else:
            return self.nums[n//2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
