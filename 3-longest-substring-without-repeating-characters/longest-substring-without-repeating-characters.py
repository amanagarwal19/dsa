class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        left=0
        right=0
        n = len(s)
        # abcabcbb
        freq = {}
        while right < n:
            ch = s[right]
            freq[ch] = freq.get(ch,0)+1
            while freq[s[right]] > 1:
                # print("removing "+s[left])
                freq[s[left]] = freq[s[left]]-1
                left = left + 1
            ans = max(ans,right-left+1)
            right = right+1

        return ans

            
            
            


        