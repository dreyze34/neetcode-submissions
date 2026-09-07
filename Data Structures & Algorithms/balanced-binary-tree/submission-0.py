# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True
        def dfs(node):
            nonlocal result
            if not node:
                return -1
            else:
                leftD, rightD = dfs(node.left), dfs(node.right)
                if abs(leftD - rightD) > 1:
                    result = False
                return 1 + max(leftD, rightD)
        dfs(root)
        return result
                    