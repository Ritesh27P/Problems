# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stk = [ root ]

        while len(stk):
            curr = stk.pop()
            if curr:
                res.append(curr.val)
            else: 
                continue
                
            if curr.right:
                stk.append(curr.right)
            if curr.left:
                stk.append(curr.left)

        return res

        
        