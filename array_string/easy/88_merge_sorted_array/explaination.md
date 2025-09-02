# 88. Merge Sorted Array

### Approach
In this problem, the first array *nums1* must be modified in place for the final result. The end section of *nums1* that will be overwritten is already filled in with 0s, allowing us to replace them with the contents of *nums2*. We can iterate over this section of *nums1*, which starts at position m, and write the contents of *nums2*, starting at position 0. The length of the *nums1* array is guarenteed to be $m+n$, allowing us to iterate until this position. 

### Solution
```
class Solution(object):
  def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    for i in range(m,m+n):
      nums1[i] = nums2[i-m]
    nums1.sort()
```

### Complexity Analysis
#### Time Complexity: $O((m+n) * log(m+n))$
First, our for loop accesses each item of the *nums2* list to add to *nums1*, resulting in $n$ iterations and a time complexity of $O(n)$. Secondly, we use the python sort function on the final array of size $m+n$, resulting in a time complexity of $O((m+n) * log(m+n))$. This results in an overall log-linear time complexity.

#### Space Complexity: $O(1)$
For all possible inputs, only the i iterator variable is used - resulting in a fixed space complexity. 

### Results

![screenshot](/array_string/easy/88_merge_sorted_array/88_merge_sorted_array.png)
