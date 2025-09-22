class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Map of numbers to their Index
    m = {}
    for i, num in enumerate(nums):
      if target - num in m:
        return [i, m[target-num]]
      else:
        m[num] = i