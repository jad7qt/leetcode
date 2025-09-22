# 1. Two Sum

### Approach
For this problem, we need to find the two numbers in the list $nums$ that add up to the input number $target$. We can store each number in $nums$ in a hashmap corresponding to it's position in the number array. Iterate through the entire $nums$ array, we can check if a second number exists already in the hashmap that, when added with our current number, equals the $target$ value. If this number exists, we can return the indices of both. If no such number exists, we can add our current number to the map.

Any duplicate numbers that add up to the target will be found as the hashmap write only occurs after checking if a summation equal to the target exists. 

### Solution
```
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
```

### Complexity Analysis
#### Time Complexity: $O(n)$
This solution only iterates through the $nums$ array, length $n$, and accesses the contents once. Accessing/writing to the hashmap is of fixed time complexity. Therefore, the overall time complexity is linear.

#### Space Complexity: $O(n)$
Our hashmap in worst case will be filled with all but one number in the number array, or length $n-1$. This simplifies to overall linear space complexity.

### Results

![screenshot](/hashmap/easy/1_two_sum/1_two_sum.png)
