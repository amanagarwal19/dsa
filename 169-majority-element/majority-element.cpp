class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        int winner = -1;
        int votes= 0;
        int i=0;
        while(i<n){
            if(votes==0) //anyone can win now, make current element as winner
            {
                winner = nums[i];
                votes++;
            }
            else if(winner==nums[i]) //someone is winning now
                    votes++;        // if i is winning, increase votes
                else
                    votes--;        // some other i may win, reduce my votes
            i++;
        }
        return winner;
    }
};