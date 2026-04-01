# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inordermap = {val: i for i, val in enumerate(inorder)}
        
        def helper(prestart,preend, instart, inend):
            if prestart > preend:
                return None
            rootval = preorder[prestart]
            root = TreeNode(rootval)

            mid = inordermap[rootval]
            leftsize = mid - instart

            root.left = helper(prestart + 1, prestart + leftsize, instart, mid - 1)
            root.right = helper(prestart + leftsize + 1, preend, mid + 1, inend)
            return root            



        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)