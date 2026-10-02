class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in nummap:
                return [nummap[remainder], i]
            nummap[num] = i
            