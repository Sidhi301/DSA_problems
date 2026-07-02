# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None :
            return None
        pos=1
        curr=head
        l1=[]
        while curr!=None:
            if left<=pos<=right:
                l1.append(curr.val)
            curr=curr.next
            pos+=1
        pos=1
        l1.reverse()
        curr=head
        idx=0
        while curr!=None:
            if left<=pos<=right:
                curr.val=l1[idx]
                idx+=1
            curr=curr.next
            pos+=1
        return head

        
                
            

        