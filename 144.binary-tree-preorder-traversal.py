# ex2tron's blog:
# http://ex2tron.wang

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root):
            if not root:
                return

            ret.append(root.val)
            preorder(root.left)
            preorder(root.right)

        ret = []
        preorder(root)

        return ret
