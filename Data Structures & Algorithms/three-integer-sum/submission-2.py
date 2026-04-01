class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.ksum(nums, 0,3,0)
    def ksum(self, nums, target, k, start):
        res = []
        if k == 2:
            left, right = start, len(nums) - 1
            while left < right:
                curr = nums[left] + nums[right]
                if curr == target:
                    res.append([nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr < target:
                    left += 1
                else:
                    right -= 1
            return res

        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            sub_res = self.ksum(nums, target - nums[i], k - 1, i + 1)
            for s in sub_res:
                res.append([nums[i]] + s)
        return res 
            