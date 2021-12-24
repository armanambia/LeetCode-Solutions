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
        res = head
        prev = res
        next_elem = prev.next
        if next_elem == None:
            return None
        
        count = 0
        temp = head
        while temp != None:
            count += 1
            temp = temp.next
        
        i = 0
                
        while i < (count - n - 1):
            prev = next_elem
            next_elem = next_elem.next
            i += 1
        
        print(prev)
        print(next_elem)
        if i == 0:
            if n == count:
                res = res.next
            else:
                prev.next = None if next_elem == None else next_elem.next
        else:
            prev.next = None if next_elem == None else next_elem.next
        return res