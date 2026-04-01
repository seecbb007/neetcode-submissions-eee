class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')
        for i in range(n):
            curr_product = 1
            for j in range(i, n):
                curr_product *= nums[j]
                res = max(res, curr_product)
        return res 
        