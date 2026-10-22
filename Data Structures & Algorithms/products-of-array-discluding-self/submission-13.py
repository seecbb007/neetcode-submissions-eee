class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixarr = [1] * n
        suffixarr = [1] * n

        for i in range(1, n):
            prefixarr[i] = prefixarr[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffixarr[i] = suffixarr[i + 1] * nums[i + 1]

        res = [1] * n

        for i in range(n):
            res[i] = prefixarr[i] * suffixarr[i]

        return res 