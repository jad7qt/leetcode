# 209. Minimum Size Subarray Sum

### Approach
Using a classic sliding window approach for this problem, we can initialize 2 pointers representing the start and end of our window, $first$ and $second$. Along with this, we can store the current size of the window in $s$ and the overall minimum length found as $ml$. 

We can start by incrementing the end of our window, adding each number to our current sum $s$. When our sum is greater than or equal to our target, we have found a solution and can check if our current window length is a new minimum. 

We can now start to remove numbers from the beginning of our list as we have already found our shortest solution starting at $first$. We can move the start of our window by incrementing $first$ and removing it's value from the summation, $s$. We can check if our new window from [$first+1$, $second$] satisfies the target requirement. If it does, we can repeat our check on the overall minimum and removing another number from the beginning. When we finally remove enough numbers where our target sum is not met, we can go back to increasing the window size at the right side, $second$, to find the next solution.

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
#### Time Complexity: $O(n)$
With this sliding window approach, both pointers iterate at worst case over the entire list length, $n$. Therefore, the time complexity of this solution is linear.

#### Space Complexity: $O(1)$
Only 4 integer values, 2 pointers and 2 summations, are stored for all inputs regardless of length. Therefore, the space complexity is fixed.

### Results

![screenshot](/sliding_window/medium/209_min_size_subarray_sum/209_min_size_subarray_sum.png)
