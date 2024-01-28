class Solution {
public:
    int hIndex(vector<int>& citations) {
        //[6,5,3,1,0]
        sort(citations.begin(),citations.end(),greater<int>());
        int n = citations.size();
        int j = n-1;
        int ans=0;
        int count=0;
        while(j>=0){
            cout<<"hi";
            if(citations[j]-1<=j){
                ans = max(ans,citations[j]);
            }
            else if(citations[j]!=0)
             {  count++;
                ans = max(ans,count);
             } 
            j--;
        }
        return ans;
    }
};