class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indg = [0] * numCourses

        for upper, basic in prerequisites:
            adj[basic].append(upper)
            indg[upper] += 1

        q = deque()
        for i in range(numCourses):
            if indg[i] == 0:
                q.append(i)
        count = 0
        while q:
            curr = q.popleft()
            count += 1
            for neighbor in adj[curr]:
                indg[neighbor] -= 1
                if indg[neighbor] == 0:
                    q.append(neighbor)
        return count == numCourses
                