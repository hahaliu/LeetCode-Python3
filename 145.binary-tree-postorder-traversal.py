# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def postorder(root):
            if not root:
                return

            postorder(root.left)
            postorder(root.right)
            ret.append(root.val)

        ret = []
        postorder(root)

        return ret


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
print(Solution().postorderTraversal(tree))
