# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexmap = {val: i for i, val in enumerate(inorder)}
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None

            rootval = preorder[pre_start]
            root = TreeNode(rootval)

            mid = indexmap[rootval]
            leftsize = mid - in_start
            
            root.left = helper(pre_start + 1, pre_start + leftsize, in_start, mid - 1)
            root.right = helper(pre_start + leftsize + 1, pre_end, mid + 1, in_end)
            return root

        return helper(0,len(preorder) - 1, 0, len(inorder) - 1)