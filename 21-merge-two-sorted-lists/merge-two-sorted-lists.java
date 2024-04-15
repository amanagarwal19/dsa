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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1==null)
            return list2;
        if(list2==null)
            return list1;
        
        ListNode dummy = null;
        ListNode curr = null;

        // Choose starting list
        if(list1.val<=list2.val){
            dummy = list1;
            curr = list1;
            list1 = list1.next;
        }else{
            dummy = list2;
            curr = list2;
            list2 = list2.next;
        }

        while(list1!=null && list2!=null){
            // 1 2 3    // 2 3 5    // 1 2 3    // 2 4 5    // 1 3 4    2       4
            // 2 4 5    // 1 2 3    // 1 3 5    // 1        // 2        3 4 5   1 2 3
            if(list1.val <= list2.val){
                curr.next = list1;
                list1 = list1.next;
            }
            else{
                curr.next = list2;
                list2 = list2.next;
            }
            curr = curr.next;
        }
       
        if(list1!=null)
            curr.next = list1;
        else if(list2!=null)
            curr.next = list2;
        return dummy;
    }
}