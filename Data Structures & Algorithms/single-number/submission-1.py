class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # res ^= num 
            res = res ^ num
        return res        
