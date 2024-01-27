class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int reader = 0,writer = 0;
        while(reader<n){
            if(nums[reader]!=val){
                nums[writer++] = nums[reader];
            }
            reader++;
        }
        return writer;
    }
};