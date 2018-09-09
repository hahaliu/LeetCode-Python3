class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 别人的代码
# class Solution:
#     # @param two ListNodes
#     # @return the intersected ListNode
#     def getIntersectionNode(self, headA, headB):
#         curA, curB = headA, headB
#         begin, tailA, tailB = None, None, None

#         # a->c->b->c
#         # b->c->a->c
#         while curA and curB:
#             if curA == curB:
#                 begin = curA
#                 break

#             if curA.next:
#                 curA = curA.next
#             elif tailA is None:
#                 tailA = curA
#                 curA = headB
#             else:
#                 break

#             if curB.next:
#                 curB = curB.next
#             elif tailB is None:
#                 tailB = curB
#                 curB = headA
#             else:
#                 break

#         return begin

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        na = self.getCount(headA)
        nb = self.getCount(headB)
        nm = max(na, nb)
        diff = abs(na-nb)

        if na > nb:
            lc, c = headA, headB
        else:
            lc, c = headB, headA

        for i in range(diff):
            lc = lc.next

        ret, result = False, ListNode(0)
        for i in range(diff, nm):
            if lc == c:
                result.next = lc
                ret = True
            elif ret and lc != c:
                ret = False
            lc = lc.next
            c = c.next

        return result.next if ret else None

    def getCount(self, head):
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        return count


l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(5)

l2 = ListNode(3)
l2.next = ListNode(3)
l2.next.next = ListNode(5)
print(Solution().getIntersectionNode(l, l2).val)
