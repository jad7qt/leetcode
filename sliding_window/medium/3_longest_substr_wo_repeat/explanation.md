# 209. Minimum Size Subarray Sum

### Approach
TODO

### Solution
```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        first, last = 0, 0
        length = 0
        substr = ""
        for last in range(len(s)):
            nextchar = s[last]
            while nextchar in substr:
                first += 1
                substr = substr[1:]
            substr = substr + nextchar
            length = max(length, len(substr))
        return length
```

### Complexity Analysis
#### Time Complexity: $O(n^2)$
For this sliding window approach, our longest case for both loops is over the entire list length, $n$. Each character is visited at most twice. However, within this loop we create 

#### Space Complexity: $O(n)$
For all inputs, a string is stored representing the substring. The length of this string, in the worst case, can be the entire size of the 

### Results

![screenshot](/sliding_window/medium/3_longest_substr_wo_repeat/3_longest_substr_wo_repeat.png)
