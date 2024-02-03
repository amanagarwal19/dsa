class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if(magazine.length() < ransomNote.length())
            return false;

        unordered_map<char,int> map;
        for(char ch:magazine)
        {
            if(map.find(ch)==map.end()) //not in map
            {
                map[ch]=1;
            }
            else{
                map[ch]++;
            }
        }

        for(char ch:ransomNote){
            if(map.find(ch)==map.end()) // char not in map
                return false;
            //else ch is in map
                map[ch] --;
            if(map[ch]==0)
                map.erase(ch);
        }

        //came here means all chars found
        return true;
    }
};