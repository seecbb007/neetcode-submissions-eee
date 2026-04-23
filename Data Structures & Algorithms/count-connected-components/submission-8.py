
class UnionFind:
    def __init__(self,n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self,i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        parenti = self.find(i)
        parentj = self.find(j)

        if parenti == parentj:
            return False
        if self.rank[parenti] > self.rank[parentj]:
            self.parent[parentj] = parenti
        elif self.rank[parentj] > self.rank[parenti]:
            self.parent[parenti] = parentj
        else:
            self.parent[parenti] = parentj
            self.rank[parentj] += 1
        self.count -= 1
        return True
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u,v)
        return uf.count