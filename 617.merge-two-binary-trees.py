# ex2tron's blog:
# http://ex2tron.wang


# 我的思路，左右是否为None分开进行讨论
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        elif t1 and t2:
            tree = TreeNode(t1.val+t2.val)
            tree.left = self.mergeTrees(t1.left, t2.left)
            tree.right = self.mergeTrees(t1.right, t2.right)
        elif t1 is None:
            tree = TreeNode(t2.val)
            tree.left = self.mergeTrees(None, t2.left)
            tree.right = self.mergeTrees(None, t2.right)
        elif t2 is None:
            tree = TreeNode(t1.val)
            tree.left = self.mergeTrees(t1.left, None)
            tree.right = self.mergeTrees(t1.right, None)

        return tree


# 我写的太复杂，别人的代码：

# class Solution:
#     def mergeTrees(self, t1, t2):
#         """
#         :type t1: TreeNode
#         :type t2: TreeNode
#         :rtype: TreeNode
#         """
#         if t1 is None:
#             return t2
#         if t2 is None:
#             return t1

#         t1.val += t2.val
#         t1.left = self.mergeTrees(t1.left, t2.left)
#         t1.right = self.mergeTrees(t1.right, t2.right)

#         return t1
