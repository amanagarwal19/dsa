class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        
        if(n<=2)
            return n;
        
        int i=1,j=1,count=1;;
        while(i<n){
            //[0,0,1,1,2,3,4]
                //[0,0,0,0,1,2,3,4,4,4,4,4]
            if(nums[i]==nums[i-1] && count<2){
                nums[j] = nums[i];
                i++;
                j++;
                count++;
            }
            //[0,1,1,2,3,4]
            else{
                nums[j] = nums[i];
                i++;
                j++;
                count=1;
            }
            while(i<n && nums[i]==nums[i-1]&&count>=2)
                i++;
        }
        return j;
    }
};