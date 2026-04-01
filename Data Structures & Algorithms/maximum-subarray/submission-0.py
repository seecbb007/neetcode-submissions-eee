class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        currsum = 0

        for r in range(len(nums)):
            currsum += nums[r]
            maxsum = max(maxsum, currsum)
            if currsum < 0:
                currsum = 0
        return maxsum