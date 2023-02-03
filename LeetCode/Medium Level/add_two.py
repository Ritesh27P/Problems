# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Optional:
    # do nothing
    pass

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr = ListNode()
        temp = arr

        carry = 0

        while True:
            if l1 and l2:
                sum = str(l1.val + l2.val + carry)
                if (len(sum) > 1):
                    carry = int(sum[:1])
                    temp.next = ListNode(int(sum[1:]))
                else:
                    carry = 0
                    temp.next = ListNode(int(sum))
            
            elif l1:
                sum = str(l1.val + carry)
                if (len(sum) > 1):
                    carry = int(sum[:1])
                    temp.next = ListNode(int(sum[1:]))
                else:
                    carry = 0
                    temp.next = ListNode(int(sum))

            elif l2:
                sum = str(l2.val + carry)
                if (len(sum) > 1):
                    carry = int(sum[:1])
                    temp.next = ListNode(int(sum[1:]))
                else:
                    carry = 0
                    temp.next = ListNode(int(sum))
            
            else:
                break

            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            temp.next = ListNode(carry)
        
        return arr.next
            

        

