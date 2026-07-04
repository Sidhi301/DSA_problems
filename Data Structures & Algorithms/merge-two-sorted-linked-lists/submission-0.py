# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNode=ListNode()
        new=newNode
        temp1=list1
        temp2=list2
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                new.next=temp1
                temp1=temp1.next
            else:
                new.next=temp2
                temp2=temp2.next
            new=new.next
        if temp2:
            new.next=temp2
        else:
            new.next=temp1
        return newNode.next


            

        