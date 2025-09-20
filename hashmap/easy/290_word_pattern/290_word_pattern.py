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