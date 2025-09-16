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