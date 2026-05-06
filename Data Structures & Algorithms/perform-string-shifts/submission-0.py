class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_move = 0
        for direction, amount in shift:
            if direction == 0:
                total_move -= amount
            else:
                total_move += amount

        n = len(s)
        finalshift = total_move % n
        return s[n - finalshift:] + s[:n - finalshift]