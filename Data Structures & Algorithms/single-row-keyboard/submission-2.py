class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        board_map = {}
        for i, char in enumerate(keyboard):
            board_map[char] = i
        total = 0
        curr_pos = 0
        for char in word:
            target_pos = board_map[char]
            total += abs(target_pos - curr_pos)
            curr_pos = target_pos
        return total
