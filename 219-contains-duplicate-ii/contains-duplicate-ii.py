class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False;
        
        map = defaultdict(list)
        for i in range(len(nums)):
            map[nums[i]].append(i)

        print(map)
        for value in map.values():
            if len(value)>=2:
                left=0
                right=1
                count=0
                while(right < len(value)):
                    if abs(value[right]-value[left])<=k:
                        return True
                    else:
                        left +=1
                    right +=1 
        return False
        