class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        numsSet = set(nums)    
        count = 0 

        for num in numsSet:
            if num - 1 not in numsSet:
                currentNum = num
                current_Seq = 1

                while currentNum + 1 in numsSet:
                    currentNum += 1
                    current_Seq += 1
                count = max(count, current_Seq) 
        return count           

