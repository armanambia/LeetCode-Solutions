# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        elif not list2:
            return list1
        v1 = list1.val
        v2 = list2.val
        if v1< v2:
            og = ListNode(v1)
            list1 = list1.next
        else:
            og = ListNode(v2)
            list2 = list2.next
        res = og
        while list1 and list2:
            v1 = list1.val
            v2 = list2.val
            if v1 < v2:
                res.next = ListNode(v1)
                list1 = list1.next
            else:
                res.next = ListNode(v2)
                list2 = list2.next
            res = res.next
        if list1:
            while list1:
                res.next = ListNode(list1.val)
                res = res.next
                list1 = list1.next
        else:
            while list2:
                res.next = ListNode(list2.val)
                res = res.next
                list2 = list2.next
        return og