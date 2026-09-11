# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        dummy = ListNode(0)
        current = dummy 
        carry = 0

        while l1 or l2 or carry :

            a = 0
            if l1:
                a = l1.val
                l1 = l1.next
        
            b = 0
            if l2:
                b = l2.val
                l2 = l2.next

            sum = a + b + carry
            digit = sum%10
            carry = sum//10

            current.next = ListNode(digit)
            current = current.next
    
        return dummy.next
