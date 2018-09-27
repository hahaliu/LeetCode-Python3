# 我的思路：子树最大+1（没有完全写出来，参考别人的代码）
# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0

        depth = 0
        for ch in root.children:
            depth = max(depth, self.maxDepth(ch))

        return depth+1
