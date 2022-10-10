# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        stack = []
        node = head
        while node != None:
            stack.append(node)
            node = node.next
        for x in range(n):
            stack.pop()
        if len(stack) == 0:
            head = head.next
        else:
            node = stack.pop()
            node.next = node.next.next
        return head