# 392. Is Subsequence

### Approach
For this problem, we need to ensure all characters of the string $s$ appear in string $t$ in the same order. To achieve this, we can use a two pointer approach. One pointer, $p1$, keeps track of the character in string $s$ that we need to find. The other pointer, $p2$, moves through the second string, $t$, to find matching characters. When a match is found, $p1$ can be moved forward. If the last character of $s$ is found, we can return True. Otherwise, if the end of string $t$ is reached and not all characters are found, return False.

### Solution
```
class Solution(object):
  def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) <= 0:
        return True
    p1, p2 = 0, 0
    while p2 < len(t):
      if t[p2] == s[p1]:
        # Char found, move to next
        p1 += 1
        if p1 >= len(s):
          return True
      p2 += 1
    return False
```

### Complexity Analysis
#### Time Complexity: $O(n)$
In the worst case scenario where we search the entire string $t$, we iterate over it's entire length, n. We are guarenteed to iterate no more than n times, resulting in a linear time complexity with respect to the length of input string $t$.

#### Space Complexity: $O(1)$
For all possible inputs, only the $p1$ and $p2$ iterator variables are used - resulting in a fixed space complexity. 

### Results

![screenshot](/two_pointer/easy/392_is_subsequence/392_is_subsequence.png)
