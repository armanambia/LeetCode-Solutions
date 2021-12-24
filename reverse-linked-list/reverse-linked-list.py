# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        l1 = head
        if l1 == None:
            return None
        while l1 != None:
            stack.append(ListNode(l1.val, None))
            l1 = l1.next
        res = stack.pop()
        cur = res
        while len(stack) > 0:
            cur.next = stack.pop()
            cur = cur.next
        return res
            