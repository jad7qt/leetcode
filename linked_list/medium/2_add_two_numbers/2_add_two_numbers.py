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
    while p1 or p2 or carry:
      first = p1.val if p1 else 0
      second = p2.val if p2 else 0
      carry, r = divmod(first + second + carry, 10)
      curr = ListNode(r)
      if prev:
        prev.next = curr
      else:
        start = curr
      prev = curr
      p1 = p1.next if p1 else None
      p2 = p2.next if p2 else None
    return start