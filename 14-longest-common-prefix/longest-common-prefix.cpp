class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        string left = strs[0];
        string right = strs[strs.size()-1];
        int i=0,j=0;
        while(i<left.size() && j<right.size()){
            if(left[i] != right[j])
                break;
            i++;
            j++;
        }
        return left.substr(0,i);
    }
};