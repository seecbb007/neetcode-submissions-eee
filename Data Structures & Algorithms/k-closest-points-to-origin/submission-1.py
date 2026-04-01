class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            if len(maxheap) < k:
                heapq.heappush(maxheap, (dist, [x,y]))
            else:
                if dist > maxheap[0][0]:
                    heapq.heappushpop(maxheap, (dist,[x,y]))

        return [p for d,p in maxheap]