# 27. Remove Element

### Approach
For this problem, simply iterating through each item in the array and checking if it matches the target value is sufficient for finding all instances and removing them. We can use a while loop with iterator variable i to hold our current position. If a number needs to be removed from the array, the iterator value should not be incremented as the next value takes the place of our popped value.

### Solution
```
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
```

### Complexity Analysis
#### Time Complexity: $O(n)$
Our while loop accesses each item of the original list once to verify if it matches the target value, resulting in a linear time complexity.

#### Space Complexity: $O(1)$
For all possible inputs, only one integer variable is used - resulting in a fixed space complexity. 

### Results

![screenshot](/array_string/easy/27_remove_element/27_remove_element.png)
