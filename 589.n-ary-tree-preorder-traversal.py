# 我的思路：先添加val，遍历children
# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def pre(tree):
            if not tree:
                return None

            ret.append(tree.val)

            for ch in tree.children:
                pre(ch)

        ret = []
        pre(root)
        return ret
