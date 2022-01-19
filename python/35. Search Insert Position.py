class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
       
        int start = 0;
        int end = nums.size();
        
        while (start < end)
        {
            
        
            int z = start + (end - start)/2;
            if (nums[z] > target) end = z;

            else
            {
                start = z+1;
                if (nums[z] == target) return z;
            }
        
        }
        return start;
    }
};