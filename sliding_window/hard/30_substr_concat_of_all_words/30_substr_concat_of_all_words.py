class Solution(object):
  def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    n = len(words[0])
    window_length = 0
    first = 0
    arr = []
    d = {}
    for word in words:
      if word in d:
        d[word] = d[word] + 1
      else:
        d[word] = 1
      window_length += len(word)

    # Determine if a string is concatenation of all words
    def isConcat(substr):
      d_temp = d.copy()
      first_substr = 0
      section = substr[first_substr:first_substr+n]
      while section in d_temp and d_temp[section] > 0:
        d_temp[section] = d_temp[section] - 1
        if first_substr+n == window_length:
          return True
        first_substr += n
        section = substr[first_substr:first_substr+n]
      return False
    
    # Iterate over all possible substrings
    for last in range(window_length-1, len(s)):
      # Check if substring is concatenation of all words
      if isConcat(s[first:last+1]):
        arr.append(first)

      # Increment first position
      first += 1
  
    return arr