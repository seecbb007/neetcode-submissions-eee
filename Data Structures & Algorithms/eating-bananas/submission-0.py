class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = left + (right - left) // 2
            if self.can(piles, mid, h):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

    def can(self, piles,k, h):
        total = 0
        for p in piles:
            total += math.ceil(p / k)
        return total <= h

        