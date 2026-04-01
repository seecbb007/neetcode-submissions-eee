class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(n):
            currp = 1
            for j in range(n):
                if i != j:
                    currp *= nums[j]
            res[i] = currp
        return res 