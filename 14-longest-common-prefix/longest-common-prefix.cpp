class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        int j=0;
        int n = strs[0].length();
        while(j<n){
            int currCh = strs[0][j];
            bool allMatch = true;
            for(int i=1;i<strs.size();i++){
                if(j > strs[i].length()-1 || strs[i][j] != currCh){
                    allMatch=false;
                    break;
                }
            }
            if(!allMatch)
                break;
            j++;
        }
        return strs[0].substr(0,j);
    }
};