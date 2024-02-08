class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums.sort()
        # -4 -1 -1 0 1 2
        for i in range(n):
            curr = nums[i]
            target = -curr;
            # [-10,5,4,5,1,1,-4] curr = -10, target = 10
            left=i+1
            right = n-1
            while(left<right):
                sum = nums[left] + nums[right]
                if sum <target:
                    left+=1
                elif sum>target:
                    right-=1
                else:
                    temp = (nums[i],nums[left],nums[right])
                    ans.add(temp)
                    left+=1
                    right-=1
                    while(left<n and nums[left]==nums[left-1]):
                        left+=1
                    while(right>=0 and nums[right]==nums[right+1]):
                        right-=1

        return ans