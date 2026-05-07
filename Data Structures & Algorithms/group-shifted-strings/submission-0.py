class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strings:
            key = []
            first = ord(s[0])
            for char in s: 
                diff = (ord(char) - first + 26) % 26
                key.append(diff)
            groups[tuple(key)].append(s)
        return list(groups.values())