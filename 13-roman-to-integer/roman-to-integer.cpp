class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int> map;
        map['I'] = 1;
        map['V'] = 5;
        map['X'] = 10;
        map['L'] = 50;
        map['C'] = 100;
        map['D'] = 500;
        map['M'] = 1000;
        int n = s.length();
        int ans = 0;
        // MCMXCIV //LVIII //III
        // Cases: IV,IX or XL,XC or CD,CM 
        for(int i=n-1;i>=0;i--){
            char ch = s[i];
            ans = ans + map[ch];
            if((ch == 'V' || ch == 'X') && i>0 && s[i-1]=='I')
            {
                ans = ans - map['I'];
                i=i-1;
            }
            if((ch == 'L' || ch == 'C') && i>0 && s[i-1]=='X')
            {
                ans = ans - map['X'];
                i=i-1;
            }
            if((ch == 'D' || ch == 'M') && i>0 && s[i-1]=='C')
            {
                ans = ans - map['C'];
                i=i-1;
            }
        }
        return ans;
    }
};