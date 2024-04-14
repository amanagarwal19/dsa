class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # ---   ---------                     -----
        #   -----     ------------
        #      --------   ----   ------ 
        #   --------          ----------
        
        # 7,12
        # 10,16

        list.sort(points,key=lambda x: x[1])
        print(points) 
        currInterval = points[0]
        ans = 1
        for i in range(1,len(points)):
            if (points[i][0] <= currInterval[1]):
                continue
            else:
                ans = ans+1
                currInterval = points[i]
        return ans
