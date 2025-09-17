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