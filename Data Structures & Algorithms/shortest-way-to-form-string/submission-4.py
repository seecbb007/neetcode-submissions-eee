class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        groups = defaultdict(list)
        for i, char in enumerate(source):
            groups[char].append(i)

        count = 1
        curridx = -1
        for char in target:
            if char not in groups:
                return -1

            idxlist = groups[char]

            found = -1
            l,r = 0, len(idxlist) - 1
            while l <= r:
                mid = (l + r) // 2
                if idxlist[mid] > curridx:
                    found = mid 
                    r = mid - 1
                else:
                    l = mid + 1

            if found == -1:
                count += 1
                curridx = idxlist[0]
            else:
                curridx = idxlist[found]
        return count

