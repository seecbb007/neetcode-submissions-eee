class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        
        def robber(houses):
            prev = curr = 0
            for h in houses:
                prev,curr = curr, max(curr, h + prev)
            return curr

        return max(robber(nums[:-1]), robber(nums[1:]))