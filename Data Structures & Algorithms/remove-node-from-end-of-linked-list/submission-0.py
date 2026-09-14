# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                curr.next, curr, prev = prev, curr.next, curr
            return prev

        tail = reverse(head)
        curr = tail
        prev = None
        c = 1
        while curr:
            if c == n:
                if not prev:
                    tail = curr.next
                    break
                else:
                    prev.next = curr.next
                    break
            curr, prev = curr.next, curr
            c += 1
        
        return reverse(tail)


            

