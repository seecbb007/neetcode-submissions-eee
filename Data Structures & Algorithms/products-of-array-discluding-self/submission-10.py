class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixarr = [1 for _ in range(len(nums))] 
        prefix = 1
        for i in range(len(nums)):
            prefixarr[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            prefixarr[i] *= suffix
            suffix *= nums[i]
        return prefixarr
        