class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-freq for freq in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()
        while q or maxheap:
            time += 1
            if maxheap:
                count = heapq.heappop(maxheap) + 1
                if count != 0:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time

        