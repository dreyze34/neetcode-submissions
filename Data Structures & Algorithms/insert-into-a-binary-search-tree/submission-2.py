# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def dfs(node):
            right_side = val > node.val
            if right_side:
                if node.right:
                    dfs(node.right)
                else:
                    node.right = TreeNode(val)
                    return
            else:
                if node.left:
                    dfs(node.left)
                else:
                    node.left = TreeNode(val)
                    return
        dfs(root)
        return root
        
        