# ex2tron's blog:
# http://ex2tron.wang

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def __repr__(self):
    #     if self:
    #         return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = float('-inf')
        self.result = float('inf')
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.result = min(self.result, node.val-self.prev)
        # print(self.result)
        self.prev = node.val
        self.dfs(node.right)
