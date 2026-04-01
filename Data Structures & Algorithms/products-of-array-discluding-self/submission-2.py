class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        arr = [1] * length

        prefix = 1;
        for i in range (length):
            arr[i] = prefix
            prefix = prefix * nums[i]
        suffix = 1
        for i in range (length - 1, -1, -1):
            arr[i] = arr[i] * suffix
            suffix = suffix * nums[i]
        return arr    