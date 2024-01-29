class Solution {
public:
    int lengthOfLastWord(string s) {
        int count=0;
        int j = s.length()-1;
        bool wordStart = false;
        while(j>=0){
            if(s[j]!=' '){
                wordStart = true;
                while(j>=0 && s[j]!=' '){
                    count++;
                    j--;
                }
            }
            if(wordStart)
                return count;
            j--;
        }
        return 0;
    }
};