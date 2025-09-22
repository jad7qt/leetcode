class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    m = {}
    for word in strs:
      alphabetical_str = "".join(sorted(word))
      if alphabetical_str in m:
        m[alphabetical_str].append(word)
      else:
        m[alphabetical_str] = [word]

    arr = []
    for value in m.values():
      arr.append(value)
    return arr