class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sumnums = sum(nums)
        setnums = sum(set(nums))

        lennums = len(nums)
        lenset = len(set(nums))

        return (sumnums - setnums) // (lennums- lenset)