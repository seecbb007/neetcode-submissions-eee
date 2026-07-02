class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            remind = target - num
            if remind in seen:
                return [seen[remind], idx]

            seen[num] = idx