class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
      return False
    # Create frequency hashmap
    m = {}
    for char in s:
      if char in m:
        m[char] = m[char] + 1
      else: 
        m[char] = 1
    # Check string t
    for char in t:
      if char in m and m[char] > 0:
        m[char] = m[char] - 1
      else:
        return False
    
    return True