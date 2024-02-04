class Solution {
public:
    bool isPalindrome(string s) {
        int i=0,j=0;
        while(j<s.length()){
            if(isalnum(s[j])){
                s[i++] = tolower(s[j]);
            }
            j++;
        }
        int right=i-1;// IMPORTANT: i is beyond last character
        int left = 0;
        cout<<s.substr(0,right);
        while(left<right){
            if(s[left]!=s[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};