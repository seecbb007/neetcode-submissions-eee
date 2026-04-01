class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(n):
            curr_product = 1
            for j in range(n):
                if i!= j:
                    curr_product *= nums[j]
            res[i] = curr_product
        return res