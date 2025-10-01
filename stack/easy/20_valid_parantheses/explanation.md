# 20. Valid Parantheses

### Approach
For this problem, we can use a stack to retain all of the previous pareentheses that have not been closed yet. Iterating through the string $s$ from start to finish, we can take each character and take one of 2 approaches:
1. If the character is a closing bracket, pop the last character from the stack and verify it is a matching open bracket. If no match or stack empty, return $False$.
2. If the character is not a closing bracket, add it to the stack.

After all characters have been accounted for, we can check the length of the stack - if the stack size is not 0, then there must be unclosed parentheses left and the string is not a valid parentheses sequence.

This approachs works for the two main forms of multiple parentheses, nested and side by side. For *side by side* parentheses, each set of parentheses is pushed and then popped from the stack, leaving it empty for the next set - returning true at the end when the stack is empty. For *nested* parentheses, (for example, "{{}}" ) the first two open brackets are pushed to the stack. When the first close bracket is found, the corresponding open bracket is popped from the stack, leaving the next close bracket to pop the first character open bracket and return true when the stack is shown to be empty. Both of these situations generalize to more complicated input possibilities. 

### Solution
```
class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    m = {
      ')': '(',
      '}': '{',
      ']': '[',
    }
    for char in s:
      if char in m:
        if len(stack) < 1 or stack[-1] != m[char]:
          return False
        else: 
          stack.pop()
      else:
        stack.append(char)
    return True if len(stack) == 0 else False
```

### Complexity Analysis
#### Time Complexity: $O(n)$
Every character of the input string, $s$, is visited once - resulting in a linear time complexity with respect to the length of the string $s$.

#### Space Complexity: $O(n)$
In the worse case, all characters of $s$ are pushed to the stack requiring $n$ space, resulting in a linear space complexity.


### Results

![screenshot](/stack/easy/20_valid_parentheses/20_valid_parentheses.png)
