class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1,n):
            res[i] = res[i - 1] * nums[i - 1]
        # [1,1,1,1]
        # [1，1，2，8]
        rightproduct = 1

        for j in range(n - 1, -1, -1):
            res[j] = res[j] * rightproduct
            rightproduct *= nums[j]

            # [48,24,12,8]
            # right = 1 * 6 = 6
            # right = 6 * 4 = 24
            # right = 24 * 2 = 48
            # right = 48 * 1 
        return res