class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            groups[sorteds].append(s)
        return list(groups.values())