class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        currmax = nums[0]
        currmin = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            tempmax = currmax

            currmax = max(n, n * tempmax, n * currmin)
            currmin = min(n, n * tempmax, n * currmin)
            res = max(res, currmax)
        return res        