# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def getmax(node):
            if not node:
                return 0
            left = max(getmax(node.left), 0)
            right = max(getmax(node.right), 0)
            curr = node.val + left + right

            self.max_sum = max(self.max_sum, curr)
            return node.val + max(left,right)

        getmax(root)
        return self.max_sum