# ex2tron's blog:
# http://ex2tron.wang

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.overrideSum(root, False)

    def overrideSum(self, root, is_left):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return root.val if is_left else 0
        else:
            return self.overrideSum(root.left, True) + self.overrideSum(root.right, False)


tree = TreeNode(3)
# tree.left = TreeNode(9)
# tree.right = TreeNode(20)
# tree.right.left = TreeNode(15)
# tree.right.right = TreeNode(7)
print(Solution().sumOfLeftLeaves(tree))
