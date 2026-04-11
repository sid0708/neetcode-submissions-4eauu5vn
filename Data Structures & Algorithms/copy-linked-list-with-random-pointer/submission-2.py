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
        oldToCopy = {}
        curr = head
        while curr:
            # create new nodes
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy.get(curr.next, None)
            copy.random = oldToCopy.get(curr.random, None)
            curr = curr.next
        # return new copy head
        return oldToCopy.get(head, None)

        