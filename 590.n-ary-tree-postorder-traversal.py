# ex2tron's blog:
# http://ex2tron.wang

# 我的思路：遍历children，再添加val
# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def post(tree):
            if not tree:
                return None

            for ch in tree.children:
                post(ch)
            ret.append(tree.val)

        ret = []
        post(root)
        return ret
