# 21. Merge Two Sorted Lists

### Approach
This problem can be solved recursively, allowing us to process a single node of our new list every recurse. We start with a base case of empty input lists: if either $list1$ or $list2$ are empty, we can return the other one. If both lists do exist, we can compart the values of each item at the head and select the one that is lowest. This will be the start of our new list, and we can then find the next node of our list - which happens to be all of the elements of both lists **without** the item we just selected. This is where our recursion happens, as we can pass the next node of our chosen ListNode and the entire unselected list to recurse and return the "head" of that sublist to set as our next ListNode in our combined sorted Linked List. After getting this sublist, we can connect the two by setting our current head's next to this sublist. The end result is the entire sorted list combined. 

### Solution
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
  def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not list1:
      return list2
    if not list2:
      return list1

    if list1.val < list2.val:
      head = list1
      head.next = self.mergeTwoLists(list1.next, list2)
    else:
      head = list2
      head.next = self.mergeTwoLists(list1, list2.next)
    
    return head
```

### Complexity Analysis
#### Time Complexity: $O(n)$
Since the solution iterates through both linked lists, we can consider the time complexity linear with respect to the length of both lists $(len(list1) + len(list2) = n)$.

#### Space Complexity: $O(n)$
The solution recursively processes each node in each linked list, pushing new stack frames to the call stack each time. This results in a linear space complexity.

### Results

![screenshot](/linked_list/easy/21_merge_two_sorted_lists/21_merge_two_sorted_lists.png)
