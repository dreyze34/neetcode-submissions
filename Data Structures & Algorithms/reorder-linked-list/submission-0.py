# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        slow = head
        prev = None
        while fast:
            fast.next, prev, fast = prev, fast, fast.next
        while prev:
            slow.next, prev.next, slow, prev = prev, slow.next, slow.next, prev.next
        
        


