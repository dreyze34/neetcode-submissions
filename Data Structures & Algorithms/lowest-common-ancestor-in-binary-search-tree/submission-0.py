# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root):
            visited = set()
            def explore(node):
                if not node:
                    return
                visited.add(node)
                explore(node.left)
                explore(node.right)
            explore(root)
            return visited

        lca = root
        left, right = dfs(lca.left), dfs(lca.right)
        while (p in left) != (q in right):
            if p == lca or q == lca:
                return lca
            lca = lca.left if p in left else lca.right
            left, right = dfs(lca.left), dfs(lca.right)
        return lca


            