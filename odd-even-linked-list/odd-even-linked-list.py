# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None or head.next.next == None:
            return head
        
        odd = head
        even = head.next
        feven = even
        
        
        while even != None and even.next != None:
            # print(odd)
            # print(even)
            odd.next = even.next
            even.next = odd.next.next
            odd.next.next = feven
            
            odd = odd.next
            even = even.next
            # print (head)
            # print('-----------------')
        return head