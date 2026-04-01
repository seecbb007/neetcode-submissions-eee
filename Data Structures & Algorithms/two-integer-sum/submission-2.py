class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newMap = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in newMap:
                return [newMap[res], i]
            newMap[num] = i     
        