
# 我的思路：循环交换即可
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


#　更简洁的写法
# def invertTree(self, root):
#     if root is not None:
#         root.left, root.right = self.invertTree(
#             root.right), self.invertTree(root.left)

#     return root
