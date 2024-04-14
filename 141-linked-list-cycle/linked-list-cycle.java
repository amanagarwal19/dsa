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
    public boolean hasCycle(ListNode head) {

        if(head==null)
            return false;
        ListNode slow=null,fast = head;
        while(slow!=fast && fast!=null && fast.next!=null){
            if(slow==null)
                slow = head;
            else
                slow = slow.next;
            fast = fast.next.next;
        }
        if(slow==fast)
            return true;
        return false;


    }
}