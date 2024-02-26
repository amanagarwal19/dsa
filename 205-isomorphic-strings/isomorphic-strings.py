class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #tape
        #pajp
        m = len(s)

        map = {}
        seen = set()
        for i in range(m):
            ch = s[i]
            if map.get(ch)==None:
                if t[i] not in seen:
                    map[ch] = t[i]
                    seen.add(t[i])
                else:
                    # Seen previously with different mapping
                    return False;
            else:
                # Mapping present for current char at s[i]
                if map.get(ch) != t[i]:
                    return False
        return True
