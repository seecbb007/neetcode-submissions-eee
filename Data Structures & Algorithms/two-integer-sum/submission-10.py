class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_idx = []
        for i, num in enumerate(nums):
            nums_with_idx.append([num, i])
        nums_with_idx.sort()

        i, j = 0, len(nums_with_idx) - 1

        while i < j:
            curr = nums_with_idx[i][0] + nums_with_idx[j][0]
            if curr == target:
                idx1,idx2 = nums_with_idx[i][1], nums_with_idx[j][1]
                return [min( idx1,idx2),max( idx1,idx2)]
            if curr < target:
                i += 1
            else:
                j -= 1
        return []