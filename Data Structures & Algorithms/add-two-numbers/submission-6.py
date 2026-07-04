# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode=ListNode(0)
        new=newNode
        
        carry=0
        digit=0
        sum1=0
       
        while l1 or l2:
            num1=l1.val if l1 else 0
            num2=l2.val if l2 else 0
        
            sum1=num1+num2+carry
            digit=sum1%10
            carry=sum1//10
            
            new.next=ListNode(digit)
            new=new.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

            if carry:
                new.next=ListNode(carry)
        return newNode.next
        

                

        