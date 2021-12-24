# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        i = 0;
        while l1 != None:
            num1 += pow(10, i) * l1.val 
            i += 1
            l1 = l1.next
        i = 0;
        while l2 != None:
            num1 += pow(10, i) * l2.val 
            i += 1
            l2 = l2.next
        dig = num1 % 10
        num1 /= 10
        res = ListNode(dig, None)
        temp = res
        while num1 != 0:
            dig = num1 % 10
            num1 /= 10
            temp.next = ListNode(dig, None)
            temp = temp.next
        
        return res
            