class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> ans(2,0);
        int n = numbers.size();
        int left = 0,right = n-1;
        while(left<right){
            int sum = numbers[left] + numbers[right];
            if(sum==target)
            {
                ans[0] = left+1;
                ans[1] = right+1;
                return ans;
            }
            if(sum<target)
                left++;
            else
                right--;
        }
        return ans;
    }
};