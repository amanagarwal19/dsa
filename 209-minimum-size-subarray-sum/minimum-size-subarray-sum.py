class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left=0
        right=0
        sum=0
        ans=1e9+1
        # [2,3,1,215,4,3]
        while right < len(nums):
            sum = sum + nums[right]
            if sum < target:
                right = right+1
            elif sum>=target:
                while left<=right and sum>=target:
                    ans = min(ans,right-left+1)
                    sum = sum - nums[left]
                    left = left+1
                right = right +1
        if ans == 1e9+1:
            return 0
        return ans

            
        