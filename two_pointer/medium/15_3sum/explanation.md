# 15. 3Sum 

### Approach
TODO

### Solution
```
class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    for first in range(len(nums)):
      if nums[first] > 0:
        break
      # skip duplicate elements
      if first > 0 and nums[first] == nums[first-1]:
        continue
      second, third = first+1, len(nums)-1
      while second < third:
        if nums[first] + nums[second] + nums[third] == 0:
          res.append([nums[first], nums[second], nums[third]])
          # Skip all duplicates
          second += 1
          third -= 1
          while nums[second] == nums[second-1] and second < third:
            second += 1
        elif nums[first] + nums[second] + nums[third] > 0:
          # decrement right pointer
          third -= 1
        else:
          # increment left pointer
          second += 1
    return res
```

### Complexity Analysis
#### Time Complexity: $O()$


#### Space Complexity: $O()$


### Results

![screenshot](/two_pointer/medium/15_3sum/15_3sum.png)
