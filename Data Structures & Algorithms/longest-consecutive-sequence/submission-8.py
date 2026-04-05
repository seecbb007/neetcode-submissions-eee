class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        setnums = set(nums)
        res = 0
        # [20,1,10,4,3,5,2]
        for num in setnums:
            if num - 1 not in setnums:
                length = 1
                while num + length in setnums:
                    length += 1
                res = max(res, length)
        return res