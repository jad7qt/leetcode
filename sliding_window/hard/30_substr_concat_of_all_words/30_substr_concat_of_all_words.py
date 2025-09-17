class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordLen = len(words[0])
        numWords = len(words)
        totalLen = wordLen * numWords
        arr = []
        d = {}

        # Create frequency map
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
        
        for initialStart in range(wordLen):
            d_temp = d.copy()
            # check each word
            first, second = initialStart, initialStart + wordLen
            substrFirst = initialStart

            for second in range(initialStart + wordLen, len(s)+1, wordLen):
                currWord = s[substrFirst:second]
                if currWord in d_temp:
                    if d_temp[currWord] > 0:
                        # word in list and frequency not violated, continue after decrementing frequency
                        d_temp[currWord] = d_temp[currWord] - 1

                        # if current length is equal to total length, add index to arr
                        if second - first == totalLen:
                            # remove word from beginning and add to arr
                            arr.append(first)
                            removedWord = s[first:first+wordLen]
                            d_temp[removedWord] = d_temp[removedWord] + 1
                            first += wordLen
                    else:
                        # word violated frequency, remove from left until no longer violated
                        while d_temp[currWord] < 1:
                            removedWord = s[first:first+wordLen]
                            d_temp[removedWord] = d_temp[removedWord] + 1
                            first += wordLen
                        d_temp[removedWord] = d_temp[removedWord] - 1
                else:
                    # word not in list, reset d_temp and move to next word
                    first = second
                    d_temp = d.copy()
                substrFirst += wordLen
        return arr