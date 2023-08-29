class Solution:
    def increasingTriplet(self, nums):
        f = 2**31 - 1
        s = 2**31 - 1
        
        if len(nums) < 3:
            return False
        
        for n in nums:
            if n <= f:
                f = n
            elif n <= s:
                s = n
            else:
                return True
        return False