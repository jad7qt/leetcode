class Solution(object):
  def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) <= 0:
      return True
    p1, p2 = 0, 0
    while p1 < len(s) and p2 < len(t):
      if t[p2] == s[p1]:
        # Char found, move to next
        p1 += 1
        if p1 >= len(s):
          return True
      p2 += 1
    return False