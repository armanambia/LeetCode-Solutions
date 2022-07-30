# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        t = head
        h = head
        while h and h.next:
            t = t.next
            h = h.next.next
            if t == h:
                return True
        return False