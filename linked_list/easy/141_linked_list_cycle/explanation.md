# 141. Linked List Cycle

### Approach
Applying Floyd's Cycle Finding Algorithm to this problem was the fastest and least space complex approach to take. s

### Solution
```
class Solution(object):
  def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False
```

### Complexity Analysis
#### Time Complexity: $O(n)$


#### Space Complexity: $O()$

### Results

![screenshot](/linked_list/easy/141_linked_list_cycle/141_linked_list_cycle.png)
