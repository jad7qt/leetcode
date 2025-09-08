# 167. Two Sum II - Input Array Is Sorted

### Approach
For this problem, we can start by using a classic two pointer approach. Given the array provided is already sorted in ascending order, we can start one pointer on the first element and the second pointer on the last element, guarenteed to be the lowest and the highest elements respectively. We can proceed as follows:

If the sum of the two elements is: 
- Equal to the target: 
  - return the 2 pointers
- Less than the target:
  - our value needs to increase
  - p1 should be incremented
- Greater than the target:
  - our value needs to decrease
  - p2 should be decremented

### Solution
```
class Solution(object):
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    p1, p2 = 0, len(numbers)-1
    while p1 < p2:
      s = numbers[p1] + numbers[p2]
      if s == target:
        return [p1+1, p2+1]
      elif s < target:
        p1 += 1
      else:
        p2 -= 1
```

### Complexity Analysis
#### Time Complexity: $O(n)$
The loop in the worst case will continue until $p1$ and $p2$ reach each other from each end of the list, incrementing once for each item - resulting in a linear time complexity. 

#### Space Complexity: $O(1)$
For all possible inputs, only the $p1$, $p2$, and $s$ integer variables are used - resulting in a fixed space complexity. 

### Results

![screenshot](/two_pointer/medium/167_two_sum_2/167_two_sum_2.png)
