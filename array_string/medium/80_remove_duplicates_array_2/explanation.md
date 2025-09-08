# 80. Remove Duplicates from Sorted Array II

### Approach
For this problem, there are two important elements I focused on: 
1. the array is sorted in ascending order
2. each element can appear at most twice

Given that the array is already sorted for us, we can iterate through the list and check 2 items ahead to see if there exist at least 3 items that are the same. If they are equal the 3rd item should be removed. This should be repeated to ensure all following values that are equal are removed. When/if an item is reached that is not equal to the current, we can move onto checking the next item in the list for duplicates.

### Solution
```
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
```

### Complexity Analysis
#### Time Complexity: $O()$


#### Space Complexity: $O(1)$
For all possible inputs, only the i iterator variable is used - resulting in a fixed space complexity. 

### Results

![screenshot](/array_string/medium/80_remove_duplicates_array_2/80_remove_duplicates_array_2.png)
