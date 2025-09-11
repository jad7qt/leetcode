# 141. Linked List Cycle

### Approach
For this problem, I started by using two pointers to step through each linked list while performing simple addition on the values of each. Since our linked lists represent numbers in reverse, we can solve this problem by calculating the addition of the first ListNodes in each list and carrying any overflow into our next summation. This is the same as adding both numbers together, storing the modulus $sum \% 10$ in the current ListNode, and carrying over the remainder $sum / 10$ to add to the next ListNode. We can repeat this cycle until we reach the end of both lists and there is no more carryover. 

### Solution
```
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
```

### Complexity Analysis
#### Time Complexity: $O(max(m,n))$
This solution iterates the entire length of both lists, resulting in a linear time complexity with respect to the longest list input. For list inputs of size $m$ and $n$, the time complexity is $O(max(m,n))$.

#### Space Complexity: $O(1)$
Given this solution only uses a few variables to iterate through the lists regardless of size, and disregarding the space taken by the returned linked list, the space complexity is fixed.

### Results

![screenshot](/linked_list/medium/2_add_two_numbers/2_add_two_numbers.png)
