# 189. Rotate Array

### Approach
For this problem, I started by copying the entire list to retain the order while I edited the original. With this copy, we can determine what values should be written for each position. Finding the position of the element to overwrite a given spot, $i$, can be determined by subtracting $i-k$. This approach works for any position where the result is non-negative. To generalize this case, we can use modulus of this subtraction by the length of the list to wrap back around from the first position to the last position instead of returning negative indices. Therefore, the position of the element we want to replace $i$ with is $(i-k)\;\%\;len(nums)$.

### Solution
```
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
      spot = (i - k) % len(nums)
      nums[i] = copy[spot]
```

### Complexity Analysis
#### Time Complexity: $O(TODO)$


#### Space Complexity: $O(n)$

### Results

![screenshot](/array_string/medium/189_rotate_array/189_rotate_array.png)
