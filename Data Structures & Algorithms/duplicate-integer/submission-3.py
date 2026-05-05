class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countnums = Counter(nums)
        for freq in countnums.values():
            if freq > 1:
                return True
        return False