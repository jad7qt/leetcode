"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Map of nodes of original to new
        if not head:
            return 
        m = {}
        curr = head
        while curr:
            m[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                m[curr].next = m[curr.next]
            if curr.random:
                m[curr].random = m[curr.random]
            curr = curr.next
        return m[head]