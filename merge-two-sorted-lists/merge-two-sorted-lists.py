# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = None
        parent = res
        while l1 != None and l2 != None:
            l1_val = l1.val
            l2_val = l2.val
            val = 0
            if l1_val < l2_val:
                val = l1_val
                l1 = l1.next
            else:
                val = l2_val
                l2 = l2.next
            
            if parent == None:
                res = ListNode(val)
                parent = res
            else:
                res.next = ListNode(val)
                res = res.next
        
        while l1 != None:
            if parent == None:
                res = ListNode(l1.val)
                parent = res
            else:
                res.next = ListNode(l1.val)
                res = res.next
            l1 = l1.next
        while l2 != None:
            if parent == None:
                res = ListNode(l2.val)
                parent = res
            else:
                res.next = ListNode(l2.val)
                res = res.next
            l2 = l2.next
        
        return parent