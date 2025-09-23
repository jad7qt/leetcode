# 202. Happy Number

### Approach
TODO

### Solution
```
class Solution(object):
  def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    # Assume the moment we hit a cycle, the number is not happy
    m = set()
    num = n
    s = 1
    while s not in m:
      m.add(s)
      s = 0
      while num > 0:
        # add squares
        s += (num % 10)**2
        num = num / 10
      if s == 1:
        return True
      num = s
    return False
```

### Complexity Analysis
#### Time Complexity: $O()$


#### Space Complexity: $O()$


### Results

![screenshot](/hashmap/easy/202_happy_number/202_happy_number.png)
