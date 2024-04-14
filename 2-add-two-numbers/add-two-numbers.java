/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode lastNode = null;
        ListNode ans = l1;

        int quotient = 0;
        int digit = 0;
        while(l1!=null && l2!=null){
            int sum = l1.val + l2.val + quotient;
            quotient = sum/10;
            digit = sum%10;
            l1.val = digit;
            if(l1.next==null)   //to preserve pointer to attach any remaining quotient
                lastNode = l1;
            l1 = l1.next;
            l2 = l2.next;
        }
        while(l1!=null){
            int sum = l1.val+quotient;
            quotient = sum/10;
            digit = sum%10;
            l1.val = digit;
            if(l1.next==null)   //to preserve pointer to attach any remaining quotient
                lastNode = l1;
            l1=l1.next;
        }
        lastNode.next = l2; //since we storing result in l1
        while(l2!=null){
            int sum = l2.val+quotient;
            quotient = sum/10;
            digit = sum%10;
            l2.val = digit;
            if(l2.next==null)   //to preserve pointer to attach any remaining quotient
                lastNode = l2;
            l2=l2.next;
        }

        if(quotient!=0){
            lastNode.next = new ListNode(quotient);
        }
        return ans;

    }
}