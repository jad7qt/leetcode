class Solution(object):
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    copy = nums[:]
    if (k == 0):
      return
    for i in range(len(nums)):
      spot = (len(nums) - k + i) % len(nums)
      nums[i] = copy[spot]