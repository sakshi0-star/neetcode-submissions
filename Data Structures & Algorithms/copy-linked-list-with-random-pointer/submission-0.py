# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        if not head:
            return None

        oldToCopy = {}

        # First pass: create copies
        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: connect pointers
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy.get(curr.next)
            copy.random = oldToCopy.get(curr.random)
            curr = curr.next

        return oldToCopy[head]