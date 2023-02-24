# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head):
        if head:
            temp = head
            temp_val = head.val

            new_head = ListNode(temp_val)
            temp_list = new_head

            while temp:
                if temp.val != temp_val:
                    temp_list.next = ListNode(temp.val)
                    temp_list = temp_list.next
                    temp_val = temp.val
                temp = temp.next

            return new_head
        
        