class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        charFreq = {}
        for char in t:
            if char in charFreq:
                charFreq[char] = charFreq[char] + 1
            else:
                charFreq[char] = 1
        minLen = float('inf')
        minFirst, minSecond = 0, 0
        first, second = 0, 0
        currCount = 0

        # sliding window here
        while second < len(s):
            currChar = s[second]
            if currChar in charFreq:
                if charFreq[currChar] > 0:
                    currCount += 1
                charFreq[currChar] = charFreq[currChar] - 1
            second += 1
            # Found a string solution
            while currCount == len(t):
                if second - first < minLen:
                    minFirst = first
                    minSecond = second
                    minLen = second - first
                if s[first] in charFreq:
                    charFreq[s[first]] = charFreq[s[first]] + 1
                    if charFreq[s[first]] > 0:
                        currCount -= 1
                first += 1

        return s[minFirst:minSecond] if minLen < float('inf') else ""