class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n,0);
        ans[0] = nums[0];
        for(int i=1;i<n;i++)
            ans[i] = ans[i-1]*nums[i];
        cout<<"\n";
        for(int i=n-2;i>=0;i--)
            nums[i] = nums[i+1]*nums[i];

        int temp=ans[0];
        for(int i=0;i<n;i++){
            if(i==0)
            { 
                temp=ans[i];
                ans[i] = nums[i+1];
            }
            else if(i==n-1)
                ans[i] = temp;
            else
            {
                int new_val = temp*nums[i+1];
                temp = ans[i];
                ans[i] = new_val;
            } 
        }
        return ans;
    }
};