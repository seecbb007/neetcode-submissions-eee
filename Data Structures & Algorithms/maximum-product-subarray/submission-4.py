class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')
        for i in range(n):
            currprodcut = 1
            for j in range(i, n):
                currprodcut *= nums[j]
                res = max(res, currprodcut)
        return res 
        