# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        
        new_head = ListNode()
        myList = new_head

        # myList.next = ListNode(2)
        # myList = myList.next

        # myList.next = ListNode(1)
        # myList= myList.next

        # return new_head.next

        temp = head
        while temp:
            if temp.next:
                temp1 = ListNode(temp.val)
                temp2 = ListNode(temp.next.val)

                myList.next = temp2
                myList = myList.next

                myList.next = temp1
                myList = myList.next

                temp = temp.next
            else:
                myList.next = temp
                # myList = myList.next
            
            temp = temp.next

        return new_head.next
                
                