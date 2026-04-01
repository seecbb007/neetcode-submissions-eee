class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,1,2,8]


        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        # i = 0, res[0]= 1, prefix = 1
        # i = 1, res[1] = 1, prefix = 2
        # i = 2, res[2] = 2, prefix = 8
        # i = 3, res[3] = 8, prefix = 48
        suffix = 1
        for j in range(n - 1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        return res 

        # i = 3, res[3] = 8, suffix = 1 * 6 = 6
        # i = 2, res[2] = 12, suffix = 4 * 6 = 24
        # i = 1, res[1] = 24, suffix = 24 * 2 = 48
        # i = 0, res[0] = 48, suffix = 48 * 1 = 48