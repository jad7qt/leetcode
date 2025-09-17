# 383. Ransom Note

### Approach
TODO

### Solution
```
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_freq = {}
        for char in magazine:
            if char in char_freq:
                char_freq[char] = char_freq[char] + 1
            else:
                char_freq[char] = 1
        for char in ransomNote:
            if char in char_freq and char_freq[char] > 0:
                char_freq[char] = char_freq[char] - 1
            else: 
                return False
        return True
```

### Complexity Analysis
#### Time Complexity: $O(n+m)$
For this solution, we iterate over each input string, $ransomNote$ and $magazine$, once with sizes $n$ and $m$ respectively. Verifying if a character in $ransomeNote$ is in $magazine$ is constant time as we check our freqency hashmap. Therefore, the overall time complexity is linear with regard to both input string lengths, $m+n$

#### Space Complexity: $O(1)$
Given that we store the frequencies of all characters in string $magazine$ in a hashmap, the largest possible size of data stored is all lowercase letters, $26$. Given this fixed upper bound of space required, this results in an overall constant space complexity for all inputs.

### Results

![screenshot](/hashmap/easy/383_ransom_note/383_ransom_note.png)
