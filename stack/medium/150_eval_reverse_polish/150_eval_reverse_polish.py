class Solution(object):
  def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for val in tokens:
      if val == "+":
        temp = stack[-1] + stack[-2]
        stack.pop()
        stack.pop()
        stack.append(temp)
      elif val == "-":
        temp = stack[-2] - stack[-1]
        stack.pop()
        stack.pop()
        stack.append(temp)
      elif val == "*":
        temp = stack[-1] * stack[-2]
        stack.pop()
        stack.pop()
        stack.append(temp)
      elif val == "/":
        temp = trunc(float(stack[-2]) / float(stack[-1]))
        stack.pop()
        stack.pop()
        stack.append(int(temp))
      else:
        stack.append(int(val))
    return stack[0]