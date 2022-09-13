class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        import heapq
        self.minHeap = []
        # heapq.heapify(self.minHeap)
        self.nums = nums
        self.heapSize = k
        
        for num in nums:
            if len(self.minHeap) < k:
                heapq.heappush(self.minHeap,num)
            else:
                heapq.heappushpop(self.minHeap,num)

    def add(self, val: int) -> int:
        
        self.nums.append(val)
        if len(self.minHeap) < self.heapSize:
            heapq.heappush(self.minHeap,val)
        else:
            heapq.heappushpop(self.minHeap,val)
        
        return self.minHeap[0] # kth largest element means smallest element in size of k numbers
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
