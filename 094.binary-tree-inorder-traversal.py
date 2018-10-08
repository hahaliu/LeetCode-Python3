# ex2tron's blog:
# http://ex2tron.wang

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ret.append(root.val)
            inorder(root.right)

        ret = []
        inorder(root)
        return ret
