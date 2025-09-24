# 155. Min Stack

### Approach
For this problem, we're required to create a datatype that can run in a fixed time complexity for each function: push, pop, top, and getMin. Given that the first three functions are already constant with a normal stack datatype, we can create a regular $stack$ this for these function. However, we need a way to track our current minimum for the stack - this becomes tricky when values are added and removed, as we need to retain previous minimums in the event that the current minimum is removed. We need to acomplish this in constant time, preventing us from storing the minimum value in an integer - popping a minimum value would take $O(n)$ time complexity to determine the new minimum.

We can use another stack to represent the history of minimums, called $m$, and store the current minimum at the end of the stack. Whenever a new value is added, we can check if it is less than the current minimum (the top of stack $m$) - if so, we can push it to this stack to update our minimum. When we remove any value from our stack, we can check if this value is also our current minimum. If so, we pop it from the minimum stack, retaining the minimum of all values that were added before it. 

In the case that minimum values are repeated (a pushed value is equal to the minimum), we need to make sure they are also repeated in our minimum stack - if not, when we pop this value it will also be removed from our minimum stack, which will result in an incorrect minimum at the end of $m$. Therefore, if a pushed value is less than OR **equal to** our minimum, it should be pushed to the $m$ stack. 

### Solution
```
class MinStack(object):

  def __init__(self):
    self.stack = []
    self.m = []

  def push(self, val):
    """
    :type val: int
    :rtype: None
    """
    self.stack.append(val)
    if len(self.m) < 1:
      self.m.append(val)
    elif val <= self.m[-1]:
      self.m.append(val)
      

  def pop(self):
    """
    :rtype: None
    """
    if self.m[-1] == self.stack[-1]:
        self.m.pop()
    self.stack.pop()

  def top(self):
    """
    :rtype: int
    """
    return self.stack[-1]

  def getMin(self):
    """
    :rtype: int
    """
    return self.m[-1]
```

### Complexity Analysis
#### Time Complexity: $O(1)$
Each function takes constant time to execute, resulting in a fixed time complexity.

#### Space Complexity: $O(n)$
Using two stacks for this solution results in worst case $n$ elements in both. This $2n$ can be simplified to overall linear space complexity with respect to $n$.

### Results

![screenshot](/stack/medium/155_min_stack/155_min_stack.png)
