class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n = len(intervals)

        i = 0;
        while(i<n and intervals[i][0] < newInterval[0]):
            i=i+1
        intervals.insert(i,newInterval)


        # IMPORTANT TO REFRESH N VAlUE
        n = len(intervals) 
        # mergeIntervals(intervals)
        ans = []
        ans.append(intervals[0])
        i=1
        #  [a,b] [c,d]
        #  [1,3] [2,5] [6,9]
        while(i<n):
            lastInterval = ans[len(ans)-1]
            lastEnding = lastInterval[1]
            currentStarting = intervals[i][0]
            currentEnding = intervals[i][1]

            if(currentStarting <= lastEnding):  #Overlap
                newEnding = max(lastEnding,currentEnding)
                ans[len(ans)-1][1] = newEnding
            else:                               # No Overlap
                ans.append(intervals[i])
            i = i+1

        return ans