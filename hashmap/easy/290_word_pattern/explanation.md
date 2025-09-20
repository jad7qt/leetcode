# 290. Word Pattern

### Approach
This solution follows a similar approach to problem 205, Isomorphic Strings, with they main difference being that characters in the the $pattern$ string map to entire words instead of other characters.

First, we split the string $s$ into its separate words, storing the result in a list to make iterating over it easy. If the length of this list  Then, we can iterate through the entire $pattern$ string and create mappings of the character in $pattern$ to its corresponding word in the list created from $s$. Every time we create a new mapping from character to word, we can add the word to our seen set to ensure no more mappings can be made to it. We move through the pattern string creating mappings if they dont already exist, and if they do, verifying that the word matches. If any of the properties are violated, we can return $False$. If the end of the pattern is reached, no bijection properties were violated; therefore, $s$ and $pattern$ follow the same pattern.

### Solution
```
class Solution(object):
  def wordPattern(self, pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    d = {}
    seen = set()
    sList = s.split()
    # If different lengths, no solution possible
    if len(sList) != len(pattern):
      return False
    for i in range(len(pattern)):
      if pattern[i] not in d:
        if sList[i] not in seen:
          d[pattern[i]] = sList[i]
          seen.add(sList[i])
        else:
          return False
      elif d[pattern[i]] != sList[i]:
        return False
    return True
```

### Complexity Analysis
#### Time Complexity: $O(n)$
In this solution, the string $s$ split takes worst case linear time with respect to the length of $s$ to split all words and generate a list, with size $n$. Our pattern loop worst case will interate through the entire length of the string $pattern$, with size $m$. Adding elements to our set and dictionary is constant time, and checking if values exist in both is also constant time. Therefore, our overall time complexity is linear with respect to the input string lengths $n$ and $m$, which are porportional so we can represent the overall complexity as $O(n)$.


#### Space Complexity: $O(n)$
In the worst case, all characters and strings are unique, resulting in a $n$ mappings and $n$ entries in $seen. Therefore, the space complexity is linear. 

### Results

![screenshot](/hashmap/easy/290_word_pattern/290_word_pattern.png)
