# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        t = head
        h = head
        if head == None:
            return False
        while h.next != None and h.next.next != None:
            t= t.next
            h = h.next.next
            if t == h:
                return True
                # t == head
                # while t != h:
                #     t = t.next
                #     h = h.next
                # return t
                # above code will finish the tortoise and hare finding the cycle start
        return False