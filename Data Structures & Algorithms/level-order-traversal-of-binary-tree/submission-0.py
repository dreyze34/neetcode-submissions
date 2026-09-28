# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = [(root, 0)]
        i = 0
        last, sub = 0, []
        while i < len(queue):
            curr, lvl = queue[i]
            if curr:
                if lvl == last:
                    sub.append(curr.val)
                else:
                    result.append(sub)
                    last = lvl
                    sub = [curr.val]
                
                queue.append((curr.left, lvl + 1))
                queue.append((curr.right, lvl + 1))
            i += 1
        if sub:
            result.append(sub)
        
        return result
            
            

