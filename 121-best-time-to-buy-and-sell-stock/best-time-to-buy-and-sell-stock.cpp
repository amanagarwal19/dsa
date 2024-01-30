class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n<=1)
            return 0; //cant sell without buying
        int totalProfit=0;
        int maximum = prices[n-1];
        for(int i=n-2;i>=0;i--){
            totalProfit = max(totalProfit,maximum - min(maximum,prices[i]));
            maximum = max(maximum, prices[i]);
            // if(prices[i] < maximum)
            //     totalProfit = max(totalProfit,(maximum-prices[i]));
            // else
            //     maximum = prices[i];
        }
        return totalProfit;
    }
};