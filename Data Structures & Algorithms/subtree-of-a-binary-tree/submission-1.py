# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False
        queue = [root]
        i = 0
        while i < len(queue):
            curr = queue[i]
            i += 1
            if isSameTree(curr, subRoot):
                return True
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
        return False

        
            
