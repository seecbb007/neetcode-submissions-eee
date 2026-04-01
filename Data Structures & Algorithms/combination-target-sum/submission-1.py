class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(remain, start):
            if remain == 0:
                res.append(list(path))
                return 
            if remain < 0:
                return 
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(remain - nums[i], i)
                path.pop()

        backtrack(target, 0)
        return res 
