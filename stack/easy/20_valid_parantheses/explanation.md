# 20. Valid Parantheses

### Approach
TODO

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
#### Time Complexity: $O()$


#### Space Complexity: $O()$


### Results

![screenshot](/stack/easy/20_valid_parentheses/20_valid_parentheses.png)
