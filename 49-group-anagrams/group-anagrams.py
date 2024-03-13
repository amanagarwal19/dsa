class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map= defaultdict(list)
        for word in strs:
            freq = [0]*26
            for i in range(len(word)):
                freq[ord(word[i]) - ord("a")] +=1;
            map[tuple(freq)].append(word)

        return map.values()
        