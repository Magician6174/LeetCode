class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import random
        def quicksearch(arr,k):
            pivot = random.randint(0,len(arr)-1)
            arr1,arr2 = [],[]
            for i in arr:
                if i > arr[pivot]:
                    arr1.append(i)
                else:
                    arr2.append(i)
            if len(arr1) >= k:
                return quicksearch(arr1,k)
            else:
                k -= len(arr1)
                if len(set(arr2)) == 1:
                    return arr2[0]
                else:
                    return quicksearch(arr2,k)
        return quicksearch(nums,k)
        
        
        
        
        """--------------Trivial Approach-----------------"""
        # nums.sort()
        # return nums[-k]
        
