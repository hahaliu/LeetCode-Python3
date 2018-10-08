# ex2tron's blog:
# http://ex2tron.wang

# 我的思路：先转换为列表，然后分配长度进行切片

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        root_lst = []
        while root:
            root_lst.append(root.val)
            root = root.next

        ret = []
        sl, remain = divmod(len(root_lst), k)
        incre, count, start = 0, 0, 0
        for _ in range(k):
            incre = 0 if count >= remain else 1
            ret.append(root_lst[start:start+sl+incre])
            start = start+sl+incre
            count += 1

        return ret


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(6)
l.next.next.next.next.next.next = ListNode(7)

print(Solution().splitListToParts(l, 10))
