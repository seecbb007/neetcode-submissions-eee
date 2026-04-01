class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        # Find 函数：找到根节点（帮主）
        def find(i):
            if parent[i] == i:
                return i
            # 路径压缩 (Path Compression)：直接让节点指向根，加速下次查找
            parent[i] = find(parent[i])
            return parent[i]

        # Union 函数：合并两个集合
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True # 合并成功
            return False # 已经在同一个集合里了，说明成环了

        for u, v in edges:
            if not union(u, v):
                # 如果 union 返回 False，说明 u 和 v 已经连通
                # 这一条边就是导致成环的罪魁祸首
                return [u, v]