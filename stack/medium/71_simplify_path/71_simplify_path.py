class Solution(object):
  def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    stack = []
    directories = path.split("/")
    for d in directories:
      # handle each input possibility
      if d == "" or d == ".":
        # skip
        continue
      elif d == "..":
        if len(stack) > 0:
          stack.pop()
      else:
        stack.append(d)
    return '/' + '/'.join(stack)