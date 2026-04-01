class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        curr = jumps = 0
        fathest = 0

        for i in range(n - 1):
            fathest = max(fathest, i + nums[i])
            if i == curr:
                jumps += 1
                curr = fathest
                if curr >= n + 1:
                    break

        return jumps 