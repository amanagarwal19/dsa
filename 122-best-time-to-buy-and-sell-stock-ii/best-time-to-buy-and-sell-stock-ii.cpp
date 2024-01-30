class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n<=1) return 0;
        int profit = 0;
        int peak=0,valley=0;
        int i=0;
        while(i<n){
            //find valley prices[i] < prices[i+1]
            // loop terminates when 2,3
            while(i<n-1 && prices[i]>=prices[i+1])
                i++;
            valley = prices[i];

            //find peak: loop terminates when 4,2
            while(i<n-1 && prices[i]<=prices[i+1]) //2 , 3
                i++;
            peak = prices[i];
            profit = max(profit,profit+(peak-valley));

            i++;
        }
        return profit;
    }
};