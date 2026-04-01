class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        num = 0
        for i in nums:
            if i != num:
                return num
            else:
                num += 1
        return num            