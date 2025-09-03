class Solution(object):
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    p1, p2 = 0, len(numbers)-1
    while p1 < p2:
      s = numbers[p1] + numbers[p2]
      if s == target:
        return [p1+1, p2+1]
      elif s < target:
        p1 += 1
      else:
        p2 -= 1