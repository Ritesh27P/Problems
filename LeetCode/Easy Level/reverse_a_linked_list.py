# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ReverseNode:
    def __init__(self, val=0, prev=None):
        self.val = val
        self.prev = prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode('value')
        temp_head = new_head

        temp = head
        while temp:
            node = ListNode(temp.val)
            if temp_head.val == "value":
                temp_head = node
            else:
                node.next = temp_head
                temp_head = node

            temp = temp.next
        
        if temp_head.val == 'value':
            return temp_head.next

        return temp_head