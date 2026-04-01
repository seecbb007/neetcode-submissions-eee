class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        nums.sort()
        for i in nums:
            if n != i:
                return n
            else:
                n +=1
        return n            
        