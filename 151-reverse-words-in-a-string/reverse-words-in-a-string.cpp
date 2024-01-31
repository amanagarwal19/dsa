class Solution {
public:
     void reverseString(string& s,int left,int right){
        cout<<"("<<left<<","<<right<<")\n";
        while(left<right){
            char ch = s[left];
            s[left] = s[right];
            s[right] = ch;
            left++;
            right--;
        }
    }

    string reverseWords(string s) {
        // the sky is blue
        // eulb si yks eht
        // blue is sky the
        int n = s.length();
        reverseString(s,0,n-1);
        int i=0;
        while(s[i]==' ')
            i++;
        s.erase(0,i);
        n=s.length();
        int j=n-1;
        while(s[j]==' ') {
            j--;
        }
        s.erase(j+1,n-1);

        n = s.length();
        i=0;
        int left=0;
        int right=0;
        while(i<s.length()){
            if(s[i]!=' ') //word start
            {
                // cout<<"s ="<<s<<"\n";
                left = i;
                while(i<s.length() && s[i]!=' ')
                    i++;
                // i may encounter a space or end of string
                reverseString(s,left,i-1);
                if(i==s.length()-1)
                    break; //last word also reversed;
                else{
                    // i is at a space and is less than n
                    left = i;
                    while(i<s.length() && s[i]==' ')
                        i++;
                    // cout<<s<<"\n";
                    // cout<<"erase "<<left<<"->"<<i<<" "<<i-left<<endl;
                    s.erase(left,i-left-1); //keep one space and remove others
                    i=left+1;
                }
            }
            // i++;
        }


        return s;
    }
};