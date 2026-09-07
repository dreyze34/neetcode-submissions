# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        def dfs(node):
            nonlocal maxD
            if not node:
                return -1
            else:
                leftD, rightD = dfs(node.left), dfs(node.right)
                if leftD + rightD + 2 > maxD:
                    maxD = leftD + rightD + 2
                return 1 + max(leftD, rightD)
        dfs(root)
        return maxD
                