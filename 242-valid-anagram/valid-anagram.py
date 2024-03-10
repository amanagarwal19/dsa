class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False;

        freq = [0]*26;
        for i in range(len(s)):
            freq[ord(s[i])-97] = freq[ord(s[i])-97] + 1 
            freq[ord(t[i])-97] = freq[ord(t[i])-97] - 1 

        print(freq)
        for i in range(0,26):
            if freq[i]!=0:
                return False;
        return True;

