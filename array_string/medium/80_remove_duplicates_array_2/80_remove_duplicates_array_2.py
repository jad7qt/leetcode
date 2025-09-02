class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-2:
            # while the element 2 spaces ahead is equal, remove it
            while i+2 < len(nums) and nums[i+2] == nums[i]:
                nums.pop(i+2)
            i += 1