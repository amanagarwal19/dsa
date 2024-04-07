class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # nothing to merge
        if(len(intervals)<=1):
            return intervals
        # 0 1 2 3 4 5
        # 0 - 2
        # 1 - 4
        # 3 - 5

        # sort based on start time
        list.sort(intervals, key=lambda x: x[0])
        ans = [intervals[0]]

        i=1    
        while(i<len(intervals)):
            lastEnding = ans[len(ans)-1][1]
            currentStart = intervals[i][0]
            currentEnding = intervals[i][1]
            if (currentStart <= lastEnding):
                ans[len(ans)-1][1] = max(currentEnding,lastEnding)
            else:
                ans.append(intervals[i])
            i = i+1
        return ans