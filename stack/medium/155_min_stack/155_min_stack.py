class MinStack(object):

  def __init__(self):
    self.stack = []
    self.m = []

  def push(self, val):
    """
    :type val: int
    :rtype: None
    """
    self.stack.append(val)
    if len(self.m) < 1:
      self.m.append(val)
    elif val <= self.m[-1]:
      self.m.append(val)
      

  def pop(self):
    """
    :rtype: None
    """
    if self.m[-1] == self.stack[-1]:
        self.m.pop()
    self.stack.pop()

  def top(self):
    """
    :rtype: int
    """
    return self.stack[-1]

  def getMin(self):
    """
    :rtype: int
    """
    return self.m[-1]
