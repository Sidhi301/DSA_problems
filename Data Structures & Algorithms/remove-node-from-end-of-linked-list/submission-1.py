# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0

        while temp:
            
            temp=temp.next
            count+=1
        if count==n:
            return head.next
        m=count-n
        
        temp=head
        for i in range(m-1):
            temp=temp.next
       
        temp.next=temp.next.next
        return head


        