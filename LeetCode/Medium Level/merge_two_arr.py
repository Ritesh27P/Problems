# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Optional:
    # //no code 
    pass 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        new_arr = ListNode()
        temp = new_arr

        while True:
            if list1 and list2:
                if list1.val < list2.val:
                    temp.next = ListNode(list1.val)
                    list1 = list1.next
                elif list1.val > list2.val:
                    temp.next = ListNode(list2.val)
                    list2 = list2.next
                else: 
                    temp.next = ListNode(list1.val)
                    list1 = list1.next
            elif list1:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            elif list2:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            else:
                break
            
            temp = temp.next

        return new_arr.next
            
        