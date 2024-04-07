class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        if(len(nums)==0):
            return ans;
        left=0
        right=1
        # 1 5 7
        # 1 2 3
        while(right<len(nums)):
            if(nums[right]==nums[right-1]+1): #continue seq
                right = right + 1
            else: #end of series   
                if(right-left==1): #only one element in series
                    ans.append(str(nums[left]))
                else:
                    ans.append(str(nums[left])+"->"+str(nums[right-1]))
                left = right
                right = right + 1

        # case 1: series ends abruptly [...,4,5,6], left at 4, right is outside
        # case 2: series does not end abruptly [...,2,4,6] left at n-1
        if(left == len(nums)-1):
            ans.append(str(nums[left]))
        else:
            ans.append(str(nums[left])+"->"+str(nums[len(nums)-1]))

        return ans
