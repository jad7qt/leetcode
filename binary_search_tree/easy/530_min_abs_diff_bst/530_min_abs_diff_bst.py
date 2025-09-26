# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diff = float('inf')

        if root.left:
            curr = root.left
            while curr.right:
                curr = curr.right
            diff = min(diff, root.val - curr.val)
            diff = min(diff, self.getMinimumDifference(root.left))

        if root.right:
            curr = root.right
            while curr.left:
                curr = curr.left
            diff = min(diff, curr.val - root.val)
            diff = min(diff, self.getMinimumDifference(root.right))

        return diff