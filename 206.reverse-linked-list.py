# ex2tron's blog:
# http://ex2tron.wang

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))
        count = 1
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
            # print("a", head, "|||", dummy)
            count += 1
        return dummy.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(6)
# l.next.next.next = ListNode(3)
# l.next.next.next.next = ListNode(4)
# l.next.next.next.next.next = ListNode(5)
# l.next.next.next.next.next.next = ListNode(6)
print(Solution().reverseList(l))
