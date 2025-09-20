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