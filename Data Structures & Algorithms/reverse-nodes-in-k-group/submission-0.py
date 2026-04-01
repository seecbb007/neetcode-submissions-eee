# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        prev = None
        p = head
        for _ in range(k):
            temp = p.next
            p.next = prev
            prev = p
            p = temp

        head.next = self.reverseKGroup(p, k)
        return prev
        