class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.length();
        int m = needle.length();
        if(n<m) return -1;

        int windowStart=0;
        int i=0;
        while(i<m){   // traverse the needle
            if(needle[i]!=haystack[windowStart+i]){ // mismatch, restart window
                windowStart+=1;
                i=0;
            }
            if(needle[i]==haystack[windowStart+i])
                i++;
            if(windowStart>(n-m)) break;    // no more space left to check
        }
        if(i==m) 
            return windowStart;
        else
            return -1;
    }
};