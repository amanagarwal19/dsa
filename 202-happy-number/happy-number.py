class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while True: 
            if num in seen:
                break
            seen.add(num)
            sum = 0
            while num>0:
                sum = sum + (num%10)**2
                num = num//10
            if sum == 1:
                return True;
            num = sum
        return False;