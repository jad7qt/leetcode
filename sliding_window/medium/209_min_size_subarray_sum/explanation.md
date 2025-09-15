# 209. Minimum Size Subarray Sum

### Approach
TODO

### Solution
```
class Solution(object):
  def minSubArrayLen(self, target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    first = 0
    ml = float('inf')
    s = 0
    for second in range(0, len(nums)):
      s += nums[second]
      while s >= target and first <= second:
        # save minimum
        ml = min(ml, second - (first-1))
        # move first pointer up and subtract from sum
        s -= nums[first]
        first += 1
    return ml if ml < float('inf') else 0
```

### Complexity Analysis
#### Time Complexity: $O()$


#### Space Complexity: $O()$

### Results

![screenshot](/sliding_window/medium/209_min_size_subarray_sum/209_min_size_subarray_sum.png)
