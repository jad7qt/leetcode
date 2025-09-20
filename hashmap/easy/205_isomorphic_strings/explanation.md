# 205. Isomorphic Strings

### Approach
To determine if the two input strings, $s$, and $t$, are isomorphic, we can iterate through the string $s$ and map each character to its corresponding index in $t$. If the character in $s$ has already been mapped to a different character OR if the character that we are mapping to already has another mapping previously, there is no possible solution and the strings are not isomorphic. We can retain this information by storing the character in $s$ as a key to the value it should map to, the character in $t$. When we create a new mapping, we can add the character in $t$ to a set, $seen$. This allows us to keep track of characters in $t$ that already have been mapped to, as no two characters in $s$ can map to the same character in $t$. If we reach the end of both strings and none of these conditions were violated, the mappings are valid and the strings are isomorphic.

### Solution
```
class Solution(object):
  def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d = {}
    seen = set()
    for i in range(len(s)):
      if s[i] in d and d[s[i]] != t[i]:
        return False
      elif s[i] not in d:
        if t[i] not in seen:
          seen.add(t[i])
          d[s[i]] = t[i]
        else:
          return False
    return True
```

### Complexity Analysis
#### Time Complexity: $O(n)$
In this solution's, our longest possible loop will interate through the entire length of string $s$. Adding elements to our set and dictionary is constant time, and checking if values exist in both is also constant time. Therefore, our overall time complexity is linear with respect to the input string length $s$.

#### Space Complexity: $O(1)$
This solution uses both a set and a dictionary to store mappings of characters from $s$ to $t$ and track which characters have been mapped already. However, our constraints guarantee that both $s$ and $t$ consist of valid ascii characters which limit them to 128 unique values. Therefore, for all inputs regardless of size, our set and dictionary will max at 128 each, resulting in a fixed space complexity. 

### Results

![screenshot](/hashmap/easy/205_isomorphic_strings/205_isomorphic_strings.png)
