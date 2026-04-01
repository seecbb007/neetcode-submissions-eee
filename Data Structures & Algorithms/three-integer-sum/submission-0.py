class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.ksum(nums,0,3, 0)

    def ksum(self, nums, target, k, start):
        res = []
        if k == 2:
            i,j = start, len(nums) - 1
            while i < j:
                curr = nums[i] + nums[j]
                if curr == target:
                    res.append([nums[i],nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1

                elif curr < target:
                    i += 1
                else:
                    j -= 1
                
            return res
        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            sub_res = self.ksum(nums, target - nums[i], k - 1, i + 1)
            for s in sub_res:
                res.append([nums[i]] + s)
        return res

                 
        