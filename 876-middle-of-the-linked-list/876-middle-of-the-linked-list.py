# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        mid = count // 2
        cur = head
        for x in range(mid):
            cur = cur.next
        return cur