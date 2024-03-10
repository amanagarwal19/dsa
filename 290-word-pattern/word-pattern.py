class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        n = len(words)
        if(n!=len(pattern)):
            return False;

        map={}
        seen=set()
        for i in range(len(pattern)):
            if(pattern[i] not in map):
                if(words[i] not in seen): #Both LHS RHS Unique
                    map[pattern[i]] = words[i]
                    seen.add(words[i])
                    # map[words[i]] = pattern[i]
                else:
                    # LHS not in map but RHS in map, so must be mapped with something else
                    return False;
            else:
                # LHS in map
                # Is it mapped to RHS?
                if(map[pattern[i]]!=words[i]): #Some seperate LHS RHS mapping present
                    return False;
        return True;