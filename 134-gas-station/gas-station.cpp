class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalGas= 0;
        int totalCost =0;
        int n = gas.size();
        int totalUsage = 0;
        int start = 0;
        for(int i=0;i<n;i++){
            totalGas += gas[i];
            totalCost += cost[i];
            totalUsage = totalUsage + (gas[i] - cost[i]);
            if(totalUsage < 0 ) // we ran out of gas, total from preivous start wont add any value
            {
                totalUsage = 0; //reset total
                start = i+1;    // next position can be potential start
            }
        }
        if(totalGas<totalCost)
            return -1;
        return start;
        

    }
};