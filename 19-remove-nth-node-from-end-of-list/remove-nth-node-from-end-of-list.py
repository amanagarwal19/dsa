# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=None
        curr = head
        front=head
        while(front!=None and n>0):
            front = front.next
            n = n-1
        
        while(front!=None):
            prev = curr
            curr = curr.next
            front = front.next

        # Edge case for deleting head
        if(curr==head):
            head = head.next 
        else:    
            prev.next = curr.next

        return head