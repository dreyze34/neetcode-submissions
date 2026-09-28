# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            while node.left:
                node = node.left
            return node
        def dfs(node, key):
            if not node:
                return None
            elif node.val == key:
                if not node.left and not node.right:
                    return None
                elif node.left and node.right:
                    successor = find_min(node.right)
                    node.val = successor.val
                    node.right = dfs(node.right, successor.val)
                    return node
                else:
                    if node.left:
                        return node.left
                    else:
                        return node.right
            elif node.val < key:
                node.right = dfs(node.right, key)
                return node
            else:
                node.left = dfs(node.left, key)
                return node

        root = dfs(root, key)
        return root




