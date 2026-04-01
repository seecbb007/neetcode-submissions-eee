class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indg = [0] * numCourses

        for upper, basic in prerequisites:
            adj[basic].append(upper)
            indg[upper] += 1
        q = deque()
        res = []
        for i in range(numCourses):
            if indg[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            res.append(curr)
            for neighbor in adj[curr]:
                indg[neighbor] -= 1
                if indg[neighbor] == 0:
                    q.append(neighbor)
        return res if len(res) == numCourses else []