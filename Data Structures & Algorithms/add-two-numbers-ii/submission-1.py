# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            if not node:
                return (0, -1)
            else:
                s, i = dfs(node.next)
                return (s + node.val * 10**(i+1), i+1)
        s = dfs(l1)[0] + dfs(l2)[0]
        prev = None
        while s >= 10:
            q, r = s // 10, s % 10
            newNode = ListNode(r)
            newNode.next, prev = prev, newNode
            s = q
        newNode = ListNode(s)
        newNode.next, prev = prev, newNode
        return newNode