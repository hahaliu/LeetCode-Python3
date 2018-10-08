# ex2tron's blog:
# http://ex2tron.wang

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getHeight(root) >= 0

    def getHeight(self, root):
        if root is None:
            return 0
        left_h, right_h = self.getHeight(root.left), self.getHeight(root.right)
        if left_h == -1 or right_h == -1 or abs(left_h-right_h) > 1:
            return -1
        return max(left_h, right_h)+1
