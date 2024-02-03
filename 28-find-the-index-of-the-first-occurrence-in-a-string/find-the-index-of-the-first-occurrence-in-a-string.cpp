class Solution {
public:
    int strStr(string haystack, string needle) {
        int i=0,j=0;
        int n = haystack.length();
        int windowStart=0;

        while(i<n){
            if(haystack[i]==needle[j]) //character match
            {
                if(j==0) //start of window
                    windowStart = i;
                i++; //check for next character
                j++;

                //this condition be below increment of j because j 
                //is checked for finishing all characters
                if(j==needle.length()) 
                    return windowStart;

            }
            else{ //if not found
                windowStart = windowStart + 1;
                i = windowStart; //restart check from next window
                j=0;
            }
        }
        return -1;
    }
};