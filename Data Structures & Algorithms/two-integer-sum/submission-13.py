class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in store:
                return [store[remain], i]
            store[num] = i