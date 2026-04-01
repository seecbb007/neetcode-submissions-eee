"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old2new = {}
        curr = head
        while curr:
            old2new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = old2new[curr]
            copy.next = old2new.get(curr.next)
            copy.random = old2new.get(curr.random)
            curr = curr.next
        return old2new[head]
