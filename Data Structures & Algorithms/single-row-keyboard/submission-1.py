class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_map = {}
        for i, char in enumerate(keyboard):
            keyboard_map[char] = i
        print(keyboard_map)
        total = 0
        curr_pos = 0
        for char in word:
            target_pos = keyboard_map[char]
            total += abs(target_pos - curr_pos)
            curr_pos = target_pos
        return total 

