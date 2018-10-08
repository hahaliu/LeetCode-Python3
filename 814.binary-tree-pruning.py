# ex2tron's blog:
# http://ex2tron.wang


# 我的思路：左右子树的值情况分类，解法有问题，没通过
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def pruneTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         if root.left is None and root.right is None:
#             if root.val == 0:
#                 root = None
#         elif root.left is None:
#             root.right = self.pruneTree(root.right)
#         elif root.right is None:
#             root.left = self.pruneTree(root.left)
#         else:
#             if root.left.val == 1 or root.right.val == 1:
#                 # 保留
#                 root.left = self.pruneTree(root.left)
#                 root.right = self.pruneTree(root.right)
#             else:
#                 root = None
#         return root


# 别人的代码：
class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None

        return root


# 别人的思路2：跟我的很像：
# class Solution:
#     def pruneTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         def prune(tree):
#             if tree is None:
#                 return True

#             # 叶节点
#             if tree.left is None and tree.right is None:
#                 if tree.val is None or tree.val == 0:
#                     return True
#                 else:
#                     return False

#             # 非叶节点：
#             prune_left = prune(tree.left)
#             prune_right = prune(tree.right)

#             if prune_left:
#                 tree.left = None
#             if prune_right:
#                 tree.right = None

#             if tree.val == 0 and prune_left and prune_right:
#                 return True
#             else:
#                 return False


tree = TreeNode(1)
tree.left = TreeNode(0)
# tree.right = TreeNode(0)
# tree.left.left = TreeNode(1)
# tree.left.right = TreeNode(1)
# tree.right.left = TreeNode(0)
# tree.right.right = TreeNode(1)
# tree.left.left.left = TreeNode(0)


print(Solution().pruneTree(tree))
