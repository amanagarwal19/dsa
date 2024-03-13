class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        # for i, j in enumerate(nums):
        #     if j in dic and i - dic[j] <= k:
        #         return True
        #     dic[j] = i
        # return False

        # INTUITIVE VERSION
        for idx in range(len(nums)):
            ele = nums[idx]
            if ele in dic: #seen before
                if idx - dic[ele] <=k:  #current index - Previous seen index <=k
                    return True
            dic[ele] = idx
        return False;