/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        if (head == null || head.next == null || head.next.next == null) return null;
        do {
            slow = slow.next;
            fast = fast.next.next;
            // System.out.println("-----iteration");
            // System.out.println(slow.val);
            // System.out.println(fast.val);
        }
        while(slow != fast && fast != null && fast.next != null && fast.next.next != null);
        slow = head;
        while(slow!=fast && fast!= null){
            slow=slow.next;
            fast = fast.next;
        }
        return fast;
    }
}