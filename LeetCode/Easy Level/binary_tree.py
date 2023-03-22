# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root):
        lst = list()
        self.recur(root, lst)
        return lst

    def recur(self, root, lst):
        if root:
            self.recur(root.left, lst)
            lst.append(root.val)
            self.recur(root.right, lst)
        
        
        

        