# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1 == 0:
            return l2
        elif l2 == 0:
            return l1
        p1, p2 = l1, l2
        start, prev = None, None
        carry = 0
        while p1 or p2:
            
            carry, r = divmod(p1.val + p2.val + carry, 10)
            print(carry,r)
            curr = ListNode(r)
            if prev:
                prev.next = curr
            else:
                start = curr
            prev = curr
            p1 = p1.next
            p2 = p2.next

        return start