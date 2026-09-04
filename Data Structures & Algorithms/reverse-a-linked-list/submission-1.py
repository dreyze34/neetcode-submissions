# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        elif not head.next:
            return head
        curr = head.next
        previous = head
        head.next = None
        while curr.next:
            nextNode = curr.next
            curr.next = previous
            previous = curr
            curr = nextNode
        curr.next = previous
        return curr

        
        