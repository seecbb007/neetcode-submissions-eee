class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        laspos = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= laspos:
                laspos = i

        return laspos == 0