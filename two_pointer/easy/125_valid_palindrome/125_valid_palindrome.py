import re

class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    letter_string = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    if letter_string == letter_string[::-1]:
      return True
    return False