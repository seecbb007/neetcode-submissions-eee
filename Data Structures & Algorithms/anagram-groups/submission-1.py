from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict where the key is a tuple (character count) and value is a list of anagrams
        newList = defaultdict(list)

        for s in strs:
            # Create a count array for the 26 lowercase letters
            count = [0] * 26
            # Update the count based on the frequency of each character in the string
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Append the string to the correct group based on its character count
            newList[tuple(count)].append(s)

        # Return the grouped anagrams
        return list(newList.values())
